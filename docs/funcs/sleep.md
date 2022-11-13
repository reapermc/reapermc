# sleep

Delays execution of the target scope by a time interval. Full entity support.


```py
with sleep(interval, threading=True, world_ctx=True, selector='auto'):
    ...
```


&nbsp;



## Arguments

**interval**
> Integer value. Delay interval specified in game ticks.


**threading**
> Boolean value, by default `True`. Threading allows the same `sleep()` called multiple times to run asynchronously. Without threading, running the same `sleep()` call more than once will terminate and override the previous ones (if they have not executed yet).


**selector**
> By default `'auto'` (handled at runtime). Limits execution to a selector type. You can specify either `'server'` or `'entity'` if you know only one will be used for further optimization (**DO NOT CALL AS ENTITY IF SET TO `server` OR VICE VERSA, IT WILL BREAK**).


**world_ctx**
> Boolean value, by default `True`. If `True`, code will be executed at the exact `Dimension`, `Position` and `Rotation` it was called from.


&nbsp;


## Remarks

Should be used alongside the `with` statement.

The target code will be executed `as` the selector calling `sleep()`, as well as `at` the position, rotation and dimension where `sleep()` was initially called from.

Keep in mind `threading` and `world_ctx` are considerably more expensive to run. If you are sure they are <u>__ABSOLUTELY NOT NECESSARY__</u> in a certain situation, set them to `False`.




&nbsp;



## Examples

1. Very simple usage of `sleep()`.

```py
function ./foo:
    say Hello!

    with sleep(40):
        summon pig ~ ~ ~                    # will 'summon' the pig where sleep() was initially ran
        
        at @s:
            summon creeper ~ ~ ~            # will run at @s after the sleep

        say Hello!... 2 seconds later!!!    # and run the 'say' as @s



```

2. Disabled `threading` example.

```py
function ./foo:
    say Hello!

    with sleep(20, threading=False):        # if function ./foo is called
        effect give @s instant_damage       # before the 'sleep()' finished
                                            # the previous sleep will be terminated
                                            # and next one started
```

3. Disabled `world_ctx` example.

```py
function ./foo:
    say Hello!

    with sleep(36, world_ctx=False):
        say World!                          # the 'say' command will still run as '@s'
        summon cow ~ ~ ~                    # but the cow will be summoned at worldspawn


function ./bar:
    say Hello!

    with sleep(36, world_ctx=False)
        at @s:
            say World!                          # just like above, the 'say' will work normally
            summon cow ~ ~ ~                    # however because of the 'at @s'
                                                # the cow will be summoned at our position
```







