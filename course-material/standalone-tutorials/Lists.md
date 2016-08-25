# Lists

Use lists to store data where order matters.
**Lists are indexed starting with 0.**

### List initialization

```
>>> my_list = []
>>> my_list
[]
>>> your_list = ["a", "b", "c", 1, 2, 3]
>>> your_list
['a', 'b', 'c', 1, 2, 3]
```

### Access and adding elements to a list

```
>>> len(my_list)
0
>>> my_list[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> my_list.append("Alice")
>>> my_list
['Alice']
>>> len(my_list)
1
>>> my_list[0]
'Alice'
>>> my_list.insert(0, "Amy")
>>> my_list
['Amy', 'Alice']
>>> my_list = ['Amy', 'Alice']
>>> 'Amy' in my_list
True
>>> 'Bob' in my_list
False
```

### Changing elements in a list

```
>>> your_list = []
>>> your_list.append("apples")
>>> your_list[0]
'apples'
>>> your_list[0] = "bananas"
>>> your_list
['bananas']
```

### Slicing lists

```
>>> her_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
>>> her_list[0]
'a'
>>> her_list[0:3]
['a', 'b', 'c']
>>> her_list[:3]
['a', 'b', 'c']
>>> her_list[-1]
'h'
>>> her_list[5:]
['f', 'g', 'h']
>>> her_list[:]
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
```

### Strings are a lot like lists

```
>>> my_string = "Hello World"
>>> my_string[0]
'H'
>>> my_string[:5]
'Hello'
>>> my_string[6:]
'World'
>>> my_string = my_string[:6] + "Jessica"
>>> my_string
'Hello Jessica'
```

One big way in which strings are different from lists is that lists are mutable (you can change them), and strings are immutable (you can't change them). To "change" a string you have to make a copy:

```
>>> h = "Hello"
>>> h[0] = "J"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> h = "J" + h[1:]
>>> h
'Jello'
### Types
>>> type(my_list)
<type 'list'>
```

[More on lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
