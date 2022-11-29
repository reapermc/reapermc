# get_time

Returns the current time into an [expression](https://github.com/rx-modules/bolt-expressions).

```py
foo = get_time(mode='daytime')
```


&nbsp;



## Arguments

**mode**
> By default `'daytime'`. Can be set to either `'daytime'`, `'gametime'` or `'day'`.


&nbsp;


## Examples

1. Retrieving the current gametime.

```py
foo = var(int)

function ./bar:
    foo = get_time('gametime')
```

2. Healing or damaging the player depending on if it's day or night.

```py
function ./example:
    # day = heal, night = damage
    if Expr(get_time()) < 13000:
        effect give @s instant_health
    else:
        effect give @s instant_damage
```
