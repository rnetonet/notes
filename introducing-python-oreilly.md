# Introducing Python - O´Reilly - Bill Lubanovic

## Numbers, Strings, Booleans and Variables

- `int('98.3')` triggers an exception
- Python promotes types to the biggest precision:

```python
>>> 2 + 4.5
6.5
```

- Two division operatores: `/` float division, `//` integer division (truncates):

```python
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> 
```

- `divmod(num, div)` returns the result and "rest" of the division

```python
>>> divmod(11, 2)
(5, 1)
```

- Math operations with variables can be shortened:

```python
>>> a = 10
>>> a += 3
>>> a
13

>>> a /= 2
>>> a
6.5
>>> 
```

- You can convert between types (`int`, `float` and `str`) using the types as functions:

```python
>>> int(10.2)
10
>>> int("10")
10
>>> # Error! String with decimal part, use float()
... int("10.2")
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: invalid literal for int() with base 10: '10.2'
>>> 

>>> float(10)
10.0
>>> float("10.2")
10.2
>>> float("10")
10.0
>>> 

>>> str(10)
'10'
>>> str(10.2)
'10.2'
>>> 
```

- Strings are sequences and immutables

```python
>>> s = "Hello World!"
>>> for letter in s:
...     print(letter)
... 
H
e
l
l
o
 
W
o
r
l
d
!
>>> 

>>> s[3] = "X" # Error! Immutable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> 
```

- Multiples ways to create strings:

```python
>>> a = 'single'
>>> b = "double"
>>> a2 = 'my "single"'
>>> b2 = "my 'double'" # you can put one quote inside the other
>>> 
>>> m1 = '''
... multiple
... lines
... '''
>>> 
>>> m2 = """
... multiple lines
... double quotes
... """
>>> 
```

- Empty strings

```python
# Each step creates a new string object and points "s" variable to it
# Remember: strings are immutable
>>> s = ""
>>> s += "Hello"
>>> s += " "
>>> s += "World"
>>> 
>>> s
'Hello World'
>>> 
```

- Escapes are interpreted in single quotes and double quotes, except for raw strings:

```python
>>> a = 'Hello\nWorld'
>>> b = "Hello\nWorld"
>>> c = r"Hello\nWorld" # raw
>>> 
>>> print(a)
Hello
World
>>> print(b)
Hello
World
>>> print(c)
Hello\nWorld
>>> 
```

- More escapes:

```python
>>> print("Others \' \" \t escapes \\ ok!")
Others ' "       escapes \ ok!
>>> 
```

- Concatenating strings

```python
# Prefered way
>>> "hello" + "world"
'helloworld'

>>> "hello" "world"
'helloworld'
>>> 
```

* Repeat strings

```python
>>> "Pi!" * 3
'Pi!Pi!Pi!'
>>> 
```

* Extract single char

```python
>>> s = "Hello World!"
>>> s[0]
'H'
>>> s[5]
' '
>>> s[6]
'W'

>>> s[-1]
'!'
>>> s[-2]
'd'
>>> s[-3]
'l'
```

- Caution with string limits

```python
>>> s[23]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

- How to change, if immutable

```python
>>> s = "Jon"
>>> s = s[:1] + "ack"
>>> s
'Jack'
>>> 
>>> # or
... 
>>> s = "Jane"
>>> s = s.replace("e", "y")
>>> s
'Jany'
>>> 
```

- Slices

```python
>>> s = "Hello World"

# Slice defaults, 0 and len(str)
>>> s[:]
'Hello World'
>>> s[0:len(s)]
'Hello World'

# Closed start, open end: [0, 3)
>>> s[0:3] # 0, 1, 2. 3 not included.
'Hel'

# Forgives wron indexes
>>> s[0:100] # gracious end check
'Hello World'
>>> s[10:100]
'd'

# Supports negative indexes
>>> s[-3:]
'rld'
>>> s[-3:len(s)]
'rld'
>>> s[-2:]
'ld'
>>> s[3:-3]
'lo Wo'

# Steps
>>> s[0:6:2]
'Hlo'
>>> s[3:12:4]
'lo'

# Backwards
>>> s[::-1]
'dlroW olleH'
>>> 
```

- Length, Split and Join

```python
# Length
>>> s = "abc"
>>> len(s)
3

# Split
>>> s = "a, b, c"
>>> s.split(",")
['a', ' b', ' c']

>>> s2 = "a  b    c"
>>> s2.split() # default to space sequences
['a', 'b', 'c']

# Join
>>> s3 = "a|b|c"
>>> s4 = "-".join( s3.split("|") )
>>> s4
'a-b-c'
>>> 
```

- More methods

```python
>>> quote = "To be, or not to be"

# Starts / ends with
>>> 
>>> quote.startswith("To")
True
>>> quote.endswith("be")
True

>>> 
>>> quote.find("or") # first offset of "or"
7
>>> quote.rfind("be") # last "be" offset
17
>>> 
>>> quote.count("be") # how many "be" s ?
2
>>> 
>>> quote.isalnum() # all letters and numbers ?
```

- Replace

```python
>>> s = "Hello World"
>>> s.replace("Hello", "Bye") # Change the first ocurrence, generates new string
'Bye World'
>>> 
>>> s # not changed
'Hello World'
>>> 
>>> s.replace("l", "x") # Changes all
'Hexxo Worxd'
>>> 
>>> s.replace("l", "x", 2) # Change the first two only
'Hexxo World'
>>> 
```

## Lists, Tuples, Dicts and Sets

- Creating

```python
>>> # Creating lists
... empty_list = []
>>> another_empty_list = list()
>>> 
>>> empty_list
[]
>>> another_empty_list
[]
>>> 
>>> # Allows any type of element, repeated elements and is mutable
... 
>>> weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
```

- Convert to list using `list()`

```python
>>> list("dog") # string to list
['d', 'o', 'g']
>>> 
>>> "a/b/c/d/e".split("/") # string to list by token
['a', 'b', 'c', 'd', 'e']
>>> 
```

- Getting by index and slicing

```python
>>> names = ["John", "Jack", "Jill"]
>>> names[0]
'John'
>>> names[2]
'Jill'
>>> 
>>> names[-1] # Index and Slice works the same for all sequences
'Jill'
>>> 
```

- Nested lists

```python
>>> matrix = [
...     [ 10, 20, 30 ],
...     [ 1, 2, 3]
... ]
>>> matrix
[[10, 20, 30], [1, 2, 3]]
>>> matrix[0] # get the first nested list
[10, 20, 30]
>>> matrix[0][1] # access the 1 offset in the first nested list
20
>>> 
```

- Support for different types

```python
>>> # Lists support any type
... l = [1, 3.14, "spam!"]
>>> l
[1, 3.14, 'spam!']
>>> l[0]
1
>>> l[1]
3.14
>>> l[2]
'spam!'
>>> 
```

- Mutable

```python
>>> l = [1, 2, 3]
>>> l[1] = "spam!"
>>> 
>>> l
[1, 'spam!', 3]
>>> 
```

- Ways to grow

```python
>>> l = [1, 2, 3]
>>> 
>>> # Grow by one element, append
... l.append(4)
>>> l
[1, 2, 3, 4]
>>> 
>>> # Grow by a list of items, extend
... others = [5, 6, 7]
>>> l.extend(others)
>>> 
>>> l
[1, 2, 3, 4, 5, 6, 7]
>>> 

