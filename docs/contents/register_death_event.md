# register_death_event

Registers a death event for an entity. The event will trigger __at__ the position where the entity died.


```py
register_death_event(death_event)
```


&nbsp;



## Arguments
 
**death_event**
> A function object. The function you pass in will be bound to the target entity and executed on death.


&nbsp;


## Remarks

Assumes current selector as the entity to which the specified function should be bound to.

The bound function will be executed `at` the target entity's death location.

The event will not execute `as` the entity, only `at` the entity's position. This is due to a limitation within minecraft which I can not circumvent. The selector running the event is a special `nether_star` item which disappears instantly on the same tick.

&nbsp;


## Examples

1. Assigning death events to entities

```py
def death_event_0():
    setblock ~ ~ ~ poppy
    say I died here


def death_event_1():
    summon creeper ~ ~3 ~ {Fuse:20s,ignited:1b}
    say Incoming!


function ./pig:
    summon pig ~ ~ ~:
        register_death_event(death_event_0)

function ./cow:
    summon cow ~ ~ ~:
        register_death_event(death_event_1)

# you can assign the same event to
# multiple entities as expected too
function ./zombie:
    summon zombie ~ ~ ~:
        register_death_event(death_event_1)
```






