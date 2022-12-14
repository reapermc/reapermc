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

`@function demo:test2`

```mcfunction
function loop_basic:reaper_framework/__internal__/loop/1/sel
```

`@function demo:test_insta`

```mcfunction
data modify storage loop_basic:reaper_framework.var data[23].v set value 30
scoreboard players set $45 loop_basic.reaper_framework.var 0
execute store result score $46 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[23].v 1
function loop_basic:reaper_framework/__internal__/loop/2/recursive
```

### reaper_framework

`@function_tag reaper_framework:__internal__/event_handler/on_server_load`

```json
{
  "values": [
    "loop_basic:reaper_framework/event/on_server_load"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_server_tick`

```json
{
  "values": [
    "loop_basic:reaper_framework/event/on_server_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_tick`

```json
{
  "values": [
    "loop_basic:reaper_framework/event/on_player_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_join`

```json
{
  "values": [
    "loop_basic:reaper_framework/event/on_player_join"
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
execute unless score $17 loop_basic.reaper_framework.var = $17 loop_basic.reaper_framework.var store result score $17 loop_basic.reaper_framework.var run seed
```

`@function reaper_framework:__internal__/sleep/nested_run_at_ctx/0`

```mcfunction
forceload add ~ ~
data modify entity @s Pos set from storage loop_basic:reaper_framework.var data[4].v.pos
data modify entity @s Rotation set from storage loop_basic:reaper_framework.var data[4].v.rot
tag @s add reaper_framework.sleep.ctx.target
```

`@function reaper_framework:__internal__/sleep/nested_run_at_ctx/1`

```mcfunction
forceload remove ~ ~
tag @s remove reaper_framework.sleep.ctx.target
tp @s 69000 0 69000
```

`@function reaper_framework:__internal__/sleep/create_ctx_marker`

```mcfunction
forceload add 69000 69000
summon marker 69000 0 69000 {Tags: ["reaper_framework.sleep.ctx", "reaper_framework.summon.init"], CustomName: '{"text": "reaper_framework.sleep.ctx", "color": "#bf0000"}'}
execute as @e[type=minecraft:marker, tag=reaper_framework.summon.init] at @s run function loop_basic:reaper_framework/summon/0
scoreboard players add #i reaper_framework.sleep.dim_id 1
```

`@function reaper_framework:__internal__/sleep/get_world_ctx`

```mcfunction
data remove storage loop_basic:reaper_framework.var data[3].v
tp @s ~ ~ ~ ~ ~
execute store result storage loop_basic:reaper_framework.var data[3].v.dim int 1 run scoreboard players get @s reaper_framework.sleep.dim_id
data modify storage loop_basic:reaper_framework.var data[3].v.pos set from entity @s Pos
data modify storage loop_basic:reaper_framework.var data[3].v.rot set from entity @s Rotation
tp @s 69000 0 69000
```

`@function reaper_framework:__internal__/sleep/run_at_ctx`

```mcfunction
execute as @e[type=marker, tag=reaper_framework.sleep.ctx] if score $5 loop_basic.reaper_framework.var = @s reaper_framework.sleep.dim_id at @s run function reaper_framework:__internal__/sleep/nested_run_at_ctx/0
```

`@function reaper_framework:__internal__/sleep/run_at_ctx_1`

```mcfunction
execute as @e[type=marker, tag=reaper_framework.sleep.ctx.target] at @s run function reaper_framework:__internal__/sleep/nested_run_at_ctx/1
```

`@function reaper_framework:__internal__/entity_nbt/garbage_collector`

```mcfunction
execute store result score $31 loop_basic.reaper_framework.var run data get entity @s Item.tag.AttributeModifiers[0].Amount 1
kill @s
execute as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score @s reaper_framework.entity_nbt.cloud = $31 loop_basic.reaper_framework.var run kill @s
```

`@function reaper_framework:__internal__/entity_nbt/ensure_entry`

```mcfunction
tag @s add reaper_framework.entity_nbt.user
forceload add 69000 69000
scoreboard players operation @s reaper_framework.entity_nbt.user = #i reaper_framework.entity_nbt.cloud
summon marker 69000 0 69000 {Tags: ["reaper_framework.entity_nbt.cloud", "reaper_framework.summon.init"], CustomName: '{"text": "reaper_framework.entity_nbt.cloud", "color": "#bf0000"}'}
execute as @e[type=minecraft:marker, tag=reaper_framework.summon.init] at @s run function loop_basic:reaper_framework/summon/1
```

`@function reaper_framework:__internal__/loop/reset_joining_player`

```mcfunction
execute if entity @s[tag=reaper_framework.entity_nbt.user] if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/28_remove
```

`@function reaper_framework:__internal__/sleep/reset_joining_player1`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/29_remove
tag @s remove loop_basic.reaper_framework.sleep.0
tag @s remove loop_basic.reaper_framework.sleep.1
tag @s remove loop_basic.reaper_framework.sleep.2
tag @s remove loop_basic.reaper_framework.sleep.3
```

`@function reaper_framework:__internal__/sleep/reset_joining_player`

```mcfunction
execute if entity @s[tag=reaper_framework.entity_nbt.user] run function reaper_framework:__internal__/sleep/reset_joining_player1
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