>>> remainder = [8, 9]
>>> l += remainder # the same as extend
>>> l
[1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> # Caution, dont confuse append with extend
... l.append([10, 11])
>>> l
[1, 2, 3, 4, 5, 6, 7, 8, 9, [10, 11]]
>>> 
```

- More list methods and operations

```python
>>> l = ['a', 'b', 'c']
>>> l.insert(2, 'x') # insert just before offset 2
>>> l
['a', 'b', 'x', 'c']
>>> 

# Insert beyond lenth, act like append
>>> lst = ['a', 'b', 'c']
>>> lst.insert(100, 'z')
>>> lst
['a', 'b', 'c', 'z']
>>> 

>>> del l[2] # del item in offset two
>>> l
['a', 'b', 'c']

# del by value
>>> l
['a', 'b', 'c']
>>> l.remove('b')
>>> l
['a', 'c']

# remove() the first found per call
>>> l = [1, 2, 3, 1, 2, 3]
>>> l.remove(1) # only the first
>>> l
[2, 3, 1, 2, 3]
>>> l.remove(1) # now, the one left
>>> l
[2, 3, 2, 3]
>>> 

>>> # Retrieve and remove, using pop(offset)
... l = [1, 2, 3]
>>> l.pop(1)
2
>>> l
[1, 3]
>>> 
>>> # If not offset is given, defaults to -1
... l.pop()
3
>>> l
[1]
>>> 

# find offset by value using index()
>>> l = ['a', 'b', 'c', 'd']
>>> l.index('c')
2
>>> l.index('z') # ops!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'z' is not in list
>>> 

# check for presence using 'in'
>>> l = ['a', 'b', 'c', 'd']
>>> 'a' in l
True
>>> 'z' in l
False
>>> 

# count() occurrences
>>> lst = ['a', 'a', 'b', 'c']
>>> lst.count('a')
2
>>> lst.count('b')
1
>>> 

>>> lst = [10, 2, 7, 1]
>>> 
>>> # sorted() returns a sorted copy of the list, the original is kept
... sorted(lst)
[1, 2, 7, 10]
>>> 
>>> lst
[10, 2, 7, 1]
>>> 
>>> # .sort(), resort in place
... lst.sort()
>>> lst
[1, 2, 7, 10]
>>> 

>>> # you cant mix types not promotable between in a sort
... lst = [10, 3.14]
>>> lst.sort()
>>> lst
[3.14, 10]
>>> 
>>> lst = [10, "a", 3.14]
>>> lst.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 

>>> # sort and sorted are ASC, to make DESC, use reverse=True
... 
>>> lst = [3, 1, 10]
>>> sorted(lst, reverse=True)
[10, 3, 1]
>>> 
>>> lst.sort(reverse=True)
>>> lst
[10, 3, 1]
>>> 


# length
>>> lst = [10, 2, 7, 1]
>>> len(lst)
4
>>> 
```

- Mutable objects, when changed, affect all references (variables) pointing to it

```python
>>> lst = ['a', 'b', 'c']
>>> another = lst
>>> 
>>> lst.append('d')
>>> 
>>> lst
['a', 'b', 'c', 'd']
>>> another
['a', 'b', 'c', 'd']
>>> 
>>> # same id, look
>>> id(lst)
140652440381576
>>> id(another)
140652440381576
>>> 
```

- But, how can i copy another object to apply changes ?

```python
>>> orig = ['a', 'b', 'c']
>>> 

# Three ways to copy a list
>>> c1 = orig.copy()
>>> c2 = list(orig)
>>> c3 = orig[:]
>>> 
>>> orig
['a', 'b', 'c']
>>> c1
['a', 'b', 'c']
>>> c2
['a', 'b', 'c']
>>> c3
['a', 'b', 'c']
>>> 

# Three different objects, changes in one dont affect anothers
>>> id(orig), id(c1), id(c2), id(c3)
(140652440266632, 140652440381192, 140652491717000, 140652440328328)
>>> 
```

## Tuples

- Constant (immutable) lists

```python
# Empty tuple
>>> empty_tpl = ()
>>> empty_tpl
()
>>> 

# Single
>>> single_tpl = (1,) # comma is required
>>> single_tpl
(1,)
>>> 

# Unpacking
>>> a, b, c = (1, 2, 3)
>>> a
1
>>> b
2
>>> c
3
>>> # Exchange values using a tuple
... a = 10
>>> b = 20
>>> a, b = b, a
>>> a
20
>>> b
10
>>> 
>>> # Convert a list to a tuple using tuple()
... lst = [1, 2, 3]
>>> tpl = tuple(lst)
>>> tpl
(1, 2, 3)
```

## Dictionaries

- Key -> value
- Key can be any immutable object (string, tuple, set, etc)

```python
(1, 2, 3)
>>> # Empty dict
... d1 = {}
>>> d2 = dict()
>>> d1
{}
>>> d2
{}
>>> 

>>> # An example
... weekdays = {
...     "Mon": "Monday",
...     "Tue": "Tuesday"
... }
>>> weekdays["Mon"]
'Monday'
>>> 

# Converting a list of two items to a dictionaria
# Obs: first item -> key, second -> value
>>> lst = [ ['a', 1], ['b', 2], ['c', 3] ]
>>> dct = dict(lst)
>>> dct
{'a': 1, 'b': 2, 'c': 3}
>>> 

# Works with tuples, strings, etc
>>> dict([ ['a', 'a'], ['b', 'b']  ])
{'a': 'a', 'b': 'b'}
>>> 
>>> dict([ (1, 10), (2, 20)  ])
{1: 10, 2: 20}
>>> 
>>> dict([ 'aa', 'bb', 'cc'  ])
{'a': 'a', 'b': 'b', 'c': 'c'}
>>> 

# Add / Update
>>> dct = {}
>>> 
>>> # adding
... dct['name'] = 'John'
>>> dct
{'name': 'John'}
>>> 
>>> # changing
... dct['name'] = 'Jack'
>>> dct
{'name': 'Jack'}
>>> 

>>> # Update with another dict
... dct = {"name": "john", "age": 34}
>>> up = {"age": 35, "surname": "rose"}
>>> 
>>> dct.update(up) # merge with up
>>> dct
{'name': 'john', 'age': 35, 'surname': 'rose'}
>>>

>>> # Deleting a key
... dct = {
...     "a": 10,
...     "b": 11
... }
>>> 
>>> dct
{'a': 10, 'b': 11}
>>> 
>>> del dct["a"]
>>> dct
{'b': 11}

# Clearing
>>> dct = {"name": "John"}
>>> dct
{'name': 'John'}
>>> 
>>> dct.clear() # or...dct = {}
>>> dct
{}

# Check for existence of a key using in
... dct = {"name": "John"}
>>> "name" in dct
True
>>> "age" in dct
False
>>> 

# Getting an item by "key"
>>> dct = {"name": "John", "age": 10}
>>> dct["name"]
'John'

# Exception if does not exist
>>> dct = {"name": "John", "age": 10}
>>> dct["name"]
'John'
>>> 
>>> dct["address"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'address'
>>> 

# Use .get(key) to avoid the exception
>>> res = dct.get("address")  # Returns None, if does not exist
>>> print(res)
None
>>> 
>>> dct.get("address", "Baker Street") # second argument can be the default value to be returned
'Baker Street'
>>> 

# Get all the keys, using keys()
# Python 3 returns a dict_keys. Use list() to get a common list.
>>> semaphore = {
...     "red": "stop",
...     "yellow": "attention",
...     "green": "go"
... }
>>> semaphore.keys()
dict_keys(['red', 'yellow', 'green'])
>>> list( semaphore.keys() )
['red', 'yellow', 'green']
>>> 
>>> # The values
... list( semaphore.values() )
['stop', 'attention', 'go']
>>> 
>>> # The items as tuples pairs
... list( semaphore.items() )
[('red', 'stop'), ('yellow', 'attention'), ('green', 'go')]
>>> 

# As lists, reference copies reflect changes
>>> a = {"name": "John"}
>>> b = a
>>> 
>>> a["name"] = "Jack"
>>> a
{'name': 'Jack'}
>>> b
{'name': 'Jack'}
>>> 

# To avoid this, use copy
>>> a = {"name": "John"}
>>> b = a.copy()
>>> 
>>> a["name"] = "Jack"
>>> a
{'name': 'Jack'}
>>> b
{'name': 'John'}
```

## Sets

- Dicts, without values.

- Keys must be unique, as in dicts

- Works when you deal with existence only, no values considered

```python
>>> # Creating a set
... empty_set = set()
>>> 
>>> even = {0, 2, 4, 6, 8}
>>> even
{0, 2, 4, 6, 8}
>>> 
>>> # To convert other types to sets, use set()
... # This discard duplicated values
... set('abc')
{'b', 'a', 'c'}
>>> 
>>> set([1, 2, 3])
{1, 2, 3}
>>> 
>>> set((10, 20, 30,10))
{10, 20, 30}
>>> 
>>> set({"name": "john", "age": 20}) # onle the keys
{'name', 'age'}
>>> 

# Test for value using in too
>>> "h" in set("aloha")
True
```

- Set operations

```python
# Intersection (what is in both)
>>> a = set("aloha")                                                                 >>> b = set("spam")                                                                  >>> a & b           
{'a'}
>>> a.intersection(b)          
{'a'}

>>> # Union, all together!
... a = {1, 2}
>>> b = {2, 3, 4}
>>> 
>>> a | b
{1, 2, 3, 4}
>>> a.union(b)
{1, 2, 3, 4}
>>> 

>>> # Difference, only what is in the first, but not in the second
... a = {1, 2, 3, 4}
>>> b = {3, 4, 5}
>>> 
>>> a - b
{1, 2}
>>> a.difference(b)
{1, 2}
>>> 

>>> # Exclusive or Symmetric difference (what is not in both)
... a = {1, 2, 3, 4}
>>> b = {1, 3, 4, 5}
>>> 
>>> a ^ b
{2, 5}
>>> a.symmetric_difference(b)
{2, 5}
>>> 

>>> # Subset (every a element is also in b ?)
... a = {1, 2, 3}
>>> b = {1, 2, 3, 4, 5, 6}
>>> 
>>> a <= b
True
>>> a.issubset(b)
True


>>> # Proper Subset (every a element is also in b, but b has at least one element not in a)
... a = {1, 2, 3}
>>> b = {1, 2, 3}
>>> 
>>> a <= b
True
>>> a < b
False
>>> 
>>> b = {1, 2, 3, 4}
>>> a <= b
True
>>> a < b
True
>>> 

# Superset (every b element is in a)
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 5}
>>> 
>>> a >= b
True
>>> a.issuperset(b)
True

# Proper superset
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 5}
>>>
>>> a > b
True
>>> 
```

## Code Structures

- Comments

```python
>>> # Comment, ignored
... print("Hello world") # Can come at line end, too
Hello world
>>> 
```

- Therei no multiline comment:

```python
>>> # There is
... # no
... # multiline comment
... 
```

- You cant comment inside strings, its just a # char:

```python
>>> print("Hello # World")
Hello # World
>>> 
```

- Breaking long lines with `\`:

```python
>>> text = "Roses are red \
... Violets are blue"
>>> print(text)
Roses are red Violets are blue
>>> 
```

- You can break math expressions too:

```python
>>> 10 + 2 \
... -3 -4 \
... + 6
11
>>> 
```

- Compare, using `if`, `elif` and `else`:

```python
>>> debug = True
>>> if debug:
...     print("I am doing...")
... else:
...     print("...")
... 
I am doing...
>>> 
```

- Using `elif`:

```python
>>> number = 2
>>> if number == 1:
...     print("First")
... elif number == 2:
...     print("Second")
... else:
...     print("The important is your participation")
... 
Second
>>> 
```

- Comparison operators:

```python
>>> 10 == 10
True
>>> 
>>> 11 != 10
True
>>> 
>>> 11 < 99
True
>>> 11 <= 14
True
>>> 
>>> 13 > 12
True
>>> 13 >= 13
True
>>> 13 >= 12
True
>>> "a" in "aloha"
True
```

- Boolean Operators (combine comparisons):

```python
# The comparisons expressions are evaluated before the combiner (and)
>>> 5 < 10 and 9 > 7
True

