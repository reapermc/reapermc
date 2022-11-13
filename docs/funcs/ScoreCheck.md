# ScoreCheck

Allows for a simple way of checking scores using python's comparison operators.

```py
if ScoreCheck(score_expr) <oper> <value>:
    ...
else:
    ...
```


## Arguments

**score_expr**
> The score you want to check. Has to be a score + objective [expression](https://github.com/rx-modules/bolt-expressions).


**oper**
> One of python's [comparison operators](https://www.w3schools.com/python/gloss_python_comparison_operators.asp).


**value**
> Can be an integer value or a score + objective [expression](https://github.com/rx-modules/bolt-expressions).


&nbsp;





## Remarks

For the time being selectors are not supported in either the `score_expr` or `value`. This should be resolved once [Bolt](https://github.com/mcbeet/bolt) starts supporting selector interpolation.


This API will most likely be deprecated once [bolt-expressions](https://github.com/rx-modules/bolt-expressions) enters data comparison territory. 

&nbsp;



## Examples

1. Check if our health is 20, if it is, give us a diamond.

```py
tmp = var(int)

function ./example:
    tmp = Data.entity('@s')['Health']           # grab the health and store in tmp
    
    if ScoreCheck(tmp) == 20:                   # check the score 
        give @s diamond 1                       # (var(int) is a score + obj combo)
```