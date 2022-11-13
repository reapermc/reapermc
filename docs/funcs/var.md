# var

Returns an [expression](https://github.com/rx-modules/bolt-expressions). In game these are either a scoreboard fake player or a storage key. Allows you to skip having to name these, respecting your own time.

```py
foo = var(var_type=None, default=None)
```


&nbsp;


## Arguments

**var_type**
> Unset, the var will be a storage. Otherwise if `int` is passed, it will be a scoreboard value instead.

**default**
> Sets a default value for the variable to be initialized with.


&nbsp;


## Remarks

Checking the value using `execute if <score/data>` can be done using `foo._target foo._path` or `bar.holder bar.obj` (`int`).

Every time `var()` is called it uses a new unique score/storage key. If you want to reuse a variable, it's recommended to call it at the lowest scope (or in general places where it won't be called multiple times by the compiler).


&nbsp;


## Examples

1. Example of a function that executes entities under 5 Health.
```py
hp = var(int)

function ./finish_him:
    # gets the current entity Health
    hp = Data.entity('@s').Health

    # checks if target can be executed
    if score hp.holder hp.obj matches ..5:
        tellraw @p [{"selector":"@s"}, {"text": " made the grimm reaper happy!"}]
        kill @s
```

2. More advanced array example.
```py
arr = var()

function ./example:
    # appends a few elements to the array
    arr = [69]
    arr.append(420)
    arr.append(25565)

    # clears the array if we're holding
    # an item while running the function
    if data entity @s SelectedItem:
        arr.remove()

    # checks if arr[0] exists
    if data storage arr._target arr[0]._path:
        tellraw @a 'arr[0] exists!'
    unless data storage arr._target arr[0]._path:
        tellraw @a 'arr[0] does not exist!'
```


