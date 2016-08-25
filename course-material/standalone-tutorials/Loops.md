# For loops

Use a `for` loop to do something to every element in a list.

```
>>> names = ["Jessica", "Adam", "Liz"]
>>> for name in names:
...     print name
...
Jessica
Adam
Liz
>>> names = ["Jessica", "Adam", "Liz"]
>>> for name in names:
...     print "Hello " + name
...
Hello Jessica
Hello Adam
Hello Liz
```

### `if` statements inside `for` loop

```
>>> for name in ["Alice", "Bob", "Cassie", "Deb", "Ellen"]:
...     if name[0] in "AEIOU":
...         print name + " starts with a vowel."
... 
Alice starts with a vowel.
Ellen starts with a vowel.
Sometimes you want to start with a new empty list, and only add to that list if some condition is true:
>>> vowel_names = []
>>> for name in ["Alice", "Bob", "Cassie", "Deb", "Ellen"]:
...     if name[0] in "AEIOU":
...         vowel_names.append(name)
... 
>>> print vowel_names
['Alice', 'Ellen']
```

### `for` loops inside `for` loops

You can put `for` loops inside `for` loops.  
The indentation dictates which `for` loop a line is in.

```
>>> letters = ["a", "b", "c"]
>>> numbers = [1, 2, 3]
>>> for letter in letters:
...     for number in numbers:
...         print letter * number
...
a
aa
aaa
b
bb
bbb
c
cc
ccc
```

The order of the for loops matters. Compare the above example with this one:

```
>>> for number in numbers:
...     for letter in letters:
...         print number * letter
...
a
b
c
aa
bb
cc
aaa
bbb
ccc
```

## Useful functions related to lists and `for` loops

### sorting lists

Use `.sort()` to sort a list:

```
>>> names = ["Eliza", "Joe", "Henry", "Harriet", "Wanda", "Pat"]
>>> names.sort()
>>> names
['Eliza', 'Harriet', 'Henry', 'Joe', 'Pat', 'Wanda']
```

### Getting the maximum and minimum values from a list

```
>>> numbers = [0, 3, 10, -1]
>>> max(numbers)
10
>>> min(numbers)
-1
```

### Generating a list of numbers easily with `range()`

The `range()` function returns a list of numbers.  
This is handy for when you want to generate a list of numbers on the fly instead of creating the list yourself:

``
>>> range(5)
[0, 1, 2, 3, 4]
Use range when you want to loop over a bunch of numbers in a list:
>>> numbers = range(5)
>>> for number in numbers:
...     print number * number
...
0
1
4
9
16
```

We could rewrite the above example like this:

```
>>> for number in range(5):
...     print number * number
...
0
1
4
9
16
```

### `while` loops

Use a while loop to loop so long as a condition is `True`.

```
>>> i = 0
>>> while i < 10:
...     print i
...     i = i + 1
... 
0
1
2
3
4
5
6
7
8
9
```

### `break` keyword

Use the `break` keyword to break out of a loop early:

```
>>> i = 0
>>> while True:
...     print i
...     i = i + 1
...     if i > 10:
...         break
... 
0
1
2
3
4
5
6
7
8
9
10
```

### Get user input with `raw_input()`

```
>>> while True:
...     input = raw_input("Please type something> ")
...     if input == "Quit":
...         print "Goodbye!"
...         break
...     else:
...         print "You said: " + input
... 
Please type something> Hello
You said: Hello
Please type something> How are you?
You said: How are you?
Please type something> Quit
Goodbye!
>>>
```

