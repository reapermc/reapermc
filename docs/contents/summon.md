# summon

Overrides the default `summon` command, giving it an optional nesting functionality.

```py
summon <entity> ~ ~ ~:
    # as & at
    # code
```


&nbsp;



## Remarks

Supports all formats of the `summon` command. The scope will run `as` and `at` the summoned entity.


&nbsp;


## Examples

1. Summoning a zombie, then giving him a score right away.

```py
function ./example:
    summon zombie:
        scoreboard players set @s my_score 69
```






