# @postload

Runs the decorated function on server load. Runs after [@load](load.md).

```py
@postload
```

&nbsp;


## Examples

1. Outputs a "`Hello World!`" message in chat on server load.

```py
@postload
def foo():
    tellraw @a 'Hello World!'
```