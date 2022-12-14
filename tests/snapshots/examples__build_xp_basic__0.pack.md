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

`@function(strip_final_newline) demo:main/nested_execute_0`

```mcfunction

```

`@function demo:main/nested_execute_1`

```mcfunction
execute if score $10 xp_basic.reaper_framework.var matches 100 run function demo:main/nested_execute_0
function xp_basic:reaper_framework/__internal__/set_xp_bar_percent/64
```

`@function demo:test`

```mcfunction
xp set @s 324 points
```

`@function demo:test2`

```mcfunction
scoreboard players set $27 xp_basic.reaper_framework.var 69
scoreboard players operation $10 xp_basic.reaper_framework.var = $27 xp_basic.reaper_framework.var
function xp_basic:reaper_framework/__internal__/set_xp/points/start
```

`@function demo:test3`

```mcfunction
execute store result score $12 xp_basic.reaper_framework.var run xp query @s points
scoreboard players operation $26 xp_basic.reaper_framework.var = $12 xp_basic.reaper_framework.var
tellraw @a {"score": {"name": "$26", "objective": "xp_basic.reaper_framework.var"}}
```

`@function demo:test4`

```mcfunction
execute store result score $12 xp_basic.reaper_framework.var run xp query @s levels
scoreboard players operation $13 xp_basic.reaper_framework.var = $12 xp_basic.reaper_framework.var
xp set @s 8662 levels
xp set @s 0 points
scoreboard players set $11 xp_basic.reaper_framework.var 100
execute if score $11 xp_basic.reaper_framework.var matches 64.. run function demo:main/nested_execute_1
execute if score $11 xp_basic.reaper_framework.var matches 32.. run function xp_basic:reaper_framework/__internal__/set_xp_bar_percent/32
execute if score $11 xp_basic.reaper_framework.var matches 16.. run function xp_basic:reaper_framework/__internal__/set_xp_bar_percent/16
execute if score $11 xp_basic.reaper_framework.var matches 8.. run function xp_basic:reaper_framework/__internal__/set_xp_bar_percent/8
execute if score $11 xp_basic.reaper_framework.var matches 4.. run function xp_basic:reaper_framework/__internal__/set_xp_bar_percent/4
execute if score $11 xp_basic.reaper_framework.var matches 2.. run function xp_basic:reaper_framework/__internal__/set_xp_bar_percent/2
execute if score $11 xp_basic.reaper_framework.var matches 1.. run function xp_basic:reaper_framework/__internal__/set_xp_bar_percent/1
scoreboard players operation $10 xp_basic.reaper_framework.var = $13 xp_basic.reaper_framework.var
function xp_basic:reaper_framework/__internal__/set_xp/levels/start
```

### reaper_framework

`@function_tag reaper_framework:__internal__/event_handler/on_server_load`

```json
{
  "values": [
    "xp_basic:reaper_framework/event/on_server_load"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_server_tick`

```json
{
  "values": [
    "xp_basic:reaper_framework/event/on_server_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_tick`

```json
{
  "values": [
    "xp_basic:reaper_framework/event/on_player_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_join`

