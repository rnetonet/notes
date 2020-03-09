# Learning Python, 5ed

## How Python Runs Programs

### Running Modules

* All Python files are modules, and are compiled to bytecode before execution.

* Imported modules bytecodes are cached in disk for optimization.

* Python compiles each module once per execution. An explicit reload should be requested if necessary.

* Bytecode files are regenerated if original source changes (compares timestamps) or its imported by a different interpreter.

* Everything in Python happens in runtime: classes, functions creation, modules linkage.
Everything happens in runtime, while the interpreter reads the code.

### Shebangs

* Avoid explicit shebang lines in unix using *env* trick:

```python
#!/usr/bin/env python3
...
```

* Since 3.3, Python for Windows handles shebangs:

```python
#!python3
...
```

### Windows Python Runner

If you call it using the `py` utility, `python3` will be used.

* You can define the version as an argument for `py`:

```bash
py -3.1 script.py
```

```bash
py -3 script.py
```

### Importing and Reloading Modules

* **Importing is also a way to run Python modules.**

* Every Python file is a module, thus can be imported.

* Imports load another file and make the resulting attributes accessible to the importer.

* In other words, importing a module means running its code.

* Imports run once per interpreter session. Subsequent imports do not reload the module.

* To force a reload, use the `imp.reload` module function:

```python
import imp
import mymodule

# ...

imp.reload(mymodule)

# ...
```

### Accessing Modules Attributes

* Modules = namespaces

* Modules are run when imported (in `import` or `from` statements) .

* Import example. Uses the module object and the dot operator to access attributes:

```python
# Load "lib.py", compile to bytecode, created a module object and assign to a "lib" variable in the current scope
import lib

# Access the function "func" defined in the top-level of "lib.py" through the "lib" variable/module.
print(lib.func(a, b))
```

* `from ... import ...` example. **Copies** the listed attributes to the importer scope:

```python
# Load, compile and run "lib". From the resulting module object, copy func as a to the current scope
from lib import func

# No need for prefix
func(a, b)
```

Its the same as in the importer:

```python
import lib

func = lib.func
```

* You can `exec()` some module, as you just typed its concent, using `exec()`:

```python
exec(open('script1.py').read())
```

* Every time you call `exec()` it executes the code as you had just typed it where you called. It is not like an import.


### Getting Help

To list all the names avaiable in a module, use `dir(module)`:

```python
>>> import antigravity
>>> dir(antigravity)
['__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'geohash',
 'hashlib',
 'webbrowser']
>>>
```

* `dir([object])`:

    * If called without object, list the names defined in the current scope;

    * If an object is passed, returns an alphabetized of its attributes.

```python
>>> # dir() -> local scope attributes
>>> dir()
['In',
 'Out',
 '_',
 '__',
 '___',
 '__builtin__',
 '__builtins__',
 '__doc__',
 '__loader__',
 '__name__',
 '__package__'

...

>>> # dir(object)
>>> s = "Hello world"
>>> dir(s)
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
```

* `help(class) or help(class.method), shows the pydoc`:

```python
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return key in self.
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getitem__(self, key, /)
 |      Return self[key].



>>> help(str.replace)
Help on method_descriptor:

replace(self, old, new, count=-1, /)
    Return a copy with all occurrences of substring old replaced by new.

      count
        Maximum number of occurrences to replace.
        -1 (the default value) means replace all occurrences.

    If the optional argument count is given, only the first count occurrences are
    replaced.

```

## Introducing Python Object Types

* Modules, classes and functions are objects too. Thus, can be passed as any other object in code.

### Numbers

> TODO: Fill

### Strings

* Booleans are numbers in Python. `True == 1`, `False == 0`.

* Strings, lists and tuples are sequences. Sequences can be indexed, starting with the `0` index:

```python
>>> s = "Hello World"
>>> s[0]
'H'
>>> s[1]
'e'
>>>
```

* Sequences can be indexed backwards (right to left), starting with `-1`:

```python
>>> s = "Hello World"
>>> s[0]
'H'
>>> s[1]
'e'
>>> s[-1]
'd'
>>> s[-2]
'l'
>>>
```

* Negative indexes are just added to the string length, so these expressions are equivalents:

```python
>>> s = "Hello World"
>>>
>>> s[-2]
'l'
>>> s[len(s)-2]
'l'
>>>
```

* Anywhere Python expects a value, you can use an expression or a variable:

```python
>>> s = "Hello World"
>>>
>>> s[1 + 1]
'l'
>>>
```

* Sequences (strings, tuples, lists) also supports slicing, **which return new objects**:

```python
>>> s = "Hello World"
>>>
>>> s[1:3]
'el'
>>>
```

**Note: the first index (`1`) is included, the second (`3`), not.**

* In slices, the first parameter defaults to `0` and the last to the `length` of the sequence. Some common usages are based on this:

```python
>>> s = "Hello World"
>>>
>>> s[:3]
'Hel'
>>> s[0:3]
'Hel'
>>>
>>> s[3:]
'lo World'
>>> s[3:len(s)]
'lo World'
>>>

>>>
>>> s[:-1]
'Hello Worl'
>>> s[:] # A copy!
'Hello World'
>>>
```

* You can create a new string concatenating two strings (`+`) or by repeating one (`*`):

```python
>>> a = "Hello"
>>> b = "World"
>>> c = a + b
>>> c
'HelloWorld'
>>>
>>> d = a * 3
>>> d
'HelloHelloHello'
>>>
```

* Python strings are immutable. You can't change it. But, you can create a new string and assign to the same variable:

```python
>>> s = "Hello World"
>>> s = "Hello World" + " " + "Again"
>>> s
'Hello World Again'
>>>
```


* Ways to declare a string in Python:

```python
>>> 'single "quotes"' # can enclose the other type
'single "quotes"'
>>> "single 'quotes'" # can enclose the other type
"single 'quotes'"
>>>
>>> """triple 'quotes'"""
"triple 'quotes'"
>>> """triple
... 'quotes'
... """
"triple \n'quotes'\n"
>>>
>>> '''triple
... "quotes"
... '''
'triple\n"quotes"\n'
>>>
>>> # newline \n and tabs \t
>>> print("test\nteste")
test
teste
>>> print("\t test; \n \t another")
         test;
         another
>>>
>>> # raw strings, does not interpretate escape codes
>>> print(r"\t test; \n \t another")
\t test; \n \t another
>>>

>>> path = r"c:\windows\dir"
>>> print(path)
c:\windows\dir
>>>
```

### Unicode Strings

* Non-ASCII text (Japanese, Russian...) is handled by *unicode strings*.

* In Python 3, the default `str` type handles unicode, while raw bytes strings (media and **encoded** text) are handled by the `bytes` type.

```python
>>> "sp\xc4m"
'spÄm'
>>> type("sp\xc4m") # the default str is unicode aware
str
>>>
>>> b"\x01c"
b'\x01c'
>>> type(b"\x01c") # bytes, bynary strings
bytes
>>>
>>> u"sp\xc4m"
'spÄm'
>>> type(u"sp\xc4m") # Python 2 unicode aware string syntax (see below). Still valid in 3.
>>>
```

* In Python 2 the default `str` is equivalent to the `bytes` type. So, it can handle bytes and ASCII letters (which are represented as single bytes). To create unicode aware strings, you need to prefix them with an `u`:

```python
>>> "sp\xc4m"
'sp\xc4m'
>>> type("sp\xc4m") # the default str is bytes string, not unicode aware
<type 'str'>
>>>
>>> print("sp\xc4m")
sp�m
>>> print("sp\xc4m") # See ? Unicode not rendered.
sp�m
>>>
>>> u"sp\xc4m"
u'sp\xc4m'
>>> type(u"sp\xc4m") # To create a unicode aware str, prefix with "u"
<type 'unicode'>
>>> print(u"sp\xc4m") # Unicode is handled now
spÄm
>>>
>>> b"sp\xc4m" # Python 2.7 and 3 syntax to create str bytes strings. In Python 2 is supported, but unecessary.
'sp\xc4m'
>>>
```

* In both Python 2 and Python 3, non-Unicode strings are 8-bits (bytes) sequences. And, when printed, are converted to ascii whenever possible.
While unicode strings are sequences of unicodes code points (which **can or can not** translate to single bytes when **encoded**).

* Mind that the bytes notion **dosen´t** apply to unicode strings. They are sequences of **unicode codepoints** ***not sequence of bytes***.

> Unicode code points do not relate to single bytes.

Example:

```python
#!/usr/bin/env python3
>>> "acentuação"
'acentuação'
>>> type("acentuação") # py3, str is unicode aware
str
>>> len("acentuação")  # the number of chars (unicode code points). nothing to do with bytes. len is unicode aware.
10
>>> "acentuação".encode() # encode the unicode string into a bytes string.
b'acentua\xc3\xa7\xc3\xa3o'
>>> type("acentuação".encode()) # bytes
bytes
>>>
>>> len( "acentuação".encode() ) # note: the code point are represented as one or more bytes
12
>>>
```

* Python 3 and 2 support the `bytearray` type, which are modifiable non-unicode sequences:

```python
>>> bar = bytearray("acentuação", "utf-8")
>>> bar
bytearray(b'acentua\xc3\xa7\xc3\xa3o')
>>> type(bar)
bytearray
>>>
>>> bar[0:0] = "àé".encode() # You can change parts
>>> bar
bytearray(b'\xc3\xa0\xc3\xa9acentua\xc3\xa7\xc3\xa3o')
>>> print(bar)
bytearray(b'\xc3\xa0\xc3\xa9acentua\xc3\xa7\xc3\xa3o')
>>> print(bar.decode()) # And decode back to a string
àéacentuação
>>>
```

* To represent a **single byte** in *unicode or non-unicode strigs*, use `\xHH`, where `HH` are two hexadecimals digits:

```python
>>> print("\xff") # a single byte
ÿ
>>> ord("\xff") # 255
255
>>>
```

* In **unicode strings** you can use `\uHHHH` for short unicode code points, or `\UHHHHHHHH` for long code points. In both patterns, each `H` represents a hexadecimal digit. So, as each hexadecimal represents 4 bits, the `\u` suppots 16-bit values and `\U`, 32 bits:

```python
>>> print("\u2122") # Trademark short codepoint
™
>>> print("\U0001F600") # Grinning face U+1F600, Python always requires 8 hex charts, so you prefix: 0001F600
😀
>>>
```

* You `encode` unicode strings to save in files. And `decode` the read file back to a unicode string.


### Lists

* Lists are mutable ordered sequences of objects of any type.

```python
>>> l = [1, "abc", 3.14, True]
>>> l
[1, 'abc', 3.14, True]
>>>
>>> l[0] = 2
>>> l
[2, 'abc', 3.14, True]
>>>
```

* Lists support the main **sequence** methods provided by Python:

> The common **sequence** methods return new objects, they don´t perform in-place changes.

```python
>>> l = [1, "abc", 3.14, True]
>>>
>>> # Length
>>> len(l)
4
>>> # Indexing
>>> l[0]
1
>>> l[-1]
True
>>> l[2]
3.14
>>>
>>> # Length slicing
>>> l[0:3]
[1, 'abc', 3.14]
>>> l[2:3]
[3.14]
>>>

>>> l + [10, 20, 30] # Returns a new list
[1, 'abc', 3.14, True, 10, 20, 30]
>>>
>>> l
[1, 'abc', 3.14, True]
>>>
>>> l * 2
[1, 'abc', 3.14, True, 1, 'abc', 3.14, True]
>>>
>>> l
[1, 'abc', 3.14, True]
>>>
```

* Lists also provide some type specific methods, which can perform *in-place* changes:

```python
>>> l = [1, "abc", 3.14, True]
>>>
>>> l.append(False) # add to the end
>>> l
[1, 'abc', 3.14, True, False]
>>>
>>> l.pop(4) # Remove and return object in index = 4
False
>>> l
[1, 'abc', 3.14, True]
>>>
>>> l.insert(1, -99) # Insert object into index 1
>>> l
[1, -99, 'abc', 3.14, True]
>>>
>>> l.remove(-99) # Remove by value
>>> l
[1, 'abc', 3.14, True]
>>>
>>> l.extend([10, 20, 30]) # Equivalente to: l += [10, 20, 30]
>>> l
[1, 'abc', 3.14, True, 10, 20, 30]
>>>
>>> # Sorting and reversing
>>> l = [3, 2, 4, 8, 1]
>>> l.sort()
>>> l
[1, 2, 3, 4, 8]
>>>
>>> l.reverse()
>>> l
[8, 4, 3, 2, 1]
>>>
```

* Python checks if the index being accessed exists, if not, an Exception is thrown:

```python
>>> l = ['a', 'b', 'c']
>>>
>>> l[0]
'a'
>>> l[1]
'b'
>>> l[2]
'c'
>>> l[3]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-5-bb49eeb9f0db> in <module>
----> 1 l[3]

IndexError: list index out of range
>>> l[99] = "z" # During assignment too
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-6-6c807f12f520> in <module>
----> 1 l[99] = "z" # During assignment too

IndexError: list assignment index out of range
>>>
```

* List can contain any object type, even other lists. This is one way to implement matrixes in Python:

```python
>>> # 3x3 matrix
>>> l = [
...     [1, 2, 3],
...     [7, 8, 9],
...     [20, 30, 40]
... ]
>>>
>>> l[0] # first row
[1, 2, 3]
>>> l[2] # third row
[20, 30, 40]
>>>
>>> l[0][0] # first row, first column
1
>>> l[1][2] # second row, third column
9
>>>
```

### Comprehensions

* List comprehensions are a succint way to process sequences and generate new lists.

```python
>>> # 3x3 matrix
... matrix = [
...     [1, 2, 3],
...     [7, 8, 9],
...     [20, 30, 40]
... ]
>>>
>>> # Get the second column for each row
>>> seconds = [row[1] for row in matrix]
>>> seconds
[2, 8, 30]
>>>
>>>
```

* They can be more complex and even include a conditional (`if`):

```python
>>> # 3x3 matrix
... matrix = [
...     [1, 2, 3],
...     [7, 8, 9],
...     [20, 30, 40]
... ]
>>>

>>> # More complex expression
>>> seconds_doubled = [row[1] * row[1] for row in matrix]
>>> seconds_doubled
[4, 64, 900]
>>>

>>> # seconds_doubled if lower than 50
>>> seconds_doubled_lt_50 = [row[1] ** 2 for row in matrix if row[1] ** 2 <= 50]
>>> seconds_doubled_lt_50
[4]
>>>
```

* List comprehensions can act over any *iterator*:

```python
>>> # Hardcoded
>>> # 3x3 matrix
... matrix = [
...     [1, 2, 3],
...     [7, 8, 9],
...     [20, 30, 40]
... ]
>>>
>>> # Extract diagonal, iterating over a literal list
>>> diagonal = [matrix[i][i] for i in [0, 1, 2]]
>>> diagonal
[1, 8, 40]
>>>
>>> # Over a string
>>> doubled_letters = [letter * 2 for letter in 'spam']
>>> doubled_letters
['ss', 'pp', 'aa', 'mm']
>>>
```

* `range(included_start_index, non_included_end_index, step)` is a built-in to create sequences of numbers:

```python
#!/usr/bin/env python2
>>> range(0, 10, 2)
[0, 2, 4, 6, 8]
>>>
```

```python
#!/usr/bin/env python3
>>> # In Py 3, range returns a generator, so its generation is on-demand, to save memory
>>> range(0, 10, 2)
range(0, 10, 2)
>>>
>>> # If you want to generate all, encapsulate it on a list
>>> list(range(0, 10, 2))
[0, 2, 4, 6, 8]
>>>
```

