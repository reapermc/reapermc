# untag

Removes the tag from current selector entity.


```py
untag(name)
```


&nbsp;


## Arguments

**name**
> String value.

&nbsp;


## Examples

1. Removes `'will_explode'` tag and explodes the entity.

```py
function ./foo:
    as @e[tag=will_explode] at @s:
        summon tnt ~ ~ ~ {Fuse:0s}
        untag('will_explode')
```

2. Removes `'my_pack.boss_0.reward'` tag and rewards the player.

```py
reward_tag = 'my_pack.boss_0.reward'

function ./foo:
    as @a[tag=reward_tag]:
        give @s diamond
        untag(reward_tag)
```
