<!--
    =====================================
    generator=datazen
    version=3.1.4
    hash=4e92d9930b81742f094d65fc35fb1b4a
    =====================================
-->

# Data Repository

([back](../README.md#getting-started))

The data repository contains all source files and configuration data that
describes the work that `rcmpy` should do.

Design goals:
- Integrates easily with version-control software by using only text data
- Can be shared by multiple active users or developers
   - Configuration files and data can be isolated to a particular user's
   "variant"
   - User-specific additions can be promoted to common, shared assets easily
   (e.g. the "new default" for users that don't tailor their own settings)
- Able to describe software/packages that should be installed, and at what
version
- The single-source-of-truth and backbone of "what software does my workflow or
entire ecosystem use"
- Be as intuitive to understand in organization and function as possible

## Top-level Configuration

See also: [schema](../rcmpy/data/schemas/Config.yaml).
