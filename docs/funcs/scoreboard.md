# scoreboard

Returns a scoreboard [expression](https://github.com/rx-modules/bolt-expressions). Automatically create  objectives.

```py
foo = scoreboard(id, criteria='dummy', display_name=None, defaults=None)
```


&nbsp;


## Arguments

**id**
> The in game scoreboard name.

**criteria**
> Scoreboard criteria. If omitted, defaults to `dummy`.

**display_name**
> Accepts a valid string or dict. Display name of the scoreboard. If omitted, defaults to the scoreboard `id`.

**defaults**
> Sets default scores to assign if they doesn't exist. Accepts dict as input. Only supports fake players. Format: `{'$fake_player': value}`.


&nbsp;


## Remarks

Multiple calls to `scoreboard()` with the same `id` will still only create the objective once.


&nbsp;


## Examples

1. Declares a scoreboard and sets `$bar` to `69`.
```py
foo = scoreboard('foo_scb')

foo['$bar'] = 69
```