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

### reapermc

`@function reapermc:death_events`

```mcfunction

```

`@function reapermc:loop`

```mcfunction

```

`@function reapermc:loop_break`

```mcfunction

```

`@function reapermc:sleep`

```mcfunction

```

`@function reapermc:object`

```mcfunction

```

`@function reapermc:var`

```mcfunction

```

### demo

`@function demo:main/nested_execute_0`

```mcfunction
data remove storage reaper:var data[2].v[0]
data remove storage reaper:var data[3].v[0]
```

`@function demo:main/nested_execute_1`

```mcfunction
data remove storage reaper:var data[2].v[0]
scoreboard players remove $8 reaper.var 1
execute store result score $6 reaper.var run data get storage reaper:var data[3].v[0] 1
data remove storage reaper:var data[3].v[0]
scoreboard players add $6 reaper.var 1
scoreboard players operation $3 reaper.var = $6 reaper.var
data modify storage reaper:var data[2].v append value 0
execute store result storage reaper:var data[2].v[-1] int 1 run scoreboard players get $8 reaper.var
data modify storage reaper:var data[3].v append value 0
execute store result storage reaper:var data[3].v[-1] int 1 run scoreboard players get $6 reaper.var
function loop_basic:reaper_framework/loop/0
function loop_basic:reaper_framework/__internal__/loop/cache/0_srv_cycle
```

`@function demo:main/nested_execute_2`

```mcfunction
data modify storage reaper:var data[2].v append value -1
function loop_basic:reaper_framework/__internal__/loop/cache/0_srv_cycle
```

`@function demo:main/nested_execute_3`

```mcfunction
scoreboard players set $8 reaper.var -1
data modify storage reaper:var data[3].v append value 0
scoreboard players set $3 reaper.var 0
function loop_basic:reaper_framework/loop/0
execute unless score $8 reaper.var matches 0 run function demo:main/nested_execute_2
```

`@function demo:main/nested_execute_4`

```mcfunction
function loop_basic:reaper_framework/__internal__/object/cache/8_0
function loop_basic:reaper_framework/__internal__/object/cache/9_0
```

`@function demo:main/nested_execute_5`

```mcfunction
function loop_basic:reaper_framework/__internal__/object/cache/10_0
scoreboard players remove $7 reaper.var 1
function loop_basic:reaper_framework/__internal__/object/cache/11_0
execute store result score $6 reaper.var run data get storage reaper:var data[0].v 1
function loop_basic:reaper_framework/__internal__/object/cache/12_0
scoreboard players add $6 reaper.var 1
scoreboard players operation $3 reaper.var = $6 reaper.var
function loop_basic:reaper_framework/__internal__/object/cache/13_0
function loop_basic:reaper_framework/__internal__/object/cache/14_0
function loop_basic:reaper_framework/loop/0
function loop_basic:reaper_framework/__internal__/loop/cache/0_ent_cycle
```

`@function demo:main/nested_execute_6`

```mcfunction
function loop_basic:reaper_framework/__internal__/object/cache/2_0
function loop_basic:reaper_framework/__internal__/loop/cache/0_ent_cycle
```

`@function demo:main/nested_execute_7`

```mcfunction
execute if entity @s unless entity @s[tag=reaper.object.holder] run function loop_basic:reaper_framework/__internal__/object/ensure_entry
scoreboard players set $7 reaper.var -1
function loop_basic:reaper_framework/__internal__/object/cache/1_0
scoreboard players set $3 reaper.var 0
function loop_basic:reaper_framework/loop/0
execute unless score $7 reaper.var matches 0 run function demo:main/nested_execute_6
```

### loop_basic

`@function loop_basic:reaper_framework/__internal__/spark/on_join`

```mcfunction
scoreboard players set @s reaper.spark 0
function loop_basic:reaper_framework/spark/prejoin
function loop_basic:reaper_framework/spark/join
function loop_basic:reaper_framework/spark/postjoin
```

`@function loop_basic:reaper_framework/__internal__/spark/init`

```mcfunction
scoreboard objectives add reaper.spark custom:leave_game {"text": "reaper.spark", "color": "#F06400"}
scoreboard players set @a reaper.spark 1
function loop_basic:reaper_framework/spark/preload
function loop_basic:reaper_framework/spark/load
function loop_basic:reaper_framework/spark/postload
function loop_basic:reaper_framework/__internal__/spark/clock
```

