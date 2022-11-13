# @pretick

Runs the decorated function every tick. Runs before [@tick](tick.md).

```py
@pretick
```

&nbsp;


## Remarks

This decorator is superior to `#minecraft:tick`, as it fixes a bug which causes `#minecraft:tick` to run before `#minecraft:load`.


&nbsp;


## Examples

1. Spawns a simple flame particle every tick under all players feet.

```py
@pretick
def foo():
    at @a:
        particle flame
```