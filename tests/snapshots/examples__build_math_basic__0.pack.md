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

`@function demo:random`

```mcfunction
scoreboard players set $14 math_basic.reaper_framework.var 0
scoreboard players set $15 math_basic.reaper_framework.var 1
function reaper_framework:__internal__/math/random/exec
scoreboard players operation $26 math_basic.reaper_framework.var = $18 math_basic.reaper_framework.var
tellraw @a {"score": {"name": "$26", "objective": "math_basic.reaper_framework.var"}}
scoreboard players set $14 math_basic.reaper_framework.var 5
scoreboard players set $15 math_basic.reaper_framework.var 10
function reaper_framework:__internal__/math/random/exec
scoreboard players operation $26 math_basic.reaper_framework.var = $18 math_basic.reaper_framework.var
tellraw @a {"score": {"name": "$26", "objective": "math_basic.reaper_framework.var"}}
scoreboard players set $14 math_basic.reaper_framework.var 1
scoreboard players set $15 math_basic.reaper_framework.var 100
function reaper_framework:__internal__/math/random/exec
scoreboard players operation $26 math_basic.reaper_framework.var = $18 math_basic.reaper_framework.var
tellraw @a {"score": {"name": "$26", "objective": "math_basic.reaper_framework.var"}}
```

`@function demo:pow`

```mcfunction
scoreboard players set $22 math_basic.reaper_framework.var 4
scoreboard players set $23 math_basic.reaper_framework.var 3
scoreboard players operation $18 math_basic.reaper_framework.var = $22 math_basic.reaper_framework.var
function reaper_framework:__internal__/math/pow/exec
scoreboard players operation $26 math_basic.reaper_framework.var = $18 math_basic.reaper_framework.var
tellraw @a {"score": {"name": "$26", "objective": "math_basic.reaper_framework.var"}}
scoreboard players set $22 math_basic.reaper_framework.var 2
scoreboard players set $23 math_basic.reaper_framework.var 5
scoreboard players operation $18 math_basic.reaper_framework.var = $22 math_basic.reaper_framework.var
function reaper_framework:__internal__/math/pow/exec
scoreboard players operation $26 math_basic.reaper_framework.var = $18 math_basic.reaper_framework.var
tellraw @a {"score": {"name": "$26", "objective": "math_basic.reaper_framework.var"}}
scoreboard players set $22 math_basic.reaper_framework.var 6
scoreboard players set $23 math_basic.reaper_framework.var 2
scoreboard players operation $18 math_basic.reaper_framework.var = $22 math_basic.reaper_framework.var
function reaper_framework:__internal__/math/pow/exec
scoreboard players operation $26 math_basic.reaper_framework.var = $18 math_basic.reaper_framework.var
tellraw @a {"score": {"name": "$26", "objective": "math_basic.reaper_framework.var"}}
```

`@function demo:sqrt`

