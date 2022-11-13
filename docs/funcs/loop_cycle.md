# loop_cycle

Lets you access the current loop cycle. You can compare it, similarly to [ScoreCheck()](ScoreCheck.md), as well as retrieve the value.

```py
loop_break
```


&nbsp;





## Remarks

You can use any of python's [comparison operators](https://www.w3schools.com/python/gloss_python_comparison_operators.asp) to compare the current loop cycle to values or other scores.

You can make it return the expression using the `loop_cycle.get()` method.



&nbsp;



## Examples

1. Running a `tellraw` command if the loop cycle is `3`.

```py
function ./foo:
    with loop(5, 40):       
        if loop_cycle == 3:
            tellraw @a 'hello! :D'
```


2. Summoning a tnt on every cycle after `5`.

```py
function ./foo:
    with loop(10, 20):
        if loop_cycle > 5:
            summon tnt
```


3. Retrieving the loop cycle value.
```py
x = scoreboard('test')['$fakeplayer']

function ./foo:
    with loop(5, 20):
        x = loop_cycle.get()

```





