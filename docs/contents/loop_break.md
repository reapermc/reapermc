# loop_break

Stops execution of the current [loop](loop.md). Behavior is similar to how the well known `break` statement would work in popular programming languages.

```py
loop_break()
```


&nbsp;


## Remarks

Due to how nesting works in `Bolt`, in the case of a conditional `loop_break`, make sure the only content in that scope is the `loop_break` call. Example:

```py
# incorrect usage

# the 'say' and 'summon' commands will brick
# the system in this example

with loop(5, 30):
    if entity @s SelectedItem:
        summon cow ~ ~ ~
        loop_break()
        say hello
```
```py
# correct usage


with loop(5, 30):
    # just separatele them
    if entity @s SelectedItem:
        summon cow ~ ~ ~
        say hello

    if entity @s SelectedItem:
        loop_break()
```

&nbsp;



## Examples

1. Stopping execution of a [loop](loop.md) if the entity holds any item.

```py
function ./foo:
    with loop(5, 40):       
        say "Hello this will run before the break!"

        if entity @s SelectedItem:
            loop_break()

        say "I will only be run if the loop hasn't been broken!"

```