```mcfunction
scoreboard players set $22 math_basic.reaper_framework.var 3
execute if score $22 math_basic.reaper_framework.var matches 214748.. run tellraw @a [{"text": "\nreapermc ", "color": "gray"}, {"text": " ERROR 'math.sqrt()' overflow. Input value of ", "color": "red"}, {"score": {"name": "$22", "objective": "math_basic.reaper_framework.var"}, "color": "red"}, {"text": " is too large.", "color": "red"}]
execute unless score $22 math_basic.reaper_framework.var matches 0.. run tellraw @a [{"text": "\nreapermc ", "color": "gray"}, {"text": " ERROR 'math.sqrt()' received input value ", "color": "red"}, {"score": {"name": "$22", "objective": "math_basic.reaper_framework.var"}, "color": "red"}, {"text": ". Negative input values not supported.", "color": "red"}]
scoreboard players operation $25 math_basic.reaper_framework.var = $22 math_basic.reaper_framework.var
scoreboard players operation $22 math_basic.reaper_framework.var *= $10000 bolt.expr.const
scoreboard players set $18 math_basic.reaper_framework.var 1255
function reaper_framework:__internal__/math/sqrt/newton_raphson
function reaper_framework:__internal__/math/sqrt/newton_raphson
function reaper_framework:__internal__/math/sqrt/newton_raphson
function reaper_framework:__internal__/math/sqrt/newton_raphson
execute if score $25 math_basic.reaper_framework.var matches 10000.. run function reaper_framework:__internal__/math/sqrt/newton_raphson
execute if score $25 math_basic.reaper_framework.var matches 100000.. run function reaper_framework:__internal__/math/sqrt/newton_raphson
execute if score $18 math_basic.reaper_framework.var matches ..0 run scoreboard players operation $18 math_basic.reaper_framework.var *= $-1 bolt.expr.const
scoreboard players operation $26 math_basic.reaper_framework.var = $18 math_basic.reaper_framework.var
tellraw @a {"score": {"name": "$26", "objective": "math_basic.reaper_framework.var"}}
scoreboard players set $22 math_basic.reaper_framework.var 6
execute if score $22 math_basic.reaper_framework.var matches 214748.. run tellraw @a [{"text": "\nreapermc ", "color": "gray"}, {"text": " ERROR 'math.sqrt()' overflow. Input value of ", "color": "red"}, {"score": {"name": "$22", "objective": "math_basic.reaper_framework.var"}, "color": "red"}, {"text": " is too large.", "color": "red"}]
execute unless score $22 math_basic.reaper_framework.var matches 0.. run tellraw @a [{"text": "\nreapermc ", "color": "gray"}, {"text": " ERROR 'math.sqrt()' received input value ", "color": "red"}, {"score": {"name": "$22", "objective": "math_basic.reaper_framework.var"}, "color": "red"}, {"text": ". Negative input values not supported.", "color": "red"}]
scoreboard players operation $25 math_basic.reaper_framework.var = $22 math_basic.reaper_framework.var
scoreboard players operation $22 math_basic.reaper_framework.var *= $10000 bolt.expr.const
scoreboard players set $18 math_basic.reaper_framework.var 1255
function reaper_framework:__internal__/math/sqrt/newton_raphson
function reaper_framework:__internal__/math/sqrt/newton_raphson
function reaper_framework:__internal__/math/sqrt/newton_raphson
function reaper_framework:__internal__/math/sqrt/newton_raphson
execute if score $25 math_basic.reaper_framework.var matches 10000.. run function reaper_framework:__internal__/math/sqrt/newton_raphson
execute if score $25 math_basic.reaper_framework.var matches 100000.. run function reaper_framework:__internal__/math/sqrt/newton_raphson
execute if score $18 math_basic.reaper_framework.var matches ..0 run scoreboard players operation $18 math_basic.reaper_framework.var *= $-1 bolt.expr.const
scoreboard players operation $26 math_basic.reaper_framework.var = $18 math_basic.reaper_framework.var
tellraw @a {"score": {"name": "$26", "objective": "math_basic.reaper_framework.var"}}
scoreboard players set $22 math_basic.reaper_framework.var 17
execute if score $22 math_basic.reaper_framework.var matches 214748.. run tellraw @a [{"text": "\nreapermc ", "color": "gray"}, {"text": " ERROR 'math.sqrt()' overflow. Input value of ", "color": "red"}, {"score": {"name": "$22", "objective": "math_basic.reaper_framework.var"}, "color": "red"}, {"text": " is too large.", "color": "red"}]
execute unless score $22 math_basic.reaper_framework.var matches 0.. run tellraw @a [{"text": "\nreapermc ", "color": "gray"}, {"text": " ERROR 'math.sqrt()' received input value ", "color": "red"}, {"score": {"name": "$22", "objective": "math_basic.reaper_framework.var"}, "color": "red"}, {"text": ". Negative input values not supported.", "color": "red"}]
scoreboard players operation $25 math_basic.reaper_framework.var = $22 math_basic.reaper_framework.var
scoreboard players operation $22 math_basic.reaper_framework.var *= $10000 bolt.expr.const
scoreboard players set $18 math_basic.reaper_framework.var 1255
function reaper_framework:__internal__/math/sqrt/newton_raphson
function reaper_framework:__internal__/math/sqrt/newton_raphson
function reaper_framework:__internal__/math/sqrt/newton_raphson
function reaper_framework:__internal__/math/sqrt/newton_raphson
execute if score $25 math_basic.reaper_framework.var matches 10000.. run function reaper_framework:__internal__/math/sqrt/newton_raphson
execute if score $25 math_basic.reaper_framework.var matches 100000.. run function reaper_framework:__internal__/math/sqrt/newton_raphson
execute if score $18 math_basic.reaper_framework.var matches ..0 run scoreboard players operation $18 math_basic.reaper_framework.var *= $-1 bolt.expr.const
scoreboard players operation $26 math_basic.reaper_framework.var = $18 math_basic.reaper_framework.var
tellraw @a {"score": {"name": "$26", "objective": "math_basic.reaper_framework.var"}}
```

### reaper_framework

`@function_tag reaper_framework:__internal__/event_handler/on_server_load`

```json
{
  "values": [
    "math_basic:reaper_framework/event/on_server_load"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_server_tick`

```json
{
  "values": [
    "math_basic:reaper_framework/event/on_server_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_tick`

```json
{
  "values": [
    "math_basic:reaper_framework/event/on_player_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_join`

```json
{
  "values": [
    "math_basic:reaper_framework/event/on_player_join"
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
execute unless score $17 math_basic.reaper_framework.var = $17 math_basic.reaper_framework.var store result score $17 math_basic.reaper_framework.var run seed
```

`@function reaper_framework:__internal__/math/random/exec`

```mcfunction
scoreboard players operation $16 math_basic.reaper_framework.var = $15 math_basic.reaper_framework.var
scoreboard players operation $16 math_basic.reaper_framework.var -= $14 math_basic.reaper_framework.var
scoreboard players add $16 math_basic.reaper_framework.var 1
scoreboard players operation $17 math_basic.reaper_framework.var *= $19 math_basic.reaper_framework.var
scoreboard players operation $17 math_basic.reaper_framework.var += $20 math_basic.reaper_framework.var
scoreboard players operation $17 math_basic.reaper_framework.var %= $21 math_basic.reaper_framework.var
scoreboard players operation $18 math_basic.reaper_framework.var = $17 math_basic.reaper_framework.var
scoreboard players operation $18 math_basic.reaper_framework.var /= $8 bolt.expr.const
scoreboard players operation $18 math_basic.reaper_framework.var %= $16 math_basic.reaper_framework.var
scoreboard players operation $18 math_basic.reaper_framework.var += $14 math_basic.reaper_framework.var
```

