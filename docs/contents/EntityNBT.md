# EntityNBT

Allows you to store and access per-entity `NBT` data in the cloud.

```py
foo = EntityNBT(path)
```


## Arguments

**path**
> Dictates the NBT path which will be used for the methods listed below.


&nbsp;




## Remarks

It's important to construct the class as the selector we intend to be using it for. 

Example:

```py
# incorrect approach
function demo:foo:
    bar = EntityNBT('bar')     # this registers the entity in the system
                               # as the selector running the demo:foo function

    as @e[type=zombie]:     # since we run this scope as @e[type=zombie],
        bar.set(10)         # we don't know if the entity we're running as
                            # was registered, which can cause major issues
                            
# correct
function demo:foo:
    as @e[type=zombie]:
        bar = EntityNBT('bar')      # on the contrary this one ensures the entity
                                    # we plan to access is always registered
        bar = 10
```


&nbsp;


## Methods

* [set](#set)
* [get](#get)
* [delete](#delete)
* [remove](#remove)
* [merge](#merge)
* [append](#append)
* [prepend](#prepend)
* [insert](#insert)



&nbsp;



## **set**
---

```py
foo.set(value, index=None)
```

**value**
> Any valid value.

**index**
> Optional for arrays. Array index which you want to set to.

&nbsp;



## **get**
---

```py
bar = foo.get(index=None)
```

**index**
> Optional for arrays. Array index which you want to retrieve.

&nbsp;


## **delete**
---

```py
foo.delete(index=None)
```

**index**
> Optional for arrays. Array index which you want to delete.

&nbsp;


## **remove**
---

```py
foo.remove(index=None)
```

**index**
> Optional for arrays. Array index which you want to delete.

&nbsp;



## **merge**

```py
foo.merge(value)
```

**value**
> Any valid value.

&nbsp;



## **append**
---

```py
foo.append(value)
```

**value**
> Any valid value.

&nbsp;



## **prepend**
---

```py
foo.prepend(value)
```

**value**
> Any valid value.

&nbsp;



## **insert**
---

```py
foo.insert(index, value)
```


**index**
> Index position to insert into.

**value**
> Any valid value.

&nbsp;



## Examples

1. Simple function which increments an `NBT` value by 1.

```py
foo = var(int)

function ./subtract_point:
    points = EntityNBT('stats.points')

    points.set(points.get() + 1)


function ./check_points:
    points = EntityNBT('stats.points')

    foo = points.get()
```

2. Function which appends the current gametime subtracted by 20 to an array.

```py
foo = var(int)

function ./append_gametime:
    my_arr = EntityNBT('my_array')

    my_arr.append(get_time('gametime') - 20)                                            
```