`@loot_table(strip_final_newline) minecraft:entities/sheep/green`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:green_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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

`@loot_table(strip_final_newline) minecraft:entities/sheep/cyan`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:cyan_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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

`@loot_table(strip_final_newline) minecraft:entities/sheep/purple`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:purple_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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

`@loot_table(strip_final_newline) minecraft:entities/sheep/brown`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:brown_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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

`@loot_table(strip_final_newline) minecraft:entities/sheep/lime`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:lime_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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

`@loot_table(strip_final_newline) minecraft:entities/sheep/black`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:black_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

`@loot_table(strip_final_newline) minecraft:entities/sheep/blue`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:blue_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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

`@loot_table(strip_final_newline) minecraft:entities/sheep/magenta`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:magenta_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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

`@loot_table(strip_final_newline) minecraft:entities/sheep/white`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:white_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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

`@loot_table(strip_final_newline) minecraft:entities/sheep/orange`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:orange_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

`@loot_table(strip_final_newline) minecraft:entities/sheep/yellow`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:yellow_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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

`@loot_table(strip_final_newline) minecraft:entities/sheep/pink`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:pink_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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

`@loot_table(strip_final_newline) minecraft:entities/sheep/red`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:red_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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

`@loot_table(strip_final_newline) minecraft:entities/sheep/gray`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gray_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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

`@loot_table(strip_final_newline) minecraft:entities/sheep/light_blue`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:light_blue_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