`@function reaper_framework:__internal__/math/pow/exec`

```mcfunction
scoreboard players operation $18 math_basic.reaper_framework.var *= $22 math_basic.reaper_framework.var
scoreboard players remove $23 math_basic.reaper_framework.var 1
execute unless score $23 math_basic.reaper_framework.var matches ..1 run function reaper_framework:__internal__/math/pow/exec
```

`@function reaper_framework:__internal__/math/sqrt/newton_raphson`

```mcfunction
scoreboard players operation $24 math_basic.reaper_framework.var = $22 math_basic.reaper_framework.var
scoreboard players operation $24 math_basic.reaper_framework.var /= $18 math_basic.reaper_framework.var
scoreboard players operation $18 math_basic.reaper_framework.var += $24 math_basic.reaper_framework.var
scoreboard players operation $18 math_basic.reaper_framework.var /= $2 bolt.expr.const
```

### minecraft

`@function_tag minecraft:load`

```json
{
  "values": [
    "math_basic:init_expressions",
    "reaper_framework:__internal__/event_handler/on_server_load/load"
  ]
}
```

### math_basic

`@function math_basic:reaper_framework/event/on_server_load`

```mcfunction
function math_basic:reaper_framework/__internal__/scoreboard/init
function math_basic:reaper_framework/__internal__/scoreboard/init_defaults
function math_basic:reaper_framework/__internal__/var/flush_memory
function math_basic:reaper_framework/__internal__/var/init_defaults
execute as @a run function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/event_handler/on_server_tick/tick
execute as @a run function reaper_framework:__internal__/loop/reset_joining_player
scoreboard players set $19 math_basic.reaper_framework.var 1630111353
scoreboard players set $20 math_basic.reaper_framework.var 1623164762
scoreboard players set $21 math_basic.reaper_framework.var 2147483647
function reaper_framework:__internal__/math/random/init
forceload add 0 0
kill @e[type=marker, tag=reaper_framework.math]
summon marker 0.0 0.0 0.0 {Tags: ["reaper_framework.math"], CustomName: '{"text": "reaper_framework.math", "color": "#bf0000"}'}
```

`@function math_basic:reaper_framework/__internal__/scoreboard/init`

```mcfunction
scoreboard objectives add math_basic.reaper_framework.var dummy {"text": "math_basic.reaper_framework.var", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.user dummy {"text": "reaper_framework.entity_nbt.user", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.cloud dummy {"text": "reaper_framework.entity_nbt.cloud", "color": "#bf0000"}
scoreboard objectives add math_basic.reaper_framework.death_events dummy {"text": "math_basic.reaper_framework.death_events", "color": "#bf0000"}
scoreboard objectives add reaper_framework.sleep.dim_id dummy {"text": "reaper_framework.sleep.dim_id", "color": "#bf0000"}
scoreboard objectives add reaper_framework.event_handler.on_player_join custom:leave_game {"text": "reaper_framework.event_handler.on_player_join", "color": "#bf0000"}
```

`@function math_basic:reaper_framework/event/on_server_tick`

```mcfunction
execute as @a at @s run function #reaper_framework:__internal__/event_handler/on_player_tick
```

`@function math_basic:reaper_framework/event/on_player_tick`

```mcfunction
execute if score @s reaper_framework.event_handler.on_player_join matches -1 run function reaper_framework:__internal__/event_handler/on_player_join/join
execute if score @s reaper_framework.event_handler.on_player_join matches 1.. run scoreboard players set @s reaper_framework.event_handler.on_player_join -1
```

`@function math_basic:reaper_framework/event/on_player_join`

```mcfunction
function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/loop/reset_joining_player
```

`@function math_basic:reaper_framework/uninstall`

```mcfunction
function math_basic:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l
function math_basic:reaper_framework/var/u_n_i_n_s_t_a_l_l
```

`@function math_basic:reaper_framework/var/u_n_i_n_s_t_a_l_l`

```mcfunction
data remove storage math_basic:reaper_framework.var data
```

`@function math_basic:reaper_framework/__internal__/var/flush_memory`

```mcfunction
data modify storage math_basic:reaper_framework.var data set value [{}, {}, {}, {}, {}, {}, {}, {}]
```

`@function math_basic:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l`

```mcfunction
scoreboard objectives remove math_basic.reaper_framework.var
scoreboard objectives remove math_basic.reaper_framework.death_events
```

`@function math_basic:init_expressions`

```mcfunction
scoreboard objectives add bolt.expr.const dummy
scoreboard players set $10000 bolt.expr.const 10000
scoreboard players set $8 bolt.expr.const 8
scoreboard players set $2 bolt.expr.const 2
```