`@function loop_basic:reaper_framework/__internal__/spark/clock`

```mcfunction
schedule function loop_basic:reaper_framework/__internal__/spark/clock 1
execute as @a if score @s reaper.spark matches 1.. at @s run function loop_basic:reaper_framework/__internal__/spark/on_join
function loop_basic:reaper_framework/spark/pretick
function loop_basic:reaper_framework/spark/tick
function loop_basic:reaper_framework/spark/posttick
```

`@function loop_basic:reaper_framework/spark/prejoin`

```mcfunction
function loop_basic:reaper_framework/__internal__/sleep/onjoin_flush
function loop_basic:reaper_framework/__internal__/loop/onjoin_flush
```

`@function loop_basic:reaper_framework/spark/preload`

```mcfunction
function loop_basic:reaper_framework/__internal__/scoreboard/init
function loop_basic:reaper_framework/__internal__/scoreboard/init_defaults
function loop_basic:reaper_framework/__internal__/var/flush_memory
function loop_basic:reaper_framework/__internal__/var/init_defaults
```

`@function loop_basic:reaper_framework/__internal__/scoreboard/init`

```mcfunction
scoreboard objectives add reaper.var dummy {"text": "reaper.var", "color": "#F06400"}
scoreboard objectives add reaper.object dummy {"text": "reaper.object", "color": "#F06400"}
scoreboard objectives add reaper.object.m dummy {"text": "reaper.object.m", "color": "#F06400"}
scoreboard objectives add reaper.sleep.dim_id dummy {"text": "reaper.sleep.dim_id", "color": "#F06400"}
scoreboard objectives add reaper.death_events dummy {"text": "reaper.death_events", "color": "#F06400"}
```

`@function loop_basic:reaper_framework/better_summon/0`

```mcfunction
scoreboard players operation @s reaper.object.m = #next reaper.object
scoreboard players add #next reaper.object 1
tag @s remove reaper.summon.init
```

`@function loop_basic:reaper_framework/__internal__/object/garbage_collector`

```mcfunction
execute store result score $2 reaper.var run data get entity @s Item.tag.AttributeModifiers[0].Amount 1
kill @s
execute as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = $2 reaper.var run kill @s
```

`@function loop_basic:reaper_framework/__internal__/scoreboard/init_defaults`

```mcfunction
execute unless score #next reaper.object = #next reaper.object run scoreboard players set #next reaper.object 0
```

`@function loop_basic:reaper_framework/object/remove_entity`

```mcfunction
scoreboard players operation $1 reaper.var = @s reaper.object
execute as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = $1 reaper.var run kill @s
scoreboard players reset @s reaper.object
tag @s remove reaper.object.holder
```

`@function loop_basic:reaper_framework/__internal__/object/ensure_entry`

```mcfunction
scoreboard players operation @s reaper.object = #next reaper.object
forceload add 69000 69000
summon marker 69000 0 69000 {Tags: ["reaper.object.m", "reaper.summon.init"], CustomName: '{"text":"reaper.object.m","color":"#F06400"}'}
execute as @e[type=minecraft:marker, tag=reaper.summon.init] at @s run function loop_basic:reaper_framework/better_summon/0
tag @s add reaper.object.holder
```

`@function loop_basic:reaper_framework/spark/pretick`

```mcfunction
execute as @e[type=item, nbt={Item: {tag: {reaper.object.death_cleanup: 1b}}}] run function loop_basic:reaper_framework/__internal__/object/garbage_collector
execute as @e[type=item] if data entity @s {Item: {tag: {reaper.death_event: 1b}}} at @s run function loop_basic:reaper_framework/__internal__/death_events/get_item_info
```

`@function loop_basic:reaper_framework/__internal__/death_events/get_item_info`

```mcfunction
execute store result score $find reaper.death_events run data get entity @s Item.tag.AttributeModifiers[0].Amount
kill @s
function loop_basic:reaper_framework/__internal__/death_events/find_event
```

`@function loop_basic:reaper_framework/better_summon/1`

