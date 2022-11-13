# @postjoin

Runs the decorated function as & at the joining player. Runs after [@join](join.md).

```py
@postjoin
```

&nbsp;


## Remarks

Will also trigger on `/reload` for every currently online player.


&nbsp;



## Examples

1. Runs a simple message as the joining player and gives them a diamond.

```py
@postjoin
def greeter():
    say Hello I just joined!
    give @s diamond
```