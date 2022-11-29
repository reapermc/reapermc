# listener

Registers a event listener for the target function. All builtin events can be found here: [Builtin Events](../misc/builtin_events.md).


```py
@listener(event)
```


&nbsp;


## Arguments

**event**
> Has to be an event object. The event you want to listen to.


&nbsp;


## Examples

1. Sending a simple `Loaded!` message on server load.

```py
@listener(on_server_load)
def load():
    say Loaded!
```

2. Giving the player a diamond on every jump.

```py
@listener(on_player_jump)
def jump_reward():
    tellraw @s {"text": "Here's your diamond!", "color": "aqua"}
    give @s diamond
```

3. Summoning a TNT under the player when they stop sneaking.

```py
@listener(on_player_sneak_end)
def sneaking_end():
    tellraw @s {"text": "Once you start you can't stop!", "color": "red"}
    summon tnt ~ ~ ~
```
