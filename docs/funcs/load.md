# @load

Runs the decorated function on server load, similarly to `#minecraft:load`.

```py
@load
```

&nbsp;


## Examples

1. Outputs a "`Hello World!`" message in chat on server load.

```py
@load
def foo():
    tellraw @a 'Hello World!'
```