# Other examples
>>> 10 < 15 or "a" in "aloha"
True
>>> 
>>> 10 < 15 and not "x" in "aloha"
True
>>>

# Multiple comparisons with the same variable 
>>> x = 7
>>> 
>>> 2 < x < 10
True
>>> 

# The same...
>>> 2 < x and x < 10
True
>>> 
```

- What Python considers `False`:

```python
# False is zero and everything empty
>>> bool(False)
False
>>> bool(None)
False
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool("")
False
>>> bool([])
False
>>> bool(())
False
>>> bool({})
False
>>> bool(set())
False
>>> 


```

- **Everything** else is `True`:

```python
>>> bool(1)
True
>>> bool("Z")
True
>>> bool(0.1)
True
>>> bool(["a"])
True
```

- `while`

```python
>>> counter = 10
>>> while counter:
...     print(counter)
...     counter -= 1
... 
10
9
8
7
6
5
4
3
2
1
>>> 
```

- Exit early from a loop using `break`

```python
>>> while True:
...     print("Press q to quit: ")
...     if input() == "q":
...             break
... 
Press q to quit: 
a
Press q to quit: 
b
Press q to quit: 
c
Press q to quit: 
q
>>> 
```

- Hurry to the next iteration of the loop using `continue`

```python
>>> counter = 0
>>> while counter <= 10:
...     counter += 1
...     if counter % 2 != 0:
...             continue
...     else:
...             print(counter ** 2)
... 
4
16
36
64
100
>>> 
```

- Check for break usage with `else` (if no `break` is used, `else` block is called):

```python
>>> counter = 0
>>> while counter <= 10:
...     counter += 1
...     if counter > 20:
...             break
... else:
...     print("No break executed!")
... 
No break executed!
>>> 
```

- `for` (consume iterators)

```python
# Iterate over lists, tuples or sets
>>> countries = ["Brazil", "EUA", "England"]
>>> for country in countries:
...     print(country)
... 
Brazil
EUA
England
>>> 