```python
>>> # In Py 3, range returns a generator, so its generation is on-demand, to save memory
>>> range(0, 10, 2)
range(0, 10, 2)
>>>
>>> # If you want to generate all, encapsulate it on a list
>>> list(range(0, 10, 2))
[0, 2, 4, 6, 8]
>>>
>>>
>>> # range follow the same rules of slice indexing, supporting negative values, etc
>>> list( range(-6, 10, 2) )
[-6, -4, -2, 0, 2, 4, 6, 8]
>>>
```

* List comprehension can return a list of any kind of objects, even other lists:

```python
>>> value_half_double = [[value, value/2, value*2] for value in range(0, 10)]
>>> value_half_double
[[0, 0.0, 0],
 [1, 0.5, 2],
 [2, 1.0, 4],
 [3, 1.5, 6],
 [4, 2.0, 8],
 [5, 2.5, 10],
 [6, 3.0, 12],
 [7, 3.5, 14],
 [8, 4.0, 16],
 [9, 4.5, 18]]
```

* List comprehensions were expanded to generate other types beyond lists. One of them are the generators, which produce values on-demand:

```python
>>> # 3x3 matrix
... matrix = [
...     [1, 2, 3],
...     [7, 8, 9],
...     [20, 30, 40]
... ]
>>>
>>> # Return a sum of each row as a generator
>>> sum_for_each_row = (sum(row) for row in matrix) # Comprehension in parentheses return a generator
>>> sum_for_each_row
<generator object <genexpr> at 0x7fe7286b1c10>
>>>
>>> # One way to require values from a generator, is using next
>>> next(sum_for_each_row)
6
>>> next(sum_for_each_row)
24
>>> next(sum_for_each_row)
90
>>>
>>> next(sum_for_each_row) # Generator was exhausted
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-56-c142c678b04d> in <module>
----> 1 next(sum_for_each_row) # Generator was exhausted

StopIteration:
>>>
>>>
```

* Generators can be used in loops:

```python
>>> # 3x3 matrix
... matrix = [
...     [1, 2, 3],
...     [7, 8, 9],
...     [20, 30, 40]
... ]
>>>
>>> sum_for_each_row = (sum(row) for row in matrix) # Comprehension in parentheses return a generator
>>>
>>> for sum_of_row in sum_for_each_row:
...     print(sum_of_row)
...
6
24
90
>>> # Exhausted in the previous loop
... for sum_of_row in sum_for_each_row:
...     print(sum_of_row)
...
>>>
>>>
```

> Remember that generators are consumed and subsequent calls can not generate values.

* The `map(fx, iterator)` returns the result of the function `fx` over the `iterator`, it also returns a generator:

```python
>>> # 3x3 matrix
... matrix = [
...     [1, 2, 3],
...     [7, 8, 9],
...     [20, 30, 40]
... ]
>>>
>>> sum_for_each_row = map(sum, matrix)
>>> for sum_of_row in sum_for_each_row:
...     print(sum_of_row)
...
6
24
90
>>>
```

* Dictionaries and Sets can also be created using comprehension syntax:

```python
>>> # 3x3 matrix
... matrix = [
...     [1, 2, 3],
...     [7, 8, 9],
...     [20, 30, 1]
... ]
>>>
>>> # Set (unique values) of the diagonal
>>> diagonal_uniq = {matrix[i][i] for i in range(0, 3)}
>>> diagonal_uniq
{1, 8}
>>>
```

```python
>>> # 3x3 matrix
... matrix = [
...     [1, 2, 3],
...     [7, 8, 9],
...     [20, 30, 1]
... ]
>>>
>>> # Dict: key is the value, value is the double
>>> doubled_diagonal = {matrix[i][i]: matrix[i][i] ** 2 for i in range(0, 3)}
>>> doubled_diagonal
{1: 1, 8: 64}
>>>
```

### Dictionaries

* Dictionaries are mutable maps that can contain any kind of object as value and any kind of imutable object as key.

* Dictionaries can grown or shrink on demand.

* Dictionaries literals are coded in curly braces:

```python
>>> d = {"food": "cheese", "quantity": 10, "status": "ready"}
>>> d
{'food': 'cheese', 'quantity': 10, 'status': 'ready'}
>>>
```

* To get a value, you index using the key:

```python
>>> d = {"food": "cheese", "quantity": 10, "status": "ready"}
>>>
>>> d["food"]
'cheese'
>>> d["quantity"]
10
>>> d["status"]
'ready'
>>>
```

* And you can change the throught indexing also:

```python
>>> d = {"food": "cheese", "quantity": 10, "status": "ready"}
>>>
>>> d["food"]
'cheese'
>>> d["quantity"]
10
>>> d["status"]
'ready'
>>>
>>> d["food"] = "beans"
>>> d
{'food': 'beans', 'quantity': 10, 'status': 'ready'}
>>>
>>> d["quantity"] += 1
>>> d
{'food': 'beans', 'quantity': 11, 'status': 'ready'}
>>>
```

* As lists, if you index something that is not there, you get an Exception:

```python
>>> d = {"food": "cheese", "quantity": 10, "status": "ready"}
>>>
>>> d["name"]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-14-3dc752b20a59> in <module>
----> 1 d["name"]

KeyError: 'name'
>>>
```

* But you can assign to inexistent keys, thus creating it:

```python
>>> d = {"food": "cheese", "quantity": 10, "status": "ready"}
>>>
>>> d["expected_time"] = 60
>>>
>>> d
{'food': 'cheese', 'quantity': 10, 'status': 'ready', 'expected_time': 60}
>>>
```

* Generally, you start with an empty dictionary `{}` and fills it:

```python
>>> john = {}
>>> john["age"] = 22
>>> john["city"] = "London"
>>>
>>> john
{'age': 22, 'city': 'London'}
>>>
```

> Dictionary indexing is very fast. Leverage it.

* Other two common ways to create a dictionary are using the `dict` with keyword arguments and, sometimes, with support of the `zip(a, b)` built-in function:

```python
>>> john = dict(age=22, city='London')
>>> john
{'age': 22, 'city': 'London'}
>>>
>>>
>>> # zip creates pairs (tuples) from two sequences. the first compose the keys, the second, the values
>>> zip(["age", "city"], [22, "London"]) # zip object
<zip at 0x7f4da5b03800>
>>>
>>> list( zip(["age", "city"], [22, "London"]) ) # as a list
[('age', 22), ('city', 'London')]
>>> john = dict(zip(["age", "city"], [22, "London"]))
>>> john
{'age': 22, 'city': 'London'}
>>>
```

> Dictionaries don´t guarantee ordering, so don´t depend on it.

* All the *container* types in Python support nesting: lists, dicts, etc.
Nesting can be used to create more complex structures:

```python
>>> john = {
...     "name": {"first": "john", "last": "doe"},
...     "jobs": ["architect", "programmer", "cleaner"],
...     "salary": 40.5
... }
>>> john
{'name': {'first': 'john', 'last': 'doe'},
 'jobs': ['architect', 'programmer', 'cleaner'],
 'salary': 40.5}
>>>
>>> # You can change nested objects
>>> john["jobs"].append("joker")
>>> john
{'name': {'first': 'john', 'last': 'doe'},
 'jobs': ['architect', 'programmer', 'cleaner', 'joker'],
 'salary': 40.5}
>>>
```

* Python is garbage collected language, so all the objects that lose all references are automatically dealocated:

```python
>>> l = [0] * 1000000
>>> l = 2 # the previous big list memory is deallocated
>>> l
2
>>>
```

* Accessing a non-existent key in a dict generates an exception:

```python
>>> data = {"a": 100, "b": 211}
>>>
>>> data["x"]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-51-56c979e698fa> in <module>
----> 1 data["x"]

KeyError: 'x'
>>>
```

* You can test the presence of a key in a dict using the `in` keyword:

```python
>>> data = {"a": 100, "b": 211}
>>> if "x" in data:
...     print(data["x"])
...
>>>
>>> data = {"a": 100, "b": 211}
>>> if "x" in data:
...     print(data["x"])
...
>>> if not "x" in data:
...     print("missing!")
...
missing!
>>>
```

* Other ways to test-before-access keys in dictionaries:

```python
>>> data = {"a": 100, "b": 211}
>>> print( data.get("x") ) # If not present, returns None
None
>>>
>>> print( data.get("x", 0) ) # You can specify a second param to be return instead of None
0
>>>
>>> data = {"a": 100, "b": 211}
>>> print( data.get("x") ) # If not present, returns None
None
>>>
>>> print( data.get("x", 0) ) # You can specify a second param to be return instead of None
0
>>> # Or using an if else short expression
>>> value = data["x"] if "x" in d else 0
>>> value
0
>>>
```

* Dictionaries don´t guarantee order, so, to iterate over it in an ordered manner you can use the `built-in` function `sorted()`:

```python
>>> data = {"a": 10, "b": 14, "c": 25}
>>> for key in sorted(data):
...     print(key)
...
a
b
c
>>>
```

### Loops

* You can iterate over *iterables* using the `for` loop in Python:

```python
>>> l = [1, 2, 3]
>>> for item in l:
...     print(item)
...
1
2
3
>>>
>>> s = "spam"
>>> for letter in s:
...     print(letter.upper())
...
S
P
A
M
>>>
>>> d = {"a": 10, "b": 20, "c": 30}
>>> for key in d:
...     print(key)
...
a
b
c
>>>
```

* The other, more generic, loop is the `while`, which tests a condition before each iteration:

```python
>>> counter = 0
>>> while counter < 10:
...     print("Spam!")
...     counter = counter + 1
...
Spam!
Spam!
Spam!
Spam!
Spam!
Spam!
Spam!
Spam!
Spam!
Spam!
>>>
```

### Iterators

* Python has an `Iterator Protocol` that make objects work with `for` loops and comprehensions. The protocol requires the object to return to respond to the `iter(object)` call with an object that return values to subsequent `next(result_object)` calls. Generators, for example, follow this protocol:

```python
>>> l = [1, 2, 3]
>>> l_iter = iter(l)
>>> l_iter
<list_iterator at 0x7f9d489410d0>
>>>
>>> next(l_iter)
1
>>> next(l_iter)
2
>>> next(l_iter)
3
>>> next(l_iter) # If no more values, throw an Exception
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-7-b7ec262db220> in <module>
----> 1 next(l_iter) # If no more values, throw an Exception

StopIteration:
>>>
```

* Remember, any comprehension can be written as a `for` loop:

```python
>>> squares = [value ** 2 for value in [10, 20, 30]]
>>> squares
[100, 400, 900]
>>>
>>> # or...
>>>
>>> squares = []
>>> for value in [10, 20, 30]:
...     squares.append(value ** 2)
...
>>> squares
[100, 400, 900]
>>>
```

> Comprehensions will usually run faster than for loops.

### Tuples

* Tuples are just like lists, sequences, nestable, of any kind of object. With one main difference: they are imutable and coded in parentheses instead of square brackets:

```python
>>> t = (1, 2, 3)
>>> t
(1, 2, 3)
>>>
>>> another_t = 1, 2, 3 # If you enumerate objects intercalated by commas, Python reads as a tuple
>>> another_t
(1, 2, 3)
>>>
>>>
```

* Tuple support all sequence operations, returning new tuples when necessary:

```python
>>> t = ("a", "b", "c")
>>> len(t)
3
>>>
>>> t + t
('a', 'b', 'c', 'a', 'b', 'c')
>>> t * 3
('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')
>>>
>>> t[0]
'a'
>>> t[1]
'b'
>>> t[2]
'c'
>>>
```

* Tuple also have some especific methods:

```python
>>> t = ("a", "b", "a", "a", "b", "b", "b", "c")
>>> t.count("a")
3
>>>
>>> t.index("b") # first index
1
>>>
```

* Tuples can´t be changed:

```python
>>> t = ("spam", "eggs", "bacon", [1, 2, 3])
>>> t
('spam', 'eggs', 'bacon', [1, 2, 3])
>>> t[0] = "42!"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-17-9130a031421f> in <module>
----> 1 t[0] = "42!"

TypeError: 'tuple' object does not support item assignment
>>>
```

* But you can change mutable elements inside a tuple:

```python
>>> t = ("spam", "eggs", "bacon", [1, 2, 3])
>>> t[3].append(4)
>>> t
('spam', 'eggs', 'bacon', [1, 2, 3, 4])
>>>
```

### Files

* Files are a core type, but you create them using the built-in `open(fname, openmode)`:

```python
>>> fp = open("example.txt", "w") # create a text file to Write
>>> fp.write("Spam!")
5
>>> fp.close()
>>>
```

* To read, `open(fname, 'r')` the file with the `'r'` openmode, which is the default if you omit:

```python
>>> fp = open("example.txt")
>>> # Read content: Always returns a string
>>> fp.read()
'Spam!'
>>> fp.close()
>>>
```

* After iterators, the best way to read a file is to iterate directly over it:

```python
>>> fp = open("/etc/hosts")
>>> for line in fp: print(line)
127.0.0.1       localhost
127.0.1.1       thinkpad
# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
>>> fp.close()
>>>
```

* In Py3 the strings are always encoded before being written to a file and decoded when read. While Py2 blindly writes and reads the string bytes to and from the file.

* In Py3 text is always read and decoded using some *encoding* and encoded when written, also using this encode. This encode is inherited from the system where the module is running, but you can explictly define:

```python
>>> # Save text file encoded as utf16
>>> fp = open("/tmp/teste.txt", "w", encoding="utf16")
>>> fp.write("acentuação!")
11
>>> fp.close()
>>>
>>> # Read the file as bytes and shows the encoded string
>>> fp = open("/tmp/teste.txt", "rb") # read as bytes
>>> fp.read()
b'\xff\xfea\x00c\x00e\x00n\x00t\x00u\x00a\x00\xe7\x00\xe3\x00o\x00!\x00'
>>> fp.close()
>>>
```

* You can `encode` and `decode` a string manually:

```python
#!/usr/bin/env python3
>>> st = "acentuação"
>>> st_utf16_encoded = st.encode("utf16") # get bytes representation for utf16 encoding
>>> st_utf16_encoded
b'\xff\xfea\x00c\x00e\x00n\x00t\x00u\x00a\x00\xe7\x00\xe3\x00o\x00'
>>>
>>> st_utf16_encoded.decode("utf16") # convert bytes to unicode string using utf16 encoding
'acentuação'
>>>
```

### Sets

* Sets are unordered collections of unique and immutable objects and are created using `set()` or `{}`:

```python
>>> x = set("spam")
>>> x
{'a', 'm', 'p', 's'}
>>>
>>> y = {"h", "a", "m", "m", "m"}
>>> y
{'a', 'h', 'm'}
>>>
>>>
```

* They support all mathematical operations for sets:

```python
>>> x = set("spam")
>>> y = {"h", "a", "m", "m", "m"}
>>>
>>> x, y
({'a', 'm', 'p', 's'}, {'a', 'h', 'm'})
>>>
>>> x & y # intersection
{'a', 'm'}
>>>
>>> x | y # union
{'a', 'h', 'm', 'p', 's'}
>>>
>>> x - y # difference
{'p', 's'}
>>>
>>> x > y # superset
False
>>> x < y # subset
False
>>>
>>>
```

* Comprehensions can be used to create sets:

```python
>>> s = {value ** 2 for value in [1, 2, 3, 4]}
>>> s
{1, 4, 9, 16}
>>>
```

* Some useful usecases for sets:

```python
>>> # Remove duplicates
>>> set("spaaaaaaam")
{'a', 'm', 'p', 's'}
>>>
>>> # Find differences
>>> set("aloha") - set("alopa")
{'h'}
>>>
>>> # unordered and duplicate indifferent comparasion
>>> set("spam") == set("spamamamamamsa")
True
>>>
```