```mcfunction
scoreboard players operation @s reaper.sleep.dim_id = #i reaper.sleep.dim_id
tag @s remove reaper.summon.init
```

`@function loop_basic:reaper_framework/__internal__/sleep/0_srv_ensure_ctx`

```mcfunction
summon marker 69000 0 69000 {Tags: ["reaper.sleep.ctx", "reaper.summon.init"], CustomName: '{"text":"reaper.sleep.ctx","color":"#F06400"}'}
execute as @e[type=minecraft:marker, tag=reaper.summon.init] at @s run function loop_basic:reaper_framework/better_summon/1
scoreboard players add #i reaper.sleep.dim_id 1
```

`@function loop_basic:reaper_framework/__internal__/sleep/0_srv_get_ctx`

```mcfunction
tp @s ~ ~ ~ ~ ~
execute store result storage reaper:var data[1].v.dim int 1 run scoreboard players get @s reaper.sleep.dim_id
data modify storage reaper:var data[1].v.pos set from entity @s Pos
data modify storage reaper:var data[1].v.rot set from entity @s Rotation
tp @s 69000 0 69000
```

`@function loop_basic:reaper_framework/__internal__/sleep/0_srv_1`

```mcfunction
data modify entity @s Pos set from storage reaper:var data[5].v.pos
data modify entity @s Rotation set from storage reaper:var data[5].v.rot
tag @s add reaper.sleep.ctx.target
```

`@function loop_basic:reaper_framework/__internal__/sleep/0_srv_3`

```mcfunction
tag @s remove reaper.sleep.ctx.target
tp @s 69000 0 69000
```

`@function loop_basic:reaper_framework/__internal__/sleep/0_srv_2`

```mcfunction
execute as @e[tag=reaper.sleep.ctx.target] run function loop_basic:reaper_framework/__internal__/sleep/0_srv_3
function loop_basic:reaper_framework/sleep/0
```

`@function loop_basic:reaper_framework/__internal__/sleep/0_srv_sch`

```mcfunction
execute store result score $10 reaper.var run data get storage reaper:var data[4].v[0] 1
execute store result score $11 reaper.var run data get storage reaper:var data[4].v[1] 1
data remove storage reaper:var data[4].v[0]
data modify storage reaper:var data[5].v set from storage reaper:var data[6].v[0]
data remove storage reaper:var data[6].v[0]
execute store result score $12 reaper.var run data get storage reaper:var data[5].v.dim 1
execute as @e[tag=reaper.sleep.ctx] if score $12 reaper.var = @s reaper.sleep.dim_id run function loop_basic:reaper_framework/__internal__/sleep/0_srv_1
execute at @e[tag=reaper.sleep.ctx.target] run function loop_basic:reaper_framework/__internal__/sleep/0_srv_2
execute if score $11 reaper.var = $10 reaper.var run function loop_basic:reaper_framework/__internal__/sleep/0_srv_sch
```

`@function loop_basic:reaper_framework/__internal__/sleep/0_srv_0`

```mcfunction
execute store result score $0 reaper.var run time query gametime
data modify storage reaper:var data[4].v append value 0
execute store result storage reaper:var data[4].v[-1] int 1 run scoreboard players get $0 reaper.var
data remove storage reaper:var data[1].v
forceload add 69000 69000
execute unless entity @e[tag=reaper.sleep.ctx, x=0] run function loop_basic:reaper_framework/__internal__/sleep/0_srv_ensure_ctx
execute as @e[tag=reaper.sleep.ctx, x=0] run function loop_basic:reaper_framework/__internal__/sleep/0_srv_get_ctx
data modify storage reaper:var data[6].v append from storage reaper:var data[1].v
schedule function loop_basic:reaper_framework/__internal__/sleep/0_srv_sch 20 append
```

`@function loop_basic:reaper_framework/__internal__/sleep/0_exec`

```mcfunction
execute unless entity @s run function loop_basic:reaper_framework/__internal__/sleep/0_srv_0
```

`@function loop_basic:reaper_framework/sleep/0`

```mcfunction
execute store result score $8 reaper.var run data get storage reaper:var data[2].v[0] 1
execute if score $8 reaper.var matches 0 run function demo:main/nested_execute_0
execute unless score $8 reaper.var matches 0 run function demo:main/nested_execute_1
```

