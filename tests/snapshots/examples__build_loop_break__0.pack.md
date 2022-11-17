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
scoreboard players set $9 reaper.var 2
scoreboard players set $10 reaper.var 0
scoreboard players operation $3 reaper.var = $10 reaper.var
function loop_break:reaper_framework/loop/0
execute unless score $9 reaper.var matches 0 run function loop_break:reaper_framework/__internal__/loop/cache/0_srv_cycle
```

`@function demo:main/nested_execute_1`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/2_0
function loop_break:reaper_framework/__internal__/loop/cache/0_ent_cycle
```

`@function demo:main/nested_execute_2`

```mcfunction
execute if entity @s unless entity @s[tag=reaper.object.holder] run function loop_break:reaper_framework/__internal__/object/ensure_entry
scoreboard players set $7 reaper.var 2
function loop_break:reaper_framework/__internal__/object/cache/1_0
scoreboard players set $3 reaper.var 0
function loop_break:reaper_framework/loop/0
execute unless score $7 reaper.var matches 0 run function demo:main/nested_execute_1
```

`@function demo:main/nested_execute_3`

```mcfunction
scoreboard players set $14 reaper.var 2
scoreboard players set $15 reaper.var 0
scoreboard players operation $3 reaper.var = $15 reaper.var
function loop_break:reaper_framework/loop/1
execute unless score $14 reaper.var matches 0 run function loop_break:reaper_framework/__internal__/loop/cache/1_srv_cycle
```

`@function demo:main/nested_execute_4`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/13_0
function loop_break:reaper_framework/__internal__/loop/cache/1_ent_cycle
```

`@function demo:main/nested_execute_5`

```mcfunction
execute if entity @s unless entity @s[tag=reaper.object.holder] run function loop_break:reaper_framework/__internal__/object/ensure_entry
scoreboard players set $7 reaper.var 2
function loop_break:reaper_framework/__internal__/object/cache/12_0
scoreboard players set $3 reaper.var 0
function loop_break:reaper_framework/loop/1
execute unless score $7 reaper.var matches 0 run function demo:main/nested_execute_4
```

`@function demo:main/nested_execute_6`

```mcfunction
data remove storage reaper:var data[6].v[0]
data remove storage reaper:var data[7].v[0]
```

`@function demo:main/nested_execute_7`

```mcfunction
data remove storage reaper:var data[6].v[0]
scoreboard players remove $20 reaper.var 1
execute store result score $6 reaper.var run data get storage reaper:var data[7].v[0] 1
data remove storage reaper:var data[7].v[0]
scoreboard players add $6 reaper.var 1
scoreboard players operation $3 reaper.var = $6 reaper.var
data modify storage reaper:var data[6].v append value 0
execute store result storage reaper:var data[6].v[-1] int 1 run scoreboard players get $20 reaper.var
data modify storage reaper:var data[7].v append value 0
execute store result storage reaper:var data[7].v[-1] int 1 run scoreboard players get $6 reaper.var
function loop_break:reaper_framework/loop/2
function loop_break:reaper_framework/__internal__/loop/cache/2_srv_cycle
```

`@function demo:main/nested_execute_8`

```mcfunction
data modify storage reaper:var data[6].v append value 2
function loop_break:reaper_framework/__internal__/loop/cache/2_srv_cycle
```

`@function demo:main/nested_execute_9`

```mcfunction
scoreboard players set $20 reaper.var 2
data modify storage reaper:var data[7].v append value 0
scoreboard players set $3 reaper.var 0
function loop_break:reaper_framework/loop/2
execute unless score $20 reaper.var matches 0 run function demo:main/nested_execute_8
```

`@function demo:main/nested_execute_10`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/30_0
function loop_break:reaper_framework/__internal__/object/cache/31_0
```

`@function demo:main/nested_execute_11`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/32_0
scoreboard players remove $7 reaper.var 1
function loop_break:reaper_framework/__internal__/object/cache/33_0
execute store result score $6 reaper.var run data get storage reaper:var data[0].v 1
function loop_break:reaper_framework/__internal__/object/cache/34_0
scoreboard players add $6 reaper.var 1
scoreboard players operation $3 reaper.var = $6 reaper.var
function loop_break:reaper_framework/__internal__/object/cache/35_0
function loop_break:reaper_framework/__internal__/object/cache/36_0
function loop_break:reaper_framework/loop/2
function loop_break:reaper_framework/__internal__/loop/cache/2_ent_cycle
```

`@function demo:main/nested_execute_12`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/24_0
function loop_break:reaper_framework/__internal__/loop/cache/2_ent_cycle
```

`@function demo:main/nested_execute_13`

```mcfunction
execute if entity @s unless entity @s[tag=reaper.object.holder] run function loop_break:reaper_framework/__internal__/object/ensure_entry
scoreboard players set $7 reaper.var 2
function loop_break:reaper_framework/__internal__/object/cache/23_0
scoreboard players set $3 reaper.var 0
function loop_break:reaper_framework/loop/2
execute unless score $7 reaper.var matches 0 run function demo:main/nested_execute_12
```

`@function demo:main/nested_execute_14`

```mcfunction
data remove storage reaper:var data[13].v[0]
data remove storage reaper:var data[14].v[0]
```

`@function demo:main/nested_execute_15`

```mcfunction
data remove storage reaper:var data[13].v[0]
scoreboard players remove $30 reaper.var 1
execute store result score $6 reaper.var run data get storage reaper:var data[14].v[0] 1
data remove storage reaper:var data[14].v[0]
scoreboard players add $6 reaper.var 1
scoreboard players operation $3 reaper.var = $6 reaper.var
data modify storage reaper:var data[13].v append value 0
execute store result storage reaper:var data[13].v[-1] int 1 run scoreboard players get $30 reaper.var
data modify storage reaper:var data[14].v append value 0
execute store result storage reaper:var data[14].v[-1] int 1 run scoreboard players get $6 reaper.var
function loop_break:reaper_framework/loop/3
function loop_break:reaper_framework/__internal__/loop/cache/3_srv_cycle
```

`@function demo:main/nested_execute_16`

```mcfunction
data modify storage reaper:var data[13].v append value 2
function loop_break:reaper_framework/__internal__/loop/cache/3_srv_cycle
```

`@function demo:main/nested_execute_17`

```mcfunction
scoreboard players set $30 reaper.var 2
data modify storage reaper:var data[14].v append value 0
scoreboard players set $3 reaper.var 0
function loop_break:reaper_framework/loop/3
execute unless score $30 reaper.var matches 0 run function demo:main/nested_execute_16
```

`@function demo:main/nested_execute_18`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/45_0
function loop_break:reaper_framework/__internal__/object/cache/46_0
```

`@function demo:main/nested_execute_19`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/47_0
scoreboard players remove $7 reaper.var 1
function loop_break:reaper_framework/__internal__/object/cache/48_0
execute store result score $6 reaper.var run data get storage reaper:var data[0].v 1
function loop_break:reaper_framework/__internal__/object/cache/49_0
scoreboard players add $6 reaper.var 1
scoreboard players operation $3 reaper.var = $6 reaper.var
function loop_break:reaper_framework/__internal__/object/cache/50_0
function loop_break:reaper_framework/__internal__/object/cache/51_0
function loop_break:reaper_framework/loop/3
function loop_break:reaper_framework/__internal__/loop/cache/3_ent_cycle
```