* You can check for the presence of some value in a set using the `in` operator:

```python
>>> "p" in set("spam")
True
>>>
```

### Decimals and Fractions

* `Decimal` type is a fixed-precision floating number type:

```python
>>> import decimal
>>>
>>> d = decimal.Decimal('3.141')
>>> d
Decimal('3.141')
>>>
>>> d + 1
Decimal('4.141')
>>>
>>> decimal.getcontext().prec = 2
>>>
>>> decimal.Decimal('1.00') / decimal.Decimal('3.00')
Decimal('0.33')
>>>
>>>
```

* Fractions `numerator / denominator`:

```python
>>> from fractions import Fraction
>>>
>>> f1 = Fraction(2, 3)
>>> f1
Fraction(2, 3)
>>>
>>> f2 = Fraction(3, 3)
>>> f2
Fraction(1, 1)
>>>
>>> f1 + f2
Fraction(5, 3)
>>>
```

### True, False and None

* Python has booleans `True` and `False` which are `1` and `0` with some display logic:

```python
>>> True + True
2
>>>
>>> False - True
-1
>>> int(True)
1
>>>
>>> int(False)
0
>>>
```

* And a placeholder object that means no-value: `None`:

```python
>>> name_to_be_defined = None
>>> name_to_be_defined is None # None is a singleton!
True
>>>
>>> name_to_be_defined
>>> print(name_to_be_defined)
None
>>>
```

### `type(object)` and how to not use it

* In Python you can get the `type`, the `class`, of any object using the `type(obj)` builtin:

```python
>>> type(None)
NoneType
>>>
>>> type(10)
int
>>>
>>> type("Example")
str
>>>
>>> type(3.14)
float
>>>
>>> import decimal
>>>
>>> type(decimal.Decimal('114.5'))
decimal.Decimal
>>>
```

* Type checking is something we avoid in Python, leveraging duck typing (polymorphism), but you can do in three main forms:

```python
>>> l = [1, 2, 3]
>>>
>>> type(l) == type([])
True
>>>
>>> type(l) == list
True
>>>
>>> isinstance(l, list)
True
>>>
```

### User-defined classes

* You can create new classes using the core types, thus extending them:

```python
>>> class Employee:
...     def __init__(self, name, pay):
...         self.name = name
...         self.pay = pay
...     def last_name(self):
...         return self.name.split()[-1]
...     def give_raise(self, raise_amount):
...         self.pay += raise_amount
...         return self.pay
...
>>>
>>> e1 = Employee("John Doe", 1000)
>>> e1.last_name()
'Doe'
>>>
>>> e1.pay
1000
>>> e1.name
'John Doe'
>>>
>>> e1.give_raise(1000)
2000
>>> e1.pay
2000
>>>
```

## Numeric Types

### Numeric literals

* Python numeric literals:

```python
>>> 123, -21, 999999999999999999999999999999999999 # Integer. Unlimited size.
(123, -21, 999999999999999999999999999999999999)
>>> 1.23, -2.3, 1.2123131231119881238111           # Floats. Implemented as C doubles. Precision dependes on the compiler. If precision is important, use a Decimal.
(1.23, -2.3, 1.2123131231119881)
>>>
>>> 0o123, 0x9ff, 0b010101                         # Integer declared as octa, hexa and binary
(83, 2559, 21)
>>>
>>> set("spam"), {"s", "p", "a", "m"}              # sets
({'a', 'm', 'p', 's'}, {'a', 'm', 'p', 's'})
>>>
>>> bool(object), True, False                      # bool() builtin, which returns the boolean value of any object and the singletons True and False
(True, True, False)
```

* To convert an `int` to hexadecimal, octal or binary:

```python
>>> i = 10
>>>
>>> hex(i), oct(i), bin(i)
('0xa', '0o12', '0b1010')
>>>
```

* To convert a string to an int use `int(st, [base])`:

```python
>>> int('5')
5
>>>
>>> # If the string is in somebase, pass it to int()
>>> int('0b010101', 2)
21
>>>
```

### Numbers in Action

* Python promotes different numeric types in expressions to the more complex type (`int` -> `float` -> `complex`);

* Operators mean different things on different objects and can be overloaded in your classes definitions.

* Python 2 and 3 difference on divisions:

```python
#!/usr/bin/env python2
>>> 10 / 2 # only integers, integer result
5
>>> 10 / 2.0 # if one is float, result is float
5.0
>>>
```

```python
#!/usr/bin/env python3
>>> 10 / 2 # always float
5.0
>>> 10 / 2.0 # always float
5.0
>>>
>>> 10 // 2 # if all are integers and you want a truncated-int result, use //
5
>>>
>>> 10 // 2.0 # if one is float, the result is float, even when truncated.
5.0
>>>
```

### Numeric display formats

* Both functions `repr` and `str` convert an object to a string representation. `repr` returns a code-like representation and `str`, a user friendly version:

```python
>>> repr('spam')
"'spam'"
>>> print('spam')
spam
>>>
```

* In Python 3 you can use `str` to decode a bytestring into an unicode string:

```python
#!/usr/bin/env python3
>>> bstr = b'xyz'
>>> bstr
b'xyz'
>>>
>>> converted = str(bstr, "utf8") # the same as bstr.decode("utf8")
>>> converted
'xyz'
>>>
```

* Python also promotes types in comparisons. And different numeric types can be compared between them.

* Python allows chained comparisons, which are an efficient way to create range tests:

```python
>>> 2 < 3 < 4
True
>>>
>>> # The same as
>>> 2 < 3 and 3 < 4
True
>>>
```

* Chained comparisons can use any operatos and have arbitrary lengths:

```python
>>> 2 < 3 != 5 > 1
True
>>>
>>> # The same as
>>> 2 < 3 and 3 != 5 and 5 > 1
True
>>>
```

* Remember, `float` is imprecise (they have a limited number of bits to represent the number). What can lead to unexpected results:

```python
>>> 1.1 + 2.2 == 3.3
False
>>> 1.1 + 2.2
3.3000000000000003
>>>
```

If you want precision, use `Decimal`:

```python
>>> import decimal
>>> decimal.getcontext().prec = 2
>>> decimal.Decimal('1.1') + decimal.Decimal('2.2') == decimal.Decimal('3.3')
True
>>> decimal.Decimal('1.1') + decimal.Decimal('2.2')
Decimal('3.3')
>>>
```

### Division: Classic, Floor, and True

* The true division operator `/` changed between Python 2 and 3.
In 2, it truncates the result when both operands are integers, else returns a floating point.
While in 3, it always returns a floating point.

```python
#!/usr/bin/env python2
>>> 2 / 3
0
>>> 2 / 3.0
0.6666666666666666
>>>
```

```python
#!/usr/bin/env python3
>>> 2 / 3
0.6666666666666666
>>> 2 / 3.0
0.6666666666666666
>>>
```

* The floor division operator `//` in the other hand, always truncates the decimal part.
It returns an integer when operands are integer, if not, a float:

```python
#!/usr/bin/env python3
>>> 13 // 9
1
>>> 13 / 9
1.4444444444444444
>>>
>>> 13 // 9.0
1.0
>>> 13 / 9.0
1.4444444444444444
>>>
```

> It works pretty much the same in Python 2.

* If you want to change the true division operator behavior in Python 2 to be equal to Python 3, you can import a module from `__future__`:

```python
#!/usr/bin/env python2
>>> 10 / 3
3
>>> 10 / 3.0
3.3333333333333335
>>>
>>> from __future__ import division
>>>
>>> 10 / 3
3.3333333333333335
>>> 10 / 3.0
3.3333333333333335
>>>
```

* Mind that `//` really is a `floor` division. It rounds down the result to the closest-down integer.
It matters for negatives only, as for positives truncation is the same as floor.

```python
>>> 10 / -2.3
-4.347826086956522
>>> 10 // -2.3
-5.0
>>>
```

* If you really want a truncated result, use `math.trunc` or `int`:

```python
>>> import math
>>>
>>> 10 / -2.3
-4.347826086956522
>>> 10 // -2.3
-5.0
>>>
>>> math.trunc( 10 / -2.3 )
-4
>>> int( 10 / -2.3 )
-4
>>>
```

### Integer precision

* Python integers can grow, limited only by the memory avaiable:

```python
>>> 2 ** 3000
1230231922161117176931558813276752514640713895736833715766118029160058800614672948775360067838593459582429649254051804908512884180898236823585082482065348331234959350355845017413023320111360666922624728239756880416434478315693675013413090757208690376793296658810662941824493488451726505303712916005346747908623702673480919353936813105736620402352744776903840477883651100322409301983488363802930540482487909763484098253940728685132044408863734754271212592471778643949486688511721051561970432780747454823776808464180697103083861812184348565522740195796682622205511845512080552010310050255801589349645928001133745474220715013683413907542779063759833876101354235184245096670042160720629411581502371248008430447184842098610320580417992206662247328722122088513643683907670360209162653670641130936997002170500675501374723998766005827579300723253474890612250135171889174899079911291512399773872178519018229989376
>>>
```

### Hex, Octal, Binary: Literals and Conversions

* Python provides alternative ways to declare integer. Using binary, octal or hexadecimal notations:

```python
>>> 0b1, 0b10000 # binary: 0b prefix
(1, 16)
>>> 0o1, 0o20    # octal: 0o prefix
(1, 16)
>>> 0x1, 0x10    # hex: 0x prefix
(1, 16)
>>>
```

> Mind that it is just *written* in these notations, Python converts it to a decimal integer and stores.

* Python always store and presents integers in their decimal form. However, you can format their output using some builtins:

```python
>>> value = 1234
>>>
>>> print(bin(value)) # binary
0b10011010010
>>> print(oct(value)) # octal
0o2322
>>>
>>> print(hex(value)) # hexadecimal
0x4d2
>>>
```

* The other way, convert a string into a base different then decimal into an integer, you can use `int(str, base_number)`:

```python
>>> value = 1234
>>> binary = bin(value)
>>> octal = oct(value)
>>> hexa = hex(value)
>>>
>>> binary, octal, hexa
('0b10011010010', '0o2322', '0x4d2')
>>>
>>> int(binary, 2)
1234
>>> int(octal, 8)
1234
>>> int(hexa, 16)
1234
>>>
>>> # 10 base is the default
>>> int('1234')
1234
>>> int('1234', 10)
1234
>>>
```

* You can also convert the integers to other bases directly in the string:

```python
>>> value = 1234
>>> binary = bin(value)
>>> octal = oct(value)
>>> hexa = hex(value)
>>>
>>> binary, octal, hexa
('0b10011010010', '0o2322', '0x4d2')
>>>
>>> print(f"{value:b} / {value:o} / {value:x}")
10011010010 / 2322 / 4d2
>>>
```

### Bitwise Operations

* Bitwise operations interpret the integers as binary strings and operate on them. Mind that the returned value is a decimal integer:

```python
>>> value = 1
>>> bin(value)
'0b1'
>>>
>>> value << 2
4
>>> bin(value << 2)
'0b100'
>>>
```

* Other logical bitwise operations:

```python
>>> a = 1
>>> b = 2
>>>
>>> bin(a), bin(b)
('0b1', '0b10')
>>>
>>> a | b # or. 1 if either bit is 1.
3
>>> bin(a | b) # or. 1 if either bit is 1.
'0b11'
>>>
>>> a & b # and. 1 if both bits are 1.
0
>>> bin(a & b) # and. 1 if both bits are 1.
'0b0'
>>>
```

* To know how many bits an integer takes to be represented as binary, use `bit_length` method:

```python
>>> a = 10
>>> b = 1000
>>> a.bit_length()
4
>>> b.bit_length()
10
>>> bin(a), bin(b)
('0b1010', '0b1111101000')
>>>
```

### Other Built-in Numeric Tools

* Other numeric tools provided by the `math` module:

```python
>>> import math
>>> # Constants
>>> math.pi, math.e
(3.141592653589793, 2.718281828459045)
>>>
>>> # Sin, tangent and cosine
>>> math.sin(3)
0.1411200080598672
>>> math.tan(3)
-0.1425465430742778
>>> math.cos(3)
-0.9899924966004454
>>>
>>> # Square root
>>> math.sqrt(9)
3.0
>>>
>>> # Exponentiation (power)
>>> math.pow(2, 4)
16.0
>>>
>>> # Builtins: abs value, summation, minimum, maximum
>>> abs(-3)
3
>>> sum([1, 2, 3])
6
>>> min([1, 2, 3])
1
>>> max([1, 2, 3])
3
>>>
```

* `max()` and `min()` can receive multiple positional arguments instead of an iterator:

```python
>>> max(1, 2, 3)
3
>>> min(1, 2, 3)
1
>>>
```

* Ways to drop the decimal part of a float point number:

```python
>>> # Next lower integer
>>> math.floor(3.14)
3
>>>
>>> # Trucate. Drop the decimal part.
>>> math.trunc(3.99)
3
>>>
>>> # Another way to truncate
>>> int(3.99)
3
>>>
>>> # round > .5, up, else, down
>>> round(2.567)
3
>>> round(2.500)
2
>>> # Round only part of the decimal part
>>> round(2.567, 2) # round up to two decimal digits
2.57
>>>
```

* You can round directly during string formatation:

```python
>>> num = 3.467
>>> print(f"{num:.2f}")
3.47
>>>
```

### `random` numbers

* The `random` module allows the generation of random floats, ints, and to pick some item of an iterator randomly.

```python
>>> import random
>>>
>>> # random float between 0 and 1
>>> random.random()
0.34056710414897984
>>> random.random()
0.2017077255141171
>>> random.random()
0.008713778769984803
>>>
>>>
>>> # random int between two ints
>>> random.randint(1, 6)
5
>>> random.randint(1, 6)
4
>>> random.randint(1, 6)
2
>>>
>>> # choose a random item in a sequence
>>> random.choice(["John", "Paul", "Vincent"])
'John'
>>>
>>> # shuffle (reorder) a sequence
>>> seq = ["John", "Paul", "Vincent"]
>>> random.shuffle(seq)
>>> seq
['John', 'Vincent', 'Paul']
>>>
```

### Decimal type

* The Decimal type is a fixed-precision float. You define how many digits the decimal part will have.
And, beyond that, you define how the extra decimal digits are handled, allowing better numeric accuracy.


* A simple example to prove the `float` type imprecision and how `Decimal` can help:

```python
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
>>>
>>> from decimal import Decimal
>>>
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')
>>>
```

* The `Decimal` type is a class provided by the `decimal` module. The precision is inherited from the value used in its creation:

```python
>>> Decimal(1)
Decimal('1')
>>>
>>> Decimal('1.3')
Decimal('1.3')
>>> Decimal('1.30')
Decimal('1.30')
>>>
>>> Decimal(1.3) # Ops! Maximum float precision used
Decimal('1.3000000000000000444089209850062616169452667236328125')
>>>
>>>
```

* When used in operations, `Decimal` precision is promoted to the biggest `Decimal` involved in the operation:

```python
>>> Decimal('1.1') + Decimal('1.20') + Decimal('1.300')
Decimal('3.600')
>>>
```

* You can specify a global (for the calling Thread) the precision and extra digits resolution method through the `decimal` module `Context` object:

```python
>>> import decimal
>>>
>>> decimal.getcontext().prec = 2
>>>
>>> decimal.Decimal(1) / decimal.Decimal(7)
Decimal('0.14')
>>>
>>> decimal.getcontext().prec = 4
>>>
>>> decimal.Decimal(1) / decimal.Decimal(7)
Decimal('0.1429')
>>>
>>>
>>> decimal.getcontext().prec = 2
>>>
>>> decimal.Decimal(1) / decimal.Decimal(7)
Decimal('0.14')
>>>
```