`@function loop_basic:reaper_framework/__internal__/loop/cache/0_srv_cycle`

```mcfunction
function loop_basic:reaper_framework/__internal__/sleep/0_exec
```

`@function loop_basic:reaper_framework/__internal__/loop/cache/0_srv_break_thread`

```mcfunction
data modify storage reaper:var data[2].v[-1] set value 0
```

`@function loop_basic:reaper_framework/__internal__/object/cache/0_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.0.cycles_left[-1] set value 0
```

`@function loop_basic:reaper_framework/__internal__/object/cache/0_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/0_1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/1_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.0.cycle_index append value 0
```

`@function loop_basic:reaper_framework/__internal__/object/cache/1_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/1_1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/2_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.0.cycles_left append value -1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/2_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/2_1
```

`@function loop_basic:reaper_framework/better_summon/2`

```mcfunction
scoreboard players operation @s reaper.sleep.dim_id = #i reaper.sleep.dim_id
tag @s remove reaper.summon.init
```

`@function loop_basic:reaper_framework/__internal__/sleep/1_ent_ensure_ctx`

```mcfunction
summon marker 69000 0 69000 {Tags: ["reaper.sleep.ctx", "reaper.summon.init"], CustomName: '{"text":"reaper.sleep.ctx","color":"#F06400"}'}
execute as @e[type=minecraft:marker, tag=reaper.summon.init] at @s run function loop_basic:reaper_framework/better_summon/2
scoreboard players add #i reaper.sleep.dim_id 1
```

`@function loop_basic:reaper_framework/__internal__/sleep/1_ent_get_ctx`

```mcfunction
tp @s ~ ~ ~ ~ ~
execute store result storage reaper:var data[1].v.dim int 1 run scoreboard players get @s reaper.sleep.dim_id
data modify storage reaper:var data[1].v.pos set from entity @s Pos
data modify storage reaper:var data[1].v.rot set from entity @s Rotation
tp @s 69000 0 69000
```

`@function loop_basic:reaper_framework/__internal__/object/cache/3_1`

```mcfunction
data modify entity @s data.__internal__.reaper.sleep.1 append from storage reaper:var data[8].v
```

`@function loop_basic:reaper_framework/__internal__/object/cache/3_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/3_1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/4_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.sleep.1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/4_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/4_1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/5_1`

```mcfunction
data remove entity @s data.__internal__.reaper.sleep.1[0]
```

`@function loop_basic:reaper_framework/__internal__/object/cache/5_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/5_1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/6_1`

```mcfunction
data remove entity @s data.__internal__.reaper.sleep.1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/6_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/6_1
```

`@function loop_basic:reaper_framework/__internal__/sleep/1_ent_3`

```mcfunction
tag @s remove reaper.sleep.1
function loop_basic:reaper_framework/__internal__/object/cache/6_0
```

`@function loop_basic:reaper_framework/__internal__/sleep/1_ent_4`

```mcfunction
data modify entity @s Pos set from storage reaper:var data[7].v.pos
data modify entity @s Rotation set from storage reaper:var data[7].v.rot
tag @s add reaper.sleep.ctx.target
```

`@function loop_basic:reaper_framework/__internal__/sleep/1_ent_6`

```mcfunction
tag @s remove reaper.sleep.ctx.target
tp @s 69000 0 69000
```

`@function loop_basic:reaper_framework/__internal__/sleep/1_ent_5`

```mcfunction
execute as @e[tag=reaper.sleep.ctx.target] run function loop_basic:reaper_framework/__internal__/sleep/1_ent_6
function loop_basic:reaper_framework/sleep/1
```

`@function loop_basic:reaper_framework/__internal__/sleep/1_ent_2`

