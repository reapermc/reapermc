# How to disable mob loot.

In order to disable mob loot similarly to the `doMobLoot` gamerule you will need to add this to your beet config.

```yml
meta:
  reapermc:
    doMobLoot: false
```

Doing so will override all vanilla entity loot tables with blank contents.

NOTE: Experience orbs will still drop. That said you can kill `kill` them yourself every tick, though that will mess with grindstones etc.


&nbsp;


# Why is this required?

Reaper requires the `doMobLoot` gamerule to be set to `True` in order to work properly.

The core systems in question are the `EntityNBT` class and `register_death_event` function. They both require `loot_table` injections in order to function properly by detecting entity deaths.

Disabling the gamerule normally will break them.

