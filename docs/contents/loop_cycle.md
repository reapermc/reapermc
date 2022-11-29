# loop_cycle

A read-only score [expression](https://github.com/rx-modules/bolt-expressions). The value is the current loop cycle starting at `0`.

```py
foo = loop_cycle
```


&nbsp;



## Remarks

Since `loop_cycle` is an [expression](https://github.com/rx-modules/bolt-expressions), you can use [Expr](./Expr.md) to compare it to other values.


&nbsp;



## Examples

1. Running a `say` command if the current loop cycle is `3`.

```py
function ./foo:
    with loop(5, 40):       
        if Expr(loop_cycle) == 3:
            say Hello! :D
```


2. Summoning a tnt on every cycle after `5`.

```py
function ./foo:
    with loop(10, 20):
        if Expr(loop_cycle) > 5:
            summon tnt
```


3. Retrieving the current loop cycle.
```py
x = scoreboard('test')['$fakeplayer']

function ./foo:
    with loop(5, 20):
        x = loop_cycle
```