`@loot_table(strip_final_newline) minecraft:entities/sheep/light_gray`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:light_gray_wool"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "minecraft:entities/sheep"
        }
      ],
      "rolls": 1.0
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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
                    "score": "reaper_framework.entity_nbt.user"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.entity_nbt.death_cleanup: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_scores",
              "entity": "this",
              "scores": {
                "reaper_framework.entity_nbt.user": {
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

### loop_basic

`@function loop_basic:reaper_framework/event/on_server_load`

```mcfunction
function loop_basic:reaper_framework/__internal__/scoreboard/init
function loop_basic:reaper_framework/__internal__/scoreboard/init_defaults
function loop_basic:reaper_framework/__internal__/var/flush_memory
function loop_basic:reaper_framework/__internal__/var/init_defaults
execute as @a run function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/event_handler/on_server_tick/tick
execute as @a run function reaper_framework:__internal__/loop/reset_joining_player
scoreboard players set $19 loop_basic.reaper_framework.var 1630111353
scoreboard players set $20 loop_basic.reaper_framework.var 1623164762
scoreboard players set $21 loop_basic.reaper_framework.var 2147483647
function reaper_framework:__internal__/math/random/init
forceload add 0 0
kill @e[type=marker, tag=reaper_framework.math]
summon marker 0.0 0.0 0.0 {Tags: ["reaper_framework.math"], CustomName: '{"text": "reaper_framework.math", "color": "#bf0000"}'}
execute store result score $47 loop_basic.reaper_framework.var run gamerule doMobLoot
execute if score $47 loop_basic.reaper_framework.var matches 0 run function loop_basic:reaper_framework/__internal__/mob_loot_gamerule_error
```

`@function loop_basic:reaper_framework/__internal__/scoreboard/init`

```mcfunction
scoreboard objectives add loop_basic.reaper_framework.var dummy {"text": "loop_basic.reaper_framework.var", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.user dummy {"text": "reaper_framework.entity_nbt.user", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.cloud dummy {"text": "reaper_framework.entity_nbt.cloud", "color": "#bf0000"}
scoreboard objectives add loop_basic.reaper_framework.death_events dummy {"text": "loop_basic.reaper_framework.death_events", "color": "#bf0000"}
scoreboard objectives add reaper_framework.sleep.dim_id dummy {"text": "reaper_framework.sleep.dim_id", "color": "#bf0000"}
scoreboard objectives add reaper_framework.event_handler.on_player_join custom:leave_game {"text": "reaper_framework.event_handler.on_player_join", "color": "#bf0000"}
```

`@function loop_basic:reaper_framework/event/on_server_tick`

```mcfunction
execute as @a at @s run function #reaper_framework:__internal__/event_handler/on_player_tick
execute as @e[type=item, nbt={Item: {tag: {reaper_framework.entity_nbt.death_cleanup: 1b}}}] run function reaper_framework:__internal__/entity_nbt/garbage_collector
```

`@function loop_basic:reaper_framework/event/on_player_tick`

```mcfunction
execute if score @s reaper_framework.event_handler.on_player_join matches -1 run function reaper_framework:__internal__/event_handler/on_player_join/join
execute if score @s reaper_framework.event_handler.on_player_join matches 1.. run scoreboard players set @s reaper_framework.event_handler.on_player_join -1
```

`@function loop_basic:reaper_framework/event/on_player_join`

```mcfunction
function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/loop/reset_joining_player
```

`@function loop_basic:reaper_framework/__internal__/loop/0/s_2`

```mcfunction
data modify storage loop_basic:reaper_framework.var data[7].v append value 0
data modify storage loop_basic:reaper_framework.var data[6].v append value 0
execute store result storage loop_basic:reaper_framework.var data[6].v[-1] int 1 run scoreboard players get $27 loop_basic.reaper_framework.var
```

`@function loop_basic:reaper_framework/__internal__/loop/0/s_3`

```mcfunction
data remove storage loop_basic:reaper_framework.var data[6].v[-1]
data remove storage loop_basic:reaper_framework.var data[7].v[-1]
```

`@function loop_basic:reaper_framework/summon/0`

```mcfunction
scoreboard players operation @s reaper_framework.sleep.dim_id = #i reaper_framework.sleep.dim_id
tag @s remove reaper_framework.summon.init
```

`@function loop_basic:reaper_framework/__internal__/sleep/0/run_at_ctx`

```mcfunction
function reaper_framework:__internal__/sleep/run_at_ctx_1
function loop_basic:reaper_framework/sleep/0
```

`@function loop_basic:reaper_framework/__internal__/sleep/0/s_sch`

```mcfunction
execute store result score $29 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[8].v[0] 1
execute store result score $30 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[8].v[1] 1
data remove storage loop_basic:reaper_framework.var data[8].v[0]
execute if score $30 loop_basic.reaper_framework.var = $29 loop_basic.reaper_framework.var run function loop_basic:reaper_framework/__internal__/sleep/0/s_sch
data modify storage loop_basic:reaper_framework.var data[10].v set from storage loop_basic:reaper_framework.var data[11].v[0]
data remove storage loop_basic:reaper_framework.var data[11].v[0]
execute store result score $5 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[10].v.dim 1
data modify storage loop_basic:reaper_framework.var data[4].v set from storage loop_basic:reaper_framework.var data[10].v
function reaper_framework:__internal__/sleep/run_at_ctx
execute at @e[type=marker, tag=reaper_framework.sleep.ctx.target, limit=1] run function loop_basic:reaper_framework/__internal__/sleep/0/run_at_ctx
```

`@function loop_basic:reaper_framework/__internal__/sleep/0/s_0`

```mcfunction
execute unless entity @e[tag=reaper_framework.sleep.ctx, x=0] run function reaper_framework:__internal__/sleep/create_ctx_marker
execute as @e[tag=reaper_framework.sleep.ctx, x=0] run function reaper_framework:__internal__/sleep/get_world_ctx
data modify storage loop_basic:reaper_framework.var data[11].v append from storage loop_basic:reaper_framework.var data[3].v
execute store result score $4 loop_basic.reaper_framework.var run time query gametime
data modify storage loop_basic:reaper_framework.var data[8].v append value 0
execute store result storage loop_basic:reaper_framework.var data[8].v[-1] int 1 run scoreboard players get $4 loop_basic.reaper_framework.var
schedule function loop_basic:reaper_framework/__internal__/sleep/0/s_sch 20 append
```

`@function loop_basic:reaper_framework/__internal__/sleep/0/sel`

```mcfunction
execute unless entity @s run function loop_basic:reaper_framework/__internal__/sleep/0/s_0
```

`@function loop_basic:reaper_framework/__internal__/loop/0/s_5`

```mcfunction
scoreboard players remove $27 loop_basic.reaper_framework.var 1
scoreboard players add $26 loop_basic.reaper_framework.var 1
```

`@function loop_basic:reaper_framework/sleep/0`

```mcfunction
execute store result score $27 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[6].v[0] 1
execute store result score $26 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[7].v[0] 1
data remove storage loop_basic:reaper_framework.var data[6].v[0]
data remove storage loop_basic:reaper_framework.var data[7].v[0]
execute unless score $27 loop_basic.reaper_framework.var matches ..0 run function loop_basic:reaper_framework/__internal__/loop/0/s_5
data modify storage loop_basic:reaper_framework.var data[6].v append value 0
execute store result storage loop_basic:reaper_framework.var data[6].v[-1] int 1 run scoreboard players get $27 loop_basic.reaper_framework.var
data modify storage loop_basic:reaper_framework.var data[7].v append value 0
execute store result storage loop_basic:reaper_framework.var data[7].v[-1] int 1 run scoreboard players get $26 loop_basic.reaper_framework.var
scoreboard players operation $7 loop_basic.reaper_framework.var = $26 loop_basic.reaper_framework.var
function loop_basic:reaper_framework/loop/0
function loop_basic:reaper_framework/__internal__/loop/0/s_start
```

`@function loop_basic:reaper_framework/__internal__/loop/0/s_4`

```mcfunction
function loop_basic:reaper_framework/__internal__/sleep/0/sel
```

`@function loop_basic:reaper_framework/__internal__/loop/0/s_start`

```mcfunction
execute store result score $27 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[6].v[-1] 1
execute if score $27 loop_basic.reaper_framework.var matches 0 run function loop_basic:reaper_framework/__internal__/loop/0/s_3
execute unless score $27 loop_basic.reaper_framework.var matches 0 run function loop_basic:reaper_framework/__internal__/loop/0/s_4
```

`@function loop_basic:reaper_framework/__internal__/loop/0/s_1`

```mcfunction
execute if score $28 loop_basic.reaper_framework.var matches 0 run function loop_basic:reaper_framework/__internal__/loop/0/s_2
function loop_basic:reaper_framework/__internal__/loop/0/s_start
```

`@function loop_basic:reaper_framework/__internal__/loop/0/s_break_thread`

```mcfunction
data modify storage loop_basic:reaper_framework.var data[6].v[-1] set value 0
scoreboard players set $28 loop_basic.reaper_framework.var 1
```

`@function loop_basic:reaper_framework/__internal__/loop/0/s_0`

```mcfunction
scoreboard players set $28 loop_basic.reaper_framework.var 0
scoreboard players set $27 loop_basic.reaper_framework.var 4
scoreboard players set $7 loop_basic.reaper_framework.var 0
function loop_basic:reaper_framework/loop/0
execute unless score $27 loop_basic.reaper_framework.var matches 0 run function loop_basic:reaper_framework/__internal__/loop/0/s_1
```

`@function loop_basic:reaper_framework/summon/1`

```mcfunction
scoreboard players operation @s reaper_framework.entity_nbt.cloud = #i reaper_framework.entity_nbt.cloud
scoreboard players add #i reaper_framework.entity_nbt.cloud 1
tag @s remove reaper_framework.summon.init
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/0_set_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/0_set_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/0_set`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/0_set_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/0_set_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/0_set_p`

```mcfunction
data modify entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycles_left[-1] set value 0
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/1_remove_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/1_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/1_remove`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/1_remove_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/1_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/1_remove_p`

```mcfunction
data remove entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycle_index[-1]
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/2_remove_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/2_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/2_remove`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/2_remove_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/2_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/2_remove_p`

```mcfunction
data remove entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycles_left[-1]
```

`@function loop_basic:reaper_framework/__internal__/loop/0/e_1`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/1_remove
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/2_remove
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/3_append_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/3_append_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/3_append`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/3_append_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/3_append_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/3_append_p`

```mcfunction
data modify entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycle_index append value 0
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/4_append_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/4_append_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/4_append`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/4_append_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/4_append_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/4_append_p`

```mcfunction
data modify entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycles_left append value 4
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/5_append_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/5_append_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/5_append`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/5_append_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/5_append_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/5_append_p`

```mcfunction
data modify entity @s data.__internal__.loop_basic.reaper_framework.sleep.1 append from storage loop_basic:reaper_framework.var data[12].v
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/6_get_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/6_get_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/6_get`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/6_get_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/6_get_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/6_get_p`

```mcfunction
data modify storage loop_basic:reaper_framework.var data[2].v set from entity @s data.__internal__.loop_basic.reaper_framework.sleep.1
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/7_remove_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/7_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/7_remove`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/7_remove_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/7_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/7_remove_p`

```mcfunction
data remove entity @s data.__internal__.loop_basic.reaper_framework.sleep.1[0]
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/8_remove_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/8_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/8_remove`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/8_remove_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/8_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/8_remove_p`

```mcfunction
data remove entity @s data.__internal__.loop_basic.reaper_framework.sleep.1
```

`@function loop_basic:reaper_framework/__internal__/sleep/1/e_sch_3`

```mcfunction
tag @s remove loop_basic.reaper_framework.sleep.1
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/8_remove
```

`@function loop_basic:reaper_framework/__internal__/sleep/1/run_at_ctx`

```mcfunction
function reaper_framework:__internal__/sleep/run_at_ctx_1
function loop_basic:reaper_framework/sleep/1
```

`@function loop_basic:reaper_framework/__internal__/sleep/1/e_sch_2`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/7_remove
data remove storage loop_basic:reaper_framework.var data[14].v[0]
execute store result score $35 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[14].v[0].ts 1
execute store result score $37 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[14].v
execute if score $37 loop_basic.reaper_framework.var matches 0 run function loop_basic:reaper_framework/__internal__/sleep/1/e_sch_3
data modify storage loop_basic:reaper_framework.var data[17].v set from storage loop_basic:reaper_framework.var data[13].v.ctx
execute store result score $5 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[17].v.dim 1
data modify storage loop_basic:reaper_framework.var data[4].v set from storage loop_basic:reaper_framework.var data[17].v
function reaper_framework:__internal__/sleep/run_at_ctx
execute at @e[type=marker, tag=reaper_framework.sleep.ctx.target, limit=1] run function loop_basic:reaper_framework/__internal__/sleep/1/run_at_ctx
execute if score $35 loop_basic.reaper_framework.var = $34 loop_basic.reaper_framework.var run function loop_basic:reaper_framework/__internal__/sleep/1/e_sch
```

`@function loop_basic:reaper_framework/__internal__/sleep/1/e_sch_1`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/6_get
data modify storage loop_basic:reaper_framework.var data[14].v set from storage loop_basic:reaper_framework.var data[2].v
data modify storage loop_basic:reaper_framework.var data[13].v set from storage loop_basic:reaper_framework.var data[14].v[0]
execute store result score $34 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[13].v.ts 1
execute if score $34 loop_basic.reaper_framework.var = $36 loop_basic.reaper_framework.var run function loop_basic:reaper_framework/__internal__/sleep/1/e_sch_2
```

`@function loop_basic:reaper_framework/__internal__/sleep/1/e_sch`

```mcfunction
execute store result score $4 loop_basic.reaper_framework.var run time query gametime
scoreboard players operation $36 loop_basic.reaper_framework.var = $4 loop_basic.reaper_framework.var
scoreboard players remove $36 loop_basic.reaper_framework.var 20
execute as @e[tag=loop_basic.reaper_framework.sleep.1] run function loop_basic:reaper_framework/__internal__/sleep/1/e_sch_1
```

`@function loop_basic:reaper_framework/__internal__/sleep/1/e_0`

```mcfunction
data modify storage loop_basic:reaper_framework.var data[13].v set from storage loop_basic:reaper_framework.var data[15].v
execute if entity @s[type=!marker, tag=!reaper_framework.entity_nbt.user] run function reaper_framework:__internal__/entity_nbt/ensure_entry
data remove storage loop_basic:reaper_framework.var data[12].v
execute store result score $4 loop_basic.reaper_framework.var run time query gametime
execute store result storage loop_basic:reaper_framework.var data[12].v.ts int 1 run scoreboard players get $4 loop_basic.reaper_framework.var
execute unless entity @e[tag=reaper_framework.sleep.ctx, x=0] run function reaper_framework:__internal__/sleep/create_ctx_marker
execute as @e[tag=reaper_framework.sleep.ctx, x=0] run function reaper_framework:__internal__/sleep/get_world_ctx
data modify storage loop_basic:reaper_framework.var data[12].v.ctx set from storage loop_basic:reaper_framework.var data[3].v
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/5_append
tag @s add loop_basic.reaper_framework.sleep.1
schedule function loop_basic:reaper_framework/__internal__/sleep/1/e_sch 20 append
```

`@function loop_basic:reaper_framework/__internal__/sleep/1/sel`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/sleep/1/e_0
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/9_get_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/9_get_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/9_get`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/9_get_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/9_get_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/9_get_p`

```mcfunction
data modify storage loop_basic:reaper_framework.var data[2].v set from entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycles_left[0]
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/10_remove_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/10_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/10_remove`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/10_remove_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/10_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/10_remove_p`

```mcfunction
data remove entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycles_left[0]
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/11_remove_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/11_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/11_remove`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/11_remove_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/11_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/11_remove_p`

```mcfunction
data remove entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycle_index[0]
```

`@function loop_basic:reaper_framework/__internal__/loop/0/e_3`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/10_remove
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/11_remove
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/12_remove_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/12_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/12_remove`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/12_remove_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/12_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/12_remove_p`

```mcfunction
data remove entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycles_left[0]
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/13_get_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/13_get_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/13_get`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/13_get_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/13_get_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/13_get_p`

```mcfunction
data modify storage loop_basic:reaper_framework.var data[2].v set from entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycle_index[0]
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/14_remove_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/14_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/14_remove`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/14_remove_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/14_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/14_remove_p`

```mcfunction
data remove entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycle_index[0]
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/15_append_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/15_append_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/15_append`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/15_append_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/15_append_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/15_append_p`

```mcfunction
data modify entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycles_left append value 0
execute store result entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycles_left[-1] int 1 run scoreboard players get $33 loop_basic.reaper_framework.var
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/16_append_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/16_append_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/16_append`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/16_append_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/16_append_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/16_append_p`

```mcfunction
data modify entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycle_index append value 0
execute store result entity @s data.__internal__.loop_basic.reaper_framework.loop.0.cycle_index[-1] int 1 run scoreboard players get $32 loop_basic.reaper_framework.var
```

`@function loop_basic:reaper_framework/__internal__/loop/0/e_4`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/12_remove
scoreboard players remove $33 loop_basic.reaper_framework.var 1
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/13_get
execute store result score $32 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[2].v 1
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/14_remove
scoreboard players add $32 loop_basic.reaper_framework.var 1
scoreboard players operation $7 loop_basic.reaper_framework.var = $32 loop_basic.reaper_framework.var
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/15_append
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/16_append
function loop_basic:reaper_framework/loop/0
function loop_basic:reaper_framework/__internal__/loop/0/e_start
```

`@function loop_basic:reaper_framework/sleep/1`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/9_get
execute store result score $33 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[2].v 1
execute if score $33 loop_basic.reaper_framework.var matches 0 run function loop_basic:reaper_framework/__internal__/loop/0/e_3
execute unless score $33 loop_basic.reaper_framework.var matches 0 run function loop_basic:reaper_framework/__internal__/loop/0/e_4
```

`@function loop_basic:reaper_framework/__internal__/loop/0/e_start`

```mcfunction
function loop_basic:reaper_framework/__internal__/sleep/1/sel
```

`@function loop_basic:reaper_framework/__internal__/loop/0/e_2`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/4_append
function loop_basic:reaper_framework/__internal__/loop/0/e_start
```

`@function loop_basic:reaper_framework/__internal__/loop/0/e_break_thread`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/0_set
execute if score $33 loop_basic.reaper_framework.var matches 4 run function loop_basic:reaper_framework/__internal__/loop/0/e_1
scoreboard players set $33 loop_basic.reaper_framework.var 0
```

`@function loop_basic:reaper_framework/__internal__/loop/0/e_0`

```mcfunction
execute if entity @s[type=!marker, tag=!reaper_framework.entity_nbt.user] run function reaper_framework:__internal__/entity_nbt/ensure_entry
scoreboard players set $33 loop_basic.reaper_framework.var 4
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/3_append
scoreboard players set $7 loop_basic.reaper_framework.var 0
function loop_basic:reaper_framework/loop/0
execute unless score $33 loop_basic.reaper_framework.var matches 0 run function loop_basic:reaper_framework/__internal__/loop/0/e_2
```

`@function loop_basic:reaper_framework/__internal__/loop/0/sel`

```mcfunction
execute unless entity @s run function loop_basic:reaper_framework/__internal__/loop/0/s_0
execute if entity @s run function loop_basic:reaper_framework/__internal__/loop/0/e_0
```

`@function loop_basic:reaper_framework/loop/0`

```mcfunction
help '$LOOP_DATA +threading'
say hi
execute if score $7 loop_basic.reaper_framework.var matches 1 run say hello <cycle 1 only>
scoreboard players set $6 loop_basic.reaper_framework.var 0
execute if data entity @p SelectedItem run scoreboard players set $6 loop_basic.reaper_framework.var 1
execute if score $6 loop_basic.reaper_framework.var matches 1 unless entity @s run function loop_basic:reaper_framework/__internal__/loop/0/s_break_thread
execute if score $6 loop_basic.reaper_framework.var matches 1 if entity @s run function loop_basic:reaper_framework/__internal__/loop/0/e_break_thread
execute unless score $6 loop_basic.reaper_framework.var matches 1 run function loop_basic:reaper_framework/loop/break_nest/0_0
```

`@function loop_basic:reaper_framework/__internal__/sleep/2/run_at_ctx`

```mcfunction
function reaper_framework:__internal__/sleep/run_at_ctx_1
function loop_basic:reaper_framework/sleep/2
```

`@function loop_basic:reaper_framework/__internal__/sleep/2/s_sch`

```mcfunction
execute store result score $5 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[18].v.dim 1
data modify storage loop_basic:reaper_framework.var data[4].v set from storage loop_basic:reaper_framework.var data[18].v
function reaper_framework:__internal__/sleep/run_at_ctx
execute at @e[type=marker, tag=reaper_framework.sleep.ctx.target, limit=1] run function loop_basic:reaper_framework/__internal__/sleep/2/run_at_ctx
```

`@function loop_basic:reaper_framework/__internal__/sleep/2/s_0`

```mcfunction
execute unless entity @e[tag=reaper_framework.sleep.ctx, x=0] run function reaper_framework:__internal__/sleep/create_ctx_marker
execute as @e[tag=reaper_framework.sleep.ctx, x=0] run function reaper_framework:__internal__/sleep/get_world_ctx
data modify storage loop_basic:reaper_framework.var data[18].v set from storage loop_basic:reaper_framework.var data[3].v
schedule function loop_basic:reaper_framework/__internal__/sleep/2/s_sch 20 replace
```

`@function loop_basic:reaper_framework/__internal__/sleep/2/sel`

```mcfunction
execute unless entity @s run function loop_basic:reaper_framework/__internal__/sleep/2/s_0
```

`@function loop_basic:reaper_framework/sleep/2`

```mcfunction
scoreboard players remove $38 loop_basic.reaper_framework.var 1
scoreboard players add $39 loop_basic.reaper_framework.var 1
scoreboard players operation $7 loop_basic.reaper_framework.var = $39 loop_basic.reaper_framework.var
function loop_basic:reaper_framework/loop/1
execute unless score $38 loop_basic.reaper_framework.var matches 0 run function loop_basic:reaper_framework/__internal__/loop/1/s_start
```

`@function loop_basic:reaper_framework/__internal__/loop/1/s_start`

```mcfunction
function loop_basic:reaper_framework/__internal__/sleep/2/sel
```

`@function loop_basic:reaper_framework/__internal__/loop/1/s_break`

```mcfunction
scoreboard players set $38 loop_basic.reaper_framework.var 0
```

`@function loop_basic:reaper_framework/__internal__/loop/1/s_0`

```mcfunction
scoreboard players set $38 loop_basic.reaper_framework.var 2
scoreboard players set $39 loop_basic.reaper_framework.var 0
scoreboard players operation $7 loop_basic.reaper_framework.var = $39 loop_basic.reaper_framework.var
function loop_basic:reaper_framework/loop/1
execute unless score $38 loop_basic.reaper_framework.var matches 0 run function loop_basic:reaper_framework/__internal__/loop/1/s_start
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/17_remove_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/17_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/17_remove`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/17_remove_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/17_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/17_remove_p`

```mcfunction
data remove entity @s data.__internal__.loop_basic.reaper_framework.loop.1
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/18_set_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/18_set_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/18_set`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/18_set_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/18_set_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/18_set_p`

```mcfunction
data modify entity @s data.__internal__.loop_basic.reaper_framework.loop.1.cycle_index set value 0
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/19_set_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/19_set_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/19_set`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/19_set_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/19_set_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/19_set_p`

```mcfunction
data modify entity @s data.__internal__.loop_basic.reaper_framework.loop.1.cycles_left set value 2
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/20_set_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/20_set_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/20_set`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/20_set_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/20_set_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/20_set_p`

```mcfunction
data modify entity @s data.__internal__.loop_basic.reaper_framework.sleep.3 set from storage loop_basic:reaper_framework.var data[19].v
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/21_get_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/21_get_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/21_get`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/21_get_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/21_get_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/21_get_p`

```mcfunction
data modify storage loop_basic:reaper_framework.var data[2].v set from entity @s data.__internal__.loop_basic.reaper_framework.sleep.3
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/22_remove_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/22_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/22_remove`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/22_remove_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/22_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/22_remove_p`

```mcfunction
data remove entity @s data.__internal__.loop_basic.reaper_framework.sleep.3
```

`@function loop_basic:reaper_framework/__internal__/sleep/3/run_at_ctx`

```mcfunction
function reaper_framework:__internal__/sleep/run_at_ctx_1
function loop_basic:reaper_framework/sleep/3
```

`@function loop_basic:reaper_framework/__internal__/sleep/3/e_sch_2`

```mcfunction
tag @s remove loop_basic.reaper_framework.sleep.3
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/22_remove
data modify storage loop_basic:reaper_framework.var data[22].v set from storage loop_basic:reaper_framework.var data[20].v.ctx
execute store result score $5 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[22].v.dim 1
data modify storage loop_basic:reaper_framework.var data[4].v set from storage loop_basic:reaper_framework.var data[22].v
function reaper_framework:__internal__/sleep/run_at_ctx
execute at @e[type=marker, tag=reaper_framework.sleep.ctx.target, limit=1] run function loop_basic:reaper_framework/__internal__/sleep/3/run_at_ctx
```

`@function loop_basic:reaper_framework/__internal__/sleep/3/e_sch_1`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/21_get
data modify storage loop_basic:reaper_framework.var data[20].v set from storage loop_basic:reaper_framework.var data[2].v
execute store result score $42 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[20].v.ts 1
execute if score $42 loop_basic.reaper_framework.var = $43 loop_basic.reaper_framework.var run function loop_basic:reaper_framework/__internal__/sleep/3/e_sch_2
```

`@function loop_basic:reaper_framework/__internal__/sleep/3/e_sch`

```mcfunction
execute store result score $4 loop_basic.reaper_framework.var run time query gametime
scoreboard players operation $43 loop_basic.reaper_framework.var = $4 loop_basic.reaper_framework.var
scoreboard players remove $43 loop_basic.reaper_framework.var 20
execute as @e[tag=loop_basic.reaper_framework.sleep.3] run function loop_basic:reaper_framework/__internal__/sleep/3/e_sch_1
```

`@function loop_basic:reaper_framework/__internal__/sleep/3/e_0`

```mcfunction
execute if entity @s[type=!marker, tag=!reaper_framework.entity_nbt.user] run function reaper_framework:__internal__/entity_nbt/ensure_entry
data remove storage loop_basic:reaper_framework.var data[19].v
execute store result score $4 loop_basic.reaper_framework.var run time query gametime
execute store result storage loop_basic:reaper_framework.var data[19].v.ts int 1 run scoreboard players get $4 loop_basic.reaper_framework.var
execute unless entity @e[tag=reaper_framework.sleep.ctx, x=0] run function reaper_framework:__internal__/sleep/create_ctx_marker
execute as @e[tag=reaper_framework.sleep.ctx, x=0] run function reaper_framework:__internal__/sleep/get_world_ctx
data modify storage loop_basic:reaper_framework.var data[19].v.ctx set from storage loop_basic:reaper_framework.var data[3].v
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/20_set
tag @s add loop_basic.reaper_framework.sleep.3
schedule function loop_basic:reaper_framework/__internal__/sleep/3/e_sch 20 replace
```

`@function loop_basic:reaper_framework/__internal__/sleep/3/sel`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/sleep/3/e_0
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/23_get_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/23_get_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/23_get`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/23_get_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/23_get_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/23_get_p`

```mcfunction
data modify storage loop_basic:reaper_framework.var data[2].v set from entity @s data.__internal__.loop_basic.reaper_framework.loop.1.cycles_left
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/24_set_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/24_set_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/24_set`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/24_set_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/24_set_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/24_set_p`

```mcfunction
execute store result entity @s data.__internal__.loop_basic.reaper_framework.loop.1.cycles_left int 1 run scoreboard players get $41 loop_basic.reaper_framework.var
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/25_get_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/25_get_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/25_get`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/25_get_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/25_get_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/25_get_p`

```mcfunction
data modify storage loop_basic:reaper_framework.var data[2].v set from entity @s data.__internal__.loop_basic.reaper_framework.loop.1.cycle_index
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/26_set_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/26_set_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/26_set`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/26_set_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/26_set_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/26_set_p`

```mcfunction
execute store result entity @s data.__internal__.loop_basic.reaper_framework.loop.1.cycle_index int 1 run scoreboard players get $40 loop_basic.reaper_framework.var
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/27_remove_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/27_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/27_remove`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/27_remove_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/27_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/27_remove_p`

```mcfunction
data remove entity @s data.__internal__.loop_basic.reaper_framework.loop.1
```

`@function loop_basic:reaper_framework/sleep/3`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/23_get
execute store result score $41 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[2].v 1
scoreboard players remove $41 loop_basic.reaper_framework.var 1
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/24_set
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/25_get
execute store result score $40 loop_basic.reaper_framework.var run data get storage loop_basic:reaper_framework.var data[2].v 1
scoreboard players add $40 loop_basic.reaper_framework.var 1
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/26_set
scoreboard players operation $7 loop_basic.reaper_framework.var = $40 loop_basic.reaper_framework.var
execute if score $41 loop_basic.reaper_framework.var matches 0 if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/27_remove
function loop_basic:reaper_framework/loop/1
execute unless score $41 loop_basic.reaper_framework.var matches 0 run function loop_basic:reaper_framework/__internal__/loop/1/e_start
```

`@function loop_basic:reaper_framework/__internal__/loop/1/e_start`

```mcfunction
function loop_basic:reaper_framework/__internal__/sleep/3/sel
```

`@function loop_basic:reaper_framework/__internal__/loop/1/e_1`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/19_set
function loop_basic:reaper_framework/__internal__/loop/1/e_start
```

`@function loop_basic:reaper_framework/__internal__/loop/1/e_break`

```mcfunction
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/17_remove
scoreboard players set $41 loop_basic.reaper_framework.var 0
```

`@function loop_basic:reaper_framework/__internal__/loop/1/e_0`

```mcfunction
execute if entity @s[type=!marker, tag=!reaper_framework.entity_nbt.user] run function reaper_framework:__internal__/entity_nbt/ensure_entry
scoreboard players set $41 loop_basic.reaper_framework.var 2
execute if entity @s run function loop_basic:reaper_framework/__internal__/entity_nbt/18_set
scoreboard players set $7 loop_basic.reaper_framework.var 0
function loop_basic:reaper_framework/loop/1
execute unless score $41 loop_basic.reaper_framework.var matches 0 run function loop_basic:reaper_framework/__internal__/loop/1/e_1
```

`@function loop_basic:reaper_framework/__internal__/loop/1/sel`

```mcfunction
execute unless entity @s run function loop_basic:reaper_framework/__internal__/loop/1/s_0
execute if entity @s run function loop_basic:reaper_framework/__internal__/loop/1/e_0
```

`@function loop_basic:reaper_framework/loop/1`

```mcfunction
help '$LOOP_DATA -threading'
summon pig ~ ~5 ~ {Health: 1.0f, DeathLootTable: "idont:exist", DeathTime: 13s}
```

`@function loop_basic:reaper_framework/__internal__/loop/2/recursive`

```mcfunction
scoreboard players add $45 loop_basic.reaper_framework.var 1
function loop_basic:reaper_framework/loop/2
execute if score $45 loop_basic.reaper_framework.var < $46 loop_basic.reaper_framework.var run function loop_basic:reaper_framework/__internal__/loop/2/recursive
```

`@function loop_basic:reaper_framework/loop/2`

```mcfunction
help '$LOOP_DATA +threading'
say hello
```

`@function loop_basic:reaper_framework/__internal__/mob_loot_gamerule_error`

```mcfunction
gamerule doMobLoot true
tellraw @a [{"text": "\nreapermc ", "color": "gray"}, {"text": " WARN Gamerule 'doMobLoot' was changed to 'True'. ", "color": "gold"}, {"text": "Explanation", "color": "gold", "underlined": true, "hoverEvent": {"action": "show_text", "contents": [{"text": "ReaperMC Docs: How to disable doMobLoot.", "color": "gray"}]}, "clickEvent": {"action": "open_url", "value": "https://github.com/reapermc/reapermc/tree/main/docs/misc/mob_loot_gamerule.md"}}, {"text": ".", "color": "gold", "hoverEvent": {"action": "show_text", "contents": [{"text": "", "color": "gray"}]}}]
```

`@function loop_basic:reaper_framework/uninstall`

```mcfunction
function loop_basic:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l
function loop_basic:reaper_framework/var/u_n_i_n_s_t_a_l_l
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/28_remove_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/28_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/28_remove`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/28_remove_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/28_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/28_remove_p`

```mcfunction
data remove entity @s data.__internal__.loop_basic.reaper_framework.loop
```

`@function loop_basic:reaper_framework/loop/break_nest/0_0`

```mcfunction
summon pig ~ ~5 ~ {Health: 1.0f, DeathLootTable: "idont:exist", DeathTime: 13s}
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/29_remove_nm`

```mcfunction
scoreboard players operation $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.user
execute at @s as @e[type=marker, tag=reaper_framework.entity_nbt.cloud] if score $3 loop_basic.reaper_framework.var = @s reaper_framework.entity_nbt.cloud run function loop_basic:reaper_framework/__internal__/entity_nbt/29_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/29_remove`

```mcfunction
execute if entity @s[type=!marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/29_remove_nm
execute if entity @s[type=marker] run function loop_basic:reaper_framework/__internal__/entity_nbt/29_remove_p
```

`@function loop_basic:reaper_framework/__internal__/entity_nbt/29_remove_p`

```mcfunction
data remove entity @s data.__internal__.loop_basic.reaper_framework.sleep
```

`@function loop_basic:reaper_framework/var/u_n_i_n_s_t_a_l_l`

```mcfunction
data remove storage loop_basic:reaper_framework.var data
```

`@function loop_basic:reaper_framework/__internal__/var/flush_memory`

```mcfunction
data modify storage loop_basic:reaper_framework.var data set value [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
```

`@function loop_basic:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l`

```mcfunction
scoreboard objectives remove loop_basic.reaper_framework.var
scoreboard objectives remove loop_basic.reaper_framework.death_events
```

### looptest

`@function looptest:test`

```mcfunction
function loop_basic:reaper_framework/__internal__/loop/0/sel
```