```mcfunction
function loop_basic:reaper_framework/__internal__/object/cache/5_0
data remove storage reaper:var data[9].v[0]
execute store result score $14 reaper.var run data get storage reaper:var data[9].v[0].ts 1
execute store result score $16 reaper.var run data get storage reaper:var data[9].v
execute if score $16 reaper.var matches 0 run function loop_basic:reaper_framework/__internal__/sleep/1_ent_3
data modify storage reaper:var data[7].v set from storage reaper:var data[10].v.ctx
execute store result score $17 reaper.var run data get storage reaper:var data[7].v.dim 1
execute as @e[tag=reaper.sleep.ctx] if score $17 reaper.var = @s reaper.sleep.dim_id run function loop_basic:reaper_framework/__internal__/sleep/1_ent_4
execute at @e[tag=reaper.sleep.ctx.target] run function loop_basic:reaper_framework/__internal__/sleep/1_ent_5
execute if score $14 reaper.var = $13 reaper.var run function loop_basic:reaper_framework/__internal__/sleep/1_ent_sch
```

`@function loop_basic:reaper_framework/__internal__/sleep/1_ent_1`

```mcfunction
function loop_basic:reaper_framework/__internal__/object/cache/4_0
data modify storage reaper:var data[9].v set from storage reaper:var data[0].v
data modify storage reaper:var data[10].v set from storage reaper:var data[9].v[0]
execute store result score $13 reaper.var run data get storage reaper:var data[10].v.ts 1
execute if score $13 reaper.var = $15 reaper.var run function loop_basic:reaper_framework/__internal__/sleep/1_ent_2
```

`@function loop_basic:reaper_framework/__internal__/sleep/1_ent_sch`

```mcfunction
execute store result score $0 reaper.var run time query gametime
scoreboard players operation $15 reaper.var = $0 reaper.var
scoreboard players remove $15 reaper.var 20
execute as @e[tag=reaper.sleep.1] run function loop_basic:reaper_framework/__internal__/sleep/1_ent_1
```

`@function loop_basic:reaper_framework/__internal__/sleep/1_ent_0`

```mcfunction
execute if entity @s unless entity @s[tag=reaper.object.holder] run function loop_basic:reaper_framework/__internal__/object/ensure_entry
data remove storage reaper:var data[8].v
execute store result score $0 reaper.var run time query gametime
execute store result storage reaper:var data[8].v.ts int 1 run scoreboard players get $0 reaper.var
data remove storage reaper:var data[1].v
forceload add 69000 69000
execute unless entity @e[tag=reaper.sleep.ctx, x=0] run function loop_basic:reaper_framework/__internal__/sleep/1_ent_ensure_ctx
execute as @e[tag=reaper.sleep.ctx, x=0] run function loop_basic:reaper_framework/__internal__/sleep/1_ent_get_ctx
data modify storage reaper:var data[8].v.ctx set from storage reaper:var data[1].v
function loop_basic:reaper_framework/__internal__/object/cache/3_0
tag @s add reaper.sleep.1
schedule function loop_basic:reaper_framework/__internal__/sleep/1_ent_sch 20 append
```

