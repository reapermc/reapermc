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
    "project_name_with_spaces:reaper_framework/event/on_server_load"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_server_tick`

```json
{
  "values": [
    "project_name_with_spaces:reaper_framework/event/on_server_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_tick`

```json
{
  "values": [
    "project_name_with_spaces:reaper_framework/event/on_player_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_join`

```json
{
  "values": [
    "project_name_with_spaces:reaper_framework/event/on_player_join"
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
execute unless score $17 project_name_with_spaces.reaper_framework.var = $17 project_name_with_spaces.reaper_framework.var store result score $17 project_name_with_spaces.reaper_framework.var run seed
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

### project_name_with_spaces

`@function project_name_with_spaces:reaper_framework/event/on_server_load`

```mcfunction
function project_name_with_spaces:reaper_framework/__internal__/scoreboard/init
function project_name_with_spaces:reaper_framework/__internal__/scoreboard/init_defaults
function project_name_with_spaces:reaper_framework/__internal__/var/flush_memory
function project_name_with_spaces:reaper_framework/__internal__/var/init_defaults
execute as @a run function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/event_handler/on_server_tick/tick
execute as @a run function reaper_framework:__internal__/loop/reset_joining_player
scoreboard players set $19 project_name_with_spaces.reaper_framework.var 1630111353
scoreboard players set $20 project_name_with_spaces.reaper_framework.var 1623164762
scoreboard players set $21 project_name_with_spaces.reaper_framework.var 2147483647
function reaper_framework:__internal__/math/random/init
forceload add 0 0
kill @e[type=marker, tag=reaper_framework.math]
summon marker 0.0 0.0 0.0 {Tags: ["reaper_framework.math"], CustomName: '{"text": "reaper_framework.math", "color": "#bf0000"}'}
say hello!
```

`@function project_name_with_spaces:reaper_framework/__internal__/scoreboard/init`

```mcfunction
scoreboard objectives add project_name_with_spaces.reaper_framework.var dummy {"text": "project_name_with_spaces.reaper_framework.var", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.user dummy {"text": "reaper_framework.entity_nbt.user", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.cloud dummy {"text": "reaper_framework.entity_nbt.cloud", "color": "#bf0000"}
scoreboard objectives add project_name_with_spaces.reaper_framework.death_events dummy {"text": "project_name_with_spaces.reaper_framework.death_events", "color": "#bf0000"}
scoreboard objectives add reaper_framework.sleep.dim_id dummy {"text": "reaper_framework.sleep.dim_id", "color": "#bf0000"}
scoreboard objectives add reaper_framework.event_handler.on_player_join custom:leave_game {"text": "reaper_framework.event_handler.on_player_join", "color": "#bf0000"}
```

`@function project_name_with_spaces:reaper_framework/event/on_server_tick`

```mcfunction
execute as @a at @s run function #reaper_framework:__internal__/event_handler/on_player_tick
```

`@function project_name_with_spaces:reaper_framework/event/on_player_tick`

```mcfunction
execute if score @s reaper_framework.event_handler.on_player_join matches -1 run function reaper_framework:__internal__/event_handler/on_player_join/join
execute if score @s reaper_framework.event_handler.on_player_join matches 1.. run scoreboard players set @s reaper_framework.event_handler.on_player_join -1
```

`@function project_name_with_spaces:reaper_framework/event/on_player_join`

```mcfunction
function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/loop/reset_joining_player
```

`@function project_name_with_spaces:reaper_framework/uninstall`

```mcfunction
function project_name_with_spaces:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l
function project_name_with_spaces:reaper_framework/var/u_n_i_n_s_t_a_l_l
```

`@function project_name_with_spaces:reaper_framework/var/u_n_i_n_s_t_a_l_l`

```mcfunction
data remove storage project_name_with_spaces:reaper_framework.var data
```

`@function project_name_with_spaces:reaper_framework/__internal__/var/flush_memory`

```mcfunction
data modify storage project_name_with_spaces:reaper_framework.var data set value [{}, {}, {}, {}, {}, {}, {}, {}]
```

`@function project_name_with_spaces:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l`

```mcfunction
scoreboard objectives remove project_name_with_spaces.reaper_framework.var
scoreboard objectives remove project_name_with_spaces.reaper_framework.death_events
```
