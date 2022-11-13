# loop_break

Stops execution of the current [loop()](loop.md). Behavior is similar to how a regular `break` statement would work in programming.

```py
loop_break()
```


&nbsp;


## Remarks

Due to how nesting works in bolt, in the case of a conditional break, make sure the only content in that scope is the `loop_break()`. Example:

```py
# THIS WILL NOT WORK!!!

if entity @s SelectedItem:
    summon cow ~ ~ ~
    loop_break()
    say hello               # this won't work, because this additional 'say' command
                            # makes bolt create a new nested function internally
```
```py
# CORRECT USAGE:

if entity @s SelectedItem:
    loop_break()
```

&nbsp;



## Examples

1. Stopping execution of a loop if the entity holds any item.

```py
function ./foo:
    with loop(5, 40):       
        tellraw @a 'Hello this will run before the break!'

        if entity @s SelectedItem:
            loop_break()

        tellraw @a "I will only be ran if the loop hasn't been broken!'

```







