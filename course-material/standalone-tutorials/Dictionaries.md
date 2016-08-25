### Dictionaries

Use dictionaries to store key/value pairs (also called a "mapping").
Dictionaries do not guarantee ordering.

A given key can only have one value, but multiple keys can have the same value.

### Initialization

```
>>> my_dict = {}
>>> my_dict
{}
>>> your_dict = {"Alice" : "chocolate", "Bob" : "strawberry", "Cara" : "mint chip"}
>>> your_dict
{'Bob': 'strawberry', 'Cara': 'mint chip', 'Alice': 'chocolate'}
```

### Adding elements to a dictionary

```
>>> your_dict["Dora"] = "vanilla"
>>> your_dict
{'Bob': 'strawberry', 'Cara': 'mint chip', 'Dora': 'vanilla', 'Alice': 'chocolate'}
```

### Accessing elements of a dictionary

```
>>> your_dict["Alice"]
'chocolate'
>>> your_dict.get("Alice")
'chocolate'
>>> your_dict["Eve"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Eve'
>>> "Eve" in her_dict
False
>>> "Alice" in her_dict
True
>>> your_dict.get("Eve")
>>> person = your_dict.get("Eve")
>>> print person
None
>>> print type(person)
<type 'NoneType'>
>>> your_dict.get("Alice")
'coconut'
```

### Changing elements of a dictionary

```
>>> your_dict["Alice"] = "coconut"
>>> your_dict
{'Bob': 'strawberry', 'Cara': 'mint chip', 'Dora': 'vanilla', 'Alice': 'coconut'}
```

### Types

```
>>> type(my_dict)
<type 'dict'>
```

[More on Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
