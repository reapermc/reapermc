# Flag

<!-- Pythonized version of the `/effect` command. -->
Allows simple checking of a lot of flags. Outputs a boolean value.


```py
if Flag(name):
    pass
else:
    pass
```


&nbsp;


## Arguments

**name**
> String value. Name of the flag you want to check. Example: `'is_in_air'`. Full list of flags: [Flags](../misc/flags.md).


&nbsp;


## Examples

1. Checking if the player is in the air.

```py
function ./foo:
    if Flag('is_in_air'):
        say 'Im in air!'
    else:
        say 'Im on ground!'
```

2. Checking if the player is holding an item in the offhand.

```py
function ./foo:
    if Flag('is_holding_wheat_seeds_offhand'):   # works for any item name
        say 'Im a left handed farmer'
```