* Lastly, you can override the global precision using `decimal.localcontext()` and the `with` statement:

```python
>>> import decimal
>>>
>>> decimal.getcontext().prec = 3
>>>
>>> decimal.Decimal(1) / decimal.Decimal(7)
Decimal('0.143')
>>>
>>> with decimal.localcontext() as ctx:
...     ctx.prec = 6
...     print( decimal.Decimal(1) / decimal.Decimal(7) )
...
0.142857
>>>
```

### Fractions

* Fractions represent rational numbers, which have a numerator and a denominator.
Avoiding the conversion to a decimal (float) result, thus avoiding the imprecision.

* Its use is very similar to `decimal.Decimal`, also being imported from a module `fractions`.

> Fractions are simplified when created.

* Basic usage:

```python
>>> from fractions import Fraction
>>>
>>> x = Fraction(1, 3)
>>> y = Fraction(4, 6) # will be simplified
>>>
>>> x
Fraction(1, 3)
>>> y
Fraction(2, 3)
>>>
>>> # Now, we can use them in mathematical operations
>>> x + y
Fraction(1, 1)
>>>
>>> x - y
Fraction(-1, 3)
>>>
>>> x * y
Fraction(2, 9)
>>>
>>> x / y
Fraction(1, 2)
>>>

>>> # Fractions can be created from floating point number STRINGS
>>>
>>> Fraction('1.34')
Fraction(67, 50)
>>>
>>> Fraction('0.25')
Fraction(1, 4)
>>>
```

* Conversions between `Fractions` and `floats` are possible:

```python
>>> v = 2.5
>>> v.as_integer_ratio() # get a possible numerator and denominator tuple for a float value
(5, 2)
>>>
>>> # Use the ratio to create a fraction
>>> frac = Fraction(* v.as_integer_ratio() ) # * unpacks a tuple as positional args
>>> frac
Fraction(5, 2)
>>>
>>> # Convert frac back to float
>>> float(frac)
2.5
>>>
>>> # And, to create a Fraction directly from float
>>> Fraction.from_float(2.5)
Fraction(5, 2)
>>>
>>> Fraction(2.5)
Fraction(5, 2)
>>>
>>> Fraction('2.5')
Fraction(5, 2)
>>>
```

* If you use a `Fraction` with a `float` in an expression, the result is a `float`. Else, always a `Fraction`:

```python
>>> f = Fraction(3, 4)
>>> f
Fraction(3, 4)
>>>
>>> f + 1
Fraction(7, 4)
>>>
>>> f + 1.5
2.25
>>>
>>> f * f
Fraction(9, 16)
>>>
```

* To handle imprecise rations, use `limit_denominator()`:

```python
>>> # Sometimes, the integer ratio is unprecise
>>> fl = 4.0 / 3.0
>>> fl
1.3333333333333333
>>>
>>> fr = Fraction(*fl.as_integer_ratio())
>>> fr
Fraction(6004799503160661, 4503599627370496)
>>>
>>> fr.limit_denominator(10) # round the fraction to this denominator or lower, if simplifiable
Fraction(4, 3)
>>>
```

### Sets

* Collection of **unique** and **immutable** objects that support set theory operations.

* Sets are **mutable** but can only hold **immutable** objects:

```python
>>> s = {1, 'b', [4, 5, 6]}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-9527d1eb6911> in <module>
----> 1 s = {1, 'b', [4, 5, 6]}

TypeError: unhashable type: 'list'
>>>
```

* Thus, a `set` can not contain another `set`:

```python
>>> sa = {1, 2, 3}
>>> sb = {sa, 4, 5, 6} # Ops! Sets are mutable!
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-39f2d0362c71> in <module>
----> 1 sb = {sa, 4, 5, 6} # Ops! Sets are mutable!

TypeError: unhashable type: 'set'
>>>

```

* Old way to create a `set`:

```python
>>> x = set('abcde')
>>> y = set('bdxyz')
>>>
>>> x, y
({'a', 'b', 'c', 'd', 'e'}, {'b', 'd', 'x', 'y', 'z'})
>>>
>>> x - y # difference
{'a', 'c', 'e'}
>>>
>>> x | y # union
{'a', 'b', 'c', 'd', 'e', 'x', 'y', 'z'}
>>>
>>> x & y # intersection
{'b', 'd'}
>>>
>>> x ^y  # symmetric difference (XOR)
{'a', 'c', 'e', 'x', 'y', 'z'}
>>>
>>> x > y, x < y # superset, subset
(False, False)
>>>
```

* You can test membership in a set using `in`:

```python
>>> x = set('abcde')
>>>
>>> x
{'a', 'b', 'c', 'd', 'e'}
>>>
>>> 'z' in x
False
>>>
>>> 'e' in x
True
>>>
```

* Set operators produce **new** sets. Each operator has a correspondent `method`. Sets also provides some method to change it in-place:

```python
>>> x = set('abcde')
>>> y = set('bdxyz')
>>>
>>> x, y
({'a', 'b', 'c', 'd', 'e'}, {'b', 'd', 'x', 'y', 'z'})
>>>
>>> z = x.intersection(y) # same as z = x & y
>>>
>>> z
{'b', 'd'}
>>>
>>> z.update(set(['k', 'l'])) # in-place intersection
>>> z
{'b', 'd', 'k', 'l'}
>>>
>>> z.add('z') # add one item
>>> z
{'b', 'd', 'k', 'l', 'z'}
>>>
>>> z.remove('z') # remove an item by value
>>> z
{'b', 'd', 'k', 'l'}
>>>
```

* `Sets` are sequences, then you can iterate over them, count - using `len()`, apply in comprehensions:

```python
>>> x = set('abcde')
>>>
>>> for letter in x: print(letter)
e
a
c
d
b
>>>
>>> len(x)
5
>>>
>>>
```

* The operators require both sides to bet sets. But, the set methods can receive any kind of iterable:

```python
>>> x = set('abcde')
>>>
>>> x
{'a', 'b', 'c', 'd', 'e'}
>>>
>>> x.intersection(["a", "z"])
{'a'}
>>>
>>> x
{'a', 'b', 'c', 'd', 'e'}
>>>
```

* Sets have a literal syntax also:

```python
>>> a = {1, 2, 3, 4}
>>> b = set([1, 2, 3, 4])
>>>
>>> a
{1, 2, 3, 4}
>>> b
{1, 2, 3, 4}
>>>
```

* Sets are close cousins of dictionary keys. They are unique, unordered and immutable.
Its so true that dictionary `.keys()` return a `view` object that supports many set operations.

* Empty sets, however, should be created using the `set()` constructor:

```python
>>> emp = set()
>>> emp
set()
>>>
```

> Note that an empty pair of curly braces `{}` produces an empty dictionary:

```python
>>> emp2 = {}
>>> emp2
{}
>>> type( emp2 )
dict
>>>
```

* `set()` is the best way to convert sequences into sets:

```python
>>> set( [1, 2, 3] )
{1, 2, 3}
>>> set( (1, 2, 3) )
{1, 2, 3}
>>>
```

### Immutable constraints and frozen sets

* Remember: `set` can only contain immutable types. So, you can't add `lists`, `dictionaries` or other `sets`:

```python
>>> s = set()
>>>
>>> s.add([1, 2, 3])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-14-66452cf70b8f> in <module>
----> 1 s.add([1, 2, 3])

TypeError: unhashable type: 'list'
>>>
>>> s.add({"a": 1, "b": 2, "c": 3})
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-2791967cf8f1> in <module>
----> 1 s.add({"a": 1, "b": 2, "c": 3})

TypeError: unhashable type: 'dict'
>>>
>>> s.add({1, 2, 3})
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-2b7b42142396> in <module>
----> 1 s.add({1, 2, 3})

TypeError: unhashable type: 'set'
>>>
```

* Immutable types can be added, as `tuples`:

```python
>>> s = set()
>>>
>>> s.add( (1, 2, 3) )
>>> s
{(1, 2, 3)}
>>>
>>> s.add("a")
>>> s
{(1, 2, 3), 'a'}
>>>
```

* If you want an immutable `set`, use the `frozenset` variant:

```python
>>> fs = frozenset([1, 1, 2, 2, 3, 3])
>>> fs
frozenset({1, 2, 3})
>>>
>>> fs.add(4) # Ops!
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-24-debfc77a6c56> in <module>
----> 1 fs.add(4) # Ops!

AttributeError: 'frozenset' object has no attribute 'add'
>>>
>>> # frozenset can be present in other sets
>>> s = set()
>>> s.add(fs)
>>> s.add(1)
>>> s.add(2)
>>> s.add(3)
>>>
>>> s
{1, 2, 3, frozenset({1, 2, 3})}
>>>
```

* Sets can also be created from comprehensions:

```python
>>> {x * x for x in (1, 2, 3)}
{1, 4, 9}
>>> {letter.upper() for letter in 'spam'}
{'A', 'M', 'P', 'S'}
>>>
```

### Sets use cases

* Remove duplicates:

```python
>>> l = [1, 2, 1, 3, 4, 2, 2, 5]
>>>
>>> unique_l = set(l)
>>> unique_l
{1, 2, 3, 4, 5}
>>>
>>> unique_l_as_list = list(unique_l)
>>> unique_l_as_list
[1, 2, 3, 4, 5]
>>>
>>> sorted_unique_l_list = sorted(unique_l_as_list)
>>> sorted_unique_l_list
[1, 2, 3, 4, 5]
>>>
```

> Rememver: the sort of the elements can be lost during the `set` conversion, because `sets` are inherently unordered.

* Use set theory operations to find differences:

```python
>>> set([1, 3, 4]) - set([1, 2, 3, 5])
{4}
>>>
>>> set('abcdefgh') - set('abdefghij')
{'c'}
>>> set('abcdefgh') ^ set('abdefghij')
{'c', 'i', 'j'}
>>> set('abcdefgh') & set('abdefghij')
{'a', 'b', 'd', 'e', 'f', 'g', 'h'}
>>>
```

* Order-neutral equality tests. Just convert both sequences to set, as the order is not taken into account for sets comparisons.
The sets just need to be a subset of each other:

```python
>>> a = set([1, 2, 3, 4])
>>> b = set([3, 2, 1, 1, 4])
>>>
>>> a == b
True

>>> a.issubset(b)
True
>>> b.issubset(a)
True
>>>

>>> set('spam') == set('pams')
True
>>>
```

* You can use sets to hold "visited" items in sequences and avoid repetition.
Remember that lists, tuples, etc, require linear search, while `dicts` and `sets` use hash-based searchs, which are faster.

* An example:

```python
>>> engineers = {'bob', 'sue', 'ann', 'vic'}
>>> managers = {'tom', 'sue'}
>>>
>>> 'bob' in engineers
True
>>> engineers & managers # who is engineer and manager
{'sue'}
>>> engineers | managers # who is not both
{'ann', 'bob', 'sue', 'tom', 'vic'}
>>>
>>> engineers - managers # engineers who are not managers
{'ann', 'bob', 'vic'}
>>>
>>> managers - engineers # managers who are not engineers
{'tom'}
>>>
>>> engineers > managers # are all managers also engineers ? (superset)
False
>>> {'bob', 'sue'} < engineers # are both bob and sue engineers?
True
>>>
>>> managers ^ engineers # who is not in both!
{'ann', 'bob', 'tom', 'vic'}
>>>
>>> managers - engineers # all managers that are not engineers
{'tom'}
>>>
```

### Booleans

* In essence Python's boolean values `True` and `False` are just the integers `1` and `0` modified to print diferently:

```python
>>> True + True
2
>>>
>>> False - True
-1
>>> int(True)
1
>>> int(False)
0
>>> # bool() is a subclass of int
>>> issubclass(bool, int)
True
>>>
```

## Dynamic typing interlude

### Variables, objects and references

* Variables (*names*) are created when declared.

* Variables are simple links to objects, without inherent type information, which is tied to the object itself.

* Variables are agnostic. Can point to any kind of object and can be *relinked* over thei lifetime.

* Variables are replaced in expressions by the object they link to, thus they need to be assigned before use.
Referecing unassigned variables in Python generate an exception.

#### Distinguish name and objects

* A variable assignment like:

```python
>>> a = 3
>>>
```

Is handled by Python in 3 steps:

1. Create an object `3` in memory;
2. Create a variable `a`, if non existent;
3. Link the variable `a` to the `3` object;

* Variables and objects are stored in different parts of memory.

* Variables always link to objects (**references**), and **never** to other variables.

* But objects can contain links to other, intrisic, objects (e.g. list containing another list).

* The links between variables and objects (references) are implemented as pointes in Python. Then, whenever a variable is used in an expression, its pointer is automatically followed by the Python interpreter and the pointed object returned.

* In simpler english:

    * Variables are entries in a table, with space for links to objects;

    * Objects are memory spaces with data and code.

    * References are automatically followed pointers from variables to objects.

#### Types Live with Objects, Not Variables

* Objects are memory spaces with its data, a reference counter (for gc) and a *type designator* field, to store the object type.

* Look the following code:

```python
>>> a = 1
>>> a = 'spam'
>>> a = 3.14
>>>
```

Before saying that the type of the variable `a` has changed, remember that variables have **no** type in Python. The type belongs to the object.
What really happens is that the **name** `a` is reassigned to new objects.

#### Objects are garbage collected

* Python objects keep a reference counter, when this number reachs zero (no more references to it in the code), the interpreter garbage collects the objects, freeing the memory. Example:

```python
>>> x = 42
>>> x = 'spam' # 42 is reclaimed
>>> x = 3.14   # 'spam' is reclaimed
>>> x = [1, 2, 3] # 3.14 is reclaimed
>>>
```

### Shared References

> Note: `id(object)` returns the object address in the memory.

* Example:

```python
>>> a = 42
>>> b = a   # a is replaced by "42", remember?
>>>
>>> id(a)
94683459779616
>>> id(b)
94683459779616
>>>
```

In the preceding code example, the `a` variable references an `int` object with value of `42`.

Then, we create a new variable `b` and assign it to the `a` variable.
But, during this assignment the `a` variable is replaced by the object it refers to, `42`. Thus, both `a` and `b` reference the same object, `42`.

* Note that variables are never related. They can point to the same object as a coincidence, but changing one to reference a new object does not affect the other:

```python
>>> a = 42
>>> b = a
>>> a = 'spam'
>>>
>>> a
'spam'
>>> b
42
>>>
```

### Shared References and in-place changes

* Some objects performe in-place change, for example, list assignments.

* Considerating that objects are always passed by references, these objects can be changed in-place and reflect in the other references:

```python
>>> l = [1, 2, 3]
>>> z = l
>>>
>>> l[0] = 3
>>>
>>> l
[3, 2, 3]
>>>
>>> z
[3, 2, 3]
>>>
>>> z[1] = 10
>>> z
[3, 10, 3]
>>>
>>> l
[3, 10, 3]
>>>
```

* But if you don´t want to share references, pass a copy. Example, with lists:

```python
>>> l = [1, 2, 3]
>>> z = l[:] # copy!
>>>
>>> l[0] = 3
>>> l
[3, 2, 3]
>>>
>>> z
[1, 2, 3]
>>>
>>> z[1] = 10
>>> z
[1, 10, 3]
>>>
>>> l
[3, 2, 3]
>>>
```

> To copy dicts and sets, use the object `.copy()` method. For lists, use the special slice syntax `[:]`.

