It is very useful tool for differents manipulating on five.

### How to use this library

To use this library just import it in that way:

```Python
from five import Five
```

Next you need create an instance of class `Five`:

```Python
my_five = Five()
```

### What the library could do

1. Library helps avoid magic `5` number for calculations:
```Python
my_five + 3  #8
my_five ** 2  #25
2 ** my_five  #32
my_five << 3  #40
if my_five < 6:
        print('It works!')  # 'It works will be displayed'
```

2. Library can be useful for translating `five` in many languages:
```Python
print(my_five.say_five_in_language('Russian'))  # пять
print(my_five.say_five_in_language('Polish'))  # pięć
```

3. You can also check for `five` in different digits:
```Python
my_five.print_five_in_digit_type('European')  # 5
my_five.print_five_in_digit_type('Arabic')  # ٥
my_five.print_five_in_digit_type('Arabic-west')  # ۵
```

4. You can also check for properties of `five`:
```Python
my_five.is_complex()  # False
my_five.is_rational()  # True
```

5. Or even represent `5` by any sort of operation:
```Python
my_five.as_sum()  # 3+2
my_five.as_fraction()  # 10/2
```

6. Function `draw_five` can draw five:
```Python
____
|
|--\
   |
---/
```
