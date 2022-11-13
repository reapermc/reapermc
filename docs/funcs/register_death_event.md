# register_death_event

Registers a death event for an entity. The event will trigger __at__ where the entity died.



```py
register_death_event(death_event)
```


&nbsp;



## Arguments
 
**death_event**
> Accepts a function name. The function you pass will be executed after the entity dies.


&nbsp;


## Remarks

Assumes current selector as the entity to which the specified function should be bound.

The bound function will be executed `at` the target entity's death location.

Executing `as` the dying entity does not work. The selector will be a special `nether_star` item that drops from the dead entity (used for detection, disappears instantly).


&nbsp;


## Examples

1. Assigning death events to entities

```py
def death_event_0():
    setblock ~ ~ ~ poppy
    say I died here


def death_event_1():
    summon creeper ~ ~3 ~ {Fuse:20s,ignited:1b}
    say death event 1



function ./pig:
    summon pig ~ ~ ~:
        register_death_event(death_event_0)

function ./cow:
    summon cow ~ ~ ~:
        register_death_event(death_event_1)

function ./zombie:
    summon zombie ~ ~ ~:
        register_death_event(death_event_1)
```






