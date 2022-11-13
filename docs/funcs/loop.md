# loop

Runs the target scope code on a loop. Full entity support.

```py
with loop(count, interval, threading=True, world_ctx=True, selector='auto'):
    ...
```


&nbsp;



## Arguments

**count**
> Can be an integer value or [expression](https://github.com/rx-modules/bolt-expressions). Amount of times the loop will run for. Can be set to `0` for an infinite loop.


**interval**
> Integer value. Delay interval specified in game ticks. Can be set to `0` to recursively execute contents.


**threading**
> Boolean value, by default `True`. Threading allows the same `loop()` call to run simultanously at a performance cost. Without threading, running the same `loop()` call more than once will terminate and override the previous ones (if they have not executed yet).


**selector**
> Limits execution to a selector. You can specify either `'server'` or `'entity'` if you know only one will be used for further optimization. By default `'auto'` (handled at runtime).


**world_ctx**
> Boolean value, by default `True`. On each `loop()` cycle, the code will run exactly at the position where it was called from.


&nbsp;


## Remarks

Should be used alongside the `with` statement.

Comboing `count=0` with `interval=0` will result in an error (*why would you want that?*).

Keep in mind `threading` and `world_ctx` are considerably more expensive to run. If you are sure they aren't necessary in a certain situation, set them to `False`.


&nbsp;



## Examples

1. Very simple usage of `loop()`.

```py
function ./foo:
    say Hello! Starting the loop!

    # count=5, interval=40
    with loop(5, 40):       
        summon pig ~ ~ ~                    # each cycle, will 'summon' the pig at the 
                                            # original position 'loop()' was called from

        at @s:
            summon creeper ~ ~ ~            # each cycle, will 'summon' the creeper at the 
                                            # current position of whoever ran the 'loop()'


        say cycle!!!                        # and each cycle, run the 'say' as @s

```

2. Disabled `threading` example:

```py
function ./foo:
    say Hello!

    with loop(2, 20, threading=False):      # if function ./foo is called
        effect give @s instant_damage       # before the 'loop()' finished
                                            # the previous loop will be terminated
                                            # and next one started
```

3. Disabled `world_ctx` example:

```py
function ./foo:
    say Hello!

    with loop(5, 36, world_ctx=False):
        say World!                          # the 'say' command will still run as '@s'
        summon cow ~ ~ ~                    # but the cow will be summoned at worldspawn


function ./bar:
    say Hello!

    with loop(5, 36, world_ctx=False)
        at @s:
            say World!                          # just like above, the 'say' will work the same way
            summon cow ~ ~ ~                    # however because of the 'at @s'
                                                # the cow will instead be summoned at our position
```







