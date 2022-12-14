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

`@function demo:test_in_air`

```mcfunction
function reaper_framework:__internal__/flag_handler/is_in_air/__condition__
execute if score $2 flag_basic.reaper_framework.var matches 1 run say 'in air!'
execute if score $2 flag_basic.reaper_framework.var matches 0 run say 'on ground!'
```

`@function demo:test_sneaking`

```mcfunction
function reaper_framework:__internal__/flag_handler/is_sneaking/__condition__
execute if score $2 flag_basic.reaper_framework.var matches 1 run say 'true'
execute if score $2 flag_basic.reaper_framework.var matches 0 run say 'false'
```

### reaper_framework

`@function_tag reaper_framework:__internal__/event_handler/on_server_load`

```json
{
  "values": [
    "flag_basic:reaper_framework/event/on_server_load"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_server_tick`

```json
{
  "values": [
    "flag_basic:reaper_framework/event/on_server_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_tick`

```json
{
  "values": [
    "flag_basic:reaper_framework/event/on_player_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_join`

```json
{
  "values": [
    "flag_basic:reaper_framework/event/on_player_join"
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

`@function reaper_framework:__internal__/math/random/init`

```mcfunction
execute unless score $17 flag_basic.reaper_framework.var = $17 flag_basic.reaper_framework.var store result score $17 flag_basic.reaper_framework.var run seed
```

`@function reaper_framework:__internal__/flag_handler/is_in_air/__condition__`

```mcfunction
execute store result score $2 flag_basic.reaper_framework.var if predicate reaper_framework:__internal__/flag_handler/is_in_air/is_in_air
```

`@function reaper_framework:__internal__/flag_handler/is_sneaking/__condition__`

```mcfunction
execute store result score $2 flag_basic.reaper_framework.var if predicate reaper_framework:__internal__/flag_handler/is_sneaking/is_sneaking
```

`@predicate reaper_framework:__internal__/flag_handler/is_in_air/is_in_air`

```json
{
  "condition": "minecraft:entity_properties",
  "entity": "this",
  "predicate": {
    "nbt": "{OnGround: 0b}"
  }
}
```

`@predicate reaper_framework:__internal__/flag_handler/is_sneaking/is_sneaking`

```json
{
  "condition": "minecraft:entity_properties",
  "entity": "this",
  "predicate": {
    "flags": {
      "is_sneaking": true
    }
  }
}
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

### flag_basic

`@function flag_basic:reaper_framework/event/on_server_load`

```mcfunction
function flag_basic:reaper_framework/__internal__/scoreboard/init
function flag_basic:reaper_framework/__internal__/scoreboard/init_defaults
function flag_basic:reaper_framework/__internal__/var/flush_memory
function flag_basic:reaper_framework/__internal__/var/init_defaults
execute as @a run function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/event_handler/on_server_tick/tick
execute as @a run function reaper_framework:__internal__/loop/reset_joining_player
scoreboard players set $19 flag_basic.reaper_framework.var 1630111353
scoreboard players set $20 flag_basic.reaper_framework.var 1623164762
scoreboard players set $21 flag_basic.reaper_framework.var 2147483647
function reaper_framework:__internal__/math/random/init
forceload add 0 0
kill @e[type=marker, tag=reaper_framework.math]
summon marker 0.0 0.0 0.0 {Tags: ["reaper_framework.math"], CustomName: '{"text": "reaper_framework.math", "color": "#bf0000"}'}
execute store result score $26 flag_basic.reaper_framework.var run gamerule doMobLoot
execute if score $26 flag_basic.reaper_framework.var matches 0 run function flag_basic:reaper_framework/__internal__/mob_loot_gamerule_error
```

`@function flag_basic:reaper_framework/__internal__/scoreboard/init`

```mcfunction
scoreboard objectives add flag_basic.reaper_framework.var dummy {"text": "flag_basic.reaper_framework.var", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.user dummy {"text": "reaper_framework.entity_nbt.user", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.cloud dummy {"text": "reaper_framework.entity_nbt.cloud", "color": "#bf0000"}
scoreboard objectives add flag_basic.reaper_framework.death_events dummy {"text": "flag_basic.reaper_framework.death_events", "color": "#bf0000"}
scoreboard objectives add reaper_framework.sleep.dim_id dummy {"text": "reaper_framework.sleep.dim_id", "color": "#bf0000"}
scoreboard objectives add reaper_framework.event_handler.on_player_join custom:leave_game {"text": "reaper_framework.event_handler.on_player_join", "color": "#bf0000"}
```

`@function flag_basic:reaper_framework/event/on_server_tick`

```mcfunction
execute as @a at @s run function #reaper_framework:__internal__/event_handler/on_player_tick
```

`@function flag_basic:reaper_framework/event/on_player_tick`

```mcfunction
execute if score @s reaper_framework.event_handler.on_player_join matches -1 run function reaper_framework:__internal__/event_handler/on_player_join/join
execute if score @s reaper_framework.event_handler.on_player_join matches 1.. run scoreboard players set @s reaper_framework.event_handler.on_player_join -1
```

`@function flag_basic:reaper_framework/event/on_player_join`

```mcfunction
function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/loop/reset_joining_player
```

`@function flag_basic:reaper_framework/__internal__/mob_loot_gamerule_error`

```mcfunction
gamerule doMobLoot true
tellraw @a [{"text": "\nreapermc ", "color": "gray"}, {"text": " WARN Gamerule 'doMobLoot' was changed to 'True'. ", "color": "gold"}, {"text": "Explanation", "color": "gold", "underlined": true, "hoverEvent": {"action": "show_text", "contents": [{"text": "ReaperMC Docs: How to disable doMobLoot.", "color": "gray"}]}, "clickEvent": {"action": "open_url", "value": "https://github.com/reapermc/reapermc/tree/main/docs/misc/mob_loot_gamerule.md"}}, {"text": ".", "color": "gold", "hoverEvent": {"action": "show_text", "contents": [{"text": "", "color": "gray"}]}}]
```

`@function flag_basic:reaper_framework/uninstall`

```mcfunction
function flag_basic:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l
function flag_basic:reaper_framework/var/u_n_i_n_s_t_a_l_l
```

`@function flag_basic:reaper_framework/var/u_n_i_n_s_t_a_l_l`

```mcfunction
data remove storage flag_basic:reaper_framework.var data
```

`@function flag_basic:reaper_framework/__internal__/var/flush_memory`

```mcfunction
data modify storage flag_basic:reaper_framework.var data set value [{}, {}, {}, {}, {}, {}, {}, {}]
```

`@function flag_basic:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l`

```mcfunction
scoreboard objectives remove flag_basic.reaper_framework.var
scoreboard objectives remove flag_basic.reaper_framework.death_events
```
