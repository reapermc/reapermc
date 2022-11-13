# get_time

Returns the current time into an [expression](https://github.com/rx-modules/bolt-expressions).

```py
foo = get_time(mode='daytime')
```


&nbsp;



## Arguments

**mode**
> By default '`daytime`' Can be set to either `'daytime'`, `'gametime'` or `'day'`.


&nbsp;


## Examples

1. Retrieving the current gametime.

```py
foo = var(int)

function ./bar:
    foo = get_time('gametime')
```

2. Retrieving the current daytime, damage or heal the player depending on if it's day or night.

```py
foo = var(int)

function ./bar:
    foo = get_time()        # defaults to 'daytime'

    # day = heal
    if score foo.holder foo.obj matches ..15999:
        effect give @s instant_health
    
    # night = damage
    if score foo.holder foo.obj matches 16000..:
        effect give @s instant_damage
```