> You also can copy passing the core object to its type constructor:

```python
>>> l = [1, 2, 3]
>>> z = list(l)
>>>
>>> l[0] = 3
>>> l
[3, 2, 3]
>>>
>>> z
[1, 2, 3]
>>>
>>> z[1] = 10
>>> z
[1, 10, 3]
>>>
>>> l
[3, 2, 3]
>>>
```

> And there is a generic `copy` module that can performe shallow copies or deepcopies (objects descedent structure is also copied):

```python
>>> import copy
>>>
>>> orig = [ [1], [2], [3] ]
>>>
>>> cp = copy.copy(orig)
>>> cp
[[1], [2], [3]]
>>>
>>>
>>> id( orig[0] )
139970774568320
>>>
>>> id( cp[0] )
139970774568320
>>>
>>>
>>> dcp = copy.deepcopy(orig)
>>>
>>> dcp
[[1], [2], [3]]
>>>
>>> id( orig[0] )
139970774568320
>>> id( dcp[0] )
139970774283712
>>>
```

### Shared References and Equality

* Python provides two ways to compare objects.

The first, compares the object data. If its equal in both (`==`):

```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>>
>>> a == b
True
>>>
```

The other (`is`) compare if both variables point to the same `memory address` (reference):

```python
>>> a = [1, 2, 3]
>>> b = a
>>>
>>> a is b
True
>>>
>>> id(a), id(b)
(139970775002048, 139970775002048)
>>>
```

```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>>
>>> a == b
True
>>>
>>> a is b
False
>>>
>>> id(a), id(b)
(139970774753216, 139970775003328)
>>>
```

### Dynamic Typing Is Everywhere

* Everything work by reference in Python. Variables are pointers (references) to objects.

* These variables, when used in expressions, are replaced by the object itself.

* If you assign a variable to another, the new variable will point to the object of the original variable also.

* A variable does not references another variable, never.

* `weakref` are references that dont prevent the object of being garbage collected. You can create them using the `weakref` module.

## String fundamentals

### Unicode: the short story