`@function demo:main/nested_execute_20`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/39_0
function loop_break:reaper_framework/__internal__/loop/cache/3_ent_cycle
```

`@function demo:main/nested_execute_21`

```mcfunction
execute if entity @s unless entity @s[tag=reaper.object.holder] run function loop_break:reaper_framework/__internal__/object/ensure_entry
scoreboard players set $7 reaper.var 2
function loop_break:reaper_framework/__internal__/object/cache/38_0
scoreboard players set $3 reaper.var 0
function loop_break:reaper_framework/loop/3
execute unless score $7 reaper.var matches 0 run function demo:main/nested_execute_20
```

### loop_break

`@function loop_break:reaper_framework/__internal__/spark/on_join`

```mcfunction
scoreboard players set @s reaper.spark 0
function loop_break:reaper_framework/spark/prejoin
function loop_break:reaper_framework/spark/join
function loop_break:reaper_framework/spark/postjoin
```

`@function loop_break:reaper_framework/__internal__/spark/init`

```mcfunction
scoreboard objectives add reaper.spark custom:leave_game {"text": "reaper.spark", "color": "#F06400"}
scoreboard players set @a reaper.spark 1
function loop_break:reaper_framework/spark/preload
function loop_break:reaper_framework/spark/load
function loop_break:reaper_framework/spark/postload
function loop_break:reaper_framework/__internal__/spark/clock
```

`@function loop_break:reaper_framework/__internal__/spark/clock`

```mcfunction
schedule function loop_break:reaper_framework/__internal__/spark/clock 1
execute as @a if score @s reaper.spark matches 1.. at @s run function loop_break:reaper_framework/__internal__/spark/on_join
function loop_break:reaper_framework/spark/pretick
function loop_break:reaper_framework/spark/tick
function loop_break:reaper_framework/spark/posttick
```

`@function loop_break:reaper_framework/spark/prejoin`

```mcfunction
function loop_break:reaper_framework/__internal__/sleep/onjoin_flush
function loop_break:reaper_framework/__internal__/loop/onjoin_flush
```

`@function loop_break:reaper_framework/spark/preload`

```mcfunction
function loop_break:reaper_framework/__internal__/scoreboard/init
function loop_break:reaper_framework/__internal__/scoreboard/init_defaults
function loop_break:reaper_framework/__internal__/var/flush_memory
function loop_break:reaper_framework/__internal__/var/init_defaults
```

`@function loop_break:reaper_framework/__internal__/scoreboard/init`

```mcfunction
scoreboard objectives add reaper.var dummy {"text": "reaper.var", "color": "#F06400"}
scoreboard objectives add reaper.object dummy {"text": "reaper.object", "color": "#F06400"}
scoreboard objectives add reaper.object.m dummy {"text": "reaper.object.m", "color": "#F06400"}
scoreboard objectives add reaper.sleep.dim_id dummy {"text": "reaper.sleep.dim_id", "color": "#F06400"}
scoreboard objectives add reaper.death_events dummy {"text": "reaper.death_events", "color": "#F06400"}
```

`@function loop_break:reaper_framework/better_summon/0`

```mcfunction
scoreboard players operation @s reaper.object.m = #next reaper.object
scoreboard players add #next reaper.object 1
tag @s remove reaper.summon.init
```

`@function loop_break:reaper_framework/__internal__/object/garbage_collector`

```mcfunction
execute store result score $2 reaper.var run data get entity @s Item.tag.AttributeModifiers[0].Amount 1
kill @s
execute as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = $2 reaper.var run kill @s
```

`@function loop_break:reaper_framework/__internal__/scoreboard/init_defaults`

```mcfunction
execute unless score #next reaper.object = #next reaper.object run scoreboard players set #next reaper.object 0
```

`@function loop_break:reaper_framework/object/remove_entity`

```mcfunction
scoreboard players operation $1 reaper.var = @s reaper.object
execute as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = $1 reaper.var run kill @s
scoreboard players reset @s reaper.object
tag @s remove reaper.object.holder
```

`@function loop_break:reaper_framework/__internal__/object/ensure_entry`

```mcfunction
scoreboard players operation @s reaper.object = #next reaper.object
forceload add 69000 69000
summon marker 69000 0 69000 {Tags: ["reaper.object.m", "reaper.summon.init"], CustomName: '{"text":"reaper.object.m","color":"#F06400"}'}
execute as @e[type=minecraft:marker, tag=reaper.summon.init] at @s run function loop_break:reaper_framework/better_summon/0
tag @s add reaper.object.holder
```

`@function loop_break:reaper_framework/spark/pretick`

```mcfunction
execute as @e[type=item, nbt={Item: {tag: {reaper.object.death_cleanup: 1b}}}] run function loop_break:reaper_framework/__internal__/object/garbage_collector
execute as @e[type=item] if data entity @s {Item: {tag: {reaper.death_event: 1b}}} at @s run function loop_break:reaper_framework/__internal__/death_events/get_item_info
```

`@function loop_break:reaper_framework/__internal__/death_events/get_item_info`

```mcfunction
execute store result score $find reaper.death_events run data get entity @s Item.tag.AttributeModifiers[0].Amount
kill @s
function loop_break:reaper_framework/__internal__/death_events/find_event
```

`@function loop_break:reaper_framework/__internal__/sleep/0_exec`

```mcfunction
execute unless entity @s run schedule function loop_break:reaper_framework/sleep/0 20 replace
```

`@function loop_break:reaper_framework/sleep/0`

```mcfunction
scoreboard players remove $9 reaper.var 1
scoreboard players add $10 reaper.var 1
scoreboard players operation $3 reaper.var = $10 reaper.var
function loop_break:reaper_framework/loop/0
execute unless score $9 reaper.var matches 0 run function loop_break:reaper_framework/__internal__/loop/cache/0_srv_cycle
```

`@function loop_break:reaper_framework/__internal__/loop/cache/0_srv_cycle`

```mcfunction
function loop_break:reaper_framework/__internal__/sleep/0_exec
```

`@function loop_break:reaper_framework/__internal__/loop/cache/0_srv_break`

```mcfunction
scoreboard players set $9 reaper.var 0
```

`@function loop_break:reaper_framework/__internal__/object/cache/0_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.0.cycles_left set value 0
```

`@function loop_break:reaper_framework/__internal__/object/cache/0_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/0_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/1_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.0.cycle_index set value 0
```

`@function loop_break:reaper_framework/__internal__/object/cache/1_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/1_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/2_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.0.cycles_left set value 2
```

`@function loop_break:reaper_framework/__internal__/object/cache/2_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/2_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/3_1`

```mcfunction
data modify entity @s data.__internal__.reaper.sleep.1 set from storage reaper:var data[2].v
```

`@function loop_break:reaper_framework/__internal__/object/cache/3_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/3_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/4_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.sleep.1
```

`@function loop_break:reaper_framework/__internal__/object/cache/4_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/4_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/5_1`

```mcfunction
data remove entity @s data.__internal__.reaper.sleep.1
```

`@function loop_break:reaper_framework/__internal__/object/cache/5_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/5_1
```

`@function loop_break:reaper_framework/__internal__/sleep/1_ent_2`

```mcfunction
tag @s remove reaper.sleep.1
function loop_break:reaper_framework/__internal__/object/cache/5_0
function loop_break:reaper_framework/sleep/1
```

`@function loop_break:reaper_framework/__internal__/sleep/1_ent_1`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/4_0
data modify storage reaper:var data[2].v set from storage reaper:var data[0].v
execute store result score $11 reaper.var run data get storage reaper:var data[2].v.ts 1
execute if score $11 reaper.var = $12 reaper.var run function loop_break:reaper_framework/__internal__/sleep/1_ent_2
```

