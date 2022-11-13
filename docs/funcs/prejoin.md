# @prejoin

Runs the decorated function as & at the joining player. Runs before [@join](join.md).

```py
@prejoin
```

&nbsp;


## Remarks

Will also trigger on `/reload` for every currently online player.


&nbsp;



## Examples

1. Runs a simple message as the joining player and gives them a diamond.

```py
@prejoin
def greeter():
    say Hello I just joined!
    give @s diamond
```