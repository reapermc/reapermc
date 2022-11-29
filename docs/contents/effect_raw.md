# effect_raw

Additional & more experimental version of [effect()](effect.md).


```py
effect_raw(id, duration, amplifier, show_particles=False)
```


&nbsp;


## Arguments

**id**
> The string id of an effect. Example: `jump_boost`, `instant_health`.

**duration**
> The duration of the effect in game ticks.

**amplifier**
> Amplifier level of the effect.

**show_particles**
> By default `False`. If set to true the effect will emit particles off the affected entity.



&nbsp;



## Remarks


The main difference between this and [effect](effect.md) is being able to precisely specify the duration in gameticks.

For players it applies the effect via an instant precisely-tweaked `area_effect_cloud`.
For non-player entities it directly modifies their `ActiveEffects` NBT.

**WARNING**: Rarely, but sometimes certain effects applied to players can become buggy and not apply, such as `levitation`. This hasn't been looked into enough as of now. a `/reload` or server restart (or exit and rejoin in singleplayer) will usually resolve the issue. It has to do with Mojang's code and I can't fix it.


&nbsp;


## Examples

1. Giving the nearest player the `strength` effect for 10 gameticks (0.5 second) with an amplifier of 8.

```py
function ./foo:
    as @p:
        effect_raw('strength', 10, 8)
```