`@function loop_break:reaper_framework/__internal__/sleep/1_ent_sch`

```mcfunction
execute store result score $0 reaper.var run time query gametime
scoreboard players operation $12 reaper.var = $0 reaper.var
scoreboard players remove $12 reaper.var 20
execute as @e[tag=reaper.sleep.1] run function loop_break:reaper_framework/__internal__/sleep/1_ent_1
```

`@function loop_break:reaper_framework/__internal__/sleep/1_ent_0`

```mcfunction
execute if entity @s unless entity @s[tag=reaper.object.holder] run function loop_break:reaper_framework/__internal__/object/ensure_entry
data remove storage reaper:var data[2].v
execute store result score $0 reaper.var run time query gametime
execute store result storage reaper:var data[2].v.ts int 1 run scoreboard players get $0 reaper.var
function loop_break:reaper_framework/__internal__/object/cache/3_0
tag @s add reaper.sleep.1
schedule function loop_break:reaper_framework/__internal__/sleep/1_ent_sch 20 append
```

`@function loop_break:reaper_framework/__internal__/sleep/1_exec`

```mcfunction
execute if entity @s run function loop_break:reaper_framework/__internal__/sleep/1_ent_0
```

`@function loop_break:reaper_framework/__internal__/object/cache/6_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.loop.0.cycles_left
```

`@function loop_break:reaper_framework/__internal__/object/cache/6_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/6_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/7_1`

```mcfunction
execute store result entity @s data.__internal__.reaper.loop.0.cycles_left int 1 run scoreboard players get $7 reaper.var
```

`@function loop_break:reaper_framework/__internal__/object/cache/7_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/7_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/8_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.loop.0.cycle_index
```

`@function loop_break:reaper_framework/__internal__/object/cache/8_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/8_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/9_1`

```mcfunction
execute store result entity @s data.__internal__.reaper.loop.0.cycle_index int 1 run scoreboard players get $6 reaper.var
```

`@function loop_break:reaper_framework/__internal__/object/cache/9_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/9_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/10_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop.0
```

`@function loop_break:reaper_framework/__internal__/object/cache/10_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/10_1
```

`@function loop_break:reaper_framework/sleep/1`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/6_0
execute store result score $7 reaper.var run data get storage reaper:var data[0].v 1
scoreboard players remove $7 reaper.var 1
function loop_break:reaper_framework/__internal__/object/cache/7_0
function loop_break:reaper_framework/__internal__/object/cache/8_0
execute store result score $6 reaper.var run data get storage reaper:var data[0].v 1
scoreboard players add $6 reaper.var 1
function loop_break:reaper_framework/__internal__/object/cache/9_0
scoreboard players operation $3 reaper.var = $6 reaper.var
execute if score $7 reaper.var matches 0 run function loop_break:reaper_framework/__internal__/object/cache/10_0
function loop_break:reaper_framework/loop/0
execute if score $5 reaper.var matches 1 run scoreboard players set $7 reaper.var 0
execute unless score $7 reaper.var matches 0 run function loop_break:reaper_framework/__internal__/loop/cache/0_ent_cycle
```

`@function loop_break:reaper_framework/__internal__/loop/cache/0_ent_cycle`

```mcfunction
function loop_break:reaper_framework/__internal__/sleep/1_exec
```

`@function loop_break:reaper_framework/__internal__/loop/cache/0_ent_break`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/0_0
```

`@function loop_break:reaper_framework/__internal__/loop/0_exec`

```mcfunction
execute unless entity @s run function demo:main/nested_execute_0
execute if entity @s run function demo:main/nested_execute_2
```

`@function loop_break:reaper_framework/loop/0`

```mcfunction
help '$LOOP_DATA -threading'
summon sheep ~ ~5 ~ {Health: 1, DeathLootTable: "idont:dropitems", DeathTime: 15}
say --
scoreboard players set $5 reaper.var 0
execute if data entity @p SelectedItem run scoreboard players set $5 reaper.var 1
execute if score $5 reaper.var matches 1 unless entity @s run function loop_break:reaper_framework/__internal__/loop/cache/0_srv_break
execute if score $5 reaper.var matches 1 if entity @s run function loop_break:reaper_framework/__internal__/loop/cache/0_ent_break
execute unless score $5 reaper.var matches 1 run function loop_break:reaper_framework/loop/break_nest/0_0
```

`@function loop_break:reaper_framework/better_summon/1`

```mcfunction
scoreboard players operation @s reaper.sleep.dim_id = #i reaper.sleep.dim_id
tag @s remove reaper.summon.init
```

`@function loop_break:reaper_framework/__internal__/sleep/2_srv_ensure_ctx`

```mcfunction
summon marker 69000 0 69000 {Tags: ["reaper.sleep.ctx", "reaper.summon.init"], CustomName: '{"text":"reaper.sleep.ctx","color":"#F06400"}'}
execute as @e[type=minecraft:marker, tag=reaper.summon.init] at @s run function loop_break:reaper_framework/better_summon/1
scoreboard players add #i reaper.sleep.dim_id 1
```

`@function loop_break:reaper_framework/__internal__/sleep/2_srv_get_ctx`

```mcfunction
tp @s ~ ~ ~ ~ ~
execute store result storage reaper:var data[1].v.dim int 1 run scoreboard players get @s reaper.sleep.dim_id
data modify storage reaper:var data[1].v.pos set from entity @s Pos
data modify storage reaper:var data[1].v.rot set from entity @s Rotation
tp @s 69000 0 69000
```

`@function loop_break:reaper_framework/__internal__/sleep/2_srv_1`

```mcfunction
data modify entity @s Pos set from storage reaper:var data[3].v.pos
data modify entity @s Rotation set from storage reaper:var data[3].v.rot
tag @s add reaper.sleep.ctx.target
```

`@function loop_break:reaper_framework/__internal__/sleep/2_srv_3`

```mcfunction
tag @s remove reaper.sleep.ctx.target
tp @s 69000 0 69000
```

`@function loop_break:reaper_framework/__internal__/sleep/2_srv_2`

```mcfunction
execute as @e[tag=reaper.sleep.ctx.target] run function loop_break:reaper_framework/__internal__/sleep/2_srv_3
function loop_break:reaper_framework/sleep/2
```

`@function loop_break:reaper_framework/__internal__/sleep/2_srv_sch`

```mcfunction
execute store result score $16 reaper.var run data get storage reaper:var data[3].v.dim 1
execute as @e[tag=reaper.sleep.ctx] if score $16 reaper.var = @s reaper.sleep.dim_id run function loop_break:reaper_framework/__internal__/sleep/2_srv_1
execute at @e[tag=reaper.sleep.ctx.target] run function loop_break:reaper_framework/__internal__/sleep/2_srv_2
```

