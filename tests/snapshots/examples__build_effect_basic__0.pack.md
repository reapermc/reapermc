# Lectern snapshot

## Data pack

`@data_pack pack.mcmeta`

```json
{
  "pack": {
    "pack_format": 10,
    "description": ""
  }
}
```

### demo

`@function demo:test`

```mcfunction
effect give @s speed 5 10 true
```

`@function demo:test1`

```mcfunction
execute if entity @s[type=player] run summon area_effect_cloud ~ ~ ~ {Radius: 0.0f, Age: 4, WaitTime: 0, Duration: 6, Effects: [{Id: 25b, Amplifier: 30b, Duration: 6, ShowParticles: 0b}]}
execute if entity @s[type=!player] run data modify entity @s ActiveEffects append value {Id: 25, Duration: 6, Amplifier: 30b, ShowIcon: 0b, ShowParticles: 0b, Ambient: 0b}
```

### reaper_framework

`@function_tag reaper_framework:__internal__/event_handler/on_server_load`

```json
{
  "values": [
    "effect_basic:reaper_framework/event/on_server_load"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_server_tick`

```json
{
  "values": [
    "effect_basic:reaper_framework/event/on_server_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_tick`

```json
{
  "values": [
    "effect_basic:reaper_framework/event/on_player_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_join`

```json
{
  "values": [
    "effect_basic:reaper_framework/event/on_player_join"
  ]
}
```

`@function reaper_framework:__internal__/event_handler/on_server_load/load`

```mcfunction
function #reaper_framework:__internal__/event_handler/on_server_load
```

`@function reaper_framework:__internal__/event_handler/on_player_join/join`

```mcfunction
scoreboard players set @s reaper_framework.event_handler.on_player_join 0
function #reaper_framework:__internal__/event_handler/on_player_join
```

`@function reaper_framework:__internal__/event_handler/on_server_tick/tick`

```mcfunction
schedule function reaper_framework:__internal__/event_handler/on_server_tick/tick 1
function #reaper_framework:__internal__/event_handler/on_server_tick
```

### minecraft

`@function_tag minecraft:load`

```json
{
  "values": [
    "reaper_framework:__internal__/event_handler/on_server_load/load"
  ]
}
```

### effect_basic

`@function effect_basic:reaper_framework/event/on_server_load`

```mcfunction
function effect_basic:reaper_framework/__internal__/scoreboard/init
function effect_basic:reaper_framework/__internal__/scoreboard/init_defaults
function effect_basic:reaper_framework/__internal__/var/flush_memory
function effect_basic:reaper_framework/__internal__/var/init_defaults
execute as @a run function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/event_handler/on_server_tick/tick
execute as @a run function reaper_framework:__internal__/loop/reset_joining_player
execute store result score $10 effect_basic.reaper_framework.var run gamerule doMobLoot
execute if score $10 effect_basic.reaper_framework.var matches 0 run function effect_basic:reaper_framework/__internal__/mob_loot_gamerule_error
```

`@function effect_basic:reaper_framework/__internal__/scoreboard/init`

```mcfunction
scoreboard objectives add effect_basic.reaper_framework.var dummy {"text": "effect_basic.reaper_framework.var", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.user dummy {"text": "reaper_framework.entity_nbt.user", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.cloud dummy {"text": "reaper_framework.entity_nbt.cloud", "color": "#bf0000"}
scoreboard objectives add effect_basic.reaper_framework.death_events dummy {"text": "effect_basic.reaper_framework.death_events", "color": "#bf0000"}
scoreboard objectives add reaper_framework.sleep.dim_id dummy {"text": "reaper_framework.sleep.dim_id", "color": "#bf0000"}
scoreboard objectives add reaper_framework.event_handler.on_player_join custom:leave_game {"text": "reaper_framework.event_handler.on_player_join", "color": "#bf0000"}
```

`@function effect_basic:reaper_framework/event/on_server_tick`

```mcfunction
execute as @a at @s run function #reaper_framework:__internal__/event_handler/on_player_tick
```

`@function effect_basic:reaper_framework/event/on_player_tick`

```mcfunction
execute if score @s reaper_framework.event_handler.on_player_join matches -1 run function reaper_framework:__internal__/event_handler/on_player_join/join
execute if score @s reaper_framework.event_handler.on_player_join matches 1.. run scoreboard players set @s reaper_framework.event_handler.on_player_join -1
```

`@function effect_basic:reaper_framework/event/on_player_join`

```mcfunction
function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/loop/reset_joining_player
```

`@function effect_basic:reaper_framework/__internal__/mob_loot_gamerule_error`

```mcfunction
gamerule doMobLoot true
tellraw @a [{"text": "\nreapermc ", "color": "gray"}, {"text": " Gamerule 'doMobLoot' was changed to 'True'. ", "color": "red"}, {"text": "Explanation", "color": "red", "underlined": true, "hoverEvent": {"action": "show_text", "contents": [{"text": "ReaperMC Docs: How to disable doMobLoot.", "color": "gray"}]}, "clickEvent": {"action": "open_url", "value": "https://github.com/reapermc/reapermc/tree/main/docs/misc/mob_loot_gamerule.md"}}, {"text": ".", "color": "red", "hoverEvent": {"action": "show_text", "contents": ""}}]
```

`@function effect_basic:reaper_framework/uninstall`

```mcfunction
function effect_basic:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l
function effect_basic:reaper_framework/var/u_n_i_n_s_t_a_l_l
```

`@function effect_basic:reaper_framework/var/u_n_i_n_s_t_a_l_l`

```mcfunction
data remove storage effect_basic:reaper_framework.var data
```

`@function effect_basic:reaper_framework/__internal__/var/flush_memory`

```mcfunction
data modify storage effect_basic:reaper_framework.var data set value [{}, {}, {}, {}, {}, {}, {}]
```

`@function effect_basic:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l`

```mcfunction
scoreboard objectives remove effect_basic.reaper_framework.var
scoreboard objectives remove effect_basic.reaper_framework.death_events
```