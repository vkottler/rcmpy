"""
An environment extension for working with template files.
"""

# third-party
from datazen.templates import environment
from jinja2 import FileSystemLoader

# internal
from rcmpy.environment.base import BaseEnvironment


class TemplateEnvironment(BaseEnvironment):
    """
    A class implementing template management for this package's runtime
    environment.
    """

    def _init_loaded(self) -> None:
        """Called during initialization if a valid configuration is loaded."""

        super()._init_loaded()

        if not hasattr(self, "jinja"):
            template_root = self.state.directory.joinpath("templates")

            # Prefer variant templates, if the variant template-directory
            # exists.
            self.jinja = environment(
                loader=FileSystemLoader(
                    [
                        x
                        for x in [
                            template_root.joinpath(self.state.variant),
                            template_root.joinpath("common"),
                        ]
                        if x.is_dir()
                    ],
                    followlinks=True,
                )
            )

            for template in self.jinja.list_templates():
                print(template)
