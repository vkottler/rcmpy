"""
An environment extension for working with template files.
"""

# built-in
from pathlib import Path
from typing import Dict, NamedTuple, Optional, Set

# third-party
from datazen.templates import environment
from jinja2 import FileSystemLoader, Template
from vcorelib.paths.info import FileChangeEvent
from vcorelib.paths.info_cache import FileChanged, file_info_cache

# internal
from rcmpy.environment.base import BaseEnvironment


class EnvTemplate(NamedTuple):
    """
    A data structure for keeping track of environment templates. If 'template'
    is None, it signals that the template does not require rendering.
    """

    name: str
    template: Optional[Template] = None


class TemplateEnvironment(BaseEnvironment):
    """
    A class implementing template management for this package's runtime
    environment.
    """

    templates: Dict[Path, EnvTemplate]

    def _load_templates(self) -> Set[str]:
        """Load template information to the environment."""

        # Keep track of templates by name.
        self.templates = {}
        template_names: Set[str] = set()
        for name in self.jinja.list_templates():
            obj = self.jinja.get_template(name)

            # We know all templates are files.
            assert obj.filename is not None

            # Keep track of template paths and their templates.
            self.templates[Path(obj.filename).resolve()] = EnvTemplate(
                name,
                obj if name.endswith("j2") else None,
            )
            template_names.add(name)

        return template_names

    def _init_loaded(self) -> bool:
        """Called during initialization if a valid configuration is loaded."""

        result = super()._init_loaded()

        # Ensure double initialization isn't possible (use an arbitrary
        # attribute set here to detect this).
        assert not hasattr(self, "jinja")

        template_root = self.state.directory.joinpath("templates")

        candidates = [template_root.joinpath("common")]

        # Only consider a 'variant' sub-directory if variant is set. Ensure
        # that the candidate directory comes first.
        if self.state.variant:
            candidates.insert(0, template_root.joinpath(self.state.variant))

        # Only consider directories that exist.
        candidates = [x for x in candidates if x.is_dir()]

        # Prefer variant templates, if the variant template-directory
        # exists.
        self.jinja = environment(
            loader=FileSystemLoader(candidates, followlinks=True)
        )

        # Check if all templates called out by the configuration were found.
        template_names = self._load_templates()
        for name in self.config.templates:
            if name not in template_names:
                self.logger.error("Template for '%s' not found!", name)
                return False

        self.updated_templates: Set[Path] = set()

        def poll_cb(change: FileChanged) -> bool:
            """Aggregate paths of templates that have been updated."""

            poll_result = True

            # If a file was removed, confirm it's not a template that's still
            # needed.
            if change.event is FileChangeEvent.REMOVED:
                assert change.old is not None
                if change.old.path in self.templates:
                    template = self.templates[change.old.path]
                    if template.name in self.config.templates:
                        # Cause environment initialization to fail.
                        nonlocal result
                        result = False

                        # Log the error and don't approve this change event.
                        self.logger.error(
                            "Template '%s' (%s) was removed but is needed!",
                            template.name,
                            change.old.path,
                        )
                        poll_result = False

            else:
                assert change.new is not None

                # Don't acknowledge changes to any files that aren't active
                # templates.
                if change.new.path not in self.templates:
                    poll_result = False
                else:
                    template = self.templates[change.new.path]

                    # Acknowledge this template change if the detected template
                    # is used by the current configuration.
                    poll_result = template.name in self.config.templates
                    if poll_result:
                        self.updated_templates.add(change.new.path)

            return poll_result

        self.template_changes = self.stack.enter_context(
            file_info_cache(
                self._cache.joinpath("templates.json"),
                poll_cb,
                logger=self.logger,
            )
        )

        # Poll template directories.
        for candidate in candidates:
            self.template_changes.poll_directory(candidate)

        # Log info about detected template changes.
        for changed in self.updated_templates:
            self.logger.info(
                "Detected change for template '%s'.",
                self.templates[changed].name,
            )

        return result