# Iterate over strings one char at a time
>>> for char in "Spam!":
...     print(char)
... 
S
p
a
m
!
>>> 

# Over a dict, you get the keys
>>> data = {
...     "name": "John",
...     "age": 40
... }
>>> 
>>> for key in data:
...     print(key)
... 
name
age

# Over dict values (using .values())
>>> for value in data.values():
...     print(value)
... 
John
40
>>> 

# Over both (.items())
>>> for key, value in data.items():
...     print(key, "->", value)
... 
name -> John
age -> 40
>>>
```

- `for` also supports `break`, `continue` and `else` (the no-break-clause).

```python
>>> colors = ["red", "blue", "green", "orange"]
>>> for color in colors:
...     if color == "purple":
...             break
... else:
...     print("Oh, no purple")
... 
Oh, no purple
>>>
```

- Use `zip()` to iterate over different sequences at the same time, bounds begin the smaller one:



```python
>>> names = ["Jack", "John", "Pamela"]
>>> ages  = [17, 32]

# Pamela is not printed, because "ages" is smaller than "names"
>>> for name, age in zip(names, ages):
...     print(name, "->", age)
... 
Jack -> 17
John -> 32
>>> 
```

- You can, also, use `zip()` to convert two list into a list of tuples or in a dict:

```python
>>> a = ["name", "age", "color"]
>>> b = ["john", 23, "blue"]
>>> 
>>> list( zip(a, b) )
[('name', 'john'), ('age', 23), ('color', 'blue')]
>>> 
>>> dict( zip(a, b) )
{'name': 'john', 'age': 23, 'color': 'blue'}
>>> 
```

- Create sequences of numbers using `range()` 

```python
>>> # range(start, stop, step)
... # start defaults to 0
... # step defaults to 1
... # stop is not included (open interval)
... for n in range(3):
...     print(n)
... 
0
1
2
>>> 
```

```python
>>> # range() returns an iterable (generates on demanda - lazy - saving memory)
... # convert to list(), if necessary
... list(range(6))
[0, 1, 2, 3, 4, 5]
>>> 
```

```python
>>> # Use a negative to go backwards
>>> for x in range(10, 0, -1):
...     print(x)
... 
10
9
8
7
6
5
4
3
2
1
>>> 
```

## Comprehensions

- A Pythonic and terse way to create complex Python objects from iterable objects

```python
>>> # A very simple number list comprehension
... lst = [number * number for number in range(10)]
>>> lst
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
```

```python
>>> # Comprehensions can have an if clause too
>>> lst = [number * number for number in range(10) if number % 2 == 0]
>>> lst
[0, 4, 16, 36, 64]
>>>
```

```python
>>> # You can, also, have more than one for
... 
>>> letters = ["a", "b", "c"]
>>> numbers = [1, 2, 3]
>>> 
>>> pairs = [(letter, number) for letter in letters for number in numbers]
>>> pairs
[('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
>>> 
>>> # if can be used too
... 
>>> pairs = [(letter, number) for letter in letters if letter == "a" for number in numbers if number ==1 or number == 2]
>>> pairs
[('a', 1), ('a', 2)]
>>> 
```

```python
>>> # Comprehensions can be used to create dicts
>>> word = "letters"
>>> char_count = {char:word.count(char) for char in word}
>>> char_count
{'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}
>>> 
```

```python
>>> # set comprehensions
>>> names = ["John", "Jack", "Jill", "Joana", "John"]
>>> clean_names = {name for name in names if "o" in name}
>>> clean_names
{'John', 'Joana'}
>>> 
```


```python
>>> # Tuples dosen´t have comprehension
>>> # Using parenthesis, you create a generator comprehension
>>> # That returns lazily only when requested and once consumed, cant be requested again
>>> 
>>> gen = (number * 2 for number in range(6))
>>> for number in gen:
...     print(number)
... 
0
2
4
6
8
10
>>> 
>>> # The generator was exhausted
... for number in gen:
...     print(number)
... 
>>> 
```

## Functions

```python

>>> # Functions are pieces of reusable code
>>> # Define with "def"
>>> def make_sound():
...     print("quack")
... 
>>> make_sound()
quack
>>> make_sound()
quack
>>> 
```

```python
>>> # Functions can return values (any object)
>>> def is_user_authorized():
...     return True
... 
>>> if is_user_authorized():
...     print("Welcome!")
... else:
...     print("Go away!")
... 
Welcome!
```

```python
# Functions can receive arguments when called
# Just define some parameters
>>> def welcome(name):
...     print("Welcome!", name)
... 
>>> welcome("John")
Welcome! John
>>> 
```

```python
# If the function dosent define a return, it implicitly returns None
>>> def sum(a, b):
...     print(a + b)
... 
>>> result = sum(10, 20)
30
>>> 
>>> print(result) # None! There was no return
None
>>> 
```

```python
# How to diferentiate None from False ? Use "is"
>>> thing = None
>>> thing is False
False
>>> thing is None
True
>>> 
```

```python
>>> # Python functions have flexible arguments
... # 1. Positional arguments (the argument is bound to the parameter of same position)
... def sum(a, b):
...     return a + b
... 
# a = 10, b = 3
>>> print( sum(10, 3) )
13
```

```python
>>> # 2. Use the parameter name to force the bound (keyword arguments)
... # This manner, you can even change the order
... def div(a, b):
...     return a / b
... 
>>> div(10, 2)
5.0
>>> 
>>> div(b=10, a=2)
0.2
>>> 
```

```python
>>> # The keyword syntax allows the specification of defaults during
... # the function definition
... def div(a, b=2):
...     return a / b
... 
>>> div(10)
5.0
>>> div(10, 3)
3.3333333333333335
>>> 
```

- If the function call mixes positional and keyword arguments, the positional should come first.

- Caution: default values for arguments are created during definition, not during call. So avoid the use of mutable objects as defaults!

```python
>>> def buggy(arg, result=[]):
...     result.append(arg)
...     return result
... 
>>> buggy(2)
[2]
>>> buggy(3)
[2, 3]
>>> 
```

- To avoid that, many programmers use `None` to indicate the first call:

```python
>>> def correct(arg, result=None):
...     if result is None:
...             result = []
...     result.append(arg)
...     return result
... 
>>> correct(2)
[2]
>>> correct(3)
[3]
>>> 
```

- If you want to gather multiple positional arguments into a single tuple, use: `*args`:

```python
>>> def itemize(*args):
...     for arg in args:
...             print("*", arg)
... 
>>> itemize("coffee", "bacon", "eggs")
* coffee
* bacon
* eggs
>>> 

>>> itemize() # but you can pass nothing too
>>> 
```

- If you want to require some positional arguments and gather the rest as a tuple:

```python
>>> def itemize_with_header(token, *args):
...     for arg in args:
...             print(token, arg)
... 
>>> 
>>> itemize_with_header("-", 1, 2, 3)
- 1
- 2
- 3
>>> 
>>> itemize_with_header() # error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: itemize_with_header() missing 1 required positional argument: 'token'
>>> 
```

- But if you want to gather keyword args into a dict, use `**kwargs`

```python
>>> def pkwargs(**kwargs):
...     for arg in kwargs:
...             print(arg, "=", kwargs[arg])
... 
>>> pkwargs(a=1, b=2, c=10)
a = 1
b = 2
c = 10
>>> 
```

- If you mix `*args` and `**kwargs`, `*args` should come before `**kwargs`:

```python
>>> def pargs(token, *args, **kwargs): # positional args, *args, **kwargs
...     for arg in args:
...             print(token, arg)
...     for arg in kwargs:
...             print(token, arg, "=", kwargs[arg])
... 
>>> 
>>> pargs("*", 1, 2, 3, a=10, b=20, c=30)
* 1
* 2
* 3
* a = 10
* b = 20
* c = 30
>>> 
```

- Document function with docstrings:

```python
>>> def sum(a, b):
...     """ Returns a + b """
...     return a + b
... 
>>> sum(2, 2)
4

# Use help(function) to see the documentation
Help on function sum in module __main__:

sum(a, b)
    Returns a + b
(END)
```

- Function are first class citizen (objects!), so you can pass them to other function, return it, set attributes:

```python
>>> def quack():
...     print("Quack!")
... 
>>> def run_it(f):
...     f()
... 
>>> 
>>> run_it(quack)
Quack!
>>> 
>>> type(quack) # not quack()! just an object, callable, but an object
<class 'function'>
>>> 
```

- Function objects can be used as elements of lists, tuples, etc. Can even be dictionarie keys.

- Inner functions:

```python
>>> def sum_with_increment(inc):
...     def inner(a, b):
...             return a + b + inc
...     return inner
... 
>>> 
>>> operation = sum_with_increment(3)
>>> operation(2, 2)
7
>>>
```

> In Python, everything is an object, and variables are names that are bound to those objects.

> Mutable objects reflect change in all references to it. Immutable objects, don´t:

```python
# Mutable object
>>> lst = []
>>> 
>>> def change_lst(l):
...     l.append("X")
... 
>>> change_lst(lst)
>>> lst
['X']
>>> 

# Immutable object
>>> num = 2
>>> def change_num(n):
...     n = n + 1 # create a new "n" in the local scope
... 
>>> change_num(num)
>>> num
2
>>>
```

- `Closures` are inner function that remember and have access to the data (arguments and defined variables) of the outer function:

```python
>>> def incrementer(step):
...     def inner(number):
...             return number + step
...     return inner

>>> inc3 = incrementer(3)
>>> inc3(10)
13
>>> 

>>> inc11 = incrementer(11)
>>> inc11(1000)
1011
>>> 

# Note! All three are functions, but inc3 and inc11 have a different scope
>>> type(incrementer)
<class 'function'>
>>> type(inc3)
<class 'function'>
>>> type(inc11)
<class 'function'>
>>> 

>>> incrementer
<function incrementer at 0x7f7c96e99c80>
>>> inc3
<function incrementer.<locals>.inner at 0x7f7c96e99d08>
>>> inc11
<function incrementer.<locals>.inner at 0x7f7c93e18b70>
>>> 
```

- `lambda` functions are single statements function that don´t have a name (anonymous)

```python
>>> words = ["spam", "eggs", "bacon"]
>>> def apply_to(sequence, function):
...     for item in sequence:
...             function(item)
... 
>>> 
>>> apply_to( words, lambda word: print(word.capitalize()) )
Spam
Eggs
Bacon
>>> 
```

- `generator` are a special kind of functions that generate data on demand.
These functions make some processing, return some data and holds their execution. 
In their next call, they remember where they were (statewise) and continue execution:

```python
>>> def firstn(n):
...     num = 0
...     while num < n:
...             yield num # use yield instead of return!
...             num += 1
... 
>>> first10 = firstn(10)
>>> first10 # generator!
<generator object firstn at 0x7f0f47fb31a8>
>>> 
>>> # iterate
... for n in first10:
...     print(n)
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
>>> 
```

## Decorators

- A decorator is a function that receives a function as argument, enhances it with some behavior and returns this enhanced function, overwriting the prior.

```python
>>> def make_verbose(function):                                                 
...     def verbose_function(*args, **kwargs):                                  
...             print(function.__name__)
...             print("args", args)
...             print("kwargs", kwargs)
...             result = function(*args, **kwargs) # unpack args and kwargs
...             print("result", result)
...             return result
...     return verbose_function
... 
>>> 
>>> def add(a, b):
...     return a + b
... 
>>> add(2, 3)
5
>>> 
>>> add = make_verbose(add)
>>> add(2, 3)
add
args (2, 3)
kwargs {}
result 5
5
>>> # Python also offers this syntax sugar
>>> @make_verbose # same as make_noise = make_verbose(make_noise)
... def make_noise(noise):
...     print(noise, "!")
... 
>>> make_noise("Meow")
make_noise
args ('Meow',)
kwargs {}
Meow !
result None
>>> 
```

```python
>>> # You can apply multiple decorators
... # The closer to def is used first, than the interpreter goes up
... 
>>> def square_it(func):
...     def decorated_func(*args, **kwargs):
...             result = func(*args, **kwargs)
...             return result * 2
...     return decorated_func
... 
>>> # minus = make_verbose( square_it(minus) )
>>> @make_verbose
... @square_it
... def minus(a, b):
...     return a - b
... 
>>> 
>>> minus(10, 8)
decorated_func
args (10, 8)
kwargs {}
result 4
4
>>>

>>> 
>>> # if you invert decorator order...
>>> # minus = square_it( make_verbose(minus) )
... @square_it
... @make_verbose
... def minus(a, b):
...     return a - b
... 
>>> minus(10, 8)
minus
args (10, 8)
kwargs {}
result 2
4
>>> 
```

## Namespaces and scope

- Python program have differents scopes. The names in each one are unrelated to the others scopes.

- Rules:
    - The main part of a program define a "global" namespace;
    - Each function defines it´s own scope, but can read global scope. To change, you to explicitly say;
    - Each module (.py) file, has its own scope

```python
>>> # To change, be explicit
... def increase_total():
...     global total # i will change this global!
...     total = total * 1.10
... 
>>> increase_total()
>>> print(total)
110.00000000000001
>>> 
```

- You can list the defined variables in the local scope with `locals()` and in the global scope with `globals()`

## Using `_` and `__` in names

- Python creators define some special variables with prefix and suffix (`_` ou `__`):

```python
>>> def sum(a, b):
...     return a + b
... 
>>> print(sum.__name__)
sum
>>> 
>>> print(sum.__doc__)
None
>>>
```

- The name of the main program, for example, is assigned to `__main__`

## Exceptions

- If an exception error happens inside a function and is not treated, it pops up in the caller stack.
- If the exceptio is not treated at all, Python prints it and terminates the program.

```python
>>> lst = ["a", "b", "c"]
>>> 
>>> index = 5

# With exception
>>> try:
...     print(lst[index])
... except:
...     print("not found")
... 
not found
>>> 

# No exception
>>> index = 1
>>> try:
...     print(lst[index])
... except:
...     print("not found")
... 
b
>>> 
```

- You can specify the type of exceptions to be handled:

```python
>>> lst = ["a", "b", "c"]
>>> 
>>> index = 4
>>> 
>>> try:
...     print(lst[index])
... except IndexError, Exception:
...     print("invalid index")
... 
invalid index
>>> 
>>> 
```

- If you want to get the exception object, use `as`:

```python
>>> try:
...     print(lst[index])
... except IndexError as err:
...     print(err)
... 
list index out of range
>>> 
```

- You can stack `except` clauses:

```python
>>> lst = [1, 2, 3]
>>> while True:
...     try:
...             position = int( input("Which position?") ) 
...             print(lst[position])
...     except IndexError as ierr:
...             print("Invalid position: ", position, ierr)
...     except Exception as err:
...             print("Something happened: ", err)
... 
Which position?1
2
Which position?
Something happened:  invalid literal for int() with base 10: ''
Which position?2
3
Which position?10
Invalid position:  10 list index out of range
Which position?xxx
Something happened:  invalid literal for int() with base 10: 'xxx'
Which position?
```

- Create your exception extending `Exception`

```python
>>> class SillyMathError(Exception):
...     pass
... 
>>> 
>>> def sum(a, b):
...     if a == b:
...             raise SillyMathError("a == b!")
...     else:
...             return a + b
... 
>>> 

>>> sum(2, 3)
5
>>> 

>>> sum(2, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in sum
__main__.SillyMathError: a == b!
>>> 

>>> try:
...     print(sum(10, 10))
... except SillyMathError as err:
...     print("Ops!", err)
... 
Ops! a == b!
```

## Command line args

- Command line args are save in `sys.argv`

```python
import sys
for index, arg in enumerate(sys.argv):
    print("sys.argv[", index, "]", "->", arg)
```

```bash
rnetonet@T440s:~$ python3 /tmp/sample.py a b c
sys.argv[ 0 ] -> /tmp/sample.py
sys.argv[ 1 ] -> a
sys.argv[ 2 ] -> b
sys.argv[ 3 ] -> c
```

## Modules and import statements

- A module is just a file of Python code

- You can refer to some module using the `import` statement:

```python
# report.py
def get_description():
    return "Sunny"
```

```python
# weather.py

# We import all the module inside the variable/namespace report
# Everything declared inside the module is avaible through "report."
import report

# See ? "report."
print(report.get_description())
```

```bash
$ python3 weather.py 
Sunny
```

- You can import a module `as` an alias

```python
# weather.py
# Instead of report, prefix with "rep."
import report as rep

print(rep.get_description())
```

- You can also, import only "parts" of a module to your namespace

```python
# weather.py

# Import to current namespace only the function "get_description()"
from report import get_description

print(get_description())
```

- These parts can be imported with an alias also

```python
# weather.py

from report import get_description as getdesc

print(getdesc())
```

> Important! Python **always** executes all the module code, than proceeds with the import. So, if you have a `print` statement on the module, when it´s imported, the `print` is run.

- Python looks for module in the paths listed in `sys.path`:

```python
>>> import sys
>>> sys.path
['', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/home/rnetonet/.local/lib/python3.6/site-packages', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages']
>>> 
```

> The empty string is the current importer folder. Mind that the first match is used, so if you have a `random.py` in the importer folder, it will not be able to access the system´s `random` module.


## Some Python - batteries included - modules

- Dictionaries `.setdefault(key, default_value)` are like ``.get()`, but the inexistent key is actually set to the default value:

```python
>>> data = {"name": "John", "age": 20}
>>> data.get("address", "Baker Street")
'Baker Street'

>>> data # The same keys
{'name': 'John', 'age': 20}
>>> 
>>> data = {"name": "John", "age": 20}
>>> data.setdefault("address", "Baker Street") # sets and returns Baker Street
'Baker Street'
>>> data # new key!
{'name': 'John', 'age': 20, 'address': 'Baker Street'}
>>> 

>>> # If the key already exists, it is returned and nothing set
... data.setdefault("name", "Paul")
'John'
>>> data
{'name': 'John', 'age': 20, 'address': 'Baker Street'}
>>> 
```

- `collections.defaultdict` is a dict with a default value for any key:

```python
>>> from collections import defaultdict

# defaultdict is initialized with a callable, called anytime the key is required without being set
# if you omit, None is used
>>> d = defaultdict(int) 
>>> 
>>> d["age"]
0
>>> d["name"]
0
>>> 

>>> d
defaultdict(<class 'int'>, {'age': 0, 'name': 0})

# It is still a dict, you can change values
>>> d["name"] = 1
>>> d["name"]
1
>>> d
defaultdict(<class 'int'>, {'age': 0, 'name': 1})
>>> 
```

- Counting with `collections.Counter`

```python
>>> from collections import Counter
>>> 
>>> d = ["spam", "eggs", "spam", "bacon"]
>>> c = Counter(d)
>>> 
>>> c
Counter({'spam': 2, 'eggs': 1, 'bacon': 1})
>>> c["spam"]
2
>>> 

>>> # Get elements in descending order using (most_common())
... # You can also pass a int limit as argument, to get the top N
... c.most_common()
[('spam', 2), ('eggs', 1), ('bacon', 1)]
>>> 
>>> c.most_common(2)
[('spam', 2), ('eggs', 1)]
>>> 

>>> # Counters have some operations
... 
>>> lst1 = ["spam", "eggs", "spam", "bacon"]
>>> c1 = Counter(lst1)
>>> c1
Counter({'spam': 2, 'eggs': 1, 'bacon': 1})
>>> 
>>> 
>>> lst2 = ["eggs", "spam", "bacon", "bacon"]
>>> c2 = Counter(lst2)
>>> c2
Counter({'bacon': 2, 'eggs': 1, 'spam': 1})
>>> 
>>> c1 + c2
Counter({'spam': 3, 'bacon': 3, 'eggs': 2})
>>> 
>>> c1 - c2
Counter({'spam': 1})
>>> 
>>> c1 & c2
Counter({'spam': 1, 'eggs': 1, 'bacon': 1})
>>> 
>>> c1 | c2
Counter({'spam': 2, 'bacon': 2, 'eggs': 1})
>>> 
```

- Python lists behave like a `stack` (LIFO) when you use `pop()`:

```python
>>> lst = ["John", "Paul", "Mal"]
>>> lst.pop()
'Mal'
>>> 
>>> lst
['John', 'Paul']
>>> 
```

- If you want a `queue` (FIFO), use `collections.deque` and `popleft()`:

```python
>>> from collections import deque
>>> 
>>> lst = ["John", "Paul", "Mal"]
>>> dqu = deque(lst)
>>> 
>>> dqu.popleft()
'John'
>>> dqu
deque(['Paul', 'Mal'])
>>> 
```

- `itertools` is a magic module to work with iterable objects:

```python
# Iterate over multiple sequences, chaining them
>>> for item in itertools.chain(["john", "jack"], [10, 22]):
...     print(item)
... 
john
jack
10
22
```

```python
# Cycle forever over an iterable
>>> for item in itertools.cycle(["red", "blue"]):
...     print(item)
red
blue
red
blue
red
blue
red
blue
red
blue
red
blue
red
...
```

```python
>>> # You can also go accumulating the values of the iterator
... for intermediary_sum in itertools.accumulate([1, 2, 3, 4, 5, 6]):
...     print(intermediary_sum)
... 
1
3
6
10
15
21
>>> 
```

```python
>>> # accumulate takes a function(a, b) as second param
... # if you want a multiplication accumulation instead of the default sum:
... for inter in itertools.accumulate([1, 2, 3, 4, 5], lambda a, b: a * b):
...     print(inter)
... 
1
2
6
24
120
>>> 
```

- Pretty Print with `pprint.pprint()`

```python
>>> # Pretty Printer with pprint
... 
>>> from pprint import pprint
>>> 
>>> d = {"name": "John", "age": 34, "address": "Baker Street", "nickname": "John Carlson Travolta"}

# See ? The output looks nicer
>>> pprint(d)
{'address': 'Baker Street',
 'age': 34,
 'name': 'John',
 'nickname': 'John Carlson Travolta'}
>>> 
```

# Objects and Classes

- A very simple example

```python
>>> class Person:
...     def __init__(self, name):
                # Inside the class, refer with "self.variable"
                # "self" means "the current object"
...             self.name = name
... 
>>> 
>>> someone = Person("John!") # self = created Person object, name = "John"

# outside, refer using the object reference name
>>> someone.name
'John!'
>>> 
```

# Inheritance

- A first simple example:

```python
>>> class Car:
...     def exclaim(self):
...             print("I am a car!")
... 
>>> class Yugo(Car):
...     pass
... 
>>> 
>>> simple_car = Car()
>>> yugo = Yugo()
>>> 
>>> simple_car.exclaim()
I am a car!

# Yugo Inherited the method!
>>> yugo.exclaim()
I am a car!

# Remember! An Yugo is a Car!
>>> isinstance(yugo, Car)
True
>>> isinstance(yugo, Yugo)
True

# But a Car is not an Yugo
>>> isinstance(simple_car, Yugo)
False
>>> 
```

- Inheritance might require you to override some methods:

```python
>>> class Yugo(Car):
...     def exclaim(self):
...             print("I am an Yugo")
... 

>>> new_yugo = Yugo()
>>> new_yugo.exclaim()
I am an Yugo
>>> 
```

- Besides overriding, you can add specific methods to subclasses

```python
>>> class Yugo(Car):
...     def exclaim(self):
...             print("I am an Yugo")
... 
>>> class Yugo(Car):
...     def exclaim(self):
...             print("I am an Yugo")
...     def need_a_push(self):
...             return True
... 
>>> 
>>> y = Yugo()
>>> y.exclaim()
I am an Yugo

# Only Yugos have this method
>>> print( y.need_a_push() )
True
>>> 
```

- Leveraging the super class implementation with `super()`

```python
# When you override, the superclass method is not called anymore
>>> class Person:
...     def __init__(self, name):
...             self.name = name
... 
>>> 

# You can call it explicitly specifying the class
>>> class EmailPerson(Person):
...     def __init__(self, name, email):
...             Person.__init__(self, name)
...             self.email = email
... 
>>> 
>>> jack = EmailPerson("Jack", "jack@hotmail.com")
>>> print(jack.name)
Jack
>>> print(jack.email)
jack@hotmail.com
>>>

# But you can use "super()" to implictly refer to the superclass
>>> class EmailPerson(Person):
...     def __init__(self, name, email):
                # super() returns the "inside" Person object of the current (EmailPerson) object, so, no need to pass self
                # methods called in this object, will use the Person implementation
...             super().__init__(name)
...             self.email = email
... 
>>> 
>>> emailperson = EmailPerson("John", "john@gmail.com")
>>> emailperson.name
'John'
>>> emailperson.email
'john@gmail.com'
>>> 
```

- Getters and Setters using properties

```python
>>> class Person:
...     def __init__(self, n):
...         self.name = n
...     
...     def get_name(self):
...         return self._name
...     
...     def set_name(self, n):
            # the getter uppercases the name
...         self._name = n.upper()
...     
...     name = property(get_name, set_name)
... 
>>> p = Person("jack")
>>> p.name
'JACK'
>>> 

>>> # get_name is accessible
... p.get_name()
'JACK'
>>> 
>>> # so is set_name
... p.set_name("paul")
>>> p.name
'PAUL'
>>> 
```

- Setting properties with decorators (`@property` comes first)

```python
>>> # When you use decorators, you loose direct access to the methods
... class NetworkItem:
...     def __init__(self, ip):
...         self.ip = ip
...     
...     @property
...     def ip(self):
...         return self._ip
...     
...     # property.setter
...     @ip.setter
...     def ip(self, ip):
...         self._ip = ip.strip() # remove any space
... 
>>> n = NetworkItem(" 1.2.3.4 ")
>>> n.ip
'1.2.3.4'
>>> n.ip = " 10.20.11.2"
>>> n.ip
'10.20.11.2'
>>>
```

- Remember, properties can be computed values also:

```python
>>> class Circle:
...     def __init__(self, radius):
...         self.radius = radius
...     
...     @property
...     def diameter(self):
...         return self.radius * 2
... 
>>> c = Circle(2.3)
>>> c.radius
2.3
>>> 
>>> c.diameter
4.6
>>> c.radius = 3
>>> c.diameter
6
>>> 
```

## Name Mangling

- Python has no `private`, `protected` accessors

- Prefixing your class or instance variables with two underscores `__` make their name mangled to the outside:

```python
class Person:
    __name = None

    def __init__(self, name):
        self.__name = name

if __name__ == "__main__":
    p = Person("Jack!")

    print(p._Person__name) # Mangled name still accessible
    print(p.__name) # Error: AttributeError: 'Person' object has no attribute '__name'
```

```bash
$ python3 sample.py 
Jack!
Traceback (most recent call last):
  File "sample.py", line 11, in <module>
    print(p.__name) # Error: AttributeError: 'Person' object has no attribute '__name'
AttributeError: 'Person' object has no attribute '__name'
rnetonet@T440s:/tmp$ 
```

> Name mangling is useful to avoid the variable being overriden in subclasses

> The programmer, the original code, dosent have to worry about the mangled name. So, in the code, you can always refer to `__var`...

## Method Types

- Python has instance methods (that receive `self`) and classmethods, that receive the `class`.

- Let´s see an example of a class that keeps tabs on its created instances:

```python
class Example:
    total = 0
    kids = []

    def __init__(self):
        Example.total += 1
        Example.kids.append(self)
    
    @classmethod
    def list_kids(cls):
        for kid in cls.kids:
            print(kid)

if __name__ == "__main__":
    a = Example()
    b = Example()
    c = Example()
    
    # Calling the class method from the class
    Example.list_kids()

    # Calling from some of the objects
    # Works too!
    a.list_kids()
```

- Python also have static methods, that are methods that do not affect the instance or the class. 
They just share the class namespace for convenience:

```python
>>> class Math:
...     @staticmethod
...     def sum(a, b): # no self or cls is passed
...             return a + b
... 
>>> 

>>> Math.sum(10, 20) # you dont need to instatiate the Math class to use
30
>>> 
```

## Duck Typing

- Python dosen´t check the type, since the method is avaiable, it is, the interface is implemented

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def noise(self):
        pass

class Dog(Animal):
    # __init__ is not overriden, so Python automatically calls
    # Animal.__init__...

    def noise(self):
        print(self.sound + " !")

class Cat(Animal):
    # Again, __init__ is not overriden

    def noise(self):
        print(self.sound + "...")


good_dog = Dog("Good", "Bark")
pretty_cat = Cat("Mewtwo", "Meow")

house_animals = [good_dog, pretty_cat]

for animal in house_animals:
    # Duck Typing
    # Python dosen´t care about the type, since the interface is avaiable
    animal.noise()
```

```bash
$ /usr/bin/python3 /tmp/sample.py
Bark !
Meow...
```

## Python Magic Methods

- Magic Methods performe some operations that have specific syntax (`==`, `=`, `<`, `>=`, etc...)
- They star and end with two underscores, like `__init__`

```python
# Word that are case insensitive for comparisons
class Word:
    def __init__(self, word):
        self.word = word
    
    def __eq__(self, value):
        # Case insensitive comparasion
        return self.word.lower() == value.word.lower()

print( Word("Aha") == Word("aHA") )
```

```bash
$ /usr/bin/python3 /tmp/sample.py
True
```

- The two most used special methods are `__init__` and `__str__`, the second the way to print (`print(obj)`, `str(obj)`...) the object:

```python
class Word:
    def __init__(self, word):
        self.word = word
    
    def __str__(self):
        return f"Word('{self.word.lower()}')"

print( Word("Aha") )
```

```bash
$ /usr/bin/python3 /tmp/sample.py
Word('aha')
```

- Another method is the `__repr__` used for object representation in the prompt:

```python
>>> class Word:
...     def __init__(self, word):
...         self.word = word
...     
...     def __repr__(self):
...         return f"Word({self.word})[{id(self)}]"
... 
>>> Word("Test!")
Word(Test!)[140579768199656]
>>> 
```

## Composition

- Prefer composition over inheritance



## Objects / Classes x Modules

- Modules are singletons (only one loaded per process)

- Module don´t support inheritance

- Keep data structures simple. Prefer to use tuples, lists, dicts...

## Named Tuple

- Subclass of tuples which elements are accessible by key `[offset]` or `.key`:

```python
# Creating
>>> Duck = namedtuple("Duck", "name tail") # "Class" name and fields
>>> 
>>> d1 = Duck("john", 21)
>>> d1
Duck(name='john', tail=21)
>>> 
>>> d1.name
'john'
>>> d1.tail
21
>>> d1[0]
'john'
>>> 
```

- Creating a `namedtuple` from a `dict`:

```python
>>> Person = namedtuple("Person", "name age")
>>> 
>>> d = {"name": "John", "age": 23}
>>> 
>>> p = Person(**d)
>>> p
Person(name='John', age=23)
>>> 
```

