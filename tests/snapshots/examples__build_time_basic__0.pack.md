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

`@function demo:main/nested_execute_0`

```mcfunction
effect give @s instant_health
say heal!
```

`@function demo:main/nested_execute_1`

```mcfunction
effect give @s instant_damage
say damage!
```

`@function demo:test`

```mcfunction
time set 324
execute store result score $4 time_basic.reaper_framework.var run time query daytime
scoreboard players operation $26 time_basic.reaper_framework.var = $4 time_basic.reaper_framework.var
```

`@function demo:test2`

```mcfunction
scoreboard players set $26 time_basic.reaper_framework.var 1234
scoreboard players operation $4 time_basic.reaper_framework.var = $26 time_basic.reaper_framework.var
function time_basic:reaper_framework/__internal__/set_time/start
```

`@function demo:example`

```mcfunction
execute store result score $4 time_basic.reaper_framework.var run time query daytime
execute unless score $4 time_basic.reaper_framework.var matches 13000.. run function demo:main/nested_execute_0
execute if score $4 time_basic.reaper_framework.var matches 13000.. run function demo:main/nested_execute_1
```

### reaper_framework

`@function_tag reaper_framework:__internal__/event_handler/on_server_load`

```json
{
  "values": [
    "time_basic:reaper_framework/event/on_server_load"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_server_tick`

```json
{
  "values": [
    "time_basic:reaper_framework/event/on_server_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_tick`

```json
{
  "values": [
    "time_basic:reaper_framework/event/on_player_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_join`

