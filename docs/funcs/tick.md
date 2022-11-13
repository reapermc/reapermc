# @tick

Runs the decorated function every tick, similarly to `#minecraft:tick`.

```py
@tick
```

&nbsp;


## Remarks

This decorator is superior to `#minecraft:tick`, as it fixes a bug which causes `#minecraft:tick` to run before `#minecraft:load`.


&nbsp;


## Examples

1. Spawns a simple flame particle every tick under all players feet.

```py
@tick
def foo():
    at @a:
        particle flame
```