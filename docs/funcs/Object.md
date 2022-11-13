# Object

A vessel which lets you use custom entity NBT.

```py
foo = Object(path)
```


## Arguments

**path**
> Dictates the NBT path which will be used for the object methods listed below.


&nbsp;




## Remarks

It's important to construct the object as the context we intend to be using objects for. 

Example:

```py
# correct
function ./foo:
    bar = Object('bar')
    
    bar = 10

# incorrect
bar = Object('bar')     # this registers the entity in the object system

function ./foo:
    bar = 10            # since we didn't register the current selector,
                        # as 'bar' is not in the selector scope
                        # the function will not work properly
```


It's not very intuitive but please use the `.get()` method when retrieving the object data, example:
`foo = my_object.get()`.

The current API is very primitive. I would love to someday create an interface similar to [bolt-expressions](https://github.com/rx-modules/bolt-expressions). Though I'm not skilled enough to take on that challenge yet.


&nbsp;


## Methods

* [\_\_rebind\_\_()](#__rebind__)
* [get()](#get)
* [delete()](#delete)
* [remove()](#remove)
* [merge()](#merge)
* [append()](#append)
* [prepend()](#prepend)
* [insert()](#insert)



&nbsp;



## **\_\_rebind\_\_()**
---

```py
foo = value
```

**value**
> Any valid value.

** This overrides the `=` operator.

&nbsp;



## **get()**
---

```py
bar = foo.get(index=None)
```

**index**
> Optional for arrays. Array index which you want to retrieve.

&nbsp;





## **delete()**
---

```py
foo.delete(index=None)
```

**index**
> Optional for arrays. Array index which you want to delete.

&nbsp;


## **remove()**
---

```py
foo.remove(index=None)
```

**index**
> Optional for arrays. Array index which you want to delete.

&nbsp;





## **merge()**

```py
foo.merge(value)
```

**value**
> Any valid value.

&nbsp;






## **append()**
---

```py
foo.append(value)
```

**value**
> Any valid value.

&nbsp;





## **prepend()**
---

```py
foo.prepend(value)
```

**value**
> Any valid value.

&nbsp;




## **insert()**
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

1. Simple function which increments an nbt key by 1.

```py
foo = var(int)

function ./subtract_point:
    points = Object('stats.points')

    points = points.get() + 1


function ./check_points:
    points = Object('stats.points')

    foo = points.get()
```

2. Function which appends the current gametime subtracted by 20 to an array.

```py
foo = var(int)

function ./append_gametime:
    my_arr = Object('my_array')

    my_arr.append(get_time('gametime') - 20)
                                                
```