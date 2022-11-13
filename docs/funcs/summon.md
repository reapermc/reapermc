# summon

Overrides the default summon command, which gives it an instant nesting option.



```py
summon <entity> ~ ~ ~:
    # as & at
    # code
```


&nbsp;



## Remarks

On top of __ANY__ use of the summon command, you can additionally follow it with a nested block. The nested block will run `as` & `at` the summoned entity.


&nbsp;


## Examples

1. Summoning a zombie, then giving him a score right away.

```py
function ./example:
    summon zombie ~ ~ ~:
        scoreboard players set @s my_score 69
```






