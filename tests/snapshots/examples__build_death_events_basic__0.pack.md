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

`@function demo:test`

```mcfunction
summon cow ~ ~ ~ {Tags: ["reaper_framework.summon.init"]}
execute as @e[type=minecraft:cow, tag=reaper_framework.summon.init] at @s run function death_events_basic:reaper_framework/summon/1
```

### reaper_framework

`@function_tag reaper_framework:__internal__/event_handler/on_server_load`

```json
{
  "values": [
    "death_events_basic:reaper_framework/event/on_server_load"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_server_tick`

```json
{
  "values": [
    "death_events_basic:reaper_framework/event/on_server_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_tick`

```json
{
  "values": [
    "death_events_basic:reaper_framework/event/on_player_tick"
  ]
}
```

`@function_tag reaper_framework:__internal__/event_handler/on_player_join`

```json
{
  "values": [
    "death_events_basic:reaper_framework/event/on_player_join"
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
execute unless score $17 death_events_basic.reaper_framework.var = $17 death_events_basic.reaper_framework.var store result score $17 death_events_basic.reaper_framework.var run seed
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
              }
            }
          ]
        }
      ]
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
              }
            }
          ]
        }
      ]
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
              }
            }
          ]
        }
      ]
    }
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
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
                    "score": "death_events_basic.reaper_framework.death_events"
                  },
                  "operation": "addition",
                  "slot": "feet"
                }
              ]
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{reaper_framework.death_event: 1b}"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:entity_properties",
              "entity": "this",
              "predicate": {
                "nbt": "{Tags:[reaper_framework.death_event]}"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### death_events_basic

`@function death_events_basic:reaper_framework/event/on_server_load`

```mcfunction
function death_events_basic:reaper_framework/__internal__/scoreboard/init
function death_events_basic:reaper_framework/__internal__/scoreboard/init_defaults
function death_events_basic:reaper_framework/__internal__/var/flush_memory
function death_events_basic:reaper_framework/__internal__/var/init_defaults
execute as @a run function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/event_handler/on_server_tick/tick
execute as @a run function reaper_framework:__internal__/loop/reset_joining_player
scoreboard players set $19 death_events_basic.reaper_framework.var 1630111353
scoreboard players set $20 death_events_basic.reaper_framework.var 1623164762
scoreboard players set $21 death_events_basic.reaper_framework.var 2147483647
function reaper_framework:__internal__/math/random/init
forceload add 0 0
kill @e[type=marker, tag=reaper_framework.math]
summon marker 0.0 0.0 0.0 {Tags: ["reaper_framework.math"], CustomName: '{"text": "reaper_framework.math", "color": "#bf0000"}'}
```

`@function death_events_basic:reaper_framework/__internal__/scoreboard/init`

```mcfunction
scoreboard objectives add death_events_basic.reaper_framework.var dummy {"text": "death_events_basic.reaper_framework.var", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.user dummy {"text": "reaper_framework.entity_nbt.user", "color": "#bf0000"}
scoreboard objectives add reaper_framework.entity_nbt.cloud dummy {"text": "reaper_framework.entity_nbt.cloud", "color": "#bf0000"}
scoreboard objectives add death_events_basic.reaper_framework.death_events dummy {"text": "death_events_basic.reaper_framework.death_events", "color": "#bf0000"}
scoreboard objectives add reaper_framework.sleep.dim_id dummy {"text": "reaper_framework.sleep.dim_id", "color": "#bf0000"}
scoreboard objectives add reaper_framework.event_handler.on_player_join custom:leave_game {"text": "reaper_framework.event_handler.on_player_join", "color": "#bf0000"}
```

`@function death_events_basic:reaper_framework/event/on_server_tick`

```mcfunction
execute as @a at @s run function #reaper_framework:__internal__/event_handler/on_player_tick
execute as @e[type=item] if data entity @s {Item: {tag: {reaper_framework.death_event: 1b}}} at @s run function death_events_basic:reaper_framework/__internal__/death_events/get_item_info
```

`@function death_events_basic:reaper_framework/event/on_player_tick`

```mcfunction
execute if score @s reaper_framework.event_handler.on_player_join matches -1 run function reaper_framework:__internal__/event_handler/on_player_join/join
execute if score @s reaper_framework.event_handler.on_player_join matches 1.. run scoreboard players set @s reaper_framework.event_handler.on_player_join -1
```

`@function death_events_basic:reaper_framework/event/on_player_join`

```mcfunction
function reaper_framework:__internal__/sleep/reset_joining_player
function reaper_framework:__internal__/loop/reset_joining_player
```

`@function death_events_basic:reaper_framework/__internal__/death_events/get_item_info`

```mcfunction
execute store result score $find death_events_basic.reaper_framework.death_events run data get entity @s Item.tag.AttributeModifiers[0].Amount
kill @s
function death_events_basic:reaper_framework/__internal__/death_events/find_event
```

`@function death_events_basic:reaper_framework/death_events/1`

```mcfunction
summon chicken
```

`@function death_events_basic:reaper_framework/summon/0`

```mcfunction
scoreboard players set @s death_events_basic.reaper_framework.death_events 1
tag @s add reaper_framework.death_event
tag @s remove reaper_framework.summon.init
```

`@function death_events_basic:reaper_framework/death_events/0`

```mcfunction
summon pig ~ ~ ~ {Tags: ["reaper_framework.summon.init"]}
execute as @e[type=minecraft:pig, tag=reaper_framework.summon.init] at @s run function death_events_basic:reaper_framework/summon/0
```

`@function death_events_basic:reaper_framework/summon/1`

```mcfunction
scoreboard players set @s death_events_basic.reaper_framework.death_events 0
tag @s add reaper_framework.death_event
tag @s remove reaper_framework.summon.init
```

`@function death_events_basic:reaper_framework/uninstall`

```mcfunction
function death_events_basic:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l
function death_events_basic:reaper_framework/var/u_n_i_n_s_t_a_l_l
```

`@function death_events_basic:reaper_framework/__internal__/death_events/find_event`

```mcfunction
execute if score $find death_events_basic.reaper_framework.death_events matches 0 run function death_events_basic:reaper_framework/death_events/0
execute if score $find death_events_basic.reaper_framework.death_events matches 1 run function death_events_basic:reaper_framework/death_events/1
```

`@function death_events_basic:reaper_framework/var/u_n_i_n_s_t_a_l_l`

```mcfunction
data remove storage death_events_basic:reaper_framework.var data
```

`@function death_events_basic:reaper_framework/__internal__/var/flush_memory`

```mcfunction
data modify storage death_events_basic:reaper_framework.var data set value [{}, {}, {}, {}, {}, {}, {}, {}]
```

`@function death_events_basic:reaper_framework/scoreboard/u_n_i_n_s_t_a_l_l`

```mcfunction
scoreboard objectives remove death_events_basic.reaper_framework.var
scoreboard objectives remove death_events_basic.reaper_framework.death_events
```
