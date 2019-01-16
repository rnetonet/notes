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

# Dictionaries

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

- What Python considers `True`:

```python

```