```json
{
  "values": [
    "xp_basic:reaper_framework/event/on_player_join"
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
execute unless score $17 xp_basic.reaper_framework.var = $17 xp_basic.reaper_framework.var store result score $17 xp_basic.reaper_framework.var run seed
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

### xp_basic

`@function xp_basic:reaper_framework/event/on_server_load`

```mcfunction
function xp_basic:reaper_framework/__internal__/scoreboard/init
function xp_basic:reaper_framework/__internal__/scoreboard/init_defaults
function xp_basic:reaper_framework/__internal__/var/flush_memory
function xp_basic:reaper_framework/__internal__/var/init_defaults
execute as @a run function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/event_handler/on_server_tick/tick
execute as @a run function reaper_framework:__internal__/loop/reset_joining_player
scoreboard players set $19 xp_basic.reaper_framework.var 1630111353
scoreboard players set $20 xp_basic.reaper_framework.var 1623164762
scoreboard players set $21 xp_basic.reaper_framework.var 2147483647
function reaper_framework:__internal__/math/random/init
forceload add 0 0
kill @e[type=marker, tag=reaper_framework.math]
summon marker 0.0 0.0 0.0 {Tags: ["reaper_framework.math"], CustomName: '{"text": "reaper_framework.math", "color": "#bf0000"}'}
execute store result score $28 xp_basic.reaper_framework.var run gamerule doMobLoot
execute if score $28 xp_basic.reaper_framework.var matches 0 run function xp_basic:reaper_framework/__internal__/mob_loot_gamerule_error
```

`@function xp_basic:reaper_framework/__internal__/scoreboard/init`

```mcfunction
scoreboard objectives add xp_basic.reaper_framework.var dummy {"text": "xp_basic.reaper_framework.var", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.user dummy {"text": "reaper_framework.entity_nbt.user", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.cloud dummy {"text": "reaper_framework.entity_nbt.cloud", "color": "#bf0000"}
scoreboard objectives add xp_basic.reaper_framework.death_events dummy {"text": "xp_basic.reaper_framework.death_events", "color": "#bf0000"}
scoreboard objectives add reaper_framework.sleep.dim_id dummy {"text": "reaper_framework.sleep.dim_id", "color": "#bf0000"}
scoreboard objectives add reaper_framework.event_handler.on_player_join custom:leave_game {"text": "reaper_framework.event_handler.on_player_join", "color": "#bf0000"}
```

`@function xp_basic:reaper_framework/event/on_server_tick`

```mcfunction
execute as @a at @s run function #reaper_framework:__internal__/event_handler/on_player_tick
```

`@function xp_basic:reaper_framework/event/on_player_tick`

```mcfunction
execute if score @s reaper_framework.event_handler.on_player_join matches -1 run function reaper_framework:__internal__/event_handler/on_player_join/join
execute if score @s reaper_framework.event_handler.on_player_join matches 1.. run scoreboard players set @s reaper_framework.event_handler.on_player_join -1
```

`@function xp_basic:reaper_framework/event/on_player_join`

```mcfunction
function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/loop/reset_joining_player
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/134217728`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 134217728
xp add @s 134217728 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/67108864`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 67108864
xp add @s 67108864 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/33554432`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 33554432
xp add @s 33554432 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/16777216`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 16777216
xp add @s 16777216 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/8388608`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 8388608
xp add @s 8388608 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/4194304`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 4194304
xp add @s 4194304 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/2097152`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 2097152
xp add @s 2097152 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/1048576`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 1048576
xp add @s 1048576 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/524288`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 524288
xp add @s 524288 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/262144`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 262144
xp add @s 262144 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/131072`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 131072
xp add @s 131072 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/65536`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 65536
xp add @s 65536 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/32768`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 32768
xp add @s 32768 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/16384`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 16384
xp add @s 16384 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/8192`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 8192
xp add @s 8192 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/4096`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 4096
xp add @s 4096 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/2048`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 2048
xp add @s 2048 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/1024`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 1024
xp add @s 1024 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/512`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 512
xp add @s 512 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/256`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 256
xp add @s 256 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/128`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 128
xp add @s 128 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/64`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 64
xp add @s 64 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/32`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 32
xp add @s 32 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/16`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 16
xp add @s 16 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/8`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 8
xp add @s 8 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/4`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 4
xp add @s 4 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/2`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 2
xp add @s 2 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/1`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 1
xp add @s 1 points
```

`@function xp_basic:reaper_framework/__internal__/set_xp/points/start`

```mcfunction
xp set @s 0 points
execute if score $10 xp_basic.reaper_framework.var matches 134217728.. run function xp_basic:reaper_framework/__internal__/set_xp/points/134217728
execute if score $10 xp_basic.reaper_framework.var matches 67108864.. run function xp_basic:reaper_framework/__internal__/set_xp/points/67108864
execute if score $10 xp_basic.reaper_framework.var matches 33554432.. run function xp_basic:reaper_framework/__internal__/set_xp/points/33554432
execute if score $10 xp_basic.reaper_framework.var matches 16777216.. run function xp_basic:reaper_framework/__internal__/set_xp/points/16777216
execute if score $10 xp_basic.reaper_framework.var matches 8388608.. run function xp_basic:reaper_framework/__internal__/set_xp/points/8388608
execute if score $10 xp_basic.reaper_framework.var matches 4194304.. run function xp_basic:reaper_framework/__internal__/set_xp/points/4194304
execute if score $10 xp_basic.reaper_framework.var matches 2097152.. run function xp_basic:reaper_framework/__internal__/set_xp/points/2097152
execute if score $10 xp_basic.reaper_framework.var matches 1048576.. run function xp_basic:reaper_framework/__internal__/set_xp/points/1048576
execute if score $10 xp_basic.reaper_framework.var matches 524288.. run function xp_basic:reaper_framework/__internal__/set_xp/points/524288
execute if score $10 xp_basic.reaper_framework.var matches 262144.. run function xp_basic:reaper_framework/__internal__/set_xp/points/262144
execute if score $10 xp_basic.reaper_framework.var matches 131072.. run function xp_basic:reaper_framework/__internal__/set_xp/points/131072
execute if score $10 xp_basic.reaper_framework.var matches 65536.. run function xp_basic:reaper_framework/__internal__/set_xp/points/65536
execute if score $10 xp_basic.reaper_framework.var matches 32768.. run function xp_basic:reaper_framework/__internal__/set_xp/points/32768
execute if score $10 xp_basic.reaper_framework.var matches 16384.. run function xp_basic:reaper_framework/__internal__/set_xp/points/16384
execute if score $10 xp_basic.reaper_framework.var matches 8192.. run function xp_basic:reaper_framework/__internal__/set_xp/points/8192
execute if score $10 xp_basic.reaper_framework.var matches 4096.. run function xp_basic:reaper_framework/__internal__/set_xp/points/4096
execute if score $10 xp_basic.reaper_framework.var matches 2048.. run function xp_basic:reaper_framework/__internal__/set_xp/points/2048
execute if score $10 xp_basic.reaper_framework.var matches 1024.. run function xp_basic:reaper_framework/__internal__/set_xp/points/1024
execute if score $10 xp_basic.reaper_framework.var matches 512.. run function xp_basic:reaper_framework/__internal__/set_xp/points/512
execute if score $10 xp_basic.reaper_framework.var matches 256.. run function xp_basic:reaper_framework/__internal__/set_xp/points/256
execute if score $10 xp_basic.reaper_framework.var matches 128.. run function xp_basic:reaper_framework/__internal__/set_xp/points/128
execute if score $10 xp_basic.reaper_framework.var matches 64.. run function xp_basic:reaper_framework/__internal__/set_xp/points/64
execute if score $10 xp_basic.reaper_framework.var matches 32.. run function xp_basic:reaper_framework/__internal__/set_xp/points/32
execute if score $10 xp_basic.reaper_framework.var matches 16.. run function xp_basic:reaper_framework/__internal__/set_xp/points/16
execute if score $10 xp_basic.reaper_framework.var matches 8.. run function xp_basic:reaper_framework/__internal__/set_xp/points/8
execute if score $10 xp_basic.reaper_framework.var matches 4.. run function xp_basic:reaper_framework/__internal__/set_xp/points/4
execute if score $10 xp_basic.reaper_framework.var matches 2.. run function xp_basic:reaper_framework/__internal__/set_xp/points/2
execute if score $10 xp_basic.reaper_framework.var matches 1.. run function xp_basic:reaper_framework/__internal__/set_xp/points/1
```

`@function xp_basic:reaper_framework/__internal__/set_xp_bar_percent/64`

```mcfunction
scoreboard players remove $11 xp_basic.reaper_framework.var 64
xp add @s 49791
```

`@function xp_basic:reaper_framework/__internal__/set_xp_bar_percent/32`

```mcfunction
scoreboard players remove $11 xp_basic.reaper_framework.var 32
xp add @s 24896
```

`@function xp_basic:reaper_framework/__internal__/set_xp_bar_percent/16`

```mcfunction
scoreboard players remove $11 xp_basic.reaper_framework.var 16
xp add @s 12448
```

`@function xp_basic:reaper_framework/__internal__/set_xp_bar_percent/8`

```mcfunction
scoreboard players remove $11 xp_basic.reaper_framework.var 8
xp add @s 6224
```

`@function xp_basic:reaper_framework/__internal__/set_xp_bar_percent/4`

```mcfunction
scoreboard players remove $11 xp_basic.reaper_framework.var 4
xp add @s 3112
```

`@function xp_basic:reaper_framework/__internal__/set_xp_bar_percent/2`

```mcfunction
scoreboard players remove $11 xp_basic.reaper_framework.var 2
xp add @s 1556
```

`@function xp_basic:reaper_framework/__internal__/set_xp_bar_percent/1`

```mcfunction
scoreboard players remove $11 xp_basic.reaper_framework.var 1
xp add @s 778
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/134217728`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 134217728
xp add @s 134217728 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/67108864`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 67108864
xp add @s 67108864 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/33554432`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 33554432
xp add @s 33554432 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/16777216`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 16777216
xp add @s 16777216 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/8388608`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 8388608
xp add @s 8388608 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/4194304`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 4194304
xp add @s 4194304 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/2097152`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 2097152
xp add @s 2097152 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/1048576`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 1048576
xp add @s 1048576 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/524288`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 524288
xp add @s 524288 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/262144`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 262144
xp add @s 262144 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/131072`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 131072
xp add @s 131072 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/65536`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 65536
xp add @s 65536 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/32768`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 32768
xp add @s 32768 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/16384`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 16384
xp add @s 16384 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/8192`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 8192
xp add @s 8192 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/4096`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 4096
xp add @s 4096 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/2048`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 2048
xp add @s 2048 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/1024`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 1024
xp add @s 1024 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/512`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 512
xp add @s 512 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/256`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 256
xp add @s 256 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/128`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 128
xp add @s 128 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/64`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 64
xp add @s 64 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/32`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 32
xp add @s 32 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/16`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 16
xp add @s 16 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/8`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 8
xp add @s 8 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/4`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 4
xp add @s 4 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/2`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 2
xp add @s 2 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/1`

```mcfunction
scoreboard players remove $10 xp_basic.reaper_framework.var 1
xp add @s 1 levels
```

`@function xp_basic:reaper_framework/__internal__/set_xp/levels/start`

```mcfunction
xp set @s 0 levels
execute if score $10 xp_basic.reaper_framework.var matches 134217728.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/134217728
execute if score $10 xp_basic.reaper_framework.var matches 67108864.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/67108864
execute if score $10 xp_basic.reaper_framework.var matches 33554432.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/33554432
execute if score $10 xp_basic.reaper_framework.var matches 16777216.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/16777216
execute if score $10 xp_basic.reaper_framework.var matches 8388608.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/8388608
execute if score $10 xp_basic.reaper_framework.var matches 4194304.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/4194304
execute if score $10 xp_basic.reaper_framework.var matches 2097152.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/2097152
execute if score $10 xp_basic.reaper_framework.var matches 1048576.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/1048576
execute if score $10 xp_basic.reaper_framework.var matches 524288.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/524288
execute if score $10 xp_basic.reaper_framework.var matches 262144.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/262144
execute if score $10 xp_basic.reaper_framework.var matches 131072.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/131072
execute if score $10 xp_basic.reaper_framework.var matches 65536.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/65536
execute if score $10 xp_basic.reaper_framework.var matches 32768.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/32768
execute if score $10 xp_basic.reaper_framework.var matches 16384.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/16384
execute if score $10 xp_basic.reaper_framework.var matches 8192.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/8192
execute if score $10 xp_basic.reaper_framework.var matches 4096.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/4096
execute if score $10 xp_basic.reaper_framework.var matches 2048.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/2048
execute if score $10 xp_basic.reaper_framework.var matches 1024.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/1024
execute if score $10 xp_basic.reaper_framework.var matches 512.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/512
execute if score $10 xp_basic.reaper_framework.var matches 256.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/256
execute if score $10 xp_basic.reaper_framework.var matches 128.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/128
execute if score $10 xp_basic.reaper_framework.var matches 64.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/64
execute if score $10 xp_basic.reaper_framework.var matches 32.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/32
execute if score $10 xp_basic.reaper_framework.var matches 16.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/16
execute if score $10 xp_basic.reaper_framework.var matches 8.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/8
execute if score $10 xp_basic.reaper_framework.var matches 4.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/4
execute if score $10 xp_basic.reaper_framework.var matches 2.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/2
execute if score $10 xp_basic.reaper_framework.var matches 1.. run function xp_basic:reaper_framework/__internal__/set_xp/levels/1
```

`@function xp_basic:reaper_framework/__internal__/mob_loot_gamerule_error`

```mcfunction
gamerule doMobLoot true
tellraw @a [{"text": "\nreapermc ", "color": "gray"}, {"text": " WARN Gamerule 'doMobLoot' was changed to 'True'. ", "color": "gold"}, {"text": "Explanation", "color": "gold", "underlined": true, "hoverEvent": {"action": "show_text", "contents": [{"text": "ReaperMC Docs: How to disable doMobLoot.", "color": "gray"}]}, "clickEvent": {"action": "open_url", "value": "https://github.com/reapermc/reapermc/tree/main/docs/misc/mob_loot_gamerule.md"}}, {"text": ".", "color": "gold", "hoverEvent": {"action": "show_text", "contents": [{"text": "", "color": "gray"}]}}]
```

`@function xp_basic:reaper_framework/uninstall`

```mcfunction
function xp_basic:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l
function xp_basic:reaper_framework/var/u_n_i_n_s_t_a_l_l
```

`@function xp_basic:reaper_framework/var/u_n_i_n_s_t_a_l_l`

```mcfunction
data remove storage xp_basic:reaper_framework.var data
```

`@function xp_basic:reaper_framework/__internal__/var/flush_memory`

```mcfunction
data modify storage xp_basic:reaper_framework.var data set value [{}, {}, {}, {}, {}, {}, {}, {}]
```

`@function xp_basic:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l`

```mcfunction
scoreboard objectives remove xp_basic.reaper_framework.var
scoreboard objectives remove xp_basic.reaper_framework.death_events
```
