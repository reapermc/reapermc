# Flag

Allows for checking the state of many things using Flags. All builtin flags can be found here: [Builtin Flags](../misc/builtin_flags.md).


```py
if Flag(flag):
    pass
else:
    pass
```


&nbsp;


## Arguments

**flag**
> A flag object. The flag which will determine the condition.


&nbsp;


## Examples

1. Checking if the player is in the air.

```py
function ./foo:
    if Flag(is_in_air):
        say 'Im in air!'
    else:
        say 'Im on ground!'
```