`@function loop_break:reaper_framework/__internal__/sleep/2_srv_0`

```mcfunction
data remove storage reaper:var data[1].v
forceload add 69000 69000
execute unless entity @e[tag=reaper.sleep.ctx, x=0] run function loop_break:reaper_framework/__internal__/sleep/2_srv_ensure_ctx
execute as @e[tag=reaper.sleep.ctx, x=0] run function loop_break:reaper_framework/__internal__/sleep/2_srv_get_ctx
data modify storage reaper:var data[3].v set from storage reaper:var data[1].v
schedule function loop_break:reaper_framework/__internal__/sleep/2_srv_sch 15 replace
```

`@function loop_break:reaper_framework/__internal__/sleep/2_exec`

```mcfunction
execute unless entity @s run function loop_break:reaper_framework/__internal__/sleep/2_srv_0
```

`@function loop_break:reaper_framework/sleep/2`

```mcfunction
scoreboard players remove $14 reaper.var 1
scoreboard players add $15 reaper.var 1
scoreboard players operation $3 reaper.var = $15 reaper.var
function loop_break:reaper_framework/loop/1
execute unless score $14 reaper.var matches 0 run function loop_break:reaper_framework/__internal__/loop/cache/1_srv_cycle
```

`@function loop_break:reaper_framework/__internal__/loop/cache/1_srv_cycle`

```mcfunction
function loop_break:reaper_framework/__internal__/sleep/2_exec
```

`@function loop_break:reaper_framework/__internal__/loop/cache/1_srv_break`

```mcfunction
scoreboard players set $14 reaper.var 0
```

`@function loop_break:reaper_framework/__internal__/object/cache/11_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.1.cycles_left set value 0
```

`@function loop_break:reaper_framework/__internal__/object/cache/11_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/11_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/12_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.1.cycle_index set value 0
```

`@function loop_break:reaper_framework/__internal__/object/cache/12_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/12_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/13_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.1.cycles_left set value 2
```

`@function loop_break:reaper_framework/__internal__/object/cache/13_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/13_1
```

`@function loop_break:reaper_framework/better_summon/2`

```mcfunction
scoreboard players operation @s reaper.sleep.dim_id = #i reaper.sleep.dim_id
tag @s remove reaper.summon.init
```

`@function loop_break:reaper_framework/__internal__/sleep/3_ent_ensure_ctx`

```mcfunction
summon marker 69000 0 69000 {Tags: ["reaper.sleep.ctx", "reaper.summon.init"], CustomName: '{"text":"reaper.sleep.ctx","color":"#F06400"}'}
execute as @e[type=minecraft:marker, tag=reaper.summon.init] at @s run function loop_break:reaper_framework/better_summon/2
scoreboard players add #i reaper.sleep.dim_id 1
```

`@function loop_break:reaper_framework/__internal__/sleep/3_ent_get_ctx`

```mcfunction
tp @s ~ ~ ~ ~ ~
execute store result storage reaper:var data[1].v.dim int 1 run scoreboard players get @s reaper.sleep.dim_id
data modify storage reaper:var data[1].v.pos set from entity @s Pos
data modify storage reaper:var data[1].v.rot set from entity @s Rotation
tp @s 69000 0 69000
```

`@function loop_break:reaper_framework/__internal__/object/cache/14_1`

```mcfunction
data modify entity @s data.__internal__.reaper.sleep.3 set from storage reaper:var data[4].v
```

`@function loop_break:reaper_framework/__internal__/object/cache/14_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/14_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/15_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.sleep.3
```

`@function loop_break:reaper_framework/__internal__/object/cache/15_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/15_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/16_1`

```mcfunction
data remove entity @s data.__internal__.reaper.sleep.3
```

`@function loop_break:reaper_framework/__internal__/object/cache/16_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/16_1
```

`@function loop_break:reaper_framework/__internal__/sleep/3_ent_3`

```mcfunction
data modify entity @s Pos set from storage reaper:var data[5].v.pos
data modify entity @s Rotation set from storage reaper:var data[5].v.rot
tag @s add reaper.sleep.ctx.target
```

`@function loop_break:reaper_framework/__internal__/sleep/3_ent_5`

```mcfunction
tag @s remove reaper.sleep.ctx.target
tp @s 69000 0 69000
```

`@function loop_break:reaper_framework/__internal__/sleep/3_ent_4`

```mcfunction
execute as @e[tag=reaper.sleep.ctx.target] run function loop_break:reaper_framework/__internal__/sleep/3_ent_5
function loop_break:reaper_framework/sleep/3
```

`@function loop_break:reaper_framework/__internal__/sleep/3_ent_2`

```mcfunction
tag @s remove reaper.sleep.3
function loop_break:reaper_framework/__internal__/object/cache/16_0
data modify storage reaper:var data[5].v set from storage reaper:var data[4].v.ctx
execute store result score $19 reaper.var run data get storage reaper:var data[5].v.dim 1
execute as @e[tag=reaper.sleep.ctx] if score $19 reaper.var = @s reaper.sleep.dim_id run function loop_break:reaper_framework/__internal__/sleep/3_ent_3
execute at @e[tag=reaper.sleep.ctx.target] run function loop_break:reaper_framework/__internal__/sleep/3_ent_4
```

`@function loop_break:reaper_framework/__internal__/sleep/3_ent_1`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/15_0
data modify storage reaper:var data[4].v set from storage reaper:var data[0].v
execute store result score $17 reaper.var run data get storage reaper:var data[4].v.ts 1
execute if score $17 reaper.var = $18 reaper.var run function loop_break:reaper_framework/__internal__/sleep/3_ent_2
```

`@function loop_break:reaper_framework/__internal__/sleep/3_ent_sch`

```mcfunction
execute store result score $0 reaper.var run time query gametime
scoreboard players operation $18 reaper.var = $0 reaper.var
scoreboard players remove $18 reaper.var 15
execute as @e[tag=reaper.sleep.3] run function loop_break:reaper_framework/__internal__/sleep/3_ent_1
```

`@function loop_break:reaper_framework/__internal__/sleep/3_ent_0`

```mcfunction
execute if entity @s unless entity @s[tag=reaper.object.holder] run function loop_break:reaper_framework/__internal__/object/ensure_entry
data remove storage reaper:var data[4].v
execute store result score $0 reaper.var run time query gametime
execute store result storage reaper:var data[4].v.ts int 1 run scoreboard players get $0 reaper.var
data remove storage reaper:var data[1].v
forceload add 69000 69000
execute unless entity @e[tag=reaper.sleep.ctx, x=0] run function loop_break:reaper_framework/__internal__/sleep/3_ent_ensure_ctx
execute as @e[tag=reaper.sleep.ctx, x=0] run function loop_break:reaper_framework/__internal__/sleep/3_ent_get_ctx
data modify storage reaper:var data[4].v.ctx set from storage reaper:var data[1].v
function loop_break:reaper_framework/__internal__/object/cache/14_0
tag @s add reaper.sleep.3
schedule function loop_break:reaper_framework/__internal__/sleep/3_ent_sch 15 append
```

`@function loop_break:reaper_framework/__internal__/sleep/3_exec`

```mcfunction
execute if entity @s run function loop_break:reaper_framework/__internal__/sleep/3_ent_0
```

`@function loop_break:reaper_framework/__internal__/object/cache/17_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.loop.1.cycles_left
```

`@function loop_break:reaper_framework/__internal__/object/cache/17_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/17_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/18_1`

```mcfunction
execute store result entity @s data.__internal__.reaper.loop.1.cycles_left int 1 run scoreboard players get $7 reaper.var
```

`@function loop_break:reaper_framework/__internal__/object/cache/18_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/18_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/19_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.loop.1.cycle_index
```

`@function loop_break:reaper_framework/__internal__/object/cache/19_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/19_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/20_1`

```mcfunction
execute store result entity @s data.__internal__.reaper.loop.1.cycle_index int 1 run scoreboard players get $6 reaper.var
```

`@function loop_break:reaper_framework/__internal__/object/cache/20_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/20_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/21_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop.1
```

`@function loop_break:reaper_framework/__internal__/object/cache/21_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/21_1
```

`@function loop_break:reaper_framework/sleep/3`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/17_0
execute store result score $7 reaper.var run data get storage reaper:var data[0].v 1
scoreboard players remove $7 reaper.var 1
function loop_break:reaper_framework/__internal__/object/cache/18_0
function loop_break:reaper_framework/__internal__/object/cache/19_0
execute store result score $6 reaper.var run data get storage reaper:var data[0].v 1
scoreboard players add $6 reaper.var 1
function loop_break:reaper_framework/__internal__/object/cache/20_0
scoreboard players operation $3 reaper.var = $6 reaper.var
execute if score $7 reaper.var matches 0 run function loop_break:reaper_framework/__internal__/object/cache/21_0
function loop_break:reaper_framework/loop/1
execute if score $5 reaper.var matches 1 run scoreboard players set $7 reaper.var 0
execute unless score $7 reaper.var matches 0 run function loop_break:reaper_framework/__internal__/loop/cache/1_ent_cycle
```

