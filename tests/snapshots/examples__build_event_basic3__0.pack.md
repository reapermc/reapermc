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

### reaper_framework

`@function_tag reaper_framework:__internal__/event_handler/on_server_load`

```json
{
  "values": [
    "event_basic3:reaper_framework/event/on_server_load"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_server_tick`

```json
{
  "values": [
    "event_basic3:reaper_framework/event/on_server_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_tick`

```json
{
  "values": [
    "event_basic3:reaper_framework/event/on_player_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_join`

```json
{
  "values": [
    "event_basic3:reaper_framework/event/on_player_join"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_glide_start`

```json
{
  "values": [
    "event_basic3:reaper_framework/event/on_player_glide_start"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_land`

```json
{
  "values": [
    "event_basic3:reaper_framework/event/on_player_land"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_jump`

```json
{
  "values": [
    "event_basic3:reaper_framework/event/on_player_jump"
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

`@function reaper_framework:__internal__/event_handler/on_player_glide_start/trigger`

```mcfunction
tag @s add reaper_framework.event_handler.on_player_glide_start.triggered
function #reaper_framework:__internal__/event_handler/on_player_glide_start
```

`@function reaper_framework:__internal__/flag_handler/is_gliding/__condition__`

```mcfunction
execute store result score $2 event_basic3.reaper_framework.var if predicate reaper_framework:__internal__/flag_handler/is_gliding/is_gliding
```

`@function reaper_framework:__internal__/event_handler/on_player_land/trigger`

```mcfunction
tag @s remove reaper_framework.event_handler.on_player_land.available
function #reaper_framework:__internal__/event_handler/on_player_land
```

`@function reaper_framework:__internal__/flag_handler/is_in_air/__condition__`

```mcfunction
execute store result score $2 event_basic3.reaper_framework.var if predicate reaper_framework:__internal__/flag_handler/is_in_air/is_in_air
```

`@function reaper_framework:__internal__/event_handler/on_player_jump/jump`

```mcfunction
scoreboard players set @s reaper_framework.event_handler.on_player_jump 0
function #reaper_framework:__internal__/event_handler/on_player_jump
```

`@predicate reaper_framework:__internal__/flag_handler/is_gliding/is_gliding`

```json
{
  "condition": "minecraft:entity_properties",
  "entity": "this",
  "predicate": {
    "nbt": "{FallFlying: 1b}"
  }
}
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

### minecraft

`@function_tag minecraft:load`

```json
{
  "values": [
    "reaper_framework:__internal__/event_handler/on_server_load/load"
  ]
}
```

### event_basic3

`@function event_basic3:reaper_framework/event/on_server_load`

```mcfunction
function event_basic3:reaper_framework/__internal__/scoreboard/init
function event_basic3:reaper_framework/__internal__/scoreboard/init_defaults
function event_basic3:reaper_framework/__internal__/var/flush_memory
function event_basic3:reaper_framework/__internal__/var/init_defaults
execute as @a run function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/event_handler/on_server_tick/tick
execute as @a run function reaper_framework:__internal__/loop/reset_joining_player
execute store result score $10 event_basic3.reaper_framework.var run gamerule doMobLoot
execute if score $10 event_basic3.reaper_framework.var matches 0 run function event_basic3:reaper_framework/__internal__/mob_loot_gamerule_error
```

`@function event_basic3:reaper_framework/__internal__/scoreboard/init`

```mcfunction
scoreboard objectives add event_basic3.reaper_framework.var dummy {"text": "event_basic3.reaper_framework.var", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.user dummy {"text": "reaper_framework.entity_nbt.user", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.cloud dummy {"text": "reaper_framework.entity_nbt.cloud", "color": "#bf0000"}
scoreboard objectives add event_basic3.reaper_framework.death_events dummy {"text": "event_basic3.reaper_framework.death_events", "color": "#bf0000"}
scoreboard objectives add reaper_framework.sleep.dim_id dummy {"text": "reaper_framework.sleep.dim_id", "color": "#bf0000"}
scoreboard objectives add reaper_framework.event_handler.on_player_join custom:leave_game {"text": "reaper_framework.event_handler.on_player_join", "color": "#bf0000"}
scoreboard objectives add reaper_framework.event_handler.on_player_jump custom:jump {"text": "reaper_framework.event_handler.on_player_jump", "color": "#bf0000"}
```

