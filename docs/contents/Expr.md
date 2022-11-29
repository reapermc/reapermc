# Expr

Allows for a simple way of comparing [expressions](https://github.com/rx-modules/bolt-expressions).
<!-- Allows for a simple way of checking scores using python's comparison operators. -->

```py
if Expr(expression) <oper> value:
    pass
else:
    pass
```


## Arguments

**score_expr**
> Any [expression](https://github.com/rx-modules/bolt-expressions) you want to compare.


**oper**
> Any of python's [comparison operators](https://www.w3schools.com/python/gloss_python_comparison_operators.asp).


**value**

> Any value including [expressions](https://github.com/rx-modules/bolt-expressions).


&nbsp;


## Remarks

Trying to compare a `storage` value to a `scoreboard` value or vice versa will always cause the `storage` value to be converted into a temporary `scoreboard` value and then compared.

Not all cases are covered, but for most it should work whether it's comparing a `storage` to a `storage`, `entity` to a `storage`, or `score` to a `score`.

&nbsp;



## Examples

1. Check if the selector health is `20`, if it is, give a diamond.

```py
tmp = var(int)

function ./example:
    tmp = Data.entity('@s').Health

    if Expr(tmp) == 20:
        give @s diamond 1
        tellraw @s {"text": "Good job!", "color": "aqua"}
```

2. Condensed version of the previous example:

```py
# we have to compare to '20.0f' here since we're
# not converting into a score using the int var

function ./example:
    if Expr(Data.entity('@s').Health) == 20.0f:
        give @s diamond 1
        tellraw @s {"text": "Good job!", "color": "aqua"}
```