`@function loop_break:reaper_framework/__internal__/loop/cache/1_ent_cycle`

```mcfunction
function loop_break:reaper_framework/__internal__/sleep/3_exec
```

`@function loop_break:reaper_framework/__internal__/loop/cache/1_ent_break`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/11_0
```

`@function loop_break:reaper_framework/__internal__/loop/1_exec`

```mcfunction
execute unless entity @s run function demo:main/nested_execute_3
execute if entity @s run function demo:main/nested_execute_5
```

`@function loop_break:reaper_framework/loop/1`

```mcfunction
help '$LOOP_DATA -threading'
summon sheep ~ ~5 ~ {Health: 1, DeathLootTable: "idont:dropitems", DeathTime: 15}
say this runs no matter fkin what
summon item ~ ~5 ~ {Item: {id: "minecraft:diamond", Count: 1b}}
scoreboard players set $5 reaper.var 0
execute if data entity @p SelectedItem run scoreboard players set $5 reaper.var 1
execute if score $5 reaper.var matches 1 unless entity @s run function loop_break:reaper_framework/__internal__/loop/cache/1_srv_break
execute if score $5 reaper.var matches 1 if entity @s run function loop_break:reaper_framework/__internal__/loop/cache/1_ent_break
execute unless score $5 reaper.var matches 1 run function loop_break:reaper_framework/loop/break_nest/1_0
```

`@function loop_break:reaper_framework/__internal__/sleep/4_srv_sch`

```mcfunction
execute store result score $22 reaper.var run data get storage reaper:var data[8].v[0] 1
execute store result score $23 reaper.var run data get storage reaper:var data[8].v[1] 1
data remove storage reaper:var data[8].v[0]
function loop_break:reaper_framework/sleep/4
execute if score $23 reaper.var = $22 reaper.var run function loop_break:reaper_framework/__internal__/sleep/4_srv_sch
```

`@function loop_break:reaper_framework/__internal__/sleep/4_srv_0`

```mcfunction
execute store result score $0 reaper.var run time query gametime
data modify storage reaper:var data[8].v append value 0
execute store result storage reaper:var data[8].v[-1] int 1 run scoreboard players get $0 reaper.var
schedule function loop_break:reaper_framework/__internal__/sleep/4_srv_sch 15 append
```

`@function loop_break:reaper_framework/__internal__/sleep/4_exec`

```mcfunction
execute unless entity @s run function loop_break:reaper_framework/__internal__/sleep/4_srv_0
```

`@function loop_break:reaper_framework/sleep/4`

```mcfunction
execute store result score $20 reaper.var run data get storage reaper:var data[6].v[0] 1
execute if score $20 reaper.var matches 0 run function demo:main/nested_execute_6
execute unless score $20 reaper.var matches 0 run function demo:main/nested_execute_7
```

`@function loop_break:reaper_framework/__internal__/loop/cache/2_srv_cycle`

```mcfunction
function loop_break:reaper_framework/__internal__/sleep/4_exec
```

`@function loop_break:reaper_framework/__internal__/loop/cache/2_srv_break_thread`

```mcfunction
data modify storage reaper:var data[6].v[-1] set value 0
```

`@function loop_break:reaper_framework/__internal__/object/cache/22_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.2.cycles_left[-1] set value 0
```

`@function loop_break:reaper_framework/__internal__/object/cache/22_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/22_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/23_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.2.cycle_index append value 0
```

`@function loop_break:reaper_framework/__internal__/object/cache/23_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/23_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/24_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.2.cycles_left append value 2
```

`@function loop_break:reaper_framework/__internal__/object/cache/24_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/24_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/25_1`

```mcfunction
data modify entity @s data.__internal__.reaper.sleep.5 append from storage reaper:var data[10].v
```

`@function loop_break:reaper_framework/__internal__/object/cache/25_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/25_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/26_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.sleep.5
```

`@function loop_break:reaper_framework/__internal__/object/cache/26_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/26_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/27_1`

```mcfunction
data remove entity @s data.__internal__.reaper.sleep.5[0]
```

`@function loop_break:reaper_framework/__internal__/object/cache/27_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/27_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/28_1`

```mcfunction
data remove entity @s data.__internal__.reaper.sleep.5
```

`@function loop_break:reaper_framework/__internal__/object/cache/28_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/28_1
```

`@function loop_break:reaper_framework/__internal__/sleep/5_ent_3`

```mcfunction
tag @s remove reaper.sleep.5
function loop_break:reaper_framework/__internal__/object/cache/28_0
```

`@function loop_break:reaper_framework/__internal__/sleep/5_ent_2`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/27_0
data remove storage reaper:var data[11].v[0]
execute store result score $26 reaper.var run data get storage reaper:var data[11].v[0].ts 1
execute store result score $28 reaper.var run data get storage reaper:var data[11].v
execute if score $28 reaper.var matches 0 run function loop_break:reaper_framework/__internal__/sleep/5_ent_3
function loop_break:reaper_framework/sleep/5
execute if score $26 reaper.var = $25 reaper.var run function loop_break:reaper_framework/__internal__/sleep/5_ent_sch
```