* Python unicode support:

    * `str` is an unicode text;
    * `bytes` is a binary data (remember: encode text is binary data also;
    * `bytearray` is a mutable `bytes`;
    * Files have two modes:
        * `text` (unicodes) and `binary`

### String literals

* Strings are immutable sequences

* There are multiple ways to create a string:

```python
>>> # Ways to create a string
>>> s1 = 'sp"am'
>>> s1
'sp"am'
>>>
>>> s2 = "sp'am"
>>> s2
"sp'am"
>>>
>>> s3 = '''
... multiple
... lines
... "spam"
... '''
>>> s3
'\nmultiple\nlines\n"spam"\n'
>>>
>>> s4 = """
... multiple
... lintes
... 'spam'
... """
>>> s4
"\nmultiple\nlintes\n'spam'\n"
>>>
>>> s5 = "s\tp\na\0m"
>>> s5
's\tp\na\x00m'
>>> print(s5)
s       p
am
>>>
>>> s6 = r"c:\windows\test.spm"
>>> s6
'c:\\windows\\test.spm'
>>>
>>> s7 = b"sp\x01am"
>>> s7
b'sp\x01am'
>>> print(s7)
b'sp\x01am'
>>>
>>> print(s7.decode())
spam
>>>
>>>
```

* Single quotes and double quotes have the same effect, but using one allows you to embed the other inside the string without escaping:

```python
>>> "knight's"
"knight's"
>>> 'knight"s'
'knight"s'
>>>
```

* Strings put side by side are automatically concatenated. But avoid it, explictly use the `+` operator:

```python
>>> "hello" " " "world"
'hello world'
>>> ("hello"
... " "
... "world")
'hello world'
>>>
```

#### Escape sequences and special characters

* You can escape some special characters inside strings, avoiding their special mining in Python syntax:

```python
>>> 'knight\'s'
"knight's"
>>> "knight\"s"
'knight"s'
>>>
```

* Backslashes allow the insertion of special characters in strings.

* The pair backslash and a char (e.g. `\t`) is replaced by a single char in the resulting string, which has the binary value specified by the escape sequence. For example, the following string results in a five-character string length:

```python
>>> s = 'a\nb\tc'
>>> s
'a\nb\tc'
>>> print(s)
a
b       c
>>> len(s)
5
>>>
```

* These escape sequences are usually only interpreted by the `print` function. The default, `repr()`, shell feedback does not interpret it.

```python
>>> s = "a\nb\tc"
>>> repr(s)
"'a\\nb\\tc'"
>>> print(s)
a
b       c
>>> s
'a\nb\tc'
>>>
>>>
>>> print(repr(s))
'a\nb\tc'
>>>
```

* Escape sequences are read as a single char:

```python
>>> s = "a\nb\tc"
>>>
>>> s
'a\nb\tc'
>>>
>>> print(s)
a
b       c
>>>
>>> len(s)
5
>>>
```

#### Unicode and bytes

* For the tenth time, bytes have no meaning or relation in the unicode world. The ASCII encoding that coincidently represents each char with a single byte. Besides that, bytes have no direct relation whatsoever with unicode characters.

* Strings (`str` in Python 3 and `unicode` in Python 2) are sequences of **code points**.

#### List of escape sequences

```python
>>> # newline
>>> print("a\nb")
a
b
>>>
>>> # backslash
>>> print("\\test")
\test
>>>
>>> # single quote
>>> print('hello \'world\'')
hello 'world'
>>>
>>> # double quote
>>> print("hello \"world\"")
hello "world"
>>>
>>> # bell
>>> print("bell: \a")
bell:
>>>
>>> # backspace
>>> print("a \b x")
a x
>>> print("a \b\b x")
 x
>>> print("a \bx")
ax
>>> # formfeed
>>> print("a\fb")
a
 b
>>> # horizontal tab
>>> print("a\tb")
a       b
>>> # vertical tab
>>> print("a\vb")
a
 b
>>> # character with hex value (two digits)
>>> print("\x19")

>>> print("\x99")

>>> print("\xAF")
¯
>>> print("\xAE")
®
>>>
>>> # character with octal value (up to three digits)
>>> print("\123")
S
>>>
>>> # null: binary 0 character (string end in C, but no effect in Python)
>>> print("a\0b")
ab
>>>
>>> # unicode char by id
>>> print("\N{asterisk}")
*
>>>
>>> # unicode character with 16 hex value (4 digits)
>>> print("\u24C2")
Ⓜ
>>>
>>> # unicode character with 32 hex value (8 digits)
>>> print("\U0001F601")
😁
>>>
>>> # if the escape sequence is not recognized, python just keeps the backslash and the other char in th
... e resulting string
>>>
>>> print("c:\python\way")
c:\python\way
>>> repr("c:\python\way") # represented as \\
"'c:\\\\python\\\\way'"
>>>
>>> print(repr("c:\python\way")) # represented as \\
'c:\\python\\way'
>>>
>>> len("c:\python\way")
13
>>>
```

#### Avoid escape sequences using `r`aw strings

* `r`aw strings avoid escape sequences interpretation. Useful for file paths, for example:

```python
>>> file_path = r"c:\new\path\for\the\file.txt"
>>> file_path
'c:\\new\\path\\for\\the\\file.txt'
>>>
>>> # you can avoid the "r" prefix escaping the backslashs
>>>
>>> file_path = "c:\\new\\path\\for\\the\\file.txt"
>>> file_path
'c:\\new\\path\\for\\the\\file.txt'
>>> print(file_path)
c:\new\path\for\the\file.txt
>>>
```

> Again, remember that default shell output uses the `repr()` representation, which tries to mimic the literal code representation of the object. To have a friendly output, you need to use `print()`:

```python
>>> file_path = r"c:\new\path\for\the\file.txt"
>>>
>>> # repr, code-like representation
>>> file_path
'c:\\new\\path\\for\\the\\file.txt'
>>>
>>> # friendly, using print
>>> print(file_path)
c:\new\path\for\the\file.txt
>>>
```

> In Python you can use forward slashes for file paths in both windows and unix environments:

```python
>>> # would work the same as: open(r"c:\windows\system32\hosts")
>>> open("c:/windows/system32/hosts")
```

#### Triple quotes for multiline strings

* You start and end with thee (single or double) quotes. You can embed escape sequences or single / double quotations. The strings ends only when another three are found:

```python
>>> a = """
... Roses are red
... Violets are blue
... "Spam"
... 'Eggs'
... """
>>> a
'\nRoses are red\nViolets are blue\n"Spam"\n\'Eggs\'\n'
>>> print(a)

Roses are red
Violets are blue
"Spam"
'Eggs'

>>>
```

* Spaces are taken into account:

```python
>>> b = """
... Roses are red
...       Violets are blue
... "Spam"
...    'Eggs'
... """
>>>
>>> b
'\nRoses are red\n      Violets are blue\n"Spam"\n   \'Eggs\'\n'
>>>
>>> print(b)

Roses are red
      Violets are blue
"Spam"
   'Eggs'

>>>
```

* Triple quotes are also used for commenting code. But, avoid this if you can.


### Strings in Action

#### Basic operations

* Concatenation and repetition:

```python
>>> # Concatenate
>>> s = "a" + "B"
>>> s
'aB'
>>>
>>> # Concatenate side by side
>>> s = "a" "B"
>>> s
'aB'
>>>
>>> # Repetition
>>> s = "a" * 4
>>> s
'aaaa
```

```python
>>> print("-" * 80, "\n message \n", "-" * 80)
--------------------------------------------------------------------------------
 message
--------------------------------------------------------------------------------
>>>
```

* Iteration `for` and membership test using `in`

```python
>>> for letter in "spam":
...     print(letter * 2)
...
ss
pp
aa
mm
>>>
>>> "s" in "spam"
True
>>>
>>> "pam" in "spam"
True
>>>
```

#### Indexing and slicing

* Indexing allows access to characters in a string by offset. Starting with `0` to `len(string) - 1`:

```python
>>> s = "spam"
>>>
>>> s[0]
's'
>>> s[1]
'p'
>>> s[2]
'a'
>>> s[3]
'm'
>>>
```

* You can use negative offsets, which are added to the `len(string)`, generating a positive offset:

```python
>>> s = "spam"
>>>
>>> s[-1]
'm'
>>> s[len(s) - 1]
'm'
>>>
>>> s[-2]
'a'
>>> s[len(s) - 2]
'a'
>>>
>>> s[-3]
'p'
>>> s[len(s) - 3]
'p'
>>>
>>>
```

* Slices permit the extraction of subsequences of characters:

```python
>>> s = "spam"
>>>
>>> s[1:3]
'pa'
>>> s[1:] # the second position defaults to len(s)
'pam'
>>> s[1:len(s)]
'pam'
>>>
>>> s[:-1] # the first position defaults to 0
'spa'
>>>
>>> # remember that the last position is not included in the slice
>>> s[0:3]
'spa'
>>> s[0:4]
'spam'
>>>
```

* In slices `[lower:upper]`, `lower` is inclusive but `upper` is noninclusive.

```python
>>> s = "spam"
>>> s[0:3]
'spa'
>>> s[0:4]
'spam'
>>>
```

* In slices `[lower:upper]`, if you omit `lower` it defaults to `zero`, else, if you omit `upper`, it defaults to the length of the sequence being sliced.

```python
>>> s = "spam"
>>>
>>> s[0:]
'spam'
>>> s[:len(s)]
'spam'
>>> s[:]
'spam'
>>>
```

> Slices always return **new** objects with the fetched items. So its a common way to make copies of sequences `seq[:]`:

```python
>>> a = [1, 2, 3]
>>> b = a[:]
>>>
>>> b[1] = 10
>>>
>>> a
[1, 2, 3]
>>> b
[1, 10, 3]
>>>
```

* Slices also support a third parameter know as step, that increments the index for each interation:

```python
>>> s = "hello world"
>>>
>>> s[::2] # indexes: 0, ..., 2, ..., 4...
'hlowrd'
>>>
>>> s[::-1] # can be negative also. indexes: 0, -1, -2, -3...
'dlrow olleh'
>>>
>>> s[5:1:-1] # you are, virtually, reversing the meaning of the lower and upper bound limits
' oll'
>>>
```

* Slice literals are just a sugar syntax for indexing with slice objects:

```python
>>> s = "hello world"
>>> # Slice syntax is just sugar syntax for slice objects:
>>> s[slice(None, None, 2)]
'hlowrd'
>>> s[slice(None, None, -1)]
'dlrow olleh'
>>> s[slice(5, 1, -1)]
' oll'
>>>
```

* One very common use of slices is to get the arguments passed for a script:

```python
import sys
print(sys.argv[1:]) # 0 is the script name
```

* Another use is to drop the very last char of a string, which can be made:

```python
>>> s = "hello worldX"
>>> print(s)
hello worldX
>>>
>>> print(s[:-1])
hello world
>>>
```

> If you just want to remove newlines and other "space" chars, use the `.rstrip()` method of the `str` type, as slicing like the last example can cut off important chars.

#### String conversion tools

* To convert a string to `int`, use `int()`:

```python
>>> int("42") + int("-10")
32
>>>
```

* To convert any object to a human-friendly string representation, use `str()`:

```python
>>> str(3.14111222229213121319232139111)
'3.141112222292131'
>>>
>>>
```

* To get a literal code representation, use `repr()`:

```python
>>> s = """
... spam
... eggs
... bacon
...     test
... """
>>> repr(s)
"'\\nspam\\neggs\\nbacon\\n    test\\n'"
>>>
```

* To convert to float use `float`:

```python
>>> float("3.1441111223111")
3.1441111223111
>>>
```

* `float`s can be converted to string using `str` also:

```python
>>> str(3.1411131)
'3.1411131'
>>>
```

* You can, but should not, convert strings to numeric types using the `eval()` builtin function:

```python
>>> eval("3.14") + eval("12")
15.14
>>>
```

> Avoid!

#### Character code conversions

* Convert a char to its numeric value using `ord()`:

```python
>>> ord("a"), ord("b"), ord("c")
(97, 98, 99)
>>>
```

* To convert a numeric value to a char, use `chr()`:

```python
>>> chr(97), chr(98), chr(99)
('a', 'b', 'c')
>>>
```

> These numbers represent the underlying unicode codepoint. In Python 3, usually the `utf-8`.

#### Changing strings 1

* Strings are immutable. To "change" a string you have to create a new one, using concatenation, slicing, etc:

```python
>>> s = "spam"
>>> s = "spam" + " " + "SPAM!"
>>> s
'spam SPAM!'
>>>

>>> s = "hello world"
>>> s = s[-1:-6:-1] + s[:5]
>>> s
'dlrowhello'
>>>
```

* Strings provide some methods that change (really, create new strings):

```python
>>> s = "Hello World"
>>> # Create new string. Does not change in-place.
>>>
>>> s.replace("World", "Bakery")
'Hello Bakery'
>>>
>>> # Original, unchanged
>>> s
'Hello World'
>>>
>>> s = s.replace("World", "Stadium")
>>> s
'Hello Stadium'
>>>
```

* Formatting also creates new strings:

```python
>>> a = "Hello"
>>> b = "World"
>>>
>>> print("{} {}!!!".format(b, a))
World Hello!!!
>>>
```

### String methods

* Replacing and finding substrings:

```python
>>> # Replace substring
>>> s = "spammy"
>>> s = s.replace("mm", "xx")
>>> s
'spaxxy'
>>>
>>> s = s.replace("xx", "zXzXzXzXzXzXzXzZx")
>>> s
'spazXzXzXzXzXzXzXzZxy'
>>>
>>> # Search the offset (index) where a substring starts in the main string
>>> s = "hello world"
>>> s.find("world")
6
>>> where = s.find("world")
>>> s[where:]
'world'
>>>
>>> # find returns -1 if not found
>>> s.find("XXX")
-1
>>>
```

> Caution: `find()` has a semantic close to the `in` operator, but the fact it results `-1` when not found can lead to wrong results:

```python
>>> s = "spam"
>>>
>>> bool( "p" in s )
True
>>> bool( s.find("p") )
True
>>>
>>> bool( "x" in s )
False
>>> bool( s.find("x") ) # Ops!
True
>>>
>>> s.find("x")
-1
>>> bool(-1)
True
>>>
```

* Python's `replace()` replaces all occurrences, but you can limit it with a third argument:

```python
>>> s = "hello world"
>>>
>>> s.replace("l", "x")
'hexxo worxd'
>>>
>>> s.replace("l", "x", 1) # only first
'hexlo world'
>>>
>>> s.replace("l", "x", 2) # only first and second
'hexxo world'
>>>
```

* If you want to mimic a `bytearray` with an unicode string, explode it into a `list`, apply the changes, then `join` it as a string again:

```python
>>> s = "hello world"
>>> s = list(s)
>>> s
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>>
>>> s[1] = 'i'
>>> s[5] = 'z'
>>>
>>> s
['h', 'i', 'l', 'l', 'o', 'z', 'w', 'o', 'r', 'l', 'd']
>>>
>>> s = "".join(s)
>>> s
'hillozworld'
>>>
```

* `spit([delimiter])`. the default `delimiter` is one or more `whitespace` chars:

```python
>>> s = "aaa bbb     ccc  ddd"
>>> s.split()
['aaa', 'bbb', 'ccc', 'ddd']
>>>
>>> s2 = "aaa, bbb, ccc, ddd"
>>> s2.split(",")
['aaa', ' bbb', ' ccc', ' ddd']
>>>
>>> s3 = "a->b->c"
>>> s3.split("->")
['a', 'b', 'c']
>>>
```

* Strip whitespace, convert case, check chars nature, check start or end:

```python
>>> line = "The knights who say Ni!\n"
>>> line.rstrip()
'The knights who say Ni!'
>>>
>>> line.upper()
'THE KNIGHTS WHO SAY NI!\n'
>>>
>>> line.lower()
'the knights who say ni!\n'
>>>
>>> line.isalpha() # all alphanumric?
False
>>>
>>> line.startswith("The")
True
>>> line.endswith("\n")
True
>>>
```

### String formating

* Python 3.6 introduced the awesome `f-strings`, which are strings with native support for interpolation. To create them, just prefix a string (single, double, or triple quotes) with an `f`:

```python
>>> name = "John"
>>> message = f"Hello! {name}"
>>> message
'Hello! John'
>>>
>>> name = "Doe"
>>> message # still the same!
'Hello! John'
>>>
```

> Note that the interpolation is done one time, when the line of code is interpreted, then it becomes a normal string.

* `f-strings` allow you to evaluate any valid Python expression:

```python
>>> print(f"{5 + 5}")
10
>>> name = "john"
>>>
>>> print(f"{name.upper()}") # functions can be called
JOHN
>>>
>>>
```

* `f-string` can be used in classes representations:

```python
>>> class Person:
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
...     def __str__(self):
...         return f"{self.name} is {self.age} years old"
...
>>> john = Person("John", 19)
>>> john
<__main__.Person at 0x7f338b328430>
>>> print(john)
John is 19 years old
>>>
```

* To display braces, use double braces:

```python
>>> print(f"{{name}}")
{name}
>>>
```

* To access dictionaries keys inside f-strings you have to use a different quotation:

```python
>>> data = {"name": "John", "age": 23}
>>> data
{'name': 'John', 'age': 23}
>>>
>>> print(f"{data['name']} is {data['age']} years old")
John is 23 years old
>>>
```

* Datetime format:

```python
>>> import datetime
>>>
>>> now = datetime.datetime.now()
>>>
>>> print(f"{now:%d/%m/%Y}")
28/02/2020
>>>
```

* Float precision:

```python
>>> val = 12.35678
>>>
>>> print(f"{val:.2f}")
12.36
>>> print(f"{val:.4f}")
12.3568
>>>
```

* Format width (with spaces or other char)

```python
>>> val = 3
>>>
>>> print(f"{val:10}") # 10 positions, filled with space
         3
>>> print(f"{val:010}") # 10 positions, filled with zero
0000000003
```

* By default, f-strings are left-justified (`<`). But you can right-justify `>` or center justify `^`:

```python
>>> print(f"{val:<10}") # 10 positions, filled with space, left justified
3
>>> print(f"{val:^10}") # 10 positions, filled with space, center justified
    3
>>> print(f"{val:>10}") # 10 positions, filled with space, right justified
         3
>>>
```

* You can format numbers under different notations:

```python
>>> num = 300
>>>
>>> print(f"Hexadecimal: {num:x}")
Hexadecimal: 12c
>>> print(f"Octal: {num:o}")
Octal: 454
>>> print(f"Binary: {num:b}")
Binary: 100101100
>>> print(f"Scientific: {num:e}")
Scientific: 3.000000e+02
>>>
```

## Lists and Dictionaries

### Lists

* Lists are arrays of object references, which Python fecths when accessed.

* When you assign to a data structure component or variable, a new reference to the same object in the right side is stored, unless you explictly require a copy.

* Ways to declare:

```python
>>> # empty
>>> l = []
>>>
>>> # literal
>>> l = [1, "a", 3.14]
>>> l
[1, 'a', 3.14]
>>>
>>> # nested
>>> x = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]
>>> x
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>>
```

#### Basic list operations

* Length, concatenation and repetition

```python
>>> # length
>>> len([1, 2, 3])
3
>>>
>>> # concatenation
>>> [1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
>>>
>>> # repetition
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>>
```

* Lists can be concatenated only with other lists

```python
>>> # lists can be concatenated only with other lists
>>> [1, 2, 3] + (1, 2, 3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-8-9812ea45e4bd> in <module>
----> 1 [1, 2, 3] + (1, 2, 3)

TypeError: can only concatenate list (not "tuple") to list
>>>
>>> [1, 2, 3] + "aloha"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-c24ae2a0b18d> in <module>
----> 1 [1, 2, 3] + "aloha"

TypeError: can only concatenate list (not "str") to list
>>>
```

* Membership and iteration:

```python
>>> 10 in [1, 2, 3]
False
>>>
>>> 3 in [1, 2, 3]
True
>>>
>>> for x in [1, 2, 3]:
...     print(x + 1)
...
...
2
3
4
>>>
```

* Comprehension and `map()`:

```python
>>> l = [c * 4 for c in 'spam']
>>> l
['ssss', 'pppp', 'aaaa', 'mmmm']
>>>
>>>
>>> list(map(abs, [-1, -2, -3]))
[1, 2, 3]
>>>
```

* Indexing, slicing and matrixes:

```python
>>> # Indexing
>>> l = [1, 'spam', 3.14]
>>> l[0]
1
>>> l[1]
'spam'
>>> l[2]
3.14
>>>
>>> # Slicing
>>> l[1:3]
['spam', 3.14]
>>>
>>> # Copy with slicing
>>> l_copy = l[:]
>>> l_copy
[1, 'spam', 3.14]
>>>
>>> l[0] = 10
>>> l
[10, 'spam', 3.14]
>>> l_copy
[1, 'spam', 3.14]
>>>
>>> # Matrixes
>>> l = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]
>>>
>>> l[0] # entire row
[1, 2, 3]
>>> l[0][1] # element
2
>>> l[0][2]
3
>>>
```

#### Changing lists in-place

* Lists are mutable. You can change their content, thus affecting all references to it.

```python
>>>
>>> l = [1, "spam", 3.14, [10, 20, 30]]
>>>
>>> # Change through indexing
>>> l[3] = 6.18
>>> l
[1, 'spam', 3.14, 6.18]
>>>
>>> # Change using slices
>>> l[1:] = [2, 3, 4, 5]
>>> l
[1, 2, 3, 4, 5]
>>>
```

* Slices assignments are really two operations. First, the selected indexes are deleted, then, the left side is inserted in the "empty space" (actually, in the first selected index and so on...). An example to help:

```python
>>> l = ["a", "b", "c", "d", "e"]
>>>
>>> l[0:2] = ["x", "y", "z"] # delete the indexes 0, 1 (remember 2 is not included) and insert x, y, zst
... arting in index 0...
>>> l
['x', 'y', 'z', 'c', 'd', 'e']
>>>
```

> Note that the left side can have more or less elements then the total of indexes selected.

* Given this property, you can performe insertions (using an empty slice) or deletions:

```python
>>> l = ["a", "b", "c"]
>>>
>>> l[0:1] = ["x", "y", "z"] # replacement
>>> l
['x', 'y', 'z', 'b', 'c']
>>>
>>> l = ["a", "b", "c"]
>>> l[0:0] = ["x", "y", "z"] # insertion. 0:0 is empty, so items are inserted in position 0 and so on
>>> l
['x', 'y', 'z', 'a', 'b', 'c']
>>>
>>> l = ["a", "b", "c"]
>>> l[1:] = [] # deletes, but inserts nothing
>>> l
['a']
>>>
```

* You can clear list using this syntax:

```python
>>> l = ["a", "b", "c"]
>>>
>>> l[:] = []
>>> l
[]
>>>
```

* Or extend:

```python
>>> l = ["a", "b", "c"]
>>>
>>> l[-1:] = ["d", "e", "f"]
>>> l
['a', 'b', 'd', 'e', 'f']
>>>
>>> l[-1:] = ["g", "h", "i"]
>>> l
['a', 'b', 'd', 'e', 'g', 'h', 'i']
>>>
```

* You should use for extension the more mnemonic `.extend()` method:

```python
>>> l = [1, 2, 3]
>>>
>>> l.extend([4, 5, 6])
>>> l
[1, 2, 3, 4, 5, 6]
>>>
```

* Appending, in-place, to a list with `.append()`:

```python
>>> l = [1, 2, 3]
>>> l.append(4)
>>> l
[1, 2, 3, 4]
>>>
>>> # Caution! append acts in-place, but + (concatenation) produces a new list
>>> l + [5]
[1, 2, 3, 4, 5]
>>> l
[1, 2, 3, 4]
>>>
```

* Sorting in-place with the `.sort()` method:

```python
>>> # In-place, default ascending sort
>>> l = [4, 1, 3, 2, 7, 0]
>>>
>>> l.sort() # in-place, ascending
>>> l
[0, 1, 2, 3, 4, 7]
>>>
>>> # Use reverse=True, to sort descending
>>> l = [4, 1, 3, 2, 7, 0]
>>>
>>> l.sort(reverse=True) # in-place, descending
>>> l
[7, 4, 3, 2, 1, 0]
>>>
>>> # Use key= to specify a function to be applied to elements before comparisons
>>> l = ["Abc", "bAc", "CdA"]
>>> l.sort()
>>> l
['Abc', 'CdA', 'bAc']
>>>
>>> # specify a function to be applied to each element before comparison
>>> l = ["Abc", "bAc", "CdA"]
>>> l.sort(key=str.lower)
>>> l
['Abc', 'bAc', 'CdA']
>>>
```

* You cant sort mixed types:

```python
>>> l = [1, "a", 3.14]
>>> l.sort()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-71-fb07ac7c73ab> in <module>
----> 1 l.sort()

TypeError: '<' not supported between instances of 'str' and 'int'
>>>
```

* You can also sort using the builtin `sorted()` function, which returns a new object instead of modifying the source object in place. It accepts the same arguments as the `.sort()` method:

```python
>>> l = [4, 1, 3, 2, 7, 0]
>>>
>>> sorted(l) # new list, sorted ascending
[0, 1, 2, 3, 4, 7]
>>>
>>> l
[4, 1, 3, 2, 7, 0]
>>>
>>> sorted(l, reverse=True) # new list, sorted descending
[7, 4, 3, 2, 1, 0]
>>>
>>> l
[4, 1, 3, 2, 7, 0]
>>>
>>> l = ["Abc", "bAc", "CdA"]
>>>
>>> sorted(l) # new list, sorted ascending
['Abc', 'CdA', 'bAc']
>>>
>>> sorted(l, key=str.lower) # new list sorted ascending with a key function defined
['Abc', 'bAc', 'CdA']
>>>
```

> The function used as `key=` in the `.sort()` method or the `sorted()` builtin should accept one and only one argument.

* Mind that the methods that perform in-place changes don't return the changed list as value, but `None`:

```python
>>> l = [4, 1, 3, 2, 7, 0]
>>>
>>> l = l.sort() # Ops!
>>> l
>>> print(l)
None
>>>
>>> l = [4, 1, 3, 2, 7, 0]
>>>
>>> l = l.append(3)
>>> l
>>> print(l)
None
>>>
```

* Mind 2: the `key=` function returned value is used in the comparison, but the list original value remains unchanged:

```python
>>> l = ["Abc", "bAc", "CdA"]
>>> sorted(l, key=str.lower) # l values remain unchanged
['Abc', 'bAc', 'CdA']
>>>
>>> l = ["Abc", "bAc", "CdA"]
>>> sorted([c.lower() for c in l]) # change l values before sorting, different results
['abc', 'bac', 'cda']
```

#### Other list methods

* `reversed()` builtin, that reverses the list order, returning a new list. Caution: it does not orders the list, just reverts.

```python
>>> l = [4, 1, 3, 2, 7, 0]
>>>
>>> list(reversed(l))
[0, 7, 2, 3, 1, 4]
>>>
>>>
```

* `.reverse()` method that inverts the elements of the list. Caution, it does not perform a sorting:

```python
>>> l = [4, 1, 3, 2, 7, 0]
>>>
>>> l.reverse()
>>>
>>> l
[0, 7, 2, 3, 1, 4]
>>>
```

* `.extend()` to grow the list in-place:

```python
>>> l = [1, 2, 3]
>>> l.extend([4, 5, 6])
>>> l
[1, 2, 3, 4, 5, 6]
>>>
```

* `.pop()` removes the last element of the list and returns:

```python
>>> l = [1, 2, 3]
>>> last = l.pop()
>>>
>>> last
3
>>>
>>> l
[1, 2]
>>>
```

* You can implement a simple `LIFO` (`last in first out`) stack using append and pop:

```python
>>> l = []
>>> l.append(1)
>>> l.append(2)
>>>
>>> l
[1, 2]
>>>
>>> l.pop()
2
>>>
>>> l
[1]
>>>
```

* `.pop()` accepts an offset as argument, which is, by default, `-1`:

```python
>>> l = ["a", "b", "c"]
>>> l.pop(0) # pops first element
'a'
>>>
>>> l
['b', 'c']
>>>
```

`.pop(0)` can be used to implement a `FIFO stack`.

* `.remove(value)` remove the first occurence of `value`:

```python
>>> l = [1, 2, 1, 2, 3]
>>> l.remove(1)
>>> l
[2, 1, 2, 3]
>>>
>>> l.remove(99) # ops!
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-121-fe5f094d900d> in <module>
----> 1 l.remove(99) # ops!

ValueError: list.remove(x): x not in list
>>>
```

* `.insert(position, obj)` insert `obj` into `position` pushing the other elements to the right:

```python
>>> l = [1, 2, 3]
>>>
>>> l.insert(0, 99)
>>> l
[99, 1, 2, 3]
>>>
```

* `.index(obj)` find the offset/index of the first occurrence of `obj`:

```python
>>> l = ["a", "b", "c", "a", "b", "c"]
>>>
>>> l.index("c")
2
>>>
>>> l.index("x") # Ops!
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-132-2f8bbb30c658> in <module>
----> 1 l.index("x") # Ops!

ValueError: 'x' is not in list
>>>
```

* `.count(obj)` count occurrences of `obj`:

```python
>>> l = ["s", "p", "a", "a", "m"]
>>>
>>> l.count("s")
1
>>> l.count("a")
2
>>>
```

* `del` elements:

```python
>>> l = ["spam", "eggs", "bacon"]
>>>
>>> # del by index
>>>
>>> del l[1]
>>> l
['spam', 'bacon']
>>>
>>> # del by slice
>>> l = ["spam", "eggs", "bacon"]
>>>
>>> del l[1:]
>>> l
['spam']
>>>
```

> Remember that a slice assigment with an empty sequence is, in practice, a deletion. But if you assign an empty list to an index, you are filling it with an empty list:

```python
>>> l = ["spam", "eggs", "bacon"]
>>>
>>> l[1:] = [] # deletion! slice assignment
>>> l
['spam']
>>>
>>> l = ["spam", "eggs", "bacon"]
>>>
>>> l[0] = [] # attribution
>>> l
[[], 'eggs', 'bacon']
>>>
```

### Dictionaries

* Collections of objects referenced by `keys`

* `keys` must be immutable, hashable, objects

* Dicts are unordered

* Can grown or shrink under demand. The hosted objects can be of any type. The immutable, hashable, restriction applys only for the `keys`.

* Ways to declare:

```python
>>> d = {"name": "John", "age": 40} # simple dict
>>> d
{'name': 'John', 'age': 40}
>>>
>>> d = {"name": "John", "data": {"age": 40, "color": "blue"}} # nesting
>>> d
{'name': 'John', 'data': {'age': 40, 'color': 'blue'}}
>>>
>>> d = dict(name="John", age=40) # alternative constructor
>>> d
{'name': 'John', 'age': 40}
>>>
>>> d = dict([("name", "john"), ("age", 40)]) # list of tuples constructor
>>> d
{'name': 'john', 'age': 40}
>>>
>>> d = dict(zip(["name", "age"], ["john", 40])) # using zip()
>>> d
{'name': 'john', 'age': 40}
>>>
>>> d = dict.fromkeys(["name", "age"]) # start a dict from keys without values
>>> d
{'name': None, 'age': None}
>>>
>>>
```

* Indexing:

```python
>>> d = {"name": "John", "data": {"age": 40, "color": "blue"}}
>>>
>>> # indexing
>>> d["name"]
'John'
>>>
>>> # nesting indexing
>>> d["data"]["age"]
40
>>>
```

* Check for membership using `in`:

```python
>>> d = {"name": "John", "data": {"age": 40, "color": "blue"}}
>>>
>>> "name" in d
True
>>>
>>> "age" in d # it dosent check inner dicts! caution
False
>>>
```

* Number of keys `len(dict)`:

```python
>>> d = {"name": "John", "age": 40}
>>>
>>> len(d)
2
>>>
```

#### Dictionaries in action

* Return `.keys()`:

```python
>>> d = {"name": "John", "age": 40}
>>>
>>> list(d.keys()) # .keys() returns an iterator, thus list() is necessary
['name', 'age']
>>>
```

```python
>>> # .keys() is implicityly called when a dict is converted or iterated
>>>
>>> d = {"name": "John", "age": 40}
>>>
>>> list(d)
['name', 'age']
>>>
>>> for key in d: print(key)
name
age
>>>
```

* Creating new keys, updating and deleting:

```python
>>> d = {"name": "John", "data": {"age": 40, "color": "blue"}} # nesting
>>> d
>>> d = {}
>>>
>>> # creating
>>> d["name"] = "John" # just assign
>>>
>>> d
{'name': 'John'}
>>>
>>> # updating
>>> d["name"] = "Paul" # simple assignment also
>>>
>>> d
{'name': 'Paul'}
>>>
>>> # deleting
>>> del d["name"]
>>> d
{}
>>>
>>> # caution when deleting unexisting keys
>>> del d["age"]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-204-c279bbd0f0e6> in <module>
----> 1 del d["age"]

KeyError: 'age'
>>>
```

You can use any object as values. There is no restriction, even when updating:

```python
>>> d = {"value": 5}
>>>
>>> d
{'value': 5}
>>>
>>> d["value"] = "John Doe"
>>> d
{'value': 'John Doe'}
>>>
>>> d["value"] = 3.14
>>> d
{'value': 3.14}
>>>
```

* Listing and iterating over values:

```python
>>> d = {"name": "John", "age": 40}
>>>
>>> d.values()
dict_values(['John', 40])
>>>
>>> list(d.values())
['John', 40]
>>>
>>> for value in d.values(): print(value) # no list necessary
John
40
>>>
>>>
```

* Listing and iterating over pairs of key and value:

```python
>>> d = {"name": "John", "age": 40}
>>>
>>> d.items()
dict_items([('name', 'John'), ('age', 40)])
>>>
>>> list(d.items())
[('name', 'John'), ('age', 40)]
>>>
>>> for key, value in d.items():
...     print(key, value)
...
name John
age 40
>>>
```

* Fetching a non-existent key in a dict produces an exception, to avoid it, use the `.get(key)` method, which returns `None` or the passed argument as result if the key is non-existent:

```python
>>> d = {"name": "John", "age": 40}
>>>
>>> d["gender"] # ops!
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-222-5736e263e07d> in <module>
----> 1 d["gender"] # ops!

KeyError: 'gender'
>>>
>>> d.get("gender") # None!
>>> d.get("gender", "They") # argument value
'They'
>>>
```

* Dicts dont support concatenation:

```python
>>> {"a": 1} + {"b": 2}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-225-557db3d74bb0> in <module>
----> 1 {"a": 1} + {"b": 2}

TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>>
```

* To join two dicts, use the `.update(another_dict)` to merge them. Caution: `another_dict` values will overwrite already existent keys:

```python
>>> a = {"name": "John", "age": 45}
>>> b = {"age": 50, "address": "Bakersvile"}
>>>
>>> a.update(b) # in-place update!
>>>
>>> a
{'name': 'John', 'age': 50, 'address': 'Bakersvile'}
>>>
```

* Dicts also have a `.pop(key)` method that returns the correspondent value and deletes the key from the dict:

```python
>>> a = {"name": "John", "age": 45}
>>>
>>> a
{'name': 'John', 'age': 45}
>>>
>>> a.pop("age")
45
>>>
>>> a
{'name': 'John'}
>>>
```

* Mapping value to key:

```python
>>> d = {"name": "John", "age": 40, "cats": 30, "dogs": 40}
>>>
>>> ks = []
>>> for key, value in d.items():
...     if value == 40:
...         ks.append(key)
...
>>> ks
['age', 'dogs']
>>>
>>> # Or, using comprehensions
>>> ks = [key for key, value in d.items() if value == 40]
>>> ks
['age', 'dogs']
>>>
```

* You can use dicts  as flexible and sparse lists:

```python
>>> d = {}
>>>
>>> d[1988] = "John"
>>> d[1976] = "Paul"
>>> d[1999] = "Adrian"
>>>
>>> d
{1988: 'John', 1976: 'Paul', 1999: 'Adrian'}
>>>
>>> d.get(2000)
>>>
```

* Dicts can be used to implement sparse matrixes:

```python
>>> matrix = {}
>>>
>>> matrix[(2, 3)] = 10
>>> matrix[(1, 4)] = 3
>>>
>>> for i in range(5):
...     for j in range(5):
...         print(matrix.get((i, j), 0))
...
0
0
0
0
0
0
0
0
0
3
0
0
0
10
0
0
0
0
0
0
0
0
0
0
0
>>>
```

* Dealing with missing key exceptions:

```python
>>> d = {"name": "John", "age": 40}
>>> # Previous check
>>> if "name" in d: print(d["name"])
John
>>> if "address" in d: print(d["address"])
>>>
>>> # Dealing with the exception
>>> try:
...     print(d["address"])
... except:
...     print("ops!")
...
ops!
>>>
>>> # using .get() method
>>> print(d.get("address"))
None
>>>
```

* Alternative ways to create dictionaries:

```python
>>> d = {"name": "Bob", "age": 40}
>>>
>>> d
{'name': 'Bob', 'age': 40}
>>>
>>> d = dict(name="bob", age=40)
>>> d
{'name': 'bob', 'age': 40}
>>>
>>>
>>> d = dict([("name", "Bob"), ("age", 40)])
>>> d
{'name': 'Bob', 'age': 40}
>>>
>>> d = dict(zip(["name", "age"], ["Bob", 40]))
>>> d
{'name': 'Bob', 'age': 40}
>>>
```

* You can create all keys with a default value (if not specified, its `None`):

```python
>>> d = dict.fromkeys(["name", "age"])
>>> d
{'name': None, 'age': None}
>>>
>>> d2 = dict.fromkeys(["age", "njobs"], 0) # instead of None, default will be 0
>>> d2
{'age': 0, 'njobs': 0}
>>>
```

#### Dictionaries comprehensions

* `zip()` usage for dictionary creation example:

```python
>>> k = ["name", "age"]
>>> v = ["Bob", 40]
>>>
>>> list( zip(k, v) ) # list is necessary. zip returns an iterator.
[('name', 'Bob'), ('age', 40)]
>>>
>>> # to construct a dict, pass the zip result as arg
>>> d = dict( zip(k, v) )
>>> d
{'name': 'Bob', 'age': 40}
>>>
```

* Using dict comprehensions to create dicts, similarly to `zip`:

```python
>>> d = {k:v for k, v in zip(["name", "age"], ["Bob", 40])}
>>> d
{'name': 'Bob', 'age': 40}
>>>
```

* Comprehensions look more verbose, but you can calculate expressions with tem:

```python
>>> d = {x: x ** 2 for x in [2, 4, 6]}
>>> d
{2: 4, 4: 16, 6: 36}
>>>
>>> words = ["spam", "eggs", "bacon"]
>>>
>>> words_adjusted = {word: word.upper() for word in words}
>>> words_adjusted
{'spam': 'SPAM', 'eggs': 'EGGS', 'bacon': 'BACON'}
>>>
```

* Comprehensions can be used to create dict with keys only and default values, just like the `dict.fromkeys()` method:

```python
>>> d = {k:0 for k in ["age", "njobs", "wins"]}
>>> d
{'age': 0, 'njobs': 0, 'wins': 0}
>>>
>>> d = dict.fromkeys("spam")
>>> d
{'s': None, 'p': None, 'a': None, 'm': None}
>>>
>>> d = {k:None for k in "spam"}
>>> d
{'s': None, 'p': None, 'a': None, 'm': None}
>>>
```

### Dictionaries views

* In Python 3 `.keys()`, `.values()` and `.items()` return `views` objects, which are iterators that return elements on demand:

```python
>>> d = {"name": "Bob", "age": 40}
>>>
>>> d
{'name': 'Bob', 'age': 40}
>>>
>>> d.keys()
dict_keys(['name', 'age'])
>>>
>>> d.values()
dict_values(['Bob', 40])
>>>
>>> d.items()
dict_items([('name', 'Bob'), ('age', 40)])
>>>
```

* These `views` objects present some interesting characteristics:

1. `views` reflect changes in the original dict:

```python
>>> d = {"name": "Bob", "age": 40}
>>>
>>> keys = d.keys()
>>> values = d.values()
>>> items = d.items()
>>>
>>> keys
dict_keys(['name', 'age'])
>>> values
dict_values(['Bob', 40])
>>> items
dict_items([('name', 'Bob'), ('age', 40)])
>>>
>>> d["job"] = "manager"
>>>
>>> keys
dict_keys(['name', 'age', 'job'])
>>> values
dict_values(['Bob', 40, 'manager'])
>>> items
dict_items([('name', 'Bob'), ('age', 40), ('job', 'manager')])
>>>
```

2. `.keys()` `view` support `set` operations:

```python
>>> a = {"name": "bob", "age": 40, "job": "manager"}
>>> b = {"age": 50, "address": "Bakersvile"}
>>>
>>> a.keys() & b.keys()
{'age'}
>>>
>>> a.keys() | b.keys()
{'address', 'age', 'job', 'name'}
>>>
>>> a.keys() ^ b.keys()
{'address', 'job', 'name'}
>>>
```

3. Caution. `views` objects don't support indexing or slicing. You need to convert them to lists:

```python
>>> d = {"name": "Bob", "age": 40}
>>>
>>> keys = d.keys()
>>> values = d.values()
>>> items = d.items()
>>>
>>> keys
dict_keys(['name', 'age'])
>>> values
>>> a = {"name": "bob", "age": 40, "job": "manager"}
>>>
>>> a.keys()
dict_keys(['name', 'age', 'job'])
>>>
>>> keys = a.keys()
>>> keys
dict_keys(['name', 'age', 'job'])
>>>
>>> keys[0] # no!
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-65-9dc1b17cffa2> in <module>
----> 1 keys[0] # no!

TypeError: 'dict_keys' object is not subscriptable
>>>
>>> keys[1:] # no!
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-66-c8c21e2fb74b> in <module>
----> 1 keys[1:] # no!

TypeError: 'dict_keys' object is not subscriptable
>>>
>>> keys_lst = list(keys)
>>> keys_lst
['name', 'age', 'job']
>>>
>>> keys_lst[0]
'name'
>>>
>>> keys_lst[1:]
['age', 'job']
>>>
```

* If interact a `.keys()` `view` with another dictionary, the `dictionary` `.keys()` method is implictly used:

```python
>>> a = {"name": "John", "age": 45}
>>>
>>> a.keys() & {"age": 50, "job": "manager"}
{'age'}
>>>
>>> a.keys() ^ {"age": 50, "job": "manager"}
{'job', 'name'}
>>>
```

* To iterate over the keys of a dict in a sorted manner you need to conver it to a `list` and call the `.sort()` method or use the `sorted()` builtin function:

```python
>>> a = {"name": "John", "age": 45}
>>>
>>> keys = list(a)
>>> keys
['name', 'age']
>>>
>>> keys.sort()
>>>
>>> for key in keys:
...     print(a[key])
...
45
John
>>>
>>> # or, using sorted(), which is the preferable way
>>> for key in sorted(a):
...     print(key, a[key])
...
age 45
name John
>>>
```

* Lastly, since Python 3, the method `.has_key()` has been removed. Test with the `in` operator instead.

## Tuple, files and everything ele

### Tuples

* Are like immutable lists which are declared using parentheses, instead of square brackets:

```python
>>> l = (1, 3.14, "spam")
>>> l
(1, 3.14, 'spam')
>>>
>>> l[0]
1
>>>
>>> l[0] = 2 # ops!
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-0430b62a20fd> in <module>
----> 1 l[0] = 2 # ops!

TypeError: 'tuple' object does not support item assignment
>>>
```

* Ways to declare and main operations:

```python
>>> # empty tuple
>>> t = ()
>>>
>>> # single element tuple (comma is required)
>>> t = (10,)
>>> t
(10,)
>>>
>>> # tuple with more elements
>>> t = (0, "ni", 1.2, 3)
>>> t
(0, 'ni', 1.2, 3)
>>>
>>> t = 0, "ni", 1.2, 3 # items separated only by a comma are intepreted as a tuple also
>>> t
(0, 'ni', 1.2, 3)
>>>
>>> # nested tuple
>>> t = ("Bob", ("manager", "developer"))
>>> t
('Bob', ('manager', 'developer'))
>>>
>>> # create a new tuple from an iterable
>>> t = tuple("spam")
>>> t
('s', 'p', 'a', 'm')
>>>
>>> # indexing
>>> t = (1, 3.14, "spam")
>>> t[0]
1
>>>
>>> # slicing
>>> t[1:]
(3.14, 'spam')
>>>
>>> # length
>>> len(t)
3
>>>
>>> # copy, using slices
>>> t2 = t[:]
>>> t2
(1, 3.14, 'spam')
>>>
>>> # concatenation, producing a new tuple
>>> t + t
(1, 3.14, 'spam', 1, 3.14, 'spam')
>>>
>>> # repetition
>>> t * 3
(1, 3.14, 'spam', 1, 3.14, 'spam', 1, 3.14, 'spam')
>>>
>>> # looping
>>> for e in t: print(e)
1
3.14
spam
>>>
>>> # membership using "in"
>>> 1 in t
True
>>>
>>> # comprehension
>>> [x * 2 for x in t]
[2, 6.28, 'spamspam']
>>>
>>> # methods index() and count()
>>> t = (1, 3.14, "spam")
>>> t.index("spam")
2
>>>
>>> t = tuple("aloha")
>>> t
('a', 'l', 'o', 'h', 'a')
>>>
>>> t.count("a") # how many "a"
2
>>>
```

* Tuples are immutable, so you dont have the same methos as with lists.

* To sort a tuple, or convert it to list, sort and convert back:

```python
>>> t = (3, 1, 2, 0, 4)
>>> t = tuple( sorted(t) )
>>> t
(0, 1, 2, 3, 4)
>>>
>>> t = (3, 1, 2, 0, 4)
>>> t = list(t)
>>> t.sort()
>>> t
[0, 1, 2, 3, 4]
>>>
>>> t = tuple(t)
>>> t
(0, 1, 2, 3, 4)
>>>
```

* You can convert a tuple to a list while processing it using comprehensions (in fact, you can do it with any iterator type of object):

```python
>>> t = (10, 20, 30)
>>>
>>> t2 = [v - 1 for v in t]
>>> t2
[9, 19, 29]
>>>
```

* Note that `tuples` are immutable but can hold mutable objects, and these objects can be changed:

```python
>>> t = ([1, 2, 3], {"name": "Bob"})
>>>
>>> t[0].append(4)
>>>
>>> t[1]["age"] = 40
>>>
>>> t
([1, 2, 3, 4], {'name': 'Bob', 'age': 40})
>>>
```

* Tuples with mutable objects are not hashable and cant be used as dict keys:

```python
>>> # when a tuple has mutable objects inside, it stops being "hashable", thus cant be used as a dict ke
... y
>>>
>>> t = ([1, 2, 3], {"name": "Bob"})
>>>
>>> d = {t: "t"} # ops!
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-24-f703edc027bc> in <module>
----> 1 d = {t: "t"} # ops!

TypeError: unhashable type: 'list'
>>>
```

### namedtuple

* Somewhat similary to dictionaries, `namedtuple` allows the creation of `tuples` which can be accessed by `key` or `position`:

```python
>>> from collections import namedtuple
>>>
>>> Person = namedtuple("Person", ("name", "age", "jobs"))
>>>
>>> p1 = Person("Bob", 40, ["dev", "manager"]) # keyword args are required
>>> p1
Person(name='Bob', age=40, jobs=['dev', 'manager'])
>>> p1.name
'Bob'
>>> p1[0]
'Bob'
>>>
>>> p1.age
40
>>> p1[1]
40
>>>
```

* `namedtuple` can be converted to dictionaries using the `._asdict()` method:

```python
>>> from collections import namedtuple
>>> Person = namedtuple("Person", ("name", "age", "jobs"))
>>>
>>> p1 = Person("Bob", 40, ["dev", "manager"]) # args are mandatory
>>> p1
Person(name='Bob', age=40, jobs=['dev', 'manager'])
>>>
>>> p1.name
'Bob'
>>> p1[0]
'Bob'
>>>
>>> p1._asdict()
{'name': 'Bob', 'age': 40, 'jobs': ['dev', 'manager']}
>>>
```

* `tuples` and `namedtuples` can be used for unpacking assignment:

```python
>>> p1
Person(name='Bob', age=40, jobs=['dev', 'manager'])
>>>
>>> name, age, jobs = p1
>>> name
'Bob'
>>> age
40
>>> jobs
['dev', 'manager']
>>>
>>> for value in p1: print(value)
Bob
40
['dev', 'manager']
>>>
```

### Files

#### Opening files

* To open a file, use the builtin `open(filename, mode)`.

Three modes are avaiable:

`r`, the default, for `reading`;
`w`, for `writing`;
`a`, for appending, usually for log files

These modes handle all data as unicode strings. If you want to deal with bytes directly, suffix them with a `b`:

`rb`, `wb` and `ab`.

If you suffix the modes with a `+`, you can `write` and `read` to it:

`r+`, `w+` and `a+`.

* You can specify a third positional argument `open(filename, mode, buffersize)` to define the buffersize.
If you set it to `0`, no buffer will be used, meaning that data is written in the moment it is requested.

* In Python 3, a keyword argument `encoding=` can be used, to define the encoding used in the file.
Remember, if you dont suffix with `b`, the file is treated as unicode text.

#### Files in Action

* The best way to read a file is using its iterator:

```python
>>> fp = open("/etc/resolv.conf")
>>> for line in fp:
...     print(line)
...
# Generated by NetworkManager

nameserver 186.207.160.71

nameserver 186.207.160.77

nameserver 8.8.8.8

# NOTE: the libc resolver may not support more than 3 nameservers.

# The nameservers listed below may not be recognized.

nameserver 1.1.1.1

nameserver 2804:14d:7210:672:186:207:160:77

nameserver 2804:14d:7210:672:186:207:160:71

>>>
```

* File content is read and written as strings. Always.

* Python always use buffers when dealing with files, so the content you write is not immediately transfered to the disk.
You can force this transference using the `.flush()` method or by passing the `buffering=0` keyword argument to the `open()` builtin.

* Files support random access. You can move the file pointer using the `.seek()` method.

* `.close()` method closes the file, releases the resources and flushs the buffer. It is automatically called when the file object is garbage collected.
But, you should include your own in long running codes.

* A simple example. Writing and reading a sample file:

```python
>>> myfile.close() # release
>>>
>>> myfile = open("myfile.txt") # reading
>>> myfile.readline() # first line
'helloo text file\n'
>>> myfile.readline() # second line
'goodbye!\n'
>>> myfile.readline() # empty lines mean the file is over. linebreaks in file comeback as '\n'.
''
```

* You can read all the file content using the `.read()` method:

```python
>>> myfile = open("myfile.txt")
>>> content = myfile.read()

>>> content
'helloo text file\ngoodbye!\n'
>>>

>>> print(content) # print interprets \n
helloo text file
goodbye!
```

* Again, if you want to go line by line, use an iterator:

```python
>>> myfile = open("myfile.txt")
>>>
>>> for line in myfile:
...     print(line, end='') # end argument is necessary so newline aren duplicated
...
helloo text file
goodbye!
>>>
```

* In Windows you can use foward slashes to form paths. Python will handle them correctly:

```python
>>> # The same result in all three options
>>> fp = open("c:\\windows\\file.txt")
>>> fp = open("c:/windows/file.txt")
>>> fp = open(r"c:\windows\file.txt")
>>>
```

#### Text and Binary files. A short history.

* Python supports two kind of file accesses: text files and binary files.
To force a binary file object, you must suffix the opening mode with a `b` letter: `rb`, `wb` or `ab`.

* Text files represent content as `str` strings. The unicode encoding (while writing) and decoding (while reading) is performed automatically.
End-of-line translation is also automatic (every newline is translated to `\n`).

* Binaty files represent file contents as `bytes` strings. No encoding or end-of-line automatic conversion is performed.
Allowing programs to access files contents unaltered.

* `pickle` can save native Python objects into binary files:

```python
>>> # Save a dict to a file
>>> d = {"a": 1, "b": 2}
>>> fp = open("d.pkl", "wb") # binary mode required
>>> import pickle
>>> pickle.dump(d, fp)
>>> fp.close()
>>>
```

```python
>>> # Reading a pickle file
>>> fp = open("d.pkl", "rb") # binary mode required
>>> import pickle
>>>
>>> d = pickle.load(fp)
>>> d
{'a': 1, 'b': 2}
>>>
```

* You can use the `json` to export and import Python objects in the JSON format, enabling sharing with other languages/platforms:

```python
>>> import json
>>>
>>> d = {"a": 1, "b": 2}
>>>
>>> json.dumps(d) # as string
'{"a": 1, "b": 2}'
>>>
>>> d_json = json.dumps(d) # as string
>>>
>>> d = json.loads(d_json)
>>> d
{'a': 1, 'b': 2}
>>>
>>> fp = open("d.json", "w") # as string!
>>> json.dump(d, fp)
>>> fp.close()
>>>
>>> fp = open("d.json")
>>> d = json.load(fp)
>>> d
{'a': 1, 'b': 2}
>>>
>>> fp.close()
>>>
```

* You can `indent` the `json` output:

```python
>>> print( json.dumps(d, indent=4) )
{
    "a": 1,
    "b": 2
}
>>>
```

## Core types review and summary

* Python variables are **references**, which are a higher-level analog of pointers in other languages that are always followed when used.

* You have to explictly require a copy of an object to avoid side-effects with mutable objects:

```python
>>> l = [1, 2, 3]
>>>
>>> a = ["spam", l]
>>> b = ["eggs", l]
>>>
>>> a
['spam', [1, 2, 3]]
>>> b
['eggs', [1, 2, 3]]
>>>
>>> l[1] = "surprise!"
>>>
>>> a
['spam', [1, 'surprise!', 3]]
>>> b
['eggs', [1, 'surprise!', 3]]
>>>
>>> c = ["bacon", l.copy()]
>>>
>>> l[1] = "another surprise!"
>>>
>>> c
['bacon', [1, 'surprise!', 3]]
>>>
```

* To `deepcopy` a data structure, use the `copy` module:

```python
>>> import copy
>>>
>>>
>>> a = [1, {"a": "x", "b": "y"}, 2]
>>> b = a.copy()
>>> c = copy.deepcopy(a)
>>>
>>> a[1]["a"] = "z"
>>> a
[1, {'a': 'z', 'b': 'y'}, 2]
>>>
>>> b # shallow copy
[1, {'a': 'z', 'b': 'y'}, 2]
>>>
>>> c # deep copy
[1, {'a': 'x', 'b': 'y'}, 2]
>>>
```

* Python has two equality tests:

`==`: objects have the same value ?

`is`: objects are the same ? (i.e. live in the same memory address)

* All comparison tests `==` are recursive. Inner objects are compared also.

### True and False in Python

* Integer `0` is `False`

* Integer `1` is `True`

* Any empty data structure is treated as `False`

* Any nonempty data structure is treated as `True`

* `None` is `False`

* All objects have an intrisic boolean value.

* `False` values:

```python
>>> False
>>> False
False
>>>
>>> bool( 0 )
False
>>> bool( 0.0 )
False
>>>
>>> bool( [] )
False
>>> bool( () )
False
>>> bool( {} )
False
>>>
>>> bool( None )
False
>>> # False is, in fact, the number 0 with a different string representation
>>> False - 1 # False == 0
-1
>>>
```

* `True` values:

```python
>>> True
True
>>>
>>> bool( 1 ), bool( -1 ) # Only 0 is False...
(True, True)
>>>
>>> bool( 0.1 )
True
>>>
>>> bool( [None] )
True
>>> bool( ("spam", "eggs") )
True
>>>
>>> bool( {"name": "bob"} )
True
>>>
>>> True + True # True is, really, the 1 number
2
>>>
```

* Given that Python objects have an intrisic boolean value, its common to perform boolean tests directly on the objects:

```python
>>> x = 3.14
>>>
>>> if x:
...     print("Its defined!")
...
Its defined!
>>>
```

### `None`

* `None` is an object in Python (a singleton) that represents the absence of value.

* You can, for example, preallocate a list using it:

```python
>>> l = [None] * 5
>>> l
[None, None, None, None, None]
>>>
```

### Everything is an object, even types

* The `type` of an `object` is an `object` of `type`, `type`.

```python
>>> type(int)
type
>>> type(float)
type
>>> type(bool)
type
>>> type(str)
type
>>> type(bytes)
type
>>>
```

* You can extend theses types (subclass), as they are, in reality, class constructors.

* They are note simple conversion functions. They are constructors.

* Python 3 includes names for other types, like functions, modules, etc. They are defined in the `types` module.

* You can, but should avoid, check for a specific type with the `isinstance(obj, type)` builtin.

```python
>>> isinstance([], list)
True
>>> isinstance(3.14, float)
True
>>> isinstance(3, int)
True
>>> isinstance("spam", str)
True
>>>
```

### Gotchas

* Assignments create references, so, multiples references to the same mutable object are all affected by changes to the object:

```python
>>> a = [1, 2, 3]
>>> b = a
>>> c = ["a", a, "d"]
>>>
>>> a[1] = "surprise!"
>>>
>>> a
[1, 'surprise!', 3]
>>>
>>> b
[1, 'surprise!', 3]
>>>
>>> c
['a', [1, 'surprise!', 3], 'd']
>>>
```

* To avoid it, create copies calling the `.copy()` method or, in case of lists, using empty slices `[:]`.

* Caution with repetition. Its like adding the object to itself multiple times:

```python
>>> a = [1, 2, 3]
>>>
>>> b = a * 3 # produces a new list, repeating a 3 times
>>> b
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>>
>>> c = a + a + a # produces a new list. same as a * 3.
>>> c
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>>
>>> d = [a] # repeats a list containing another list
>>>
>>> e = d * 3
>>> e
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
>>>
>>> f = d + d + d
>>> f
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
>>>
```

> Note that, in the previous example,  the repetition (`b = a * 3`) products a new list, thus it is not affected by changes in `a`.
While `d` keeps a reference to `a`, being affected by posterior changes:

```python
>>> a[1] = "suprise!"
>>> b
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>>
>>> d
[[1, 'suprise!', 3]]
>>>
```

To avoid shared references, make copies:

```python
>>> d = [list(a)] * 3 # list(obj) makes a copie as a list
>>> a[1] = "aloha"
>>> a
[1, 'aloha', 3]
>>>
>>> d
[[1, 'suprise!', 3], [1, 'suprise!', 3], [1, 'suprise!', 3]]
>>>
```

* Also mind that repetition repeats the reference, even if you create a copy:

```python
>>> a = [1, 2, 3]
>>>
>>> b = [list(a)] * 3
>>> b
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
>>>
>>> b[0][1] = "surprise!"
>>> b # Same reference! It is only one list, reference three times
[[1, 'surprise!', 3], [1, 'surprise!', 3], [1, 'surprise!', 3]]
>>>
```

* **Cyclic data structures**: are container objects that have a reference to themselves.

```python
>>> a = [1, 2, 3]
>>>
>>> b = a * 3
>>> b
>>> lst = [1, 2, 3]
>>>
>>> lst.append(lst)
>>>
>>> lst
[1, 2, 3, [...]] # Python detects them and represents as ...
>>>
>>> for item in lst:
...     print(item)
...
1
2
3
[1, 2, 3, [...]]
>>>
```

* Lastly: immutable objects can't be change in place. You should concatenate, repeat or slice them to create a new object.
Then, you can assign to the same variable, replacing the original object:

```python
>>> t = (1, 2, 3)
>>> t[1] = 0 # no!
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-81-48e1fb88af36> in <module>
----> 1 t[1] = 0 # no!

TypeError: 'tuple' object does not support item assignment
>>>
>>> t = (t[1], 0) + (3,)
>>> t
(2, 0, 3)
>>>

```