```json
{
  "values": [
    "time_basic:reaper_framework/event/on_player_join"
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
execute unless score $17 time_basic.reaper_framework.var = $17 time_basic.reaper_framework.var store result score $17 time_basic.reaper_framework.var run seed
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

### time_basic

`@function time_basic:reaper_framework/event/on_server_load`

```mcfunction
function time_basic:reaper_framework/__internal__/scoreboard/init
function time_basic:reaper_framework/__internal__/scoreboard/init_defaults
function time_basic:reaper_framework/__internal__/var/flush_memory
function time_basic:reaper_framework/__internal__/var/init_defaults
execute as @a run function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/event_handler/on_server_tick/tick
execute as @a run function reaper_framework:__internal__/loop/reset_joining_player
scoreboard players set $19 time_basic.reaper_framework.var 1630111353
scoreboard players set $20 time_basic.reaper_framework.var 1623164762
scoreboard players set $21 time_basic.reaper_framework.var 2147483647
function reaper_framework:__internal__/math/random/init
forceload add 0 0
kill @e[type=marker, tag=reaper_framework.math]
summon marker 0.0 0.0 0.0 {Tags: ["reaper_framework.math"], CustomName: '{"text": "reaper_framework.math", "color": "#bf0000"}'}
```

`@function time_basic:reaper_framework/__internal__/scoreboard/init`

```mcfunction
scoreboard objectives add time_basic.reaper_framework.var dummy {"text": "time_basic.reaper_framework.var", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.user dummy {"text": "reaper_framework.entity_nbt.user", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.cloud dummy {"text": "reaper_framework.entity_nbt.cloud", "color": "#bf0000"}
scoreboard objectives add time_basic.reaper_framework.death_events dummy {"text": "time_basic.reaper_framework.death_events", "color": "#bf0000"}
scoreboard objectives add reaper_framework.sleep.dim_id dummy {"text": "reaper_framework.sleep.dim_id", "color": "#bf0000"}
scoreboard objectives add reaper_framework.event_handler.on_player_join custom:leave_game {"text": "reaper_framework.event_handler.on_player_join", "color": "#bf0000"}
```

`@function time_basic:reaper_framework/event/on_server_tick`

```mcfunction
execute as @a at @s run function #reaper_framework:__internal__/event_handler/on_player_tick
```

`@function time_basic:reaper_framework/event/on_player_tick`

```mcfunction
execute if score @s reaper_framework.event_handler.on_player_join matches -1 run function reaper_framework:__internal__/event_handler/on_player_join/join
execute if score @s reaper_framework.event_handler.on_player_join matches 1.. run scoreboard players set @s reaper_framework.event_handler.on_player_join -1
```

`@function time_basic:reaper_framework/event/on_player_join`

```mcfunction
function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/loop/reset_joining_player
```

`@function time_basic:reaper_framework/__internal__/set_time/32768`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 32768
time add 32768
```

`@function time_basic:reaper_framework/__internal__/set_time/16384`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 16384
time add 16384
```

`@function time_basic:reaper_framework/__internal__/set_time/8192`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 8192
time add 8192
```

`@function time_basic:reaper_framework/__internal__/set_time/4096`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 4096
time add 4096
```

`@function time_basic:reaper_framework/__internal__/set_time/2048`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 2048
time add 2048
```

`@function time_basic:reaper_framework/__internal__/set_time/1024`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 1024
time add 1024
```

`@function time_basic:reaper_framework/__internal__/set_time/512`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 512
time add 512
```

`@function time_basic:reaper_framework/__internal__/set_time/256`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 256
time add 256
```

`@function time_basic:reaper_framework/__internal__/set_time/128`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 128
time add 128
```

`@function time_basic:reaper_framework/__internal__/set_time/64`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 64
time add 64
```

`@function time_basic:reaper_framework/__internal__/set_time/32`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 32
time add 32
```

`@function time_basic:reaper_framework/__internal__/set_time/16`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 16
time add 16
```

`@function time_basic:reaper_framework/__internal__/set_time/8`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 8
time add 8
```

`@function time_basic:reaper_framework/__internal__/set_time/4`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 4
time add 4
```

`@function time_basic:reaper_framework/__internal__/set_time/2`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 2
time add 2
```

`@function time_basic:reaper_framework/__internal__/set_time/1`

```mcfunction
scoreboard players remove $4 time_basic.reaper_framework.var 1
time add 1
```

`@function time_basic:reaper_framework/__internal__/set_time/start`

```mcfunction
time set 0
execute if score $4 time_basic.reaper_framework.var matches 32768.. run function time_basic:reaper_framework/__internal__/set_time/32768
execute if score $4 time_basic.reaper_framework.var matches 16384.. run function time_basic:reaper_framework/__internal__/set_time/16384
execute if score $4 time_basic.reaper_framework.var matches 8192.. run function time_basic:reaper_framework/__internal__/set_time/8192
execute if score $4 time_basic.reaper_framework.var matches 4096.. run function time_basic:reaper_framework/__internal__/set_time/4096
execute if score $4 time_basic.reaper_framework.var matches 2048.. run function time_basic:reaper_framework/__internal__/set_time/2048
execute if score $4 time_basic.reaper_framework.var matches 1024.. run function time_basic:reaper_framework/__internal__/set_time/1024
execute if score $4 time_basic.reaper_framework.var matches 512.. run function time_basic:reaper_framework/__internal__/set_time/512
execute if score $4 time_basic.reaper_framework.var matches 256.. run function time_basic:reaper_framework/__internal__/set_time/256
execute if score $4 time_basic.reaper_framework.var matches 128.. run function time_basic:reaper_framework/__internal__/set_time/128
execute if score $4 time_basic.reaper_framework.var matches 64.. run function time_basic:reaper_framework/__internal__/set_time/64
execute if score $4 time_basic.reaper_framework.var matches 32.. run function time_basic:reaper_framework/__internal__/set_time/32
execute if score $4 time_basic.reaper_framework.var matches 16.. run function time_basic:reaper_framework/__internal__/set_time/16
execute if score $4 time_basic.reaper_framework.var matches 8.. run function time_basic:reaper_framework/__internal__/set_time/8
execute if score $4 time_basic.reaper_framework.var matches 4.. run function time_basic:reaper_framework/__internal__/set_time/4
execute if score $4 time_basic.reaper_framework.var matches 2.. run function time_basic:reaper_framework/__internal__/set_time/2
execute if score $4 time_basic.reaper_framework.var matches 1.. run function time_basic:reaper_framework/__internal__/set_time/1
```

`@function time_basic:reaper_framework/uninstall`

```mcfunction
function time_basic:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l
function time_basic:reaper_framework/var/u_n_i_n_s_t_a_l_l
```

`@function time_basic:reaper_framework/var/u_n_i_n_s_t_a_l_l`

```mcfunction
data remove storage time_basic:reaper_framework.var data
```

`@function time_basic:reaper_framework/__internal__/var/flush_memory`

```mcfunction
data modify storage time_basic:reaper_framework.var data set value [{}, {}, {}, {}, {}, {}, {}, {}]
```

`@function time_basic:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l`

```mcfunction
scoreboard objectives remove time_basic.reaper_framework.var
scoreboard objectives remove time_basic.reaper_framework.death_events
```
