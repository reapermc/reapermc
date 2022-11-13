# tag

Tags the current selector entity.


```py
tag(name)
```


&nbsp;


## Arguments

**name**
> String value.

&nbsp;


## Examples

1. Tags all zombies with the tag `scaryman`.

```py
function ./foo:
    as @e[type=zombie]:
        say I eat humans
        tag('scaryman')
```
