# var

Anonymous `scoreboard` & `storage` locations. Returns an [expression](https://github.com/rx-modules/bolt-expressions).


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

Value can be done using [Expr](./Expr.md). For cases not covered by it, you can alternatively do this to access the data:

```py
foo = var(int)

if score foo.holder foo.obj matches 69:
    pass
```
```py
bar = var()

if data storage bar._target bar._path:
    pass
```


Every time `var()` is called it uses a new unique score/storage key. If you want to reuse a variable, it's recommended to call it at the lowest scope (or in general places where it won't be called multiple times by the compiler).


&nbsp;


## Examples

1. Example of a function that kills entities under 5 Health.
```py
current_hp = var(int)

function ./finish_him:
    # gets the current entity Health
    entity_hp = Data.entity('@s').Health

    # saves current hp into the var(int)
    current_hp = entity_hp

    # checks if target can be executed
    if Expr(current_hp) < 5:
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