`@function loop_break:reaper_framework/__internal__/sleep/5_ent_1`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/26_0
data modify storage reaper:var data[11].v set from storage reaper:var data[0].v
data modify storage reaper:var data[12].v set from storage reaper:var data[11].v[0]
execute store result score $25 reaper.var run data get storage reaper:var data[12].v.ts 1
execute if score $25 reaper.var = $27 reaper.var run function loop_break:reaper_framework/__internal__/sleep/5_ent_2
```

`@function loop_break:reaper_framework/__internal__/sleep/5_ent_sch`

```mcfunction
execute store result score $0 reaper.var run time query gametime
scoreboard players operation $27 reaper.var = $0 reaper.var
scoreboard players remove $27 reaper.var 15
execute as @e[tag=reaper.sleep.5] run function loop_break:reaper_framework/__internal__/sleep/5_ent_1
```

`@function loop_break:reaper_framework/__internal__/sleep/5_ent_0`

```mcfunction
execute if entity @s unless entity @s[tag=reaper.object.holder] run function loop_break:reaper_framework/__internal__/object/ensure_entry
data remove storage reaper:var data[10].v
execute store result score $0 reaper.var run time query gametime
execute store result storage reaper:var data[10].v.ts int 1 run scoreboard players get $0 reaper.var
function loop_break:reaper_framework/__internal__/object/cache/25_0
tag @s add reaper.sleep.5
schedule function loop_break:reaper_framework/__internal__/sleep/5_ent_sch 15 append
```

`@function loop_break:reaper_framework/__internal__/sleep/5_exec`

```mcfunction
execute if entity @s run function loop_break:reaper_framework/__internal__/sleep/5_ent_0
```

`@function loop_break:reaper_framework/__internal__/object/cache/29_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.loop.2.cycles_left[0]
```

`@function loop_break:reaper_framework/__internal__/object/cache/29_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/29_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/30_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop.2.cycles_left[0]
```

`@function loop_break:reaper_framework/__internal__/object/cache/30_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/30_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/31_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop.2.cycle_index[0]
```

`@function loop_break:reaper_framework/__internal__/object/cache/31_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/31_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/32_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop.2.cycles_left[0]
```

`@function loop_break:reaper_framework/__internal__/object/cache/32_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/32_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/33_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.loop.2.cycle_index[0]
```

`@function loop_break:reaper_framework/__internal__/object/cache/33_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/33_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/34_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop.2.cycle_index[0]
```

`@function loop_break:reaper_framework/__internal__/object/cache/34_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/34_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/35_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.2.cycles_left append value 0
execute store result entity @s data.__internal__.reaper.loop.2.cycles_left[-1] int 1 run scoreboard players get $7 reaper.var
```

`@function loop_break:reaper_framework/__internal__/object/cache/35_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/35_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/36_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.2.cycle_index append value 0
execute store result entity @s data.__internal__.reaper.loop.2.cycle_index[-1] int 1 run scoreboard players get $6 reaper.var
```

`@function loop_break:reaper_framework/__internal__/object/cache/36_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/36_1
```

`@function loop_break:reaper_framework/sleep/5`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/29_0
execute store result score $7 reaper.var run data get storage reaper:var data[0].v 1
execute if score $7 reaper.var matches 0 run function demo:main/nested_execute_10
execute unless score $7 reaper.var matches 0 run function demo:main/nested_execute_11
```

`@function loop_break:reaper_framework/__internal__/loop/cache/2_ent_cycle`

```mcfunction
function loop_break:reaper_framework/__internal__/sleep/5_exec
```

