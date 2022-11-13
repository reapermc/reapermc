# @preload

Runs the decorated function on server load. Runs before [@load](load.md).

```py
@preload
```

&nbsp;


## Examples

1. Outputs a "`Hello World!`" message in chat on server load.

```py
@preload
def foo():
    tellraw @a 'Hello World!'
```