`@function loop_basic:reaper_framework/__internal__/sleep/1_exec`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/sleep/1_ent_0
```

`@function loop_basic:reaper_framework/__internal__/object/cache/7_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.loop.0.cycles_left[0]
```

`@function loop_basic:reaper_framework/__internal__/object/cache/7_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/7_1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/8_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop.0.cycles_left[0]
```

`@function loop_basic:reaper_framework/__internal__/object/cache/8_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/8_1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/9_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop.0.cycle_index[0]
```

`@function loop_basic:reaper_framework/__internal__/object/cache/9_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/9_1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/10_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop.0.cycles_left[0]
```

`@function loop_basic:reaper_framework/__internal__/object/cache/10_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/10_1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/11_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.loop.0.cycle_index[0]
```

`@function loop_basic:reaper_framework/__internal__/object/cache/11_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/11_1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/12_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop.0.cycle_index[0]
```

`@function loop_basic:reaper_framework/__internal__/object/cache/12_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/12_1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/13_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.0.cycles_left append value 0
execute store result entity @s data.__internal__.reaper.loop.0.cycles_left[-1] int 1 run scoreboard players get $7 reaper.var
```

`@function loop_basic:reaper_framework/__internal__/object/cache/13_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/13_1
```

`@function loop_basic:reaper_framework/__internal__/object/cache/14_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.0.cycle_index append value 0
execute store result entity @s data.__internal__.reaper.loop.0.cycle_index[-1] int 1 run scoreboard players get $6 reaper.var
```

`@function loop_basic:reaper_framework/__internal__/object/cache/14_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/14_1
```

`@function loop_basic:reaper_framework/sleep/1`

```mcfunction
function loop_basic:reaper_framework/__internal__/object/cache/7_0
execute store result score $7 reaper.var run data get storage reaper:var data[0].v 1
execute if score $7 reaper.var matches 0 run function demo:main/nested_execute_4
execute unless score $7 reaper.var matches 0 run function demo:main/nested_execute_5
```

`@function loop_basic:reaper_framework/__internal__/loop/cache/0_ent_cycle`

```mcfunction
function loop_basic:reaper_framework/__internal__/sleep/1_exec
```

`@function loop_basic:reaper_framework/__internal__/loop/cache/0_ent_break_thread`

```mcfunction
function loop_basic:reaper_framework/__internal__/object/cache/0_0
```

`@function loop_basic:reaper_framework/__internal__/loop/0_exec`

```mcfunction
execute unless entity @s run function demo:main/nested_execute_3
execute if entity @s run function demo:main/nested_execute_7
```

`@function loop_basic:reaper_framework/loop/0`

```mcfunction
help '$LOOP_DATA +threading'
scoreboard players set $5 reaper.var 0
execute if data entity @p SelectedItem run scoreboard players set $5 reaper.var 1
execute if score $5 reaper.var matches 1 unless entity @s run function loop_basic:reaper_framework/__internal__/loop/cache/0_srv_break_thread
execute if score $5 reaper.var matches 1 if entity @s run function loop_basic:reaper_framework/__internal__/loop/cache/0_ent_break_thread
execute unless score $5 reaper.var matches 1 run function loop_basic:reaper_framework/loop/break_nest/0_0
```

`@function loop_basic:reaper_framework/__internal__/object/cache/15_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop
```

`@function loop_basic:reaper_framework/__internal__/object/cache/15_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/15_1
```

`@function loop_basic:reaper_framework/__internal__/loop/onjoin_flush1`

```mcfunction
function loop_basic:reaper_framework/__internal__/object/cache/15_0
tag @s remove reaper.loop.0
```

`@function loop_basic:reaper_framework/__internal__/loop/onjoin_flush`

```mcfunction
execute if entity @s[tag=reaper.object.holder] run function loop_basic:reaper_framework/__internal__/loop/onjoin_flush1
```

`@function loop_basic:reaper_framework/loop/break_nest/0_0`

```mcfunction
scoreboard players operation $4 reaper.var = $3 reaper.var
tellraw @a {"score": {"name": "$4", "objective": "reaper.var"}, "color": "yellow"}
```

`@function loop_basic:reaper_framework/__internal__/object/cache/16_1`

```mcfunction
data remove entity @s data.__internal__.reaper.sleep
```

`@function loop_basic:reaper_framework/__internal__/object/cache/16_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_basic:reaper_framework/__internal__/object/cache/16_1
```

`@function loop_basic:reaper_framework/__internal__/sleep/onjoin_flush1`

```mcfunction
function loop_basic:reaper_framework/__internal__/object/cache/16_0
tag @s remove reaper.sleep.0
tag @s remove reaper.sleep.1
```

`@function loop_basic:reaper_framework/__internal__/sleep/onjoin_flush`

```mcfunction
execute if entity @s[tag=reaper.object.holder] run function loop_basic:reaper_framework/__internal__/sleep/onjoin_flush1
```

`@function loop_basic:reaper_framework/__internal__/var/flush_memory`

```mcfunction
data modify storage reaper:var data set value [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
```

### minecraft

`@function_tag minecraft:load`

```json
{
  "values": [
    "loop_basic:reaper_framework/__internal__/spark/init"
  ]
}
```

`@loot_table minecraft:entities/shulker`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "chance": 0.5,
          "condition": "minecraft:random_chance_with_looting",
          "looting_multiplier": 0.0625
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:shulker_shell"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/iron_golem`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:poppy"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/cat`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:string"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/fox`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/zombie_horse`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:rotten_flesh"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/blaze`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:blaze_rod"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/pillager`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/snow_golem`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 15.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:snowball"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/rabbit`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:rabbit_hide"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:rabbit"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        },
        {
          "chance": 0.1,
          "condition": "minecraft:random_chance_with_looting",
          "looting_multiplier": 0.03
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:rabbit_foot"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/polar_bear`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            },
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:cod",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            },
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:salmon"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/trader_llama`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:leather"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/illusioner`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/guardian`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:prismarine_shard"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            },
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            }
          ],
          "name": "minecraft:cod",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:prismarine_crystals",
          "weight": 2
        },
        {
          "type": "minecraft:empty"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        },
        {
          "chance": 0.025,
          "condition": "minecraft:random_chance_with_looting",
          "looting_multiplier": 0.01
        }
      ],
      "entries": [
        {
          "type": "minecraft:loot_table",
          "functions": [
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            }
          ],
          "name": "minecraft:gameplay/fishing/fish"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/piglin`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/parrot`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:feather"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/goat`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/dolphin`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            },
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            }
          ],
          "name": "minecraft:cod"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/sheep`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:mutton"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/squid`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:ink_sac"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/axolotl`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/giant`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/vindicator`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:emerald"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/armor_stand`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/panda`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bamboo"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/wandering_trader`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/cave_spider`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:string"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": -1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:spider_eye"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/witch`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:glowstone_dust"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:sugar"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:redstone"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:spider_eye"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:glass_bottle"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:gunpowder"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:stick",
          "weight": 2
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 3.0,
        "min": 1.0
      }
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/tadpole`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/zombie`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:rotten_flesh"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        },
        {
          "chance": 0.025,
          "condition": "minecraft:random_chance_with_looting",
          "looting_multiplier": 0.01
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:carrot"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            }
          ],
          "name": "minecraft:potato"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/bee`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/skeleton`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:arrow"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:bone"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/cow`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:leather"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:beef"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/creeper`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:gunpowder"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:entity_properties",
          "entity": "killer",
          "predicate": {
            "type": "#minecraft:skeletons"
          }
        }
      ],
      "entries": [
        {
          "type": "minecraft:tag",
          "expand": true,
          "name": "minecraft:creeper_drop_music_discs"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/mule`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:leather"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/phantom`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:phantom_membrane"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/glow_squid`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:glow_ink_sac"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/zombified_piglin`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:rotten_flesh"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:gold_nugget"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        },
        {
          "chance": 0.025,
          "condition": "minecraft:random_chance_with_looting",
          "looting_multiplier": 0.01
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_ingot"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/husk`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:rotten_flesh"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        },
        {
          "chance": 0.025,
          "condition": "minecraft:random_chance_with_looting",
          "looting_multiplier": 0.01
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:carrot"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            }
          ],
          "name": "minecraft:potato"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/pufferfish`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:pufferfish"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "chance": 0.05,
          "condition": "minecraft:random_chance"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:bone_meal"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/mooshroom`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:leather"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:beef"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/vex`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/villager`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/frog`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/magma_cube`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "conditions": [
            {
              "condition": "minecraft:inverted",
              "term": {
                "condition": "minecraft:damage_source_properties",
                "predicate": {
                  "source_entity": {
                    "type": "minecraft:frog"
                  }
                }
              }
            },
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "type_specific": {
                  "type": "slime",
                  "size": {
                    "min": 2
                  }
                }
              }
            }
          ],
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": -2.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:magma_cream"
        },
        {
          "type": "minecraft:item",
          "conditions": [
            {
              "condition": "minecraft:damage_source_properties",
              "predicate": {
                "source_entity": {
                  "type": "minecraft:frog",
                  "type_specific": {
                    "type": "frog",
                    "variant": "minecraft:warm"
                  }
                }
              }
            }
          ],
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:pearlescent_froglight"
        },
        {
          "type": "minecraft:item",
          "conditions": [
            {
              "condition": "minecraft:damage_source_properties",
              "predicate": {
                "source_entity": {
                  "type": "minecraft:frog",
                  "type_specific": {
                    "type": "frog",
                    "variant": "minecraft:cold"
                  }
                }
              }
            }
          ],
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:verdant_froglight"
        },
        {
          "type": "minecraft:item",
          "conditions": [
            {
              "condition": "minecraft:damage_source_properties",
              "predicate": {
                "source_entity": {
                  "type": "minecraft:frog",
                  "type_specific": {
                    "type": "frog",
                    "variant": "minecraft:temperate"
                  }
                }
              }
            }
          ],
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:ochre_froglight"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/zoglin`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:rotten_flesh"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/wither`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/pig`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:porkchop"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/evoker`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:totem_of_undying"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:emerald"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/ghast`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:ghast_tear"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:gunpowder"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/salmon`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            }
          ],
          "name": "minecraft:salmon"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "chance": 0.05,
          "condition": "minecraft:random_chance"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:bone_meal"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/endermite`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/spider`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:string"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": -1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:spider_eye"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/enderman`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:ender_pearl"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/elder_guardian`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:prismarine_shard"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            },
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            }
          ],
          "name": "minecraft:cod",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:prismarine_crystals",
          "weight": 2
        },
        {
          "type": "minecraft:empty"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:wet_sponge"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        },
        {
          "chance": 0.025,
          "condition": "minecraft:random_chance_with_looting",
          "looting_multiplier": 0.01
        }
      ],
      "entries": [
        {
          "type": "minecraft:loot_table",
          "functions": [
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            }
          ],
          "name": "minecraft:gameplay/fishing/fish"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/hoglin`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            },
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:porkchop"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:leather"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/slime`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:entity_properties",
          "entity": "this",
          "predicate": {
            "type_specific": {
              "type": "slime",
              "size": 1
            }
          }
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "conditions": [
            {
              "condition": "minecraft:inverted",
              "term": {
                "condition": "minecraft:damage_source_properties",
                "predicate": {
                  "source_entity": {
                    "type": "minecraft:frog"
                  }
                }
              }
            }
          ],
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:slime_ball"
        },
        {
          "type": "minecraft:item",
          "conditions": [
            {
              "condition": "minecraft:damage_source_properties",
              "predicate": {
                "source_entity": {
                  "type": "minecraft:frog"
                }
              }
            }
          ],
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:slime_ball"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/ocelot`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/stray`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:arrow"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:bone"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant",
              "limit": 1
            },
            {
              "function": "minecraft:set_potion",
              "id": "minecraft:slowness"
            }
          ],
          "name": "minecraft:tipped_arrow"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/strider`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:string"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/turtle`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:seagrass",
          "weight": 3
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:damage_source_properties",
          "predicate": {
            "is_lightning": true
          }
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:bowl"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/wither_skeleton`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": -1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:coal"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:bone"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        },
        {
          "chance": 0.025,
          "condition": "minecraft:random_chance_with_looting",
          "looting_multiplier": 0.01
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:wither_skeleton_skull"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/donkey`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:leather"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/skeleton_horse`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:bone"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/wolf`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/ender_dragon`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/cod`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            }
          ],
          "name": "minecraft:cod"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "chance": 0.05,
          "condition": "minecraft:random_chance"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:bone_meal"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/player`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper.death_event]}"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/drowned`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:rotten_flesh"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        },
        {
          "chance": 0.11,
          "condition": "minecraft:random_chance_with_looting",
          "looting_multiplier": 0.02
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:copper_ingot"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/allay`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/tropical_fish`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:tropical_fish"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "chance": 0.05,
          "condition": "minecraft:random_chance"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:bone_meal"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/llama`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:leather"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/chicken`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:feather"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:chicken"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/piglin_brute`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/zombie_villager`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:rotten_flesh"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:killed_by_player"
        },
        {
          "chance": 0.025,
          "condition": "minecraft:random_chance_with_looting",
          "looting_multiplier": 0.01
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:carrot"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            }
          ],
          "name": "minecraft:potato"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/horse`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:leather"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/warden`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:sculk_catalyst"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/silverfish`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/ravager`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:saddle"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table minecraft:entities/bat`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_star",
          "functions": [
            {
              "function": "minecraft:set_attributes",
              "modifiers": [
                {
                  "attribute": "minecraft:generic.luck",
                  "name": "",
                  "amount": {
                    "type": "minecraft:score",
                    "target": "this",
                    "score": "reaper.object"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper.object.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper.object": {
                  "min": 0
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### loop

`@function loop:test`

```mcfunction
function loop_basic:reaper_framework/__internal__/loop/0_exec
```
