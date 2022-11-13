# ReaperMC
[![GitHub Actions](https://github.com/reapermc/reapermc/workflows/CI/badge.svg)](https://github.com/reapermc/reapermc/actions)

> A high level framework for the Bolt scripting language.




## Introduction

Reaper is a framework for the [Bolt](https://github.com/mcbeet/bolt) scripting language. It features complex yet optimized, high level yet simple to use functions.


The goal of this project is to reduce the time developers waste. The aim is to enable developers in creating things faster while focusing on the important bits.

For further info about the project, check [here](about.md).

## Installation

```bash
pip install reapermc
```



## Getting started

This package is designed to be used within `.bolt` scripts, inside a bolt enabled project. I will never officially support `.mcfunction` files.

To enable Reaper inside your project, you will need to add `reapermc` to your `require` list inside the beet config file.
```yaml
require:
    - bolt
    - reapermc
```



Modules named `<namespace>:main` will automatically be the entrypoint.

To use Reaper's functions, you'll need to import them. (**This won't be necessary in the future**).

```py
# my_project:main

from reapermc:api import sleep, set_time, tag

def become_wizard():
    tellraw @s 'You will become a wizard...'

    with sleep(40):
        set_time(13000)
        tag('wizardman')
        tellraw @s 'You are now a wizard!'
```


# Documentation

The documentation for this project can be found [here](docs/table_of_contents.md).



---

License - [MIT](https://github.com/reapermc/reapermc/blob/main/LICENSE)

