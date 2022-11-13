# effect

Pythonized version of the `/effect` command.


```py
effect(id, duration, amplifier, show_particles=False)
```


&nbsp;


## Arguments

**id**
> The string id of an effect. Example: `jump_boost`, `instant_health`.

**duration**
> The duration of the effect in seconds.

**amplifier**
> Amplifier level of the effect.

**show_particles**
> By default `False`. If set to true the effect will emit particles off the affected entity.



&nbsp;


## Examples

1. Giving the nearest player the poison effect for 3 seconds with amplifier of 5.

```py
function ./foo:
    as @p:
        effect('poison', 3, 5)
```
