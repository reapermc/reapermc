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

`@function demo:scb_const`

```mcfunction
execute unless score @s scb matches 69.. run say 'scb < 69'
execute if score @s scb matches 69.. run say 'scb >= 69'
```

`@function demo:scb_scb`

```mcfunction
execute if score @s scb < @s scb run say 'scb < scb'
execute if score @s scb >= @s scb run say 'scb >= scb'
```

`@function demo:scb_stge`

```mcfunction
execute store result score $0 expr_basic2.reaper_framework.var run data get storage stge:stge stge 1
execute if score @s scb < $0 expr_basic2.reaper_framework.var run say 'scb < stge'
execute if score @s scb >= $0 expr_basic2.reaper_framework.var run say 'scb >= stge'
```

`@function demo:stge_const`

```mcfunction
execute store result score $0 expr_basic2.reaper_framework.var run data get storage stge:stge stge 1
execute unless score $0 expr_basic2.reaper_framework.var matches 69.. run say 'stge < 69'
execute if score $0 expr_basic2.reaper_framework.var matches 69.. run say 'stge >= 69'
```

`@function demo:stge_scb`

```mcfunction
execute store result score $0 expr_basic2.reaper_framework.var run data get storage stge:stge stge 1
execute if score $0 expr_basic2.reaper_framework.var < @s scb run say 'stge < scb'
execute if score $0 expr_basic2.reaper_framework.var >= @s scb run say 'stge >= scb'
```

`@function demo:stge_stge`

```mcfunction
execute store result score $0 expr_basic2.reaper_framework.var run data get storage stge:stge stge 1
execute store result score $1 expr_basic2.reaper_framework.var run data get storage stge:stge stge 1
execute if score $0 expr_basic2.reaper_framework.var < $1 expr_basic2.reaper_framework.var run say 'stge < stge'
execute if score $0 expr_basic2.reaper_framework.var >= $1 expr_basic2.reaper_framework.var run say 'stge >= stge'
```

### reaper_framework

`@function_tag reaper_framework:__internal__/event_handler/on_server_load`

```json
{
  "values": [
    "expr_basic2:reaper_framework/event/on_server_load"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_server_tick`

```json
{
  "values": [
    "expr_basic2:reaper_framework/event/on_server_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_tick`

```json
{
  "values": [
    "expr_basic2:reaper_framework/event/on_player_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_join`

```json
{
  "values": [
    "expr_basic2:reaper_framework/event/on_player_join"
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

### expr_basic2

`@function expr_basic2:reaper_framework/event/on_server_load`

```mcfunction
function expr_basic2:reaper_framework/__internal__/scoreboard/init
function expr_basic2:reaper_framework/__internal__/scoreboard/init_defaults
function expr_basic2:reaper_framework/__internal__/var/flush_memory
function expr_basic2:reaper_framework/__internal__/var/init_defaults
execute as @a run function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/event_handler/on_server_tick/tick
execute as @a run function reaper_framework:__internal__/loop/reset_joining_player
execute store result score $14 expr_basic2.reaper_framework.var run gamerule doMobLoot
execute if score $14 expr_basic2.reaper_framework.var matches 0 run function expr_basic2:reaper_framework/__internal__/mob_loot_gamerule_error
```

`@function expr_basic2:reaper_framework/__internal__/scoreboard/init`

```mcfunction
scoreboard objectives add expr_basic2.reaper_framework.var dummy {"text": "expr_basic2.reaper_framework.var", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.user dummy {"text": "reaper_framework.entity_nbt.user", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.cloud dummy {"text": "reaper_framework.entity_nbt.cloud", "color": "#bf0000"}
scoreboard objectives add expr_basic2.reaper_framework.death_events dummy {"text": "expr_basic2.reaper_framework.death_events", "color": "#bf0000"}
scoreboard objectives add reaper_framework.sleep.dim_id dummy {"text": "reaper_framework.sleep.dim_id", "color": "#bf0000"}
scoreboard objectives add reaper_framework.event_handler.on_player_join custom:leave_game {"text": "reaper_framework.event_handler.on_player_join", "color": "#bf0000"}
scoreboard objectives add scb dummy {"text": "scb", "color": "gold"}
```

`@function expr_basic2:reaper_framework/event/on_server_tick`

```mcfunction
execute as @a at @s run function #reaper_framework:__internal__/event_handler/on_player_tick
```

`@function expr_basic2:reaper_framework/event/on_player_tick`

```mcfunction
execute if score @s reaper_framework.event_handler.on_player_join matches -1 run function reaper_framework:__internal__/event_handler/on_player_join/join
execute if score @s reaper_framework.event_handler.on_player_join matches 1.. run scoreboard players set @s reaper_framework.event_handler.on_player_join -1
```

`@function expr_basic2:reaper_framework/event/on_player_join`

```mcfunction
function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/loop/reset_joining_player
```

`@function expr_basic2:reaper_framework/__internal__/mob_loot_gamerule_error`

```mcfunction
gamerule doMobLoot true
tellraw @a [{"text": "\nreapermc ", "color": "gray"}, {"text": " Gamerule 'doMobLoot' was changed to 'True'. ", "color": "red"}, {"text": "Explanation", "color": "red", "underlined": true, "hoverEvent": {"action": "show_text", "contents": [{"text": "ReaperMC Docs: How to disable doMobLoot.", "color": "gray"}]}, "clickEvent": {"action": "open_url", "value": "https://github.com/reapermc/reapermc/tree/main/docs/misc/mob_loot_gamerule.md"}}, {"text": ".", "color": "red", "hoverEvent": {"action": "show_text", "contents": ""}}]
```

`@function expr_basic2:reaper_framework/uninstall`

```mcfunction
function expr_basic2:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l
function expr_basic2:reaper_framework/var/u_n_i_n_s_t_a_l_l
```

`@function expr_basic2:reaper_framework/var/u_n_i_n_s_t_a_l_l`

```mcfunction
data remove storage expr_basic2:reaper_framework.var data
```

`@function expr_basic2:reaper_framework/__internal__/var/flush_memory`

```mcfunction
data modify storage expr_basic2:reaper_framework.var data set value [{}, {}, {}, {}, {}, {}, {}]
```

`@function expr_basic2:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l`

```mcfunction
scoreboard objectives remove expr_basic2.reaper_framework.var
scoreboard objectives remove expr_basic2.reaper_framework.death_events
scoreboard objectives remove scb
```
