# ole

[stoQ](https://stoq-framework.readthedocs.io/en/v2/index.html) plugin that carves executables from payloads.

## Plugin Classes

- [Worker](https://stoq-framework.readthedocs.io/en/v2/dev/workers.html)

## Configuration

All options below may be set by:

- [plugin configuration file](https://stoq-framework.readthedocs.io/en/v2/dev/plugin_overview.html#configuration)
- [`stoq` command](https://stoq-framework.readthedocs.io/en/v2/gettingstarted.html#plugin-options)
- [`Stoq` class](https://stoq-framework.readthedocs.io/en/v2/dev/core.html?highlight=plugin_opts#using-providers)

### Options

- `pe_headers` [str]: Regex pattern to match for PE headers (i.e., MZ or ZM)

> Paths may be relative to the module, or a full path.