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
execute store result storage bolt.expr:temp 7o9rjbsscog7r_0 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_0
execute at @s run tp @s ^ ^ ^10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[2] 100
execute store result storage bolt.expr:temp 7o9rjbsscog7r_1 float 0.001 run scoreboard players get $24 math_trig.reaper_framework.var
data modify storage math_trig:reaper_framework.var data[5].v set from storage bolt.expr:temp 7o9rjbsscog7r_1
tp @s 0.0 0.0 0.0
```

`@function demo:main/nested_execute_1`

```mcfunction
execute store result storage bolt.expr:temp 7o9rjbsscog7r_2 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_2
execute at @s run tp @s ^ ^ ^10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[2] 100
execute store result storage bolt.expr:temp 7o9rjbsscog7r_3 float 0.001 run scoreboard players get $24 math_trig.reaper_framework.var
data modify storage math_trig:reaper_framework.var data[5].v set from storage bolt.expr:temp 7o9rjbsscog7r_3
tp @s 0.0 0.0 0.0
```

`@function demo:main/nested_execute_2`

```mcfunction
execute store result storage bolt.expr:temp 7o9rjbsscog7r_4 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_4
execute at @s run tp @s ^ ^ ^10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[2] 100
execute store result storage bolt.expr:temp 7o9rjbsscog7r_5 float 0.001 run scoreboard players get $24 math_trig.reaper_framework.var
data modify storage math_trig:reaper_framework.var data[5].v set from storage bolt.expr:temp 7o9rjbsscog7r_5
tp @s 0.0 0.0 0.0
```

`@function demo:main/nested_execute_3`

```mcfunction
execute store result storage bolt.expr:temp 7o9rjbsscog7r_6 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_6
execute at @s run tp @s ^ ^ ^10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[2] 100
execute store result storage bolt.expr:temp 7o9rjbsscog7r_7 float 0.001 run scoreboard players get $24 math_trig.reaper_framework.var
data modify storage math_trig:reaper_framework.var data[5].v set from storage bolt.expr:temp 7o9rjbsscog7r_7
tp @s 0.0 0.0 0.0
```

`@function demo:main/nested_execute_4`

```mcfunction
execute store result storage bolt.expr:temp 7o9rjbsscog7r_8 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_8
execute at @s run tp @s ^ ^ ^10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[2] 100
execute store result storage bolt.expr:temp 7o9rjbsscog7r_9 float 0.001 run scoreboard players get $24 math_trig.reaper_framework.var
data modify storage math_trig:reaper_framework.var data[5].v set from storage bolt.expr:temp 7o9rjbsscog7r_9
tp @s 0.0 0.0 0.0
```

`@function demo:main/nested_execute_5`

```mcfunction
execute store result storage bolt.expr:temp 7o9rjbsscog7r_10 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_10
execute at @s run tp @s ^ ^ ^-10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[0] 100
execute store result storage bolt.expr:temp 7o9rjbsscog7r_11 float 0.001 run scoreboard players get $24 math_trig.reaper_framework.var
data modify storage math_trig:reaper_framework.var data[5].v set from storage bolt.expr:temp 7o9rjbsscog7r_11
tp @s 0.0 0.0 0.0
```

`@function demo:main/nested_execute_6`

```mcfunction
execute store result storage bolt.expr:temp 7o9rjbsscog7r_12 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_12
execute at @s run tp @s ^ ^ ^-10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[0] 100
execute store result storage bolt.expr:temp 7o9rjbsscog7r_13 float 0.001 run scoreboard players get $24 math_trig.reaper_framework.var
data modify storage math_trig:reaper_framework.var data[5].v set from storage bolt.expr:temp 7o9rjbsscog7r_13
tp @s 0.0 0.0 0.0
```

`@function demo:main/nested_execute_7`

```mcfunction
execute store result storage bolt.expr:temp 7o9rjbsscog7r_14 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_14
execute at @s run tp @s ^ ^ ^-10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[0] 100
execute store result storage bolt.expr:temp 7o9rjbsscog7r_15 float 0.001 run scoreboard players get $24 math_trig.reaper_framework.var
data modify storage math_trig:reaper_framework.var data[5].v set from storage bolt.expr:temp 7o9rjbsscog7r_15
tp @s 0.0 0.0 0.0
```

`@function demo:main/nested_execute_8`

```mcfunction
execute store result storage bolt.expr:temp 7o9rjbsscog7r_16 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_16
execute at @s run tp @s ^ ^ ^-10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[0] 100
execute store result storage bolt.expr:temp 7o9rjbsscog7r_17 float 0.001 run scoreboard players get $24 math_trig.reaper_framework.var
data modify storage math_trig:reaper_framework.var data[5].v set from storage bolt.expr:temp 7o9rjbsscog7r_17
tp @s 0.0 0.0 0.0
```

`@function demo:main/nested_execute_9`

```mcfunction
execute store result storage bolt.expr:temp 7o9rjbsscog7r_18 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_18
execute at @s run tp @s ^ ^ ^-10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[0] 100
execute store result storage bolt.expr:temp 7o9rjbsscog7r_19 float 0.001 run scoreboard players get $24 math_trig.reaper_framework.var
data modify storage math_trig:reaper_framework.var data[5].v set from storage bolt.expr:temp 7o9rjbsscog7r_19
tp @s 0.0 0.0 0.0
```

`@function demo:main/nested_execute_10`

```mcfunction
execute store result storage bolt.expr:temp 7o9rjbsscog7r_20 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_20
execute at @s run tp @s ^ ^ ^10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[2] -100
execute store result score $25 math_trig.reaper_framework.var run data get entity @s Pos[0] 100
scoreboard players operation $25 math_trig.reaper_framework.var *= $1000 bolt.expr.const
scoreboard players operation $25 math_trig.reaper_framework.var /= $24 math_trig.reaper_framework.var
execute store result storage math_trig:reaper_framework.var data[5].v int 1 run scoreboard players get $25 math_trig.reaper_framework.var
tp @s 0.0 0.0 0.0
```

`@function demo:main/nested_execute_11`

```mcfunction
execute store result storage bolt.expr:temp 7o9rjbsscog7r_21 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_21
execute at @s run tp @s ^ ^ ^10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[2] -100
execute store result score $25 math_trig.reaper_framework.var run data get entity @s Pos[0] 100
scoreboard players operation $25 math_trig.reaper_framework.var *= $1000 bolt.expr.const
scoreboard players operation $25 math_trig.reaper_framework.var /= $24 math_trig.reaper_framework.var
execute store result storage math_trig:reaper_framework.var data[5].v int 1 run scoreboard players get $25 math_trig.reaper_framework.var
tp @s 0.0 0.0 0.0
```

`@function demo:main/nested_execute_12`

```mcfunction
execute store result storage bolt.expr:temp 7o9rjbsscog7r_22 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_22
execute at @s run tp @s ^ ^ ^10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[2] -100
execute store result score $25 math_trig.reaper_framework.var run data get entity @s Pos[0] 100
scoreboard players operation $25 math_trig.reaper_framework.var *= $1000 bolt.expr.const
scoreboard players operation $25 math_trig.reaper_framework.var /= $24 math_trig.reaper_framework.var
execute store result storage math_trig:reaper_framework.var data[5].v int 1 run scoreboard players get $25 math_trig.reaper_framework.var
tp @s 0.0 0.0 0.0
```

`@function demo:main/nested_execute_13`

```mcfunction
execute store result storage bolt.expr:temp 7o9rjbsscog7r_23 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_23
execute at @s run tp @s ^ ^ ^10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[2] -100
execute store result score $25 math_trig.reaper_framework.var run data get entity @s Pos[0] 100
scoreboard players operation $25 math_trig.reaper_framework.var *= $1000 bolt.expr.const
scoreboard players operation $25 math_trig.reaper_framework.var /= $24 math_trig.reaper_framework.var
execute store result storage math_trig:reaper_framework.var data[5].v int 1 run scoreboard players get $25 math_trig.reaper_framework.var
tp @s 0.0 0.0 0.0
```

`@function demo:main/nested_execute_14`

```mcfunction
execute store result storage bolt.expr:temp 7o9rjbsscog7r_24 float 1 run scoreboard players get $22 math_trig.reaper_framework.var
data modify entity @s Rotation[0] set from storage bolt.expr:temp 7o9rjbsscog7r_24
execute at @s run tp @s ^ ^ ^10
execute store result score $24 math_trig.reaper_framework.var run data get entity @s Pos[2] -100
execute store result score $25 math_trig.reaper_framework.var run data get entity @s Pos[0] 100
scoreboard players operation $25 math_trig.reaper_framework.var *= $1000 bolt.expr.const
scoreboard players operation $25 math_trig.reaper_framework.var /= $24 math_trig.reaper_framework.var
execute store result storage math_trig:reaper_framework.var data[5].v int 1 run scoreboard players get $25 math_trig.reaper_framework.var
tp @s 0.0 0.0 0.0
```

`@function demo:cos`

```mcfunction
scoreboard players set $22 math_trig.reaper_framework.var 6
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_0
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
scoreboard players set $22 math_trig.reaper_framework.var 12
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_1
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
scoreboard players set $22 math_trig.reaper_framework.var 99999
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_2
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
scoreboard players set $22 math_trig.reaper_framework.var 3333
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_3
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
scoreboard players set $22 math_trig.reaper_framework.var 3336
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_4
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
```

`@function demo:sin`

```mcfunction
scoreboard players set $22 math_trig.reaper_framework.var 6
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_5
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
scoreboard players set $22 math_trig.reaper_framework.var 12
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_6
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
scoreboard players set $22 math_trig.reaper_framework.var 99999
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_7
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
scoreboard players set $22 math_trig.reaper_framework.var 3333
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_8
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
scoreboard players set $22 math_trig.reaper_framework.var 3336
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_9
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
```

`@function demo:tan`

```mcfunction
scoreboard players set $22 math_trig.reaper_framework.var 6
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_10
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
scoreboard players set $22 math_trig.reaper_framework.var 12
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_11
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
scoreboard players set $22 math_trig.reaper_framework.var 99999
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_12
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
scoreboard players set $22 math_trig.reaper_framework.var 3333
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_13
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
scoreboard players set $22 math_trig.reaper_framework.var 3336
execute as @e[type=marker, tag=reaper_framework.math] at @s run function demo:main/nested_execute_14
tellraw @a {"nbt": "data[5].v", "storage": "math_trig:reaper_framework.var"}
```

### reaper_framework

`@function_tag reaper_framework:__internal__/event_handler/on_server_load`

```json
{
  "values": [
    "math_trig:reaper_framework/event/on_server_load"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_server_tick`

```json
{
  "values": [
    "math_trig:reaper_framework/event/on_server_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_tick`

```json
{
  "values": [
    "math_trig:reaper_framework/event/on_player_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_join`

```json
{
  "values": [
    "math_trig:reaper_framework/event/on_player_join"
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
execute unless score $17 math_trig.reaper_framework.var = $17 math_trig.reaper_framework.var store result score $17 math_trig.reaper_framework.var run seed
```

### minecraft

`@function_tag minecraft:load`

```json
{
  "values": [
    "math_trig:init_expressions",
    "reaper_framework:__internal__/event_handler/on_server_load/load"
  ]
}
```

### math_trig

`@function math_trig:reaper_framework/event/on_server_load`

```mcfunction
function math_trig:reaper_framework/__internal__/scoreboard/init
function math_trig:reaper_framework/__internal__/scoreboard/init_defaults
function math_trig:reaper_framework/__internal__/var/flush_memory
function math_trig:reaper_framework/__internal__/var/init_defaults
execute as @a run function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/event_handler/on_server_tick/tick
execute as @a run function reaper_framework:__internal__/loop/reset_joining_player
scoreboard players set $19 math_trig.reaper_framework.var 1630111353
scoreboard players set $20 math_trig.reaper_framework.var 1623164762
scoreboard players set $21 math_trig.reaper_framework.var 2147483647
function reaper_framework:__internal__/math/random/init
forceload add 0 0
kill @e[type=marker, tag=reaper_framework.math]
summon marker 0.0 0.0 0.0 {Tags: ["reaper_framework.math"], CustomName: '{"text": "reaper_framework.math", "color": "#bf0000"}'}
execute store result score $26 math_trig.reaper_framework.var run gamerule doMobLoot
execute if score $26 math_trig.reaper_framework.var matches 0 run function math_trig:reaper_framework/__internal__/mob_loot_gamerule_error
```

`@function math_trig:reaper_framework/__internal__/scoreboard/init`

```mcfunction
scoreboard objectives add math_trig.reaper_framework.var dummy {"text": "math_trig.reaper_framework.var", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.user dummy {"text": "reaper_framework.entity_nbt.user", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.cloud dummy {"text": "reaper_framework.entity_nbt.cloud", "color": "#bf0000"}
scoreboard objectives add math_trig.reaper_framework.death_events dummy {"text": "math_trig.reaper_framework.death_events", "color": "#bf0000"}
scoreboard objectives add reaper_framework.sleep.dim_id dummy {"text": "reaper_framework.sleep.dim_id", "color": "#bf0000"}
scoreboard objectives add reaper_framework.event_handler.on_player_join custom:leave_game {"text": "reaper_framework.event_handler.on_player_join", "color": "#bf0000"}
```

`@function math_trig:reaper_framework/event/on_server_tick`

```mcfunction
execute as @a at @s run function #reaper_framework:__internal__/event_handler/on_player_tick
```

`@function math_trig:reaper_framework/event/on_player_tick`

```mcfunction
execute if score @s reaper_framework.event_handler.on_player_join matches -1 run function reaper_framework:__internal__/event_handler/on_player_join/join
execute if score @s reaper_framework.event_handler.on_player_join matches 1.. run scoreboard players set @s reaper_framework.event_handler.on_player_join -1
```

`@function math_trig:reaper_framework/event/on_player_join`

```mcfunction
function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/loop/reset_joining_player
```

`@function math_trig:reaper_framework/__internal__/mob_loot_gamerule_error`

```mcfunction
gamerule doMobLoot true
tellraw @a [{"text": "\nreapermc ", "color": "gray"}, {"text": " WARN Gamerule 'doMobLoot' was changed to 'True'. ", "color": "gold"}, {"text": "Explanation", "color": "gold", "underlined": true, "hoverEvent": {"action": "show_text", "contents": [{"text": "ReaperMC Docs: How to disable doMobLoot.", "color": "gray"}]}, "clickEvent": {"action": "open_url", "value": "https://github.com/reapermc/reapermc/tree/main/docs/misc/mob_loot_gamerule.md"}}, {"text": ".", "color": "gold", "hoverEvent": {"action": "show_text", "contents": [{"text": "", "color": "gray"}]}}]
```

`@function math_trig:reaper_framework/uninstall`

```mcfunction
function math_trig:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l
function math_trig:reaper_framework/var/u_n_i_n_s_t_a_l_l
```

`@function math_trig:reaper_framework/var/u_n_i_n_s_t_a_l_l`

```mcfunction
data remove storage math_trig:reaper_framework.var data
```

`@function math_trig:reaper_framework/__internal__/var/flush_memory`

```mcfunction
data modify storage math_trig:reaper_framework.var data set value [{}, {}, {}, {}, {}, {}, {}, {}]
```

`@function math_trig:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l`

```mcfunction
scoreboard objectives remove math_trig.reaper_framework.var
scoreboard objectives remove math_trig.reaper_framework.death_events
```

`@function math_trig:init_expressions`

```mcfunction
scoreboard objectives add bolt.expr.const dummy
scoreboard players set $1000 bolt.expr.const 1000
```
