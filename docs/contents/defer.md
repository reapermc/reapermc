# @defer

Marks the decorated function to run after bolt is done compiling.

```py
@defer
```

&nbsp;


## Examples

1. Prints the amount of times `foo()` has been called by the end of compilation.
```py
count = 0

@defer
def display_count():       # runs last, will print '3' in this case
    print(count)

def increment():
    global count
    
    count += 1

increment()
increment()
increment()
```