`@function loop_break:reaper_framework/__internal__/loop/cache/2_ent_break_thread`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/22_0
```

`@function loop_break:reaper_framework/__internal__/loop/2_exec`

```mcfunction
execute unless entity @s run function demo:main/nested_execute_9
execute if entity @s run function demo:main/nested_execute_13
```

`@function loop_break:reaper_framework/loop/2`

```mcfunction
help '$LOOP_DATA +threading'
say -->
scoreboard players set $5 reaper.var 0
execute if data entity @p SelectedItem run scoreboard players set $5 reaper.var 1
execute if score $5 reaper.var matches 1 unless entity @s run function loop_break:reaper_framework/__internal__/loop/cache/2_srv_break_thread
execute if score $5 reaper.var matches 1 if entity @s run function loop_break:reaper_framework/__internal__/loop/cache/2_ent_break_thread
execute unless score $5 reaper.var matches 1 run function loop_break:reaper_framework/loop/break_nest/2_0
```

`@function loop_break:reaper_framework/better_summon/3`

```mcfunction
scoreboard players operation @s reaper.sleep.dim_id = #i reaper.sleep.dim_id
tag @s remove reaper.summon.init
```

`@function loop_break:reaper_framework/__internal__/sleep/6_srv_ensure_ctx`

```mcfunction
summon marker 69000 0 69000 {Tags: ["reaper.sleep.ctx", "reaper.summon.init"], CustomName: '{"text":"reaper.sleep.ctx","color":"#F06400"}'}
execute as @e[type=minecraft:marker, tag=reaper.summon.init] at @s run function loop_break:reaper_framework/better_summon/3
scoreboard players add #i reaper.sleep.dim_id 1
```

`@function loop_break:reaper_framework/__internal__/sleep/6_srv_get_ctx`

```mcfunction
tp @s ~ ~ ~ ~ ~
execute store result storage reaper:var data[1].v.dim int 1 run scoreboard players get @s reaper.sleep.dim_id
data modify storage reaper:var data[1].v.pos set from entity @s Pos
data modify storage reaper:var data[1].v.rot set from entity @s Rotation
tp @s 69000 0 69000
```

`@function loop_break:reaper_framework/__internal__/sleep/6_srv_1`

```mcfunction
data modify entity @s Pos set from storage reaper:var data[16].v.pos
data modify entity @s Rotation set from storage reaper:var data[16].v.rot
tag @s add reaper.sleep.ctx.target
```

`@function loop_break:reaper_framework/__internal__/sleep/6_srv_3`

```mcfunction
tag @s remove reaper.sleep.ctx.target
tp @s 69000 0 69000
```

`@function loop_break:reaper_framework/__internal__/sleep/6_srv_2`

```mcfunction
execute as @e[tag=reaper.sleep.ctx.target] run function loop_break:reaper_framework/__internal__/sleep/6_srv_3
function loop_break:reaper_framework/sleep/6
```

`@function loop_break:reaper_framework/__internal__/sleep/6_srv_sch`

```mcfunction
execute store result score $32 reaper.var run data get storage reaper:var data[15].v[0] 1
execute store result score $33 reaper.var run data get storage reaper:var data[15].v[1] 1
data remove storage reaper:var data[15].v[0]
data modify storage reaper:var data[16].v set from storage reaper:var data[17].v[0]
data remove storage reaper:var data[17].v[0]
execute store result score $34 reaper.var run data get storage reaper:var data[16].v.dim 1
execute as @e[tag=reaper.sleep.ctx] if score $34 reaper.var = @s reaper.sleep.dim_id run function loop_break:reaper_framework/__internal__/sleep/6_srv_1
execute at @e[tag=reaper.sleep.ctx.target] run function loop_break:reaper_framework/__internal__/sleep/6_srv_2
execute if score $33 reaper.var = $32 reaper.var run function loop_break:reaper_framework/__internal__/sleep/6_srv_sch
```

`@function loop_break:reaper_framework/__internal__/sleep/6_srv_0`

```mcfunction
execute store result score $0 reaper.var run time query gametime
data modify storage reaper:var data[15].v append value 0
execute store result storage reaper:var data[15].v[-1] int 1 run scoreboard players get $0 reaper.var
data remove storage reaper:var data[1].v
forceload add 69000 69000
execute unless entity @e[tag=reaper.sleep.ctx, x=0] run function loop_break:reaper_framework/__internal__/sleep/6_srv_ensure_ctx
execute as @e[tag=reaper.sleep.ctx, x=0] run function loop_break:reaper_framework/__internal__/sleep/6_srv_get_ctx
data modify storage reaper:var data[17].v append from storage reaper:var data[1].v
schedule function loop_break:reaper_framework/__internal__/sleep/6_srv_sch 15 append
```

`@function loop_break:reaper_framework/__internal__/sleep/6_exec`

```mcfunction
execute unless entity @s run function loop_break:reaper_framework/__internal__/sleep/6_srv_0
```

`@function loop_break:reaper_framework/sleep/6`

```mcfunction
execute store result score $30 reaper.var run data get storage reaper:var data[13].v[0] 1
execute if score $30 reaper.var matches 0 run function demo:main/nested_execute_14
execute unless score $30 reaper.var matches 0 run function demo:main/nested_execute_15
```

`@function loop_break:reaper_framework/__internal__/loop/cache/3_srv_cycle`

```mcfunction
function loop_break:reaper_framework/__internal__/sleep/6_exec
```

`@function loop_break:reaper_framework/__internal__/loop/cache/3_srv_break_thread`

```mcfunction
data modify storage reaper:var data[13].v[-1] set value 0
```

`@function loop_break:reaper_framework/__internal__/object/cache/37_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.3.cycles_left[-1] set value 0
```

`@function loop_break:reaper_framework/__internal__/object/cache/37_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/37_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/38_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.3.cycle_index append value 0
```

`@function loop_break:reaper_framework/__internal__/object/cache/38_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/38_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/39_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.3.cycles_left append value 2
```

`@function loop_break:reaper_framework/__internal__/object/cache/39_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/39_1
```

`@function loop_break:reaper_framework/better_summon/4`

```mcfunction
scoreboard players operation @s reaper.sleep.dim_id = #i reaper.sleep.dim_id
tag @s remove reaper.summon.init
```

`@function loop_break:reaper_framework/__internal__/sleep/7_ent_ensure_ctx`

```mcfunction
summon marker 69000 0 69000 {Tags: ["reaper.sleep.ctx", "reaper.summon.init"], CustomName: '{"text":"reaper.sleep.ctx","color":"#F06400"}'}
execute as @e[type=minecraft:marker, tag=reaper.summon.init] at @s run function loop_break:reaper_framework/better_summon/4
scoreboard players add #i reaper.sleep.dim_id 1
```

`@function loop_break:reaper_framework/__internal__/sleep/7_ent_get_ctx`

```mcfunction
tp @s ~ ~ ~ ~ ~
execute store result storage reaper:var data[1].v.dim int 1 run scoreboard players get @s reaper.sleep.dim_id
data modify storage reaper:var data[1].v.pos set from entity @s Pos
data modify storage reaper:var data[1].v.rot set from entity @s Rotation
tp @s 69000 0 69000
```

`@function loop_break:reaper_framework/__internal__/object/cache/40_1`

```mcfunction
data modify entity @s data.__internal__.reaper.sleep.7 append from storage reaper:var data[19].v
```

`@function loop_break:reaper_framework/__internal__/object/cache/40_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/40_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/41_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.sleep.7
```

`@function loop_break:reaper_framework/__internal__/object/cache/41_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/41_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/42_1`

```mcfunction
data remove entity @s data.__internal__.reaper.sleep.7[0]
```

`@function loop_break:reaper_framework/__internal__/object/cache/42_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/42_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/43_1`

```mcfunction
data remove entity @s data.__internal__.reaper.sleep.7
```

`@function loop_break:reaper_framework/__internal__/object/cache/43_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/43_1
```

`@function loop_break:reaper_framework/__internal__/sleep/7_ent_3`

```mcfunction
tag @s remove reaper.sleep.7
function loop_break:reaper_framework/__internal__/object/cache/43_0
```

`@function loop_break:reaper_framework/__internal__/sleep/7_ent_4`

```mcfunction
data modify entity @s Pos set from storage reaper:var data[18].v.pos
data modify entity @s Rotation set from storage reaper:var data[18].v.rot
tag @s add reaper.sleep.ctx.target
```

`@function loop_break:reaper_framework/__internal__/sleep/7_ent_6`

```mcfunction
tag @s remove reaper.sleep.ctx.target
tp @s 69000 0 69000
```

`@function loop_break:reaper_framework/__internal__/sleep/7_ent_5`

```mcfunction
execute as @e[tag=reaper.sleep.ctx.target] run function loop_break:reaper_framework/__internal__/sleep/7_ent_6
function loop_break:reaper_framework/sleep/7
```

`@function loop_break:reaper_framework/__internal__/sleep/7_ent_2`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/42_0
data remove storage reaper:var data[20].v[0]
execute store result score $36 reaper.var run data get storage reaper:var data[20].v[0].ts 1
execute store result score $38 reaper.var run data get storage reaper:var data[20].v
execute if score $38 reaper.var matches 0 run function loop_break:reaper_framework/__internal__/sleep/7_ent_3
data modify storage reaper:var data[18].v set from storage reaper:var data[21].v.ctx
execute store result score $39 reaper.var run data get storage reaper:var data[18].v.dim 1
execute as @e[tag=reaper.sleep.ctx] if score $39 reaper.var = @s reaper.sleep.dim_id run function loop_break:reaper_framework/__internal__/sleep/7_ent_4
execute at @e[tag=reaper.sleep.ctx.target] run function loop_break:reaper_framework/__internal__/sleep/7_ent_5
execute if score $36 reaper.var = $35 reaper.var run function loop_break:reaper_framework/__internal__/sleep/7_ent_sch
```