`@function event_basic3:reaper_framework/event/on_server_tick`

```mcfunction
execute as @a at @s run function #reaper_framework:__internal__/event_handler/on_player_tick
```

`@function event_basic3:reaper_framework/event/on_player_tick`

```mcfunction
execute if score @s reaper_framework.event_handler.on_player_join matches -1 run function reaper_framework:__internal__/event_handler/on_player_join/join
execute if score @s reaper_framework.event_handler.on_player_join matches 1.. run scoreboard players set @s reaper_framework.event_handler.on_player_join -1
function reaper_framework:__internal__/flag_handler/is_gliding/__condition__
execute if score $2 event_basic3.reaper_framework.var matches 1 if entity @s[tag=!reaper_framework.event_handler.on_player_glide_start.triggered] run function reaper_framework:__internal__/event_handler/on_player_glide_start/trigger
execute if score $2 event_basic3.reaper_framework.var matches 0 run tag @s remove reaper_framework.event_handler.on_player_glide_start.triggered
function reaper_framework:__internal__/flag_handler/is_in_air/__condition__
execute if score $2 event_basic3.reaper_framework.var matches 1 run tag @s add reaper_framework.event_handler.on_player_land.available
execute if score $2 event_basic3.reaper_framework.var matches 0 if entity @s[tag=reaper_framework.event_handler.on_player_land.available] run function reaper_framework:__internal__/event_handler/on_player_land/trigger
execute if score @s reaper_framework.event_handler.on_player_jump matches 1.. run function reaper_framework:__internal__/event_handler/on_player_jump/jump
```

`@function event_basic3:reaper_framework/event/on_player_join`

```mcfunction
function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/loop/reset_joining_player
```

`@function event_basic3:reaper_framework/event/on_player_glide_start`

```mcfunction
execute rotated ~180 -35 run function delta:api/launch_looking
```

`@function event_basic3:reaper_framework/event/on_player_land`

```mcfunction
item replace entity @s armor.chest with elytra
```

`@function event_basic3:reaper_framework/event/on_player_jump`

```mcfunction
say <event_basic3> jumped!
```

`@function event_basic3:reaper_framework/__internal__/mob_loot_gamerule_error`

```mcfunction
gamerule doMobLoot true
tellraw @a [{"text": "\nreapermc ", "color": "gray"}, {"text": " Gamerule 'doMobLoot' was changed to 'True'. ", "color": "red"}, {"text": "Explanation", "color": "red", "underlined": true, "hoverEvent": {"action": "show_text", "contents": [{"text": "ReaperMC Docs: How to disable doMobLoot.", "color": "gray"}]}, "clickEvent": {"action": "open_url", "value": "https://github.com/reapermc/reapermc/tree/main/docs/misc/mob_loot_gamerule.md"}}, {"text": ".", "color": "red", "hoverEvent": {"action": "show_text", "contents": ""}}]
```

`@function event_basic3:reaper_framework/uninstall`

```mcfunction
function event_basic3:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l
function event_basic3:reaper_framework/var/u_n_i_n_s_t_a_l_l
```

`@function event_basic3:reaper_framework/var/u_n_i_n_s_t_a_l_l`

```mcfunction
data remove storage event_basic3:reaper_framework.var data
```

`@function event_basic3:reaper_framework/__internal__/var/flush_memory`

```mcfunction
data modify storage event_basic3:reaper_framework.var data set value [{}, {}, {}, {}, {}, {}, {}]
```

`@function event_basic3:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l`

```mcfunction
scoreboard objectives remove event_basic3.reaper_framework.var
scoreboard objectives remove event_basic3.reaper_framework.death_events
```
