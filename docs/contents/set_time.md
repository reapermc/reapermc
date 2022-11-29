# set_time

Sets the current time of day to a specified value.


```py
set_time(value)
```


&nbsp;


## Arguments

**value**
> Can be an integer or an [expression](https://github.com/rx-modules/bolt-expressions).


&nbsp;


## Examples

1. Setting time to a constant value.

```py
function ./foo:
    set_time(12000)

function ./bar:
    x = 69
    set_time(x)
```

2. Setting time to an expression (here, our `Health` multiplied by `10`).

```py
foobar = scoreboard('foo')['$bar']

function ./example:
    foobar = Data.entity('@s').Health   # get @s 'Health'
    foobar *= 10                        # multiply by 10

    # set the time to the expression
    set_time(foobar)
```