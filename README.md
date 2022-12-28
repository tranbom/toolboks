# toolboks

toolboks is a lightweight utility library.


## Installation

Install with pip:

`pip install toolboks`


## Usage

Most functions are available by simply importing toolboks directly:

```
> import toolboks as tb

> nested_list = [1,2,3,[4,5,[6,7,8]]]
> tb.expand(nested_list, depth=1)
[1, 2, 3, 4, 5, [6, 7, 8]]
```


Modules can also be imported separately:

```
from toolboks import xdg

# get user base dirs according to the XDG base directory specification
base_dirs = xdg.base_dirs()
```

## Module Overview

| Module    | Description                     | Classes | Functions       |
|-----------|---------------------------------|---------|-----------------|
| config    | Configuration file functions    |         | read_config     |
| listlib   | List manipulation & helpers     |         | expand, flatten |
| modifiers | Common data modifiers           |         | filter_abs_path |
| system    | Common system related functions |         | context, getenv |
| xdg       | Functions for XDG base dirs     |         | base_dirs, cache_home, config_dirs, config_home,<br> data_dirs, data_home, runtime_dir, state_home,<br> user_dirs, user_home |


## Command Line Interface
toolboks has a command line interface with shell commands for relevant functions from the toolboks library.  
It is available as a separate package: [toolboks-cli](https://pypi.org/project/toolboks-cli/)

Install it with pip:
`pip install toolboks-cli`

See documentation of toolboks-cli for more information on available commands.


## License

GPL-3.0-only