`@function loop_break:reaper_framework/__internal__/sleep/7_ent_1`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/41_0
data modify storage reaper:var data[20].v set from storage reaper:var data[0].v
data modify storage reaper:var data[21].v set from storage reaper:var data[20].v[0]
execute store result score $35 reaper.var run data get storage reaper:var data[21].v.ts 1
execute if score $35 reaper.var = $37 reaper.var run function loop_break:reaper_framework/__internal__/sleep/7_ent_2
```

`@function loop_break:reaper_framework/__internal__/sleep/7_ent_sch`

```mcfunction
execute store result score $0 reaper.var run time query gametime
scoreboard players operation $37 reaper.var = $0 reaper.var
scoreboard players remove $37 reaper.var 15
execute as @e[tag=reaper.sleep.7] run function loop_break:reaper_framework/__internal__/sleep/7_ent_1
```

`@function loop_break:reaper_framework/__internal__/sleep/7_ent_0`

```mcfunction
execute if entity @s unless entity @s[tag=reaper.object.holder] run function loop_break:reaper_framework/__internal__/object/ensure_entry
data remove storage reaper:var data[19].v
execute store result score $0 reaper.var run time query gametime
execute store result storage reaper:var data[19].v.ts int 1 run scoreboard players get $0 reaper.var
data remove storage reaper:var data[1].v
forceload add 69000 69000
execute unless entity @e[tag=reaper.sleep.ctx, x=0] run function loop_break:reaper_framework/__internal__/sleep/7_ent_ensure_ctx
execute as @e[tag=reaper.sleep.ctx, x=0] run function loop_break:reaper_framework/__internal__/sleep/7_ent_get_ctx
data modify storage reaper:var data[19].v.ctx set from storage reaper:var data[1].v
function loop_break:reaper_framework/__internal__/object/cache/40_0
tag @s add reaper.sleep.7
schedule function loop_break:reaper_framework/__internal__/sleep/7_ent_sch 15 append
```

`@function loop_break:reaper_framework/__internal__/sleep/7_exec`

```mcfunction
execute if entity @s run function loop_break:reaper_framework/__internal__/sleep/7_ent_0
```

`@function loop_break:reaper_framework/__internal__/object/cache/44_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.loop.3.cycles_left[0]
```

`@function loop_break:reaper_framework/__internal__/object/cache/44_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/44_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/45_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop.3.cycles_left[0]
```

`@function loop_break:reaper_framework/__internal__/object/cache/45_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/45_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/46_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop.3.cycle_index[0]
```

`@function loop_break:reaper_framework/__internal__/object/cache/46_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/46_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/47_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop.3.cycles_left[0]
```

`@function loop_break:reaper_framework/__internal__/object/cache/47_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/47_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/48_1`

```mcfunction
data modify storage reaper:var data[0].v set from entity @s data.__internal__.reaper.loop.3.cycle_index[0]
```

`@function loop_break:reaper_framework/__internal__/object/cache/48_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/48_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/49_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop.3.cycle_index[0]
```

`@function loop_break:reaper_framework/__internal__/object/cache/49_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/49_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/50_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.3.cycles_left append value 0
execute store result entity @s data.__internal__.reaper.loop.3.cycles_left[-1] int 1 run scoreboard players get $7 reaper.var
```

`@function loop_break:reaper_framework/__internal__/object/cache/50_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/50_1
```

`@function loop_break:reaper_framework/__internal__/object/cache/51_1`

```mcfunction
data modify entity @s data.__internal__.reaper.loop.3.cycle_index append value 0
execute store result entity @s data.__internal__.reaper.loop.3.cycle_index[-1] int 1 run scoreboard players get $6 reaper.var
```

`@function loop_break:reaper_framework/__internal__/object/cache/51_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/51_1
```

`@function loop_break:reaper_framework/sleep/7`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/44_0
execute store result score $7 reaper.var run data get storage reaper:var data[0].v 1
execute if score $7 reaper.var matches 0 run function demo:main/nested_execute_18
execute unless score $7 reaper.var matches 0 run function demo:main/nested_execute_19
```

`@function loop_break:reaper_framework/__internal__/loop/cache/3_ent_cycle`

```mcfunction
function loop_break:reaper_framework/__internal__/sleep/7_exec
```

`@function loop_break:reaper_framework/__internal__/loop/cache/3_ent_break_thread`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/37_0
```

`@function loop_break:reaper_framework/__internal__/loop/3_exec`

```mcfunction
execute unless entity @s run function demo:main/nested_execute_17
execute if entity @s run function demo:main/nested_execute_21
```

`@function loop_break:reaper_framework/loop/3`

```mcfunction
help '$LOOP_DATA +threading'
say -->
scoreboard players set $5 reaper.var 0
execute if data entity @p SelectedItem run scoreboard players set $5 reaper.var 1
execute if score $5 reaper.var matches 1 unless entity @s run function loop_break:reaper_framework/__internal__/loop/cache/3_srv_break_thread
execute if score $5 reaper.var matches 1 if entity @s run function loop_break:reaper_framework/__internal__/loop/cache/3_ent_break_thread
execute unless score $5 reaper.var matches 1 run function loop_break:reaper_framework/loop/break_nest/3_0
```

`@function loop_break:reaper_framework/__internal__/object/cache/52_1`

```mcfunction
data remove entity @s data.__internal__.reaper.loop
```

`@function loop_break:reaper_framework/__internal__/object/cache/52_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/52_1
```

`@function loop_break:reaper_framework/__internal__/loop/onjoin_flush1`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/52_0
tag @s remove reaper.loop.0
tag @s remove reaper.loop.1
tag @s remove reaper.loop.2
tag @s remove reaper.loop.3
```

`@function loop_break:reaper_framework/__internal__/loop/onjoin_flush`

```mcfunction
execute if entity @s[tag=reaper.object.holder] run function loop_break:reaper_framework/__internal__/loop/onjoin_flush1
```

`@function loop_break:reaper_framework/loop/break_nest/0_0`

```mcfunction
particle flash
say hello
```

`@function loop_break:reaper_framework/loop/break_nest/1_0`

```mcfunction
say this runs after the possible break
particle flash
```

`@function loop_break:reaper_framework/loop/break_nest/2_0`

```mcfunction
summon sheep ~ ~5 ~ {Health: 1, DeathLootTable: "idont:dropitems", DeathTime: 15}
particle flash
summon item ~ ~5 ~ {Item: {id: "minecraft:diamond", Count: 1b}}
```

`@function loop_break:reaper_framework/loop/break_nest/3_0`

```mcfunction
summon sheep ~ ~5 ~ {Health: 1, DeathLootTable: "idont:dropitems", DeathTime: 15}
particle flash
```

`@function loop_break:reaper_framework/__internal__/object/cache/53_1`

```mcfunction
data remove entity @s data.__internal__.reaper.sleep
```

`@function loop_break:reaper_framework/__internal__/object/cache/53_0`

```mcfunction
execute if entity @s at @s as @e[type=marker, tag=reaper.object.m] if score @s reaper.object.m = @e[tag=reaper.object.holder, sort=nearest, limit=1] reaper.object run function loop_break:reaper_framework/__internal__/object/cache/53_1
```

`@function loop_break:reaper_framework/__internal__/sleep/onjoin_flush1`

```mcfunction
function loop_break:reaper_framework/__internal__/object/cache/53_0
tag @s remove reaper.sleep.0
tag @s remove reaper.sleep.1
tag @s remove reaper.sleep.2
tag @s remove reaper.sleep.3
tag @s remove reaper.sleep.4
tag @s remove reaper.sleep.5
tag @s remove reaper.sleep.6
tag @s remove reaper.sleep.7
```

`@function loop_break:reaper_framework/__internal__/sleep/onjoin_flush`

```mcfunction
execute if entity @s[tag=reaper.object.holder] run function loop_break:reaper_framework/__internal__/sleep/onjoin_flush1
```

`@function loop_break:reaper_framework/__internal__/var/flush_memory`

```mcfunction
data modify storage reaper:var data set value [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
```

### minecraft

`@function_tag minecraft:load`

```json
{
  "values": [
    "loop_break:reaper_framework/__internal__/spark/init"
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

### loop

`@function loop:no_context`

```mcfunction
function loop_break:reaper_framework/__internal__/loop/0_exec
```

`@function loop:context`

```mcfunction
function loop_break:reaper_framework/__internal__/loop/1_exec
```

`@function loop:no_context_threaded`

```mcfunction
function loop_break:reaper_framework/__internal__/loop/2_exec
```

`@function loop:context_threaded`

```mcfunction
function loop_break:reaper_framework/__internal__/loop/3_exec
```
