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

## Python statements

* If you need to span an expression for multiple lines, enclose in parentheses:

```python
if (A == 1 and
    B == 2 and
    C == 3):
        print('spam' * 3)
```

### Assignments

* Assignments create references. Python variables are more like pointers than data storage areas.

* Variables are, whenever used in an expression, replaced by the value/object it points to.

* Assignments forms:

```python
>>> spam = "Spam"
>>> spam
'Spam'
>>>
>>> spam, ham = "spam", "eggs"
>>> spam
'spam'
>>> ham
'eggs'
>>>
>>> a, b, c, d = "spam"
>>> a, b, c, d
('s', 'p', 'a', 'm')
>>>
>>> a, *b = "spam"
>>> a, b
('s', ['p', 'a', 'm'])
>>>
>>> spam = ham = "lunch"
>>> spam
'lunch'
>>> ham
'lunch'
>>>
>>> spam = 0
>>> spam += 1
>>> spam
1
>>>
```

* Tuple unpacking. If you declare multiple variables on left and multiple values on right side, Python bind them respectively.

```python
>>> a, b, c = 1, 2, 3 # tuple unpacking. tuple is implictly created
>>> a
1
>>> b
2
>>> c
3
>>>
>>> a, b, c = (1, 2, 3) # tuple unpacking. same behavior.
>>> a, b, c
(1, 2, 3)
>>> a
1
>>> b
2
>>> c
3
>>>
```

* Tuple unpacking has been expanded for different sequence types:

```python
>>> [a, b, c] = (1, 2, 3)
>>> a
1
>>> b
2
>>> c
3
>>>
```

* In tuple unpacking, number of left side variables should match right side values.
If not, an exception is thrown:

```python
>>> [a, b, c] = (1, 2)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-42-5004ed3e1c4e> in <module>
----> 1 [a, b, c] = (1, 2)

ValueError: not enough values to unpack (expected 3, got 2)
>>>
```

* You can handle a variant number of right side values with the extended sequence assignment:

```python
>>> a, *b = [1, 2, 3, 4, 5]
>>> a
1
>>> b
[2, 3, 4, 5]
>>>
```

#### Sequence assignments

```python
>>> nudge = 1
>>> wink = 2
>>>
>>> a, b = nudge, wink
>>> a, b
(1, 2)
>>>
>>> [c, d] = [nudge, wink]
>>> c, d
(1, 2)
>>>
```

* The right side is evaluated first, so you can use sequence assignments to swap two variables values without an auxiliar:

```python
>>> a = 1
>>> b = 2
>>> a, b
(1, 2)
>>>
>>> a, b = b, a
>>> a
2
>>> b
1
>>>
```

* You can use it with any sequence:

```python
>>> [a, b, c] = (1, 2, 3)
>>> a, b, c
(1, 2, 3)
>>>
>>> (a, b, c) = "ABC"
>>> a, b, c
('A', 'B', 'C')
>>>
```

* Even nested sequences can be used:

```python
>>> (a, b), c = "AB", "SP"
>>> a
'A'
>>> b
'B'
>>> c
'SP'
>>>
```

* One common idiom is assignments with `range()` series:

```python
>>> a, b, c = range(3)
>>> a, b, c
(0, 1, 2)
>>>
```

* Another idiom is to separate the first column of a "row" (list):

```python
>>> l = [1, 2, 3, 4]
>>> while l:
...     front, l = l[0], l[1:]
...     print(front, l)
...
1 [2, 3, 4]
2 [3, 4]
3 [4]
4 []
>>>
```

* If you dont know the lenght of the right side values to unpack, you can used the extended syntax `*variable`, which creates a list with the remaining unassigned values of the right side:

```python
>>> a, *b = range(10)
>>> a, b
(0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>>
```

You can use it in the start or in the middle also:

```python
>>> *a, b = range(10)
>>> a, b
([0, 1, 2, 3, 4, 5, 6, 7, 8], 9)
>>>
```

```python
>>> a, *b, c = range(10)
>>> a, b, c
(0, [1, 2, 3, 4, 5, 6, 7, 8], 9)
>>>
```

The extended syntax works with any iterable:

```python
>>> *a, b = "spam"
>>> a, b
(['s', 'p', 'a'], 'm')
>>>
>>> a, *b, c = "spam"
>>> a, b, c
('s', ['p', 'a'], 'm')
>>>
>>> a, b, *c = "spam"
>>> a, b, c
('s', 'p', ['a', 'm'])
>>>
```

> Caution: extended unpacking remembers a slicing, but it is not the same. Extended slicing always returns a list, while slicing returns an object of the same type as the sliced:

```python
>>> a, *b, c = (1, 2, 3, 4, 5)
>>> a, b, c
(1, [2, 3, 4], 5)
>>>
>>> t = (1, 2, 3, 4, 5)
>>> a = t[0]
>>> c = t[-1]
>>> b = t[1:-1]
>>> b
(2, 3, 4)
>>>
```

* With extended syntax, the last example becomes even easier to write:

```python
>>> l = 1, 2, 3, 4, 5
>>>
>>> while l:
...     front, *l = l
...     print(front, l)
...
1 [2, 3, 4, 5]
2 [3, 4, 5]
3 [4, 5]
4 [5]
5 []
>>>
```

#### Some boundary cases:

* The starred name is always assigned a list, even when only one element is matched:

```python
>>> a, *b = (10, 20)
>>> a, b
(10, [20])
>>>
```

* The starred name is assigned last, so it can be an empty list sometimes:

```python
>>> a, *b, c = [1, 2]
>>> a, b, c
(1, [], 2)
>>>
```

* You can only have one starred name:

```python
>>> *a, *b = [1, 2, 3, 4]
  File "<ipython-input-5-d621ef55cf15>", line 1
    *a, *b = [1, 2, 3, 4]
    ^
SyntaxError: two starred expressions in assignment

>>>
```

* You cant have only a starred name:

```python
>>> *a = [1, 2, 3]
  File "<ipython-input-6-2e13dd4112ba>", line 1
    *a = [1, 2, 3]
    ^
SyntaxError: starred assignment target must be in a list or tuple

>>>
```

You need it to be a tuple at least:

```python
>>> *a, = [1, 2, 3]
>>> a
[1, 2, 3]
>>>
```

* First, rest syntax using extended assignment syntax:

```python
>>> first, *rest = [1, 2, 3]
>>> first, rest
(1, [2, 3])
```

* Rest, last syntax using ext. assignment syntax:

```python
>>> *rest, last = [1, 2, 3]
>>> rest, last
([1, 2], 3)
>>>
```

* Extended assignment syntax in foor loops:

```python
>>> for a, *middle, end in [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)]:
...     print(a, middle, end)
...
1 [2, 3] 4
5 [6, 7] 8
9 [10, 11] 12
>>>
```

* Multiple target assignment make all references point to the same object:

> Caution: there is only one object and multiple, shared, references. Which are subject to side-effects of in-place change with mutable types.

```python
>>> a = b = c = [1, 2, 3]
>>> a, b, c
([1, 2, 3], [1, 2, 3], [1, 2, 3])
>>>
>>> c[0] = 10
>>>
>>> a, b, c
([10, 2, 3], [10, 2, 3], [10, 2, 3])
>>>
```

* Avoid that assigning to multiple lists:

```python
>>> a, b, c = [], [], []
>>> a, b, c
([], [], [])
>>>
>>> a.append(10)
>>> a
[10]
>>> b
[]
>>> c
[]
>>>
```

* **Augmented assignments**, shorthands

```python
>>> a = [1, 2, 3]
>>>
>>> a = a + [4, 5, 6] # concatenation, creating a new object
>>> a
[1, 2, 3, 4, 5, 6]
>>>
>>> a.extend([7, 8, 9]) # appends in-place
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> # if you call a shorthand concatenation syntax +=, python implictly uses the .extend() method, which is faster
>>> a += [10]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>>
```

> This intelligent behavior is more flexible with types, while simple concatenation is more restrict:

```python
>>> a = [1, 2, 3]
>>>
>>> a += "spam"
>>> a
[1, 2, 3, 's', 'p', 'a', 'm']
>>>
>>> a = a + "spam" # Ops!
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-27-0f920944855b> in <module>
----> 1 a = a + "spam" # Ops!

TypeError: can only concatenate list (not "str") to list
>>>
```

* Other augmented assignments examples:

```python
>>> a = 10
>>>
>>> a += 1
>>> a
11
>>>
>>> a *= 2
>>> a
22
>>> a /= 3
>>> a
7.333333333333333
>>>
>>> a **= 2
>>> a
53.77777777777777
>>>
```

* The intelligent behavior of shorthand assignments can cause divergences when using mutable types. Concatenation (`a = a + [...]`) always create a new object, while `.extend([...])` or `a += [...]` change the object in  place. Its important for shared references:

```python
>>> a = b = [1, 2, 3]
>>> a, b
([1, 2, 3], [1, 2, 3])
>>>
>>> a = a + [4]
>>> a
[1, 2, 3, 4]
>>>
>>> b
[1, 2, 3]
>>>
>>>
>>> # shorthand
>>> a = b = [1, 2, 3]
>>> a += [4]
>>> a, b
([1, 2, 3, 4], [1, 2, 3, 4])
>>>
```

#### Naming conventions

* Names started with an underscore `_x` are not imported in a statement like `from module import *`

* Names with two underscore as prefix and suffix `__example__` are system-defined and have special meaning, usually, for the intepreter

* `__var` (underscore only as prefix) are *mangled* (localized) to the enclosing class.

* `_` is the last expression result in the shell

#### Names have no type. Objects do.

* names/variables are only references which are auto-translated when used in expression. They don't keep track of the referenced object type. The type information resides in the object itself.

* Expression statements and in-place changes:


#### print()

`print([obj1, obj2, ...], [sep=' '], [end='\n'], file=sys.stdout, flush=False)`

* `print()` converts the object to a string representation (`str(object)`), then outputs.

* Some examples:

```python
>>> print() # blank line

>>>
```

```python
>>> print(1, 2, 3, sep='-')
1-2-3
>>>
```

```python
>>> print(1, 2, 3, sep='-', end='*\n*\n')
1-2-3*
*
>>>
```

* `print()` is the same as `sys.stdout.write()`, just friendly

```python
>>> import sys
>>> sys.stdout.write("Hello World" + "\n") # it dosent include \n by default and returns the numbers of chars written
Hello World
12
>>>
```

* `sys.stdout` is a file-like object which is used by default in the `print()` function.
So, you can reassign it and make `print()` write to a file or any other stream:

> You should open the file as `a+` (append mode) if you want to mantain the current content before opening it.

```python
>>> import sys
>>> sys.stdout = open("/tmp/output.txt", "w")
>>> print("Hello World!")
>>> print("Bye!")
>>>

rnetodev@T440s:~$ cat /tmp/output.txt
Hello World!
Bye!
Do you really want to exit ([y]/n)?
```

* If you want to temporaly change the `print()`/`sys.stdout` behavior, you can save `sys.stdout` to a temporary variable and then reassign it:

```python
>>> import sys
>>> _stdout = sys.stdout
>>> sys.stdout = open("/tmp/log.txt", "a")
>>> print("Hi!")
>>> print("Hello!")
>>>
>>> sys.stdout = _stdout
>>>
>>> print("Hi!")
Hi!
>>> print("Hello!")
Hello!
>>>
Do you really want to exit ([y]/n)?
rnetodev@T440s:~$ cat /tmp/log.txt
Hi!
Hello!
Hi!
Hello!
rnetodev@T440s:~$
```

* Or, more simple, use the `file` keyword parameter of the `print()` function in Python 3. You should pass an open `file` object or any other object with a `write()` method, which will be then used by `print()`:

```python
#!/usr/bin/env python3
>>> fp = open("/tmp/log.txt", "a")
>>>
>>> print("Another bye!", file=fp)
>>>
>>> fp.close()
>>>
>>> print("Byeeee")
Byeeee
>>>
rnetodev@T440s:~$ cat /tmp/log.txt
Hi!
Hello!
Hi!
Hello!
Another bye!
rnetodev@T440s:~$
```

* The `file` keyword of the `print()` function can be used to print to `stderr` also:

```python
import sys
print("Bug!", file=sys.stderr)
```

* Outer objects are represented using `__str__`, inner objects, with `__repr__`:

```python
>>> print("spam", ("eggs", "bacon")) # spam is outer, no quotes. eggs and bacon, inner, quotes.
spam ('eggs', 'bacon')
>>>
```

* A simple `if` statement:

```python
>>> x = 'killer'
>>> if x == 'roger':
...     print("shave")
... elif x == 'bugs':
...     print('ops!')
... elif x == 'chairs':
...     print('ops! again!')
... else:
...     print('run away!')
...
run away!
```

> You can have multiple `elif` statements.

* There is no *switch*. Use `if` and multiple `elif` or a dictionarie:

```python
>>> job = 'manager'
>>>
>>> if job == 'manager':
...     pay = 10_000
... elif job == 'developer':
...     pay = 9_000
... elif job == 'designer':
...     pay = 9_500
... else:
...     pay = 0
...
>>> print(pay)
10000
>>> print(job)
manager
>>>
>>> # or, as a dict
>>> d = {
...     "manager": 10_000,
...     "developer": 9_000,
...     "designer": 9_5000
... }
>>> print(d[job])
10000
>>>
```

* In `if` statements, the `else` clause handles the default behavior (if not condition is match). With dictionaries, you can use the `.get()` method:

```python
>>> default_price = 1.99
>>>
>>> prices = {
...     "apple": 0.99,
...     "mango": 1.29,
...     "pineapple": 1.49
... }
>>>
>>> prices.get("grape", default_price)
1.99
>>>
```

Or, using an `if` with the `in` operator and an `else` clause:

```python
>>> default_price = 1.99
>>>
>>> prices = {
...     "apple": 0.99,
...     "mango": 1.29,
...     "pineapple": 1.49
... }
>>>
>>> if "grape" in prices:
...     print(prices["grape"])
... else:
...     print(default_price)
...
1.99
>>>
```

Or, with a `try` block:

```python
>>> default_price = 1.99
>>>
>>> prices = {
...     "apple": 0.99,
...     "mango": 1.29,
...     "pineapple": 1.49
... }
>>>
>>> try:
...     print(prices["grape"])
... except KeyError:
...     print("bad choice")
...
bad choice
>>>
```

* boolean tests `and` / `or` always return one of the objects used, instead of `True` or `False`:

```python
>>> a = 0.0 or 9
>>> a
9
>>> a = "" and -1
>>> a
''
>>>
```

* Python logical operators `and` / `or` always return one of the object compared and short-circuit:

> `and` returns the first object with a false value or the last with a true value.

> `or` returns the first object with a true value or the last with a false value.

```python
# and returns
>>> 1 and 2 # both are true, so the second is returned
2
>>>
>>> "spam" or {} # first is true: returns spam, {} is not interpreted
'spam'
>>>
>>> [] and {} # [] first is false: short circuits and is returned
[]
>>>
>>> [] or {} # doesn't short circuits, returns {}
{}
>>>
```

* `if/else` ternary operator:

```python
>>> x = 10
>>>
>>> answer = "spam" if x == 11 else "eggs"
>>> answer
'eggs'
>>>
>>>
```

> Caution: The ternary operator also short circuits:

```python
>>> print("spam") if 10 / 2 > 0 else print("eggs")
spam
>>> print("spam") if 10 / 2 < 0 else print("eggs")
eggs
>>>
```

* The "return object" behavior is used in some common coding idioms:

1. Return the first True object from a fixed set:

```python
>>> a = 0
>>> b = ""
>>> c = []
>>> d = 1.618
>>> e = {}
>>>
>>> answer = a or b or c or d or e
>>> answer
1.618
>>>
```

2. Designate a default value if variable is false:

```python
>>> name = input("Enter your name:") or "anonymous"
Enter your name:
>>> name
'anonymous'
>>>
```

* Again, caution with the short circuit behavior:

```python
>>> input("Click enter to continue: ") and print("Bye!")
Click enter to continue:
''
>>>
```

To guarantee both functions will run, execute them before comparisons:

```python
>>> tmp1 = f1()
>>> tmp2 = f2()
>>>
>>> tmp1 or tmp2
```

* You can use `filter()`, `any()` and `all()` builtins to perform some logical filtering/analysis:

1. `filter()` return only Treu values from seq:

```python
>>> lst = [1, 2, 3, 0, "", 6, 7]
>>> list(filter(bool, lst))  # bool is the function to apply for each element. list() is necessary, as it returns a generator
[1, 2, 3, 6, 7]
>>>
```

2. `any(seq)` any value is `True` in `seq` ?

```python
>>> any([0, "", {}])
False
>>> any([0, "", {}, 3.14])
True
>>>
```

3. `all(seq)` are all elements `True` ?

```python
>>> all([1, 2, 3])
True
>>>
>>> all([1, 2, 3, 0])
False
>>>
```

## while and for loops

* `while` syntax:

```python
while condition:
    ...logic_block...
else:
    ...no_break_block...
```

The `condition` is checked. If `True`, the `logic_block` is executed. The `logic_block` does not trigger any `break` statement, the `condition` is checked again and, if `True`, the `logic_block` is run again, and so on:

```python
>>> x = 3
>>> while x: # x != 0
...     print(x)
...     x -= 1
...
3
2
1
>>>
```

The `else` statement block is executed if no `break` statement is triggered in the `logic_block.`

```python
>>> x = 3
>>> while x: # x != 0
...     print(x)
...     x -= 1
... else:
...     print("No breaks so far!")
...
3
2
1
No breaks so far!
>>>
```

* Other `while` examples:

Infinite loop:

```python
>>> while True:
...     print("CTRL+C to stop!")
...
```

Progressive slicing a string:

```python
>>> s = "spam!"
>>> while s:
...     print(s)
...     s = s[1:]
...
spam!
pam!
am!
m!
!
>>>
```

* Python does not have a `do/while`, to emulate it, create an `infinite loop` with a `break` on the exit condition:

```python
while True:
    .....logic_block.....
    if exit_condition: break
```

* Python has some especial statements that can be used inside loops:

`continue`: skips the remainder of the current logic block and jumps to the next condition check (header line):

```python
>>> a = 10
>>>
>>> # print only odds
>>> while a:
...     a -= 1
...     if not a % 2 == 0:
...         continue
...     print(a)
...
8
6
4
2
0
>>>
```

`break`: terminates the closest loop immediately:

```python
>>> a = 10
>>>
>>> while a:
...     a -= 1
...     if a == 3: break
...     print(a)
...
9
8
7
6
5
4
>>>
```

> Caution: `break` just stops one loop, the on which it is inclosed. Not all loops.

```python
>>> a = 5
>>> b = 3
>>>
>>> while a:
...     print("a", a)
...     a -= 1
...     while b:
...         if b == 1: break
...         print("b", b)
...         b -= 1
...
a 5
b 3
b 2
a 4
a 3
a 2
a 1
>>>
>>>
```

* Python also has a `pass` statement that does **nothing**! It is just a placeholder:

```python
>>> a = 10
>>>
>>> while a:
...     pass
...     a -= 1
...
>>>
```

* And, remember, the `else` clause in loops are executed when the loop executes fully, that is, no `break` statement is issued:

```python
>>> lst = [1, 3, 5, 7, 9]
>>>
>>> while lst:
...     item = lst.pop()
...     if item % 2 == 0: break # even? exit
...     print(item)
... else:
...     print("No even in list!")
...
9
7
5
3
1
No even in list!
>>>
```

Its commonly used to execute some action just after the loop concludes:

```python
>>> s = 0
>>> lst = [1, 3, 5, 7, 9]
>>> while lst:
...     s += lst.pop()
... else:
...     print("The sum is", s)
...
The sum is 25
>>>
```

Or to get the last value of some variable changed in the loop:

```python
>>> lst = [1, 3, 5, 7, 2, 9]
>>>
>>> # look for the even one
>>> there_is_some_even = False
... while lst:
...     item = lst.pop()
...     if item % 2 == 0: there_is_some_even = True
... else:
...     print("There is some even?", there_is_some_even)
...
There is some even? True
>>>
```

### ... (Ellipsis) as an alternative to `pass` or as an initial variable value

In Python 3, `...` can be used instead of `pass` or as a placeholder for variables.

```python
>>> def to_be_defined(): ...  # ... = pass
>>>
```

Or as an initial variable value:

```python
>>> placeholder_var = ... # ... = None
>>> placeholder_var
Ellipsis
>>> bool( placeholder_var )
True
>>> placeholder_var is None
False
>>> placeholder_var == None
False
>>>
```

> Caution! `...` creates an `Ellipsis` object, which is completely different from `None`, and has a `True` boolean value.

* `continue` jumps to the next loop cycle, immediately interrupting the current one:

```python
>>> x = 10
>>>
>>> while x:
...     x -= 1
...     if x % 2 == 0: continue # skip odds
...     print(x)
...
9
7
5
3
1
>>>
```

* To break out from multiple chained loops you should exceptions. Remember: `break` just ends the closest loop.

* The `else` clause of loops is run if the loops dosent run at all. That is, the condition first check is `False` for `while` loops or the sequence is empty, in for loops:

```python
>>> x = 0
>>>
>>> while x:
...     print(x)
...     x -= 1
... else:
...     print("X is not valid")
...
X is not valid
>>>
```

### `for` loops

Structure:

```python
for targets in objects_sequence:
    logic_block
else: # no break
    nobreak_block
```

It assigns each item (or collection of items) from `objects_sequence` into `targets` and execute the `logic_block` with this context.

`targets` usually (if no `break` is issued) mantain the last objects from the sequence when the loop ends.

The `else` clause has the same behavior as in `while` loops: run a block of code if no `break` happend during the loop.

Some examples:

```python
>>> for x in ["spam", "eggs", "bacon"]:
...     print(x)
...
spam
eggs
bacon
>>>
```

Another example with sum and multiplication product of a list:

```python
>>> summation = 0
>>> product = 1
>>>
>>> for item in [1, 2, 3, 4]:
...     summation += item
...     product *= item
...
>>> summation
10
>>> product
24
>>>
```

* `for` works with any sequence type or object that respects the iterator protocol:

```python
>>> b = ("and", "you", "are")
>>>
>>> for x in a: print(x)
l
u
m
b
e
r
j
a
c
k
>>>
>>> for y in b: print(y)
and
you
are
>>>
```

* `Tuple unpacking` work in `for` header declarations:

```python
>>> t = [ (1, 2), (3, 4), (5, 6) ]
>>>
>>> for a, b in t:
...     print(a)
...     print(b)
...
1
2
3
4
5
6
>>>
>>> t = [ (1, 2, 2, 1), (3, 4, 4, 3), (5, 6, 6, 5) ]
>>> for a, *b in t:
...     print(a)
...     print(b)
...
1
[2, 2, 1]
3
[4, 4, 3]
5
[6, 6, 5]
>>>
```

* Tuple unpacking and for loops are useful to iterate over dictionaries:

```python
>>> d = {"a": 1, "b": 2, "c": 3}
>>>
>>> for key in d:
...     print(key)
...
a
b
c
>>>
>>> for key, value in d.items():
...     print(key, " -> ", value)
...
a  ->  1
b  ->  2
c  ->  3
>>>
```

* A more complicated `for` example with an inner `for` and an `else` clause:

```python
In [1]: items = ["aaa", 111, (4, 5), 2.01]

In [2]: searches = [(4, 5), 3.14]

In [3]: for search in searches:
   ...:     for item in items:
   ...:         if search == item:
   ...:             print(f"{search} was found!")
   ...:             break # break the for item in items loop
   ...:         else:
   ...:             print(f"{search} was NOT found") # if no break is issued, the search was not found
   ...:
(4, 5) was NOT found
(4, 5) was NOT found
(4, 5) was found!
3.14 was NOT found
3.14 was NOT found
3.14 was NOT found
3.14 was NOT found

In [4]:
```

* To read a file char by char use `_file_.read(1)` and check if it is empty `EOF`:

```python
>>> fp = open("/etc/hostname", "r")
>>>
>>> while True:
...     char = fp.read(1) # read exactly one char
...     if not char:      # EOF returns an empty char. While newlines come as \n.
...         break
...     print(char)
...
T
4
4
0
s
>>>
```

or

```python
>>> fp = open("/etc/hostname", "r")
>>>
>>> for char in fp.read():
...     print(char)
...
T
4
4
0
s


>>>

```

* You can, also, read a file line by line:

using a while:

```python
>>> fp = open("/etc/shells", "r")
>>> while True:
...     line = fp.readline()
...     if not line: break
...     print(line)
...
# /etc/shells: valid login shells

/bin/sh

/bin/bash

/bin/rbash

/bin/dash

>>>
```

Or, using a for:

```python
>>> fp = open("/etc/shells", "r")
>>>
>>> for line in fp.readlines(): print(line)
# /etc/shells: valid login shells

/bin/sh

/bin/bash

/bin/rbash

/bin/dash

>>>
```

You can even omit the `.readlines()` call, which is the default iterator for file objects:

```python
>>> fp = open("/etc/shells", "r")
>>>
>>> for line in fp: print(line)
# /etc/shells: valid login shells

/bin/sh

/bin/bash

/bin/rbash

/bin/dash

>>>
>>> fp.close()
>>>
```

* When in doubt, use `for` loops. Avoid, if possible, `while`.

* `range(start, end, step)` create integers (generator):

> you need to convert it to a `list()` to see the results, as it returns a generator.

> `start` is inclusive, but `end` is exclusive:

```python
>>> # It default starts from zero
>>> list( range(11) )
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> # end is not inclusive
>>> list( range(0, 10) )
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> # To go until 10, end should be 11
>>> list( range(0, 11) )
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>>
>>> # You can define a custom step
>>> list( range(0, 11, 2) )
[0, 2, 4, 6, 8, 10]
>>>
>>> list( range(0, 11, 3) )
[0, 3, 6, 9]
>>>
>>> # It handles negatives
>>> list( range(10, -1, -1) )
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>>
>>>
```

* Iterate using offsets (indexes) instead of an iterator:

```python
>>> lst = [1, 3.14, "spam"]
>>>
>>> for i in range(len(lst)): # len(lst) is 3, as range-end is exclusive, it generates 0, 1, 2
...     print(lst[i])
...
1
3.14
spam
>>>
```

* Indexes can be useful if you need to create slices or something like that:

```python
>>> s = "spam"
>>> for i in range(len(s)):
...     s = s[1:] + s[:1]
...     print(s)
...
pams
amsp
mspa
spam
```

```python
>>> s = "spam"
>>> for i in range(len(s)):
...     x = s[i:] + s[:i]
...     print(x)
...
spam
pams
amsp
mspa
>>>
```

* You can use indexes to skip some items while looping:

```python
>>> s = "hello world"
>>>
>>> for i in range(0, len(s), 2):
...     print(s[i])
...
h
l
o
w
r
d
>>>
```

> Note that you can do the same, in a simpler way, using slices:

```python
>>> s = "hello world"
>>>
>>> for char in s[::2]:
...     print(char)
...
h
l
o
w
r
d
>>>
```

* Indexes and `for` loops are useful to traverse a list while changing it:

```python
>>> s = "hello world"
>>>
>>> for char in s[::2]:
...     print(char)
...
h
l
o
w
r
d
>>>
```

You need to use indexes:

```python
>>> l = [1, 2, 3, 4, 5]
>>>
>>> for i in range(len(l)):
...     l[i] += 1
...
>>> l
[2, 3, 4, 5, 6]
>>>
```

* Travese two sequence in parallel with `zip()`:

* `zip(seq1, seq2, seq3...)` returns a list of tuples pairing elements of the sequences in tuples:

> `zip()` returns a generator, so `list` is necessary.

```python
>>> list( zip([1, 2, 3], [4, 5, 6], [7, 8, 9]) )
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
>>>
```

Its quite useful in `for` loops:

```python
>>> names = ["john", "paul", "manoela"]
>>> ages = [31, 33, 25]
>>>
>>> for name, age in zip(names, ages):
...     print(name, " -> ", age)
...
john  ->  31
paul  ->  33
manoela  ->  25
>>>
```

* `zip()` truncates on the lowest length:

```python
>>> list( zip([1, 2, 3, 4, 5], ["a", "b", "c"]) )
[(1, 'a'), (2, 'b'), (3, 'c')]
>>>
```

* `zip()` can be used to create `dict` also:

```python
>>> keys = ["name", "age"]
>>> items = ["John", 32]
>>>
>>> data = dict( zip(keys, items) )
>>> data
{'name': 'John', 'age': 32}
>>>
```

* If you need to iterate over a sequence and gather the indexes and values, use `enumerate()`:

```python
>>> s = "spam"
>>> for index, value in enumerate(s):
...     print(f"{index}: {value}")
...
0: s
1: p
2: a
3: m
>>>
```

* `os.popen` provides a file-like interface for executing and reading shell commands:

```python
>>> import os
>>>
>>> fp = os.popen("ls /tmp")
>>> fp.readlines()
['sddm-:0-tvDMFr\n',
 'sddm-auth2a1e5e24-f8a7-4255-975f-ec4ddf02ae52\n',
 'ssh-voDvxxKvIxCW\n',
 'systemd-private-9657f3a3970c402b85f01132f2e26ec8-ModemManager.service-lQDJ33\n',
 'systemd-private-9657f3a3970c402b85f01132f2e26ec8-redis-server.service-Jqk3nt\n',
 'systemd-private-9657f3a3970c402b85f01132f2e26ec8-rtkit-daemon.service-eqhFDz\n',
 'systemd-private-9657f3a3970c402b85f01132f2e26ec8-systemd-resolved.service-YJppUU\n',
 'systemd-private-9657f3a3970c402b85f01132f2e26ec8-systemd-timesyncd.service-v3f1nZ\n',
 'tmp.2bOs3ttxT9\n',
 'upd\n',
 'VSCode Crashes\n',
 'xauth-1000-_0\n']
>>> fp.close()
>>>
```

### Iteration protocol

* `iterable`: object that responds to the `iter()` builtin returning an `iterator` object, which returns a value for each `next(iterator)` call.

* An `iterator` object has a method `__next__()` that returns a value each time it is called or raises a `StopIteration` exception. Example, files are `iterators`:

```python
>>> fp = open("/etc/shells")
>>>
>>> fp.__next__()
'# /etc/shells: valid login shells\n'
>>> fp.__next__()
'/bin/sh\n'
>>> fp.__next__()
'/bin/bash\n'
>>> fp.__next__()
'/bin/rbash\n'
>>> fp.__next__()
'/bin/dash\n'
>>> fp.__next__()
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-69-ea64a490840b> in <module>
----> 1 fp.__next__()

StopIteration:
>>>
```

This `__next__()` call and treating the `StopIteration` exception is exactly what `for` does under the hood:

```python
>>> fp = open("/etc/shells")
>>>
>>> for line in fp:
...     print(line)
...
# /etc/shells: valid login shells

/bin/sh

/bin/bash

/bin/rbash

/bin/dash
```

> Its the best way to read a file!

* In Python 2 the method was called `next()` without underscores. In Python 3, it became `__next__`. To enhance compability, a builtin function `next()` was created to call the right method.

```python
>>> fp = open("/etc/shells")
>>>
>>> next(fp)
'# /etc/shells: valid login shells\n'
>>> next(fp)
'/bin/sh\n'
>>> next(fp)
'/bin/bash\n'
>>> next(fp)
'/bin/rbash\n'
>>> next(fp)
'/bin/dash\n'
>>> next(fp)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-80-651d4e07234e> in <module>
----> 1 next(fp)

StopIteration:
>>>
```

* One detail is missing. Before the successive calls to `next(iterator)` the for loop asks the object for an iterator through the builtin `iter(object)`, the `object` then returns an `iterator`, in which the successive `next(iterator)` calls are made. Example:

```python
>>> fp = open("/etc/shells")
>>>
>>> i = iter(fp)
>>> i
<_io.TextIOWrapper name='/etc/shells' mode='r' encoding='UTF-8'>
>>>
>>> next(i)
'# /etc/shells: valid login shells\n'
>>> next(i)
'/bin/sh\n'
>>> next(i)
'/bin/bash\n'
>>> next(i)
'/bin/rbash\n'
>>> next(i)
'/bin/dash\n'
>>> next(i)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-90-a883b34d6d8a> in <module>
----> 1 next(i)

StopIteration:
>>>
```

* Sometimes the `iterable` and the `iterator` are the same objects, a good example are files:

```python
>>> fp = open("/etc/shells")
>>>
>>> iter(fp) is fp
True
>>>
```

But lists, tuples, dictionaries, return different objects as `iterators`:

```python
>>> lst = [1, 2, 3]
>>>
>>> i_lst = iter(lst)
>>> i_lst
<list_iterator at 0x7fcc0578cba8>
>>>
>>> lst is i_lst
False
>>>
>>> lst == i_lst
False
>>>
```

This enables concurrent iterations in different positions:

```python
>>> lst = [1, 2, 3]
>>>
>>> i1 = iter(lst)
>>> i2 = iter(lst)
>>>
>>> next(i1)
1
>>> next(i1)
2
>>>
>>> next(i2)
1
>>>
>>> next(i1)
3
>>>
>>> next(i2)
2
>>>
```

* Dictionaries, for example, are `iterable` too, and their `iterator` return its keys.

```python
>>> d = {"name": "John", "age": 23, "job": "developer"}
>>>
>>> i_d = iter(d)
>>>
>>> next(i_d)
'name'
>>> next(i_d)
'age'
>>> next(i_d)
'job'
>>>
```

You can iterate directly over dicts:

```python
>>> d = {"name": "John", "age": 23, "job": "developer"}
>>>
>>> i_d = iter(d)
>>>
>>> next(i_d)
'name'
>>> next(i_d)
'age'
>>> next(i_d)
'job'
>>>
>>> for key in d:
...     print(key)
...
name
age
job
>>>
```

* All `iterable` objects return a value per time, thats why we use `list()` conversion to see all the values:

```python
>>> r = range(11)
>>>
>>> it_r = iter(r)
>>> next(it_r)
0
>>> next(it_r)
1
>>> next(it_r)
2
>>> next(it_r)
3
>>>
>>>
>>>
>>> r = range(11)
>>>
>>> list(r)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>>
```

* Even `enumerate()` is an `iterable`:

```python
>>> lst = ["spam", "eggs", "bacon"]
>>>
>>> e = enumerate(lst)
>>>
>>> i = iter(e)
>>> next(i)
(0, 'spam')
>>> next(i)
(1, 'eggs')
>>> next(i)
(2, 'bacon')
>>>
```

* The basic `iterator` usage is:

```python
# Get iterator from iterable object with iter()
i = iter(obj)

# Get all values until StopIteration is launched:
while True:
    try:
        v = next(i)
        # do something with v
    except StopIteration:
        break
```

#### list comprehension

* Are an inverted for

* Basic syntax:

```python
>>> s = 'spam'
>>>
>>> z = [c.upper() for c in s]
>>> z
['S', 'P', 'A', 'M']
>>>
```

* Extended syntax with an `if`:

```python
>>> s = 'spam'
>>>
>>> z = [c.upper() * 2 for c in s if c in ('a', 'p')]
>>>
>>> z
['PP', 'AA']
>>>
```

* You can nest `for` and `if` in list comprehensions:

```python
>>> a = ["spam", "eggs", "bacon"]
>>> b = ["america", "bulgaria", "zambia"]
>>>
>>> lst = [f"{x} -> {y}" for x in a if "s" in x for y in b if "b" in y]
>>> lst
['spam -> bulgaria', 'spam -> zambia', 'eggs -> bulgaria', 'eggs -> zambia']
>>>
```

* Basically, the syntax is:

`[expr for_and_if1  aninhanated_for_and_if2 aninhanted_for_and_if3]`...

Which can be translated to:


```python
res = []

for_and_if1:
    for_and_if2:
        for_and_if3:
            res.append( expr )

return res
```

* In Python, every time you read a sequence left-to-right you are using the iterator protocol described (`iter()`, `next()...next...next()`):

Iterator protocolo usage in builtins:

```python
>>> # Many builtins work and/or produce iterators
>>> # Example: a file
>>>
>>> sorted(open("/etc/shells"))
['# /etc/shells: valid login shells\n',
 '/bin/bash\n',
 '/bin/dash\n',
 '/bin/rbash\n',
 '/bin/sh\n']
>>>
>>> list( zip( open("/etc/shells"), open("/etc/shells") ) )
[('# /etc/shells: valid login shells\n',
  '# /etc/shells: valid login shells\n'),
 ('/bin/sh\n', '/bin/sh\n'),
 ('/bin/bash\n', '/bin/bash\n'),
 ('/bin/rbash\n', '/bin/rbash\n'),
 ('/bin/dash\n', '/bin/dash\n')]
>>>
>>> list( enumerate(open("/etc/shells") ))
[(0, '# /etc/shells: valid login shells\n'),
 (1, '/bin/sh\n'),
 (2, '/bin/bash\n'),
 (3, '/bin/rbash\n'),
 (4, '/bin/dash\n')]
>>>
>>> list( open("/etc/shells") )
['# /etc/shells: valid login shells\n',
 '/bin/sh\n',
 '/bin/bash\n',
 '/bin/rbash\n',
 '/bin/dash\n']
>>>
>>> tuple( open("/etc/shells") )
('# /etc/shells: valid login shells\n',
 '/bin/sh\n',
 '/bin/bash\n',
 '/bin/rbash\n',
 '/bin/dash\n')
>>>
>>> "$".join( open("/etc/shells") )
'# /etc/shells: valid login shells\n$/bin/sh\n$/bin/bash\n$/bin/rbash\n$/bin/dash\n'
>>>
>>>
```

Iterator protocol usage in language syntax:

```python
>>> a, b, c, d, e = open("/etc/shells")
>>> a, b, c, d, e
('# /etc/shells: valid login shells\n',
 '/bin/sh\n',
 '/bin/bash\n',
 '/bin/rbash\n',
 '/bin/dash\n')
>>>
>>> a, *b = open("/etc/shells")
>>> a, b
('# /etc/shells: valid login shells\n',
 ['/bin/sh\n', '/bin/bash\n', '/bin/rbash\n', '/bin/dash\n'])
>>>
>>> "/bin/bash\n" in open("/etc/shells")
True
>>>
>>> l = [1, 2, 3]
>>>
>>> l[1:] = open("/etc/shells")
>>> l
[1,
 '# /etc/shells: valid login shells\n',
 '/bin/sh\n',
 '/bin/bash\n',
 '/bin/rbash\n',
 '/bin/dash\n']
>>>
>>> l = ["spam"]
>>> l.extend(open("/etc/shells"))
>>> l
['spam',
 '# /etc/shells: valid login shells\n',
 '/bin/sh\n',
 '/bin/bash\n',
 '/bin/rbash\n',
 '/bin/dash\n']
>>>
```

* Functions have a special `*arg` syntax that unpacks a sequence into positional arguments and support iterables also. So you can, for example, unzip a `zip()` object:

```python
>>> a = ["john", "paul", "amelia"]
>>> b = [3000, 5000, 1500]
>>>
>>> list( zip(a, b) )
[('john', 3000), ('paul', 5000), ('amelia', 1500)]
>>>
>>> x, y = zip( *zip(a, b) )
>>> x, y
(('john', 'paul', 'amelia'), (3000, 5000, 1500))
>>>
>>>
```

> **Caution:** many iterators are exhaustable!

```python
>>> lst = [1, 2, 3]
>>>
>>> mlst = map(lambda x: x + 1, lst)
>>>
>>> list(mlst) # ok!
[2, 3, 4]
>>>
>>> list(mlst) # exhausted!
[]
>>>
```

* Some new iterables in Python 3:

`range()`

```python
>>> r = range(6)
>>> i = iter(r)
>>> next(i)
0
>>> next(i)
1
>>> next(i)
2
>>> next(i)
3
>>> next(i)
4
>>> next(i)
5
>>> next(i)
-------------------------------------------------------------
StopIteration               Traceback (most recent call last)
<ipython-input-206-a883b34d6d8a> in <module>
----> 1 next(i)

StopIteration:
>>>
```

`range()`, despite being an iterator, supports indexing, slicing, and `len()`:

```python
>>> l = range(11)
>>>
>>> l[0:5]
range(0, 5)
>>>
>>> l[6]
6
>>>
>>> len(l)
11
>>>
```

* `range()` returns a inexhaustible iterator, so you can have multiple concurrent:

```python
>>> r = range(11)
>>>
>>> i1 = iter(r)
>>> i2 = iter(r)
>>>
>>> next(i1)
0
>>> next(i1)
1
>>> next(i1)
2
>>>
>>>
>>> next(i2)
0
>>>
```

* Some iterators are exhaustible: `zip`, `map` and `filter`:

```python
>>> a = [1, 2, 3]
>>> b = ['a', 'b', 'c']
>>>
>>> z = zip(a, b)
>>>
>>> # uses the iterator
>>> for pair in z:
...     print(pair)
...
(1, 'a')
(2, 'b')
(3, 'c')
>>>
>>> # exhausted
>>> for pair in z:
...     print(pair)
...
>>>
>>>
```

```python
>>> lst = (-1, -2, -3.14)
>>>
>>> abs_map = map(abs, lst)
>>>
>>> i1 = iter(abs_map)
>>> i2 = iter(abs_map)
>>>
>>> next(i1)
1
>>> next(i2)
2
>>>
```

```python
>>> # filter return only the elements for which the passed function returns True
>>>
>>> lst = [1, 0, '', 'spam', 3.14]
>>> filt_lst = filter(bool, lst)
>>>
>>> for true_el in filt_lst:
...     print(true_el)
...
1
spam
3.14
>>>
>>> # exhausted
>>> for true_el in filt_lst:
...     print(true_el)
...
>>>
```

* `range()` is a really different `iterable`. It supports multiple/concurrent iterators, indexing and slicing.

```python
>>> r = range(0, 11, 2)
>>> list(r) # see the generated numbers
[0, 2, 4, 6, 8, 10]
>>>
>>> r[1]
2
>>>
>>> r[1:3]
range(2, 6, 2)
>>>
>>> i1 = iter(r)
>>> i2 = iter(r)
>>>
>>> next(i1)
0
>>> next(i1)
2
>>>
>>> next(i2)
0
>>>
>>> len(r)
6
>>>
```

> `range()` requires an `iter()` call. You cant iterate directly over it:

```python
>>> r = range(0, 11, 2)
>>>
>>> next(r) # ops! iter is required
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-27-98884c9717c1> in <module>
----> 1 next(r) # ops! iter is required

TypeError: 'range' object is not an iterator
>>>

```

`map`, `zip` and `filter` can be iterated directly, because the object itself is the iterator:

```python
>>> lst = ["spam", "eggs", "bacon"]
>>>
>>> m_lst = map(str.upper, lst)
>>>
>>> next(m_lst)
'SPAM'
>>> next(m_lst)
'EGGS'
>>> next(m_lst)
'BACON'
>>> next(m_lst)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-43-eac1f37a30b8> in <module>
----> 1 next(m_lst)

StopIteration:
>>>
>>> # There is only one iterator, which is the object and is exhausted
>>> new_iter_m_lst = iter(m_lst)
>>> next(new_iter_m_lst)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-46-bcc66cdbe430> in <module>
----> 1 next(new_iter_m_lst)

StopIteration:
>>>
```

* Dictionaries methods `.keys()`, `.values()` and `.items()` return iterator `views` objects.
These `views` reflect at all time the dictionarie structure and respond to the iterator protocol:

```python
>>> d = {"name": "John", "age": 45}
>>>
>>> keys = d.keys()
>>>
>>> ikeys = iter(keys) # you need to require an iterator
>>> next(ikeys)
'name'
>>> next(ikeys)
'age'
>>> next(ikeys)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-52-b89178b9aff7> in <module>
----> 1 next(ikeys)

StopIteration:
>>>
>>> d["job"] = "developer"
>>>
>>> # To see the new key, you need a new iterator throught iter()
>>> ikeys = iter(keys) # you need to require an iterator
>>> next(ikeys)
'name'
>>> next(ikeys)
'age'
>>> next(ikeys)
'job'
>>> next(ikeys)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-59-b89178b9aff7> in <module>
----> 1 next(ikeys)
```

This behavior is repeated by `.values()` and `.items()`:

```python
>>> d["job"] = "developer"
>>>
>>> next(ikeys)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
>>> d = {"name": "John", "age": 45}
>>>
>>> ivalues = iter(d.values())
>>> next(ivalues)
'John'
>>> next(ivalues)
45
>>> next(ivalues)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-64-e0b0802e7d22> in <module>
----> 1 next(ivalues)

StopIteration:
>>>
>>> iitems = iter(d.items())
>>> next(iitems)
('name', 'John')
>>> next(iitems)
('age', 45)
>>> next(iitems)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-68-cee89d66f73b> in <module>
----> 1 next(iitems)

StopIteration:
>>>
>>>
```

* Dict are themselves iterables and respond to `iter()`, returning the `keys_view`:

```python
>>> d = {"name": "John", "age": 45}
>>>
>>> i_d = iter(d)
>>> next(i_d)
'name'
>>> next(i_d)
'age'
>>> next(i_d)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-75-7e3ea04201b3> in <module>
----> 1 next(i_d)

StopIteration:
>>>
>>> i_d2 = iter(d)
>>> next(i_d2)
'name'
>>> next(i_d2)
'age'
>>>
>>> iter(d)
<dict_keyiterator at 0x7f7c0785cb88>
>>> iter(d.keys())
<dict_keyiterator at 0x7f7c07ebf138>
>>>
>>>
```

> To iterate over a sorted sequence of dictionary keys, use `sorted(dict)`:

```python
>>> d = {"z": 3, "b": 10, "x": 15, "a": 1}
>>>
>>> for key in sorted(d):
...     print(key)
...
a
b
x
z
>>>
```


## Documentation and getting help

* emty `dir()`  returns the caller context local variables, just like `locals()`:

```python
>>> dir() # return local variables
['In',
 'Out',
 '_',
 '_1',
 '_2',
 '_3',
 '_4',
 '__',
 '___',
 '__builtin__',
 '__builtins__',
 '__doc__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 '_dh',
 '_i',
 '_i1',
 '_i2',
 '_i3',
 '_i4',
 '_i5',
 '_ih',
 '_ii',
 '_iii',
 '_oh',
 'exit',
 'get_ipython',
 'quit']
>>>
>>> sorted(dir()) == sorted(locals())
True
>>> len(dir()), len(locals())
(34, 34)
>>>
```

* `dir(object)`, `dir(type)` or `dir(module)` return the attributes (methods and variables) of the object/type:

```python
>>> s = "spam"
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
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmod__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'capitalize',
 'casefold',
 'center',
 'count',
 'encode',
 'endswith',
 'expandtabs',
 'find',
 'format',
 'format_map',
 'index',
 'isalnum',
 'isalpha',
 'isdecimal',
 'isdigit',
 'isidentifier',
 'islower',
 'isnumeric',
 'isprintable',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',
 'lower',
 'lstrip',
 'maketrans',
 'partition',
 'replace',
 'rfind',
 'rindex',
 'rjust',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill']
>>>
>>>
>>> dir(float)
['__abs__',
 '__add__',
 '__bool__',
 '__class__',
 '__delattr__',
 '__dir__',
 '__divmod__',
 '__doc__',
 '__eq__',
 '__float__',
 '__floordiv__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getformat__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__int__',
 '__le__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__neg__',
 '__new__',
 '__pos__',
 '__pow__',
 '__radd__',
 '__rdivmod__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rfloordiv__',
 '__rmod__',
 '__rmul__',
 '__round__',
 '__rpow__',
 '__rsub__',
 '__rtruediv__',
 '__setattr__',
 '__setformat__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 '__truediv__',
 '__trunc__',
 'as_integer_ratio',
 'conjugate',
 'fromhex',
 'hex',
 'imag',
 'is_integer',
 'real']
>>>
>>>
>>> import random
>>> dir(random)
['BPF',
 'LOG4',
 'NV_MAGICCONST',
 'RECIP_BPF',
 'Random',
 'SG_MAGICCONST',
 'SystemRandom',
 'TWOPI',
 '_BuiltinMethodType',
 '_MethodType',
 '_Sequence',
 '_Set',
 '__all__',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 '_acos',
 '_bisect',
 '_ceil',
 '_cos',
 '_e',
 '_exp',
 '_inst',
 '_itertools',
 '_log',
 '_pi',
 '_random',
 '_sha512',
 '_sin',
 '_sqrt',
 '_test',
 '_test_generator',
 '_urandom',
 '_warn',
 'betavariate',
 'choice',
 'choices',
 'expovariate',
 'gammavariate',
 'gauss',
 'getrandbits',
 'getstate',
 'lognormvariate',
 'normalvariate',
 'paretovariate',
 'randint',
 'random',
 'randrange',
 'sample',
 'seed',
 'setstate',
 'shuffle',
 'triangular',
 'uniform',
 'vonmisesvariate',
 'weibullvariate']
>>>
```

* `docstrings` are documentation multiline strings declared in the begin of modules, classes and functions, before
any executing code. These strings are read by the python interpreter and saved as the `.__doc__` attribute of these objects.

Example: `sample_module.py`:

```python
"""
Module documentation...
"""

def my_function(a, b):
    """
    My_function documentation
    """
    pass

class Klass:
    """
    Klass documentation...
    """

    def __init__(self, attr1, attr2):
        """
        Constructor method
        """
        pass

# if running as "python sample_module.py"
if __name__ == "__main__":
    print(__doc__) # sample_module.__doc__
    print(my_function.__doc__)
    print(Klass.__doc__)
    print(Klass.__init__.__doc__)

```

Output:

```bash

Module documentation...


    My_function documentation


    Klass documentation...


        Constructor method
```

Almost all objects present in the Python language and in the standard library have docstrings:

```python
>>> print( random.__doc__ )
Random variable generators.

    integers
    --------
           uniform within range

    sequences
    ---------
           pick random element
           pick random sample
           pick weighted random sample
           generate random permutation

    distributions on the real line:
    ------------------------------
           uniform
           triangular
           normal (Gaussian)
           lognormal
           negative exponential
           gamma
           beta
           pareto
           Weibull

    distributions on the circle (angles 0 to 2pi)
    ---------------------------------------------
           circular uniform
           von Mises

General notes on the underlying Mersenne Twister core generator:

* The period is 2**19937-1.
* It is one of the most extensively tested generators in existence.
* The random() method is implemented in C, executes in a single Python step,
  and is, therefore, threadsafe.


>>>
```

The `types` also have docstrings:

```python
>>> print( int.__doc__ )
int(x=0) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
>>>
```

* The `help(ojb)` inspects and prints the docstrings of an object and its attributes in a nice, formatted way:

```python
>>> help(str)
>>>
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
:
```

`help()` mixes object structure, throught introspection, and docstrings.

## Functions

* `def` is excutable code. the function does not exists until `def` is executed.

* `functions` are `objects` that respond to `function()` (`__call__`) method.

* `def` creates a new `function object` and assigns it to the specified name.
This name is a variable/reference as any other. Can be used in lists, dicts, everywhere a variable/reference can be placed.

* `lambda` creates an anonymous functions (that does not have a reference/variable pointing to it) in an one-line statement and returns the function object as result.

* `return` sends an object back to the caller. When no `return` is specified or an empty `result` is used, the caller gets back a `None` value.

* `yield` sends an object back to the caller, but remember where it left off. The next time the function is called, it returns from there.

* `global`: variables defined inside a function are visible only inside the function block.
To change a variable defined in the `module`, the function needs to it in its block with the `global` prefix.

* `nonlocal`: allows the current function scope to change a variable from an outer function scope that wraps the current one.
You need list the variable in the block with a `nonlocal` prefix.

* Objects are passed by assignment (reference). The reference is duplicated. **No object copy is made**.

* arguments are passed by position, unless otherwise defined.
by default, arguments should match the function-defined parameters.
you can pass arguments as keywords: `arg=value` and change the default order.

you can use `*pargs` to allow multiple-flexible positional arguments in the parameters definition,
or `**kwargs` for multiple-flexible keyword arguments.

* `def` is a regular python statement. so it can be used anywhere other statements are used: inside other functions, in `if` blocks, etc:

```python
>>> operation = "+"
>>>
>>> if operation == "+":
...     def step(a, b):
...         return a + b
... elif operation == "*":
...     def step(a, b):
...         return a * b
...
>>>
>>> step(10, 3)
13
>>>
```

* `def` block code is evaluated only when the function is called `()`.

* Remember, function are just objects and their names are normal references.

You can make a copy of the reference and use the function:

```python
>>> def s(a, b):
...     return a + b
...
>>>
>>> plus = s
>>>
>>> plus(10, 20)
30
>>>
```

Being objects, you can even define attributes in it:

```python
>>> def inc(val):
...     return val + getattr(inc, "step", 1)
...
>>>
>>> inc(10)
11
>>> inc.step = 100
>>>
>>> inc(10)
110
>>>
```

* Functions parameters and assignments in its block are `local variables`, visible only in the block scope while running.
They are born when code starts executing and die when the block ends, they arent accessible from outside the block.


## Scopes

* Python looks for names/variables in namespaces. Where you declare a name/variable defines its scope (where it can be found, the namespace its is inserted).

* `functions` have their own namespace to avoid collisions. all names declared inside a function block are part of the function namespace and dont affect the outside. In other words, the variables defined inside a function block are isolated from the outside and only exist during the block execution.

* Python has three different scopes:

1. inside a `def`, creating a `local` variable to that function.
2. in an enclosing `def`, thus being `local` to this function but `nonlocal` to all inner functions.
3. in the module context, thus being a `global`.

```python
>>> x = 10 # global
>>> def outer():
...     y = 20 # nonlocal
...     def inner():
...         z = 30 # local
...         print(z, y, x)
...     return inner
...
>>>
>>> fx = outer() # returns inner
>>> fx() # calls inner
30 20 10
>>>
```

You can even user the same name:

```python
>>> x = 10 # global
>>> def outer():
...     x = 20 # nonlocal
...     def inner():
...         x = 30 # local
...         print("local", x)
...     print("nonlocal", x)
...     return inner
...
...
>>> fx = outer()
nonlocal 20
>>> fx()
local 30
>>>
>>> print("global", x)
global 10
>>>
```

* Each `module` (file) is a global scope.
When imported the variables become attributes of the module object, but are simple variables inside the module code.

* Each file is a global scope and they dont communicate, unless `import` is used.

* All assigments (`=`, `import`, `def`) inside functions are `local` unless declare `nonlocal` or `global`.

* Everytime a function is called, a new `local` scope is created and destructed after the function ends.

* Builtins are always the last namespace looked, as they are avaiable in all modules.

* Scope resolution order: local -> nonlocal -> global

Examples:

function -> module

```python
>>> x = 30
>>> def fx():
...     y = 10
...     print(x, y)
...
>>>
>>> fx()
30 10
>>>
```


inner_function -> outer_function -> module

```python
>>> a = 10
>>>
>>> def outer():
...     b = 20
...     def inner():
...         c = 30
...         print(a, b, c)
...     return inner
...
>>>
>>> fx = outer()
>>> fx()
10 20 30
>>>
```

* The LEGB rule:

1. Inside `def` all assignment creates local variables.

2. Name lookup follows the sequence: Local, Enclosing, Global and Builtin (LEGB)

3. Inside functions, you can declare variables with `global` or `nonlocal` to exceptionally point to outer scopes.
This is required to **change** them. To just read, Python automatically looks up outer scopes (see **2**).

During the lookup, the first match wins.

* The `builtins` module is automatically the last scope searched.
But, to inspect it you need to import it...go figure:

```python
>>> import builtins
>>> dir(builtins)
['ArithmeticError',
 'AssertionError',
 'AttributeError',
 'BaseException',
 'BlockingIOError',
 'BrokenPipeError',
 'BufferError',
 'BytesWarning',
 'ChildProcessError',
 'ConnectionAbortedError',
 'ConnectionError',
 'ConnectionRefusedError',
 'ConnectionResetError',
 'DeprecationWarning',
 'EOFError',
 'Ellipsis',
 'EnvironmentError',
 'Exception',
 'False',
 'FileExistsError',
 'FileNotFoundError',
 'FloatingPointError',
 'FutureWarning',
 'GeneratorExit',
 'IOError',
 'ImportError',
 'ImportWarning',
 'IndentationError',
 'IndexError',
 'InterruptedError',
 'IsADirectoryError',
 'KeyError',
 'KeyboardInterrupt',
 'LookupError',
 'MemoryError',
 'ModuleNotFoundError',
 'NameError',
 'None',
 'NotADirectoryError',
 'NotImplemented',
 'NotImplementedError',
 'OSError',
 'OverflowError',
 'PendingDeprecationWarning',
 'PermissionError',
 'ProcessLookupError',
 'RecursionError',
 'ReferenceError',
 'ResourceWarning',
 'RuntimeError',
 'RuntimeWarning',
 'StopAsyncIteration',
 'StopIteration',
 'SyntaxError',
 'SyntaxWarning',
 'SystemError',
 'SystemExit',
 'TabError',
 'TimeoutError',
 'True',
 'TypeError',
 'UnboundLocalError',
 'UnicodeDecodeError',
 'UnicodeEncodeError',
 'UnicodeError',
 'UnicodeTranslateError',
 'UnicodeWarning',
 'UserWarning',
 'ValueError',
 'Warning',
 'ZeroDivisionError',
 '__IPYTHON__',
 '__build_class__',
 '__debug__',
 '__doc__',
 '__import__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'abs',
 'all',
 'any',
 'ascii',
 'bin',
 'bool',
 'bytearray',
 'bytes',
 'callable',
 'chr',
 'classmethod',
 'compile',
 'complex',
 'copyright',
 'credits',
 'delattr',
 'dict',
 'dir',
 'display',
 'divmod',
 'enumerate',
 'eval',
 'exec',
 'filter',
 'float',
 'format',
 'frozenset',
 'get_ipython',
 'getattr',
 'globals',
 'hasattr',
 'hash',
 'help',
 'hex',
 'id',
 'input',
 'int',
 'isinstance',
 'issubclass',
 'iter',
 'len',
 'license',
 'list',
 'locals',
 'map',
 'max',
 'memoryview',
 'min',
 'next',
 'object',
 'oct',
 'open',
 'ord',
 'pow',
 'print',
 'property',
 'range',
 'repr',
 'reversed',
 'round',
 'set',
 'setattr',
 'slice',
 'sorted',
 'staticmethod',
 'str',
 'sum',
 'super',
 'tuple',
 'type',
 'vars',
 'zip']
>>>
```

* The `builtins` module is always imported by Python and the last step in name resolution, so you can reference it implictly or explictly:

```python
>>> zip
zip
>>>
>>> import builtins
>>> builtins.zip
zip
>>>
>>> zip is builtins.zip
True
>>>
```

* Names defined in inner scopes in the LEGB lookup path overrides the outer definitions in the scope they are declared:

```python
>>> X = 99
>>>
>>> def fx():
...     X = 109 # local X = 100
...     X += 1 # local X = local X + 1
...     print(X)
...
...
>>> fx()
110
>>>
>>> X
99
>>>
```

* From inside a function you can reference `nonlocal` and `global` variables.
But, to change them you need to explictly declare them as `nonlocal` or `global`:

1. Reading a global

```python
>>> CONSTANT = 3.14
>>>
>>> def fx():
...     print(CONSTANT)
...
>>> fx()
3.14
>>>
```

2. Overriding a global

```python
>>> CONSTANT = 3.14
>>>
>>> def fx():
...     CONSTANT = 1.618
...     print(CONSTANT)
...
>>>
>>> fx()
1.618
>>>
>>> print(CONSTANT)
3.14
>>>
```

3. Changing a global

```python
>>> CONSTANT = 3.14
>>>
>>> def fx():
...     global CONSTANT
...     CONSTANT = 1.618
...     print(CONSTANT)
...
>>>
>>> fx()
1.618
>>>
>>> print(CONSTANT)
1.618
>>>
```

4. Creating a variable in the `global` scope:

```python
>>> def fx():
...     global Y
...     Y = 100
...     print(Y)
...
...
>>> fx()
100
>>>
>>> print(Y)
100
>>>
```

* Closures are factory functions, functions that create and return other functions.
The returned function have access to the scope of the creating function even after it was executed.
The inner-created-returned function mantains the outer function scope. This is called state retention:

```python
>>> def fouter():
...     x = 10
...     def finner():
...         print(x)
...     return finner
...
>>> fx = fouter()
>>> fx()
10
>>>
```

* But caution, each inner function return has its own `state`:

```python
>>> def fouter():
...     x = 10
...     def finner():
...         nonlocal x
...         x += 1
...         print(x)
...     return finner
...
>>>
>>> fx1 = fouter()
>>>
>>> fx2 = fouter()
>>>
>>> fx1()
11
>>> fx1()
12
>>> fx1()
13
>>>
>>> fx2()
11
>>> fx2()
12
>>> fx2()
13
>>>
```

Even for mutable types:

```python
>>> def fouter():
...     lst = []
...     def finner():
...         nonlocal lst
...         lst.append("spam")
...         print(lst)
...     return finner
...
>>>
>>> f1 = fouter()
>>> f2 = fouter()
>>>
>>> f1()
['spam']
>>> f1()
['spam', 'spam']
>>> f1()
['spam', 'spam', 'spam']
>>>
>>>
>>> f2()
['spam']
>>> f2()
['spam', 'spam']
>>> f2()
['spam', 'spam', 'spam']
>>>
```

This state replaces the notion of "classes" in some cases.

* `State retention` is true to classes returned from functions also.

* Retainging enclosing scope state with defaults:

* In Python 2, state retention was made passing default arguments to the inner function:

```python
>>> def fouter():
...     lst = []
...     def finner(lst=lst): # assigns a local, finner, lst to the outer fouter-lst
...         lst.append("spam")
...         print(lst)
...     return finner
...
>>>
>>> f1 = fouter()
>>> f2 = fouter()
>>>
>>> f1()
['spam']
>>> f1()
['spam', 'spam']
>>> f1()
['spam', 'spam', 'spam']
>>>
>>> f2()
['spam']
>>> f2()
['spam', 'spam']
>>> f2()
['spam', 'spam', 'spam']
>>>
```

* You define function that calls function which are not defined yet, because function blocks are interpreted only when the function is called.
So you just need to declare the called function before calling the caller function.

```python
>>> def a():
...     b()
...
>>> a()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-2-8d7b4527e81d> in <module>
----> 1 a()

<ipython-input-1-bddf4de40dfd> in a()
      1 def a():
----> 2     b()
      3

NameError: name 'b' is not defined
>>>
>>> def b():
...     print("b!")
...
>>> a()
b!
>>>
```

* `lambda`s also have access to enclosing function scope:

```python
>>> def fouter(incrementer):
...     return lambda value: value + incrementer
...
>>>
>>> finc = fouter(10)
>>>
>>> finc(3)
13
>>>
```

* Caution: if you return multiple functions created through in a loop, they might end up referencing the same value, because there is only one state retained:

```python
>>> def make_incrementers(n):
...     incrementers = []
...     for i in range(1, n + 1):
...         incrementers.append(lambda x: x + i) # the lambda body references i from the enclosing function, but i will be n + 1 when the function is called
...     return incrementers
...
>>> incs = make_incrementers(3)
>>> incs
[<function __main__.make_incrementers.<locals>.<lambda>(x)>,
 <function __main__.make_incrementers.<locals>.<lambda>(x)>,
 <function __main__.make_incrementers.<locals>.<lambda>(x)>]
>>>
>>> incs[0](10)
13
>>> incs[1](10)
13
>>> incs[2](10)
13
>>>
```

To avoid it, you need to make a copy through default arguments:

```python
>>> def make_incrementers(n):
...     incrementers = []
...     for i in range(1, n + 1):
...         incrementers.append(lambda x, i=i: x + i) # i=i makes a local-lambda-scope copy of i
...     return incrementers
...
...
>>>
>>> incs = make_incrementers(3)
>>> incs[0](10)
11
>>> incs[1](10)
12
>>> incs[2](10)
13
>>>
```

* Python looks all enclosing functions scopes (`nonlocal`) before going to the `global` scope:

```python
>>> def f1():
...     x = 10
...     def f2():
...         def f3():
...           print(x)
...         return f3
...     return f2
...
>>> f2 = f1()
>>> f3 = f2()
>>> f3()
10
>>>
>>>
```

* Remember that the state retention (`enclosing scopes`) variables can be made writable if declared using `nonlocal`:

```python
>>> def fouter():
...     x = 10
...     def finner():
...         nonlocal x
...         x += 1
...         print(x)
...     return finner
...
>>> fx = fouter()
>>> fx()
11
>>> fx()
12
>>> fx()
13
>>> fx()
14
>>> fx()
15
>>>
```

But, unlike `global` scope, you cant create a new variable in the enclosing scope:

```python
>>> def fouter():
...     def finner():
...         nonlocal x
...         x = 10
...         print(x)
...     return finner
...
  File "<ipython-input-35-1432c16bf945>", line 3
    nonlocal x
    ^
SyntaxError: no binding for nonlocal 'x' found

>>>
```

`nonlocal` statements require the variable to already be defined when they are read by the interpreter:

```python
>>> x = 10
...
... def fouter():
...     def finner():
...         nonlocal x
...         print(x)
...     return finner
...
  File "<ipython-input-37-f179fe6492c2>", line 5
    nonlocal x
    ^
SyntaxError: no binding for nonlocal 'x' found

>>>
```

while `global` check when the function is called, because the global scope can change between declaration and calling:

```python
>>> def fouter():
...     z = 30
...     def finner():
...         global z
...         print(z)
...     return finner
...
>>>
>>> fx = fouter()
>>> fx()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-40-2d1b3bb81149> in <module>
----> 1 fx()

<ipython-input-38-c62e113b35d2> in finner()
      3     def finner():
      4         global z
----> 5         print(z)
      6     return finner
      7

NameError: name 'z' is not defined
>>>
```

* An example of state using `nonlocal`:

```python
>>> def outer():
...     counter = 0
...     def inner():
...         nonlocal counter
...         counter += 1
...         print(counter)
...     return inner
...
>>>
>>> fx = outer()
>>> fx()
1
>>> fx()
2
>>> fx()
3
>>>
>>>
>>> fx2 = outer()
>>> fx2()
1
>>> fx2()
2
>>>
```

* When you instatiate an object, it gets a copy of the declared class state:

```python
>>> class Test:
...     state = []
...
>>>
>>> t = Test()
>>> t.state.append("spam")
>>>
>>> t.state
['spam']
>>> Test.state
['spam']
>>>
```

its the same as:

```python
>>> class Test:
...     state = []
...
>>>
>>> t = Test()
>>> #
>>> # As function parameters, class attributes are passed by assignment to the objects
>>> #
>>> t.state = Test.state
>>>
>>> t.state
['spam']
>>> Test.state
['spam']
>>>
```

but if you change the instance reference, you dont affect the class:

```python
>>> t.state = [] # new object, t.state and Test.state point to different objects now
>>> t.state.append("eggs")
>>> t.state
['eggs']
>>>
>>> Test.state
['spam']
>>>
```

but caution: instance or classmethods dont look in the class or instance scope, they still follow LEGB rule:

```python
>>> class Test:
...     x = 10
...     def example(self):
...         print(x)
...
>>>
>>> t = Test()
>>> t.example()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-78-4c06bfe216ad> in <module>
----> 1 t.example()

<ipython-input-76-b936780132d6> in example(self)
      2     x = 10
      3     def example(self):
----> 4         print(x)
      5

NameError: name 'x' is not defined
>>>
```

to access the instance attribute use the `self` reference and the class, use the class name:

```python
>>> class Test:
...     x = 10
...     def example(self):
...         print(self.x)
...         print(Test.x)
...
>>> t = Test()
>>> t.example()
10
10
>>>
```

Being different references, you can make them point to different objects:

```python
>>> class Test:
...     x = 10
...     def example(self):
...         print(self.x)
...         print(Test.x)
...     def change(self):
...         self.x = 99
...         Test.x = 11
...
>>>
>>> t = Test()
>>> t.example()
10
10
>>> t.change()
>>> t.example()
99
11
>>>
```

* Again, if both point to the same mutable object, side-effects apply:

```python
>>> class Test:
...     state = []
...
>>>
>>> t = Test()
>>>
>>> t.state.append("spam")
>>> t.state
['spam']
>>>
>>> Test.state
['spam']
>>>
>>> # Diverging them
>>> t.state = []
>>> Test.state = []
>>>
>>> t.state.append("eggs")
>>>
>>> t.state
['eggs']
>>> Test.state
[]
>>>
```

* State retention using function attributes:

```python
>>> def maker(increment):
...     def inc(value):
...         return value + inc.increment
...     inc.increment = increment
...     return inc
...
>>>
>>> inc3 = maker(3)
>>> inc3(10)
13
>>>
>>> inc4 = maker(4)
>>> inc4(10)
14
>>>
```

* function attributes are better than `nonlocal` state.

* You can change mutable objects in enclosing scope without `nonlocal`:

```python
>>> def outer():
...     state = {}
...     def inner(k, v):
...         state[k] = v
...         return state
...     return inner
...
>>>
>>> fx = outer()
>>> fx("a", 10)
{'a': 10}
>>> fx("b", 20)
{'a': 10, 'b': 20}
>>> fx("c", 30)
{'a': 10, 'b': 20, 'c': 30}
>>>
```

## Arguments

* Function arguments are passed by assignment:

```python
>>> def hello(name):
...     print("Hello, ", name)
...
>>>
>>> var = "John"
>>> # Python implictly performs: name=var in the function code block
>>> # remember that whenever we use a variable in Python expressions, it is replaced by the object itself (automatic dereference)
>>> hello(var)
Hello,  John
>>>
```

* Changing the reference inside the block does not affect the passed reference (argument). It is not an aliasing:

```python
>>> def hello(name):
...     name = name.upper() # upper() creates a new object, name starts pointing this new object
...     print("Hello, ", name)
...
>>> var = "John"
>>> hello(var)
Hello,  JOHN
>>>
>>> var # remains unchanged!
'John'
>>>
```

* But, as always, references to mutable objects are suscetible to side-effects:

```python
>>> def spam_appender(lst):
...     lst.append("spam")
...     print(lst)
...
>>>
>>> orig_lst = []
>>> spam_appender(orig_lst)
['spam']
>>>
>>> orig_lst
['spam']
>>>
```

* Function can return multiple values as tuples, lists, sets...

```python
>>> def antecessor_and_sucessor(num):
...     return num-1, num+1
...
>>>
>>> antecessor_and_sucessor(10)
(9, 11)
>>>
```

* The function call assignment creates a copy of the reference passed as argument, thus it is not possible to change the caller reference
from inside the function. To do that, you have to explictly overwrite them with the result of the function:

```python
>>> def square(num):
...     return num * num
...
>>>
>>> val = 10
>>>
>>> val = square(val)
>>> val
100
>>>
```

* Python has many tools to flexibilize the function calls:

1. Positional, classic, method.

Passed arguments match in position the declared parameters in the function header:

```python
>>> def s(a, b):
...     return a + b
...
>>> s(10, 20) # 10 -> a, 20 -> b
30
>>>
```

In this method, you should respect the order and quantity:

```python
>>> def s(a, b):
...     return a + b
...
>>>
>>> s(20, 10) # inverting the order you also invert the assignment order: a=20, b=10 now
30
>>>
```

2. You can use the parameters name as keywords to ignore the order:

```python
>>> def upper_lower(a, b):
...     print(a.upper())
...     print(b.lower())
...
>>> upper_lower("Spam", "eGGs")
SPAM
eggs
>>>
>>> upper_lower(b="Spam", a="eGGs") # subvert the order
EGGS
spam
>>>
```

Caution, once you use a keyword argument, you can use a positional argument anymore:

```python
>>> def upper_lower(a, b):
...     print(a.upper())
...     print(b.lower())
...
>>>
>>> upper_lower(a="Spam", "eGGs")
  File "<ipython-input-30-6e4279792f71>", line 1
    upper_lower(a="Spam", "eGGs")
                         ^
SyntaxError: positional argument follows keyword argument

>>>
```

3. Default values, turning some parameters optional as they assum a default value if not passed:

```python
>>> def pow(num, pot=2):
...     return num ** pot
...
>>>
>>> pow(10)
100
>>>
>>> pow(10, 3)
1000
>>>
>>> pow(pot=4, num=2)
16
>>>
```

4. Varargs: you can collect multiple positional arguments (`*args`) or multiple keyword arguments (`**kwargs`):

```python
>>> def multiple_pos(a, b, *c):
...     print(a, b, c)
...
>>>
>>> multiple_pos(10, 20, 30, 40, 50)
10 20 (30, 40, 50)
>>>
```

The remainder positional arguments `*c` are aglutinated in a single `tuple`.

You can vararg keyword arguments also into a dictionarie:

```python
>>> def varargs_keywords(a, b, **c):
...     print(a, b, c)
...
>>>
>>> varargs_keywords(10, 20, name="john", age=30)
10 20 {'name': 'john', 'age': 30}
>>>
```

Caution: you cant pass a keyword argument to a positional remaind collector or a position into a keywords collector:

```python
>>> def varargs_positional(a, b, *c):
...     print(a, b, c)
...
>>>
>>> varargs_positional(10, 20, name="john")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-40-a5812c406e6d> in <module>
----> 1 varargs_positional(10, 20, name="john")

TypeError: varargs_positional() got an unexpected keyword argument 'name'
>>>
```

```python
>>> def varargs_keywords(a, b, **c):
...     print(a, b, c)
...
>>>
>>> varargs_keywords(10, 20, 30)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-42-e195f875fab9> in <module>
----> 1 varargs_keywords(10, 20, 30)

TypeError: varargs_keywords() takes 2 positional arguments but 3 were given
>>>
```

But you can use both collectors together, being the `keywords` always the last:

```python
>>> def varargs_positional_and_keywords(a, b, *c, **d):
...     print(a, b, c, d)
...
>>> varargs_positional_and_keywords(10, 20, 30, 40, 50, name="john", age=30)
10 20 (30, 40, 50) {'name': 'john', 'age': 30}
>>>
>>>
```

You can omit collector parameters `*args` and `**kwargs`, which will be then empty tuples and dicts:

```python
>>> def varargs_positional(a, b, *c):
...     print(a, b, c)
...
>>>
>>> varargs_positional(10, 20)
10 20 ()
>>>
```

```python
>>> def varargs_keywords(a, b, **c):
...     print(a, b, c)
...
>>>
>>> varargs_keywords(10, 20)
10 20 {}
>>>
```

* You can unpack sequences or dictionaries in the call as, respectively, positional arguments or keywords arguments:

```python
>>> numbers = [1, 3]
>>>
>>> def add(a, b):
...     return a + b
...
>>> add(*numbers) # numbers[0] becomes a, and numbers[1] becomes b
4
>>>
```

* Function **calls** should follow the order:

1. positional args;
2. keyword args;
3. *positional_collection;
4. **keywords_collection;


* Function `headers` shoud follow the order:

1. positional args;
2. default keywords args;
3. *positional_collection;
4. keyword only arguments;
5. **keywords_collection;

* You cant pass an argument multiple times:

```python
>>> def u_and_l(a, b):
...     print(a.upper())
...     print(b.lower())
...
>>>
>>> u_and_l(a="a", b="b", a="c")
  File "<ipython-input-53-24792643517d>", line 1
    u_and_l(a="a", b="b", a="c")
                         ^
SyntaxError: keyword argument repeated

>>>
```

* Function parameters and the function header can have annotations, which are save in the function object:

```python
>>> def add(a:int, b:int) -> int:
...     return a + b
...
>>>help(add)

Help on function add in module __main__:

add(a:int, b:int) -> int
(END)
```

these annotation are not inforce during runtime:

```python
>>> add("spam", "eggs")
'spameggs'
>>>
```

We will talk about them later.

* Lets see some examples to consolidate the learning:

1. positional

```python
>>> def f(a, b, c):
...     print(a, b, c)
...
>>> f(1, 3.14, "spam")
1 3.14 spam
>>>
```

> If you define three positional args, you need to call the function with three positional in the specified order.

2. keywords. you can bypass the order of the header definition using keywords arguments:

```python
>>> def f(a, b, c):
...     print(a, b, c)
...
>>>
>>> f(c=1, b=2, a=3)
3 2 1
>>>
```

3. You can mix positional and keywords, but after the first keywords, all other arguments must be keywords:

```python
>>> def f(a, b, c):
...     print(a, b, c)
...
>>>
>>> f(1, c=2, b=3)
1 3 2
>>>
```

4. defaults.

Make some arguments optional, giving them default values if not specified during the call.

```python
>>> def f(a, b=2, c=3):
...     print(a, b, c)
...
>>>
>>> f(10)
10 2 3
>>> f(10, 20)
10 20 3
>>> f(10, 20, 30)
10 20 30
>>>
```

You can provide only some keyword arguments, without caring for order:

```python
>>> def f(a, b=2, c=3):
...     print(a, b, c)
...
>>>
>>> f(1, c=30)
1 2 30
>>>
>>> f(10, b=95)
10 95 3
>>>
>>> f(33, c=42, b=12)
33 12 42
>>>
```

In the examples, `a`, for being positional, is still required.

* The assignment-like expression mean different things in a function call and in a function header definition.

1. In the function header definition, it means an argument with a default, thus optional:

```python
>>> def pow(num, value=2):
...     return num ** value
...
>>> pow(2)
4
>>>
>>>
```

2. In a function call, it means a name resolution approach, which makes the ordering optional:

```python
>>> def add(a, b):
...     return a + b
...
>>> add(b=10, a=30)
40
>>>
```

**Important:** One common mistake is to use a mutable object as a default value for an argument.

The function definition is executed only once, meaning that only a single default object is created, therefore
it is reused in every function call:

```python
>>> def append(value, lst=[]): # a single list is created in memory. if not passed as argument, the same object will be used in every call
...     lst.append(value)
...     return lst
...
>>>
>>> append("spam")
['spam']
>>> append("eggs")
['spam', 'eggs']
>>>
>>> new_lst = []
>>> append("bacon", new_lst)
['bacon']
>>>
```

To avoid that, move the default value assignment to the function body:

```python
>>> def append(value, lst=None):
...     if lst is None:
...         lst = []
...
...     lst.append(value)
...     return lst
...
>>>
>>> append("spam")
['spam']
>>> append("eggs")
['eggs']
>>>
>>> l = []
>>> append("spam", l)
['spam']
>>> append("eggs", l)
['spam', 'eggs']
>>>
```

* Varargs in function header definition:

1. Collecting unmatched positional arguments `*args`:

```python
>>> def f(*args):
...     print(type(args))
...     print(args)
...
>>>
>>> f(1, 2, 3)
<class 'tuple'>
(1, 2, 3)
>>>
```

2. Collecting keywords argument in a `dict()`:

```python
>>> def f(**kwargs):
...     print(type(kwargs))
...     print(kwargs)
...
>>> f(a=1, b=2, c=3)
<class 'dict'>
{'a': 1, 'b': 2, 'c': 3}
>>>
```

3. You can combine positional arguments, `*args` and `**kwargs` to create really flexible function calls:

```python
>>> def f(a, *args, **kwargs):
...     print(a, args, kwargs)
...
>>>
>>> f(1, 2, 3, 4, x="spam", y="eggs")
1 (2, 3, 4) {'x': 'spam', 'y': 'eggs'}
>>>
```

* You can use `*sequence` and `**dict` in function calls:

1. `*sequence` unpacks the sequence into positional arguments:

```python
>>> def f(a, b, c):
...     print(a)
...     print(b)
...     print(c)
...
>>>
>>> lst = [1, 2, 3]
>>>
>>> f(*lst) # same as f(1, 2, 3)
1
2
3
>>>
```

The quantity still needs to match:

```python
>>> lst1 = [1, 2]
>>> lst2 = [1, 2, 3, 4]
>>>
>>> def f(a, b, c):
...     print(a)
...     print(b)
...     print(c)
...
>>>
>>> f(*lst1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-14-e0a7996d1e7c> in <module>
----> 1 f(*lst1)

TypeError: f() missing 1 required positional argument: 'c'
>>>
>>> f(*lst2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-001413d28f47> in <module>
----> 1 f(*lst2)

TypeError: f() takes 3 positional arguments but 4 were given
>>>
```

2. `**dictionary` unpacks the dict into a list of keyword arguments `key=value`:

```python
>>> def f(a, b, c):
...     print(a)
...     print(b)
...     print(c)
...
>>>
>>> d = {
...     "a": 1,
...     "b": 2,
...     "c": 3
... }
>>>
>>> f(**d) # same as f(a=1, b=2, c=3)
1
2
3
>>>
```

3. You can mix positional, `*args` and `*kwargs`:

```python
>>> def f(a, b, c, d, e):
...     print(a)
...     print(b)
...     print(c)
...     print(d)
...     print(e)
...
>>>
>>> args = (2, 3)
>>> kwargs = {"d": 4, "e": 5}
>>>
>>> f(1, *args, **kwargs)
1
2
3
4
5
>>>
```

The unpacking `*args` syntax in function calls accepts any `iterable`.

* The `*args` and the `**kwargs` syntax is useful for wrapper functions:

```python
>>> def debug(fx, *args, **kwargs):
...     print("Calling", fx, "with arguments", args, "and keyword arguments", kwargs)
...     fx(*args, **kwargs)
...
>>>
>>> def f(a, b, c, d, e, f):
...     print(a, b, c, d, e, f)
...
>>> t = 1, 2, 3
>>> d = {"d": 4, "e": 5, "f": 6}
>>>
>>> debug(f, *t, **d)
Calling <function f at 0x7ff9c1906e18> with arguments (1, 2, 3) and keyword arguments {'d': 4, 'e': 5, 'f': 6}
1 2 3 4 5 6
>>>
```

* Keyword only arguments are named arguments declared after the `*args` in the function header:

```python
>>> def f(a, *b, c):
...     print(a, b, c)
...
>>>
>>> f(10, 1, 2, 3, c=99)
10 (1, 2, 3) 99
>>>
>>> # you need to pass c as a keyword argument
>>> f(10, 1, 2, 3, 99)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-45-c020b26c9cb0> in <module>
----> 1 f(10, 1, 2, 3, 99)

TypeError: f() missing 1 required keyword-only argument: 'c'
>>>
```

* You can use a single `*` instead of `*args` to create a keyword only function:

```python
>>> def f(*, a, b, c):
...     print(a, b, c)
...
>>>
>>> f(1, 2, 3) # all arguments should be keywords
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-47-a36a0be0faac> in <module>
----> 1 f(1, 2, 3) # all arguments should be keywords

TypeError: f() takes 0 positional arguments but 3 were given
>>>
>>> f(a=1, b=2, c=3) # all arguments should be keywords
1 2 3
>>>
```

Or a function that accept some positional arguments, but other should be passed as keywords:

```python
>>> def f(a, b, *, c):
...     print(a)
...     print(b)
...     print(c)
...
>>>
>>> f(1, 2, c=3)
1
2
3
>>>
```

Another example:

```python
>>> def knownly(a, *, b, c):
...     print(a, b, c)
...
>>>
>>> knownly(1, c=3, b=2)
1 2 3
>>>
>>> knownly(c=3, b=2, a=1)
1 2 3
>>>
>>> knownly(1, 2, 3) # ops! b and c must be keywords
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-56-88c29389ade0> in <module>
----> 1 knownly(1, 2, 3) # ops! b and c must be keywords

TypeError: knownly() takes 1 positional argument but 3 were given
>>>
>>> knownly(1, 2, b=3, c=4) # only one positional allowed
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-57-42c2a13692fd> in <module>
----> 1 knownly(1, 2, b=3, c=4) # only one positional allowed

TypeError: knownly() takes 1 positional argument but 2 positional arguments (and 2 keyword-only arguments) were given
>>>
>>> knownly(1) # you need to pass b and c as keyword
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-58-43e8c596fb62> in <module>
----> 1 knownly(1) # you need to pass b and c as keyword

TypeError: knownly() missing 2 required keyword-only arguments: 'b' and 'c'
>>>
```

* The `*` alone indicates that the function does not accept variable positional arguments, but that after it `*` all arguments should be keywords.

* Mandatory keyword arguments can have defaults too:

```python
>>> def f(a, *, b=2, c=3):
...     print(a, b, c)
...
>>>
>>> f(1)
1 2 3
>>>
>>> f(1, 2, 3) # no! b and c still must be keyword args
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-61-9d43a16a342c> in <module>
----> 1 f(1, 2, 3) # no! b and c still must be keyword args

TypeError: f() takes 1 positional argument but 3 were given
>>>
>>> f(1, b=20, c=30)
1 20 30
>>>
>>> f(1, b=20)
1 20 3
>>> f(1, c=30)
1 2 30
>>> f(1, c=30, b=20) # you can subvert the order
1 20 30
>>>
```

* Mandatory keyword-only arguments should come after the `*args` or `*` positional collector.
Before, they are positional arguments with default values:

```python
>>> def f(a, b=2, *, c):
...     print(a, b, c)
...
>>>
>>> f(1, c=3)
1 2 3
>>> f(1, 2, 3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-69-1c2a18ab906a> in <module>
----> 1 f(1, 2, 3)

TypeError: f() takes from 1 to 2 positional arguments but 3 were given
>>> f(1, 2, c=3)
1 2 3
>>>
```

## More on function

* Python supports recursion:

```python
# summation
>>> def summation(*args):
...     if not args: return 0
...     return args[0] + summation(*args[1:])
...
>>>
>>> summation(1, 2, 3)
6
>>> summation(1, 2, 3, 4, 5)
15
>>>
```

Each call has its own state (its own `args`), see:

```python
>>> def summation(*args):
...     print(args)
...     if not args: return 0
...     return args[0] + summation(*args[1:])
...
>>>
>>> summation(1, 2, 3)
(1, 2, 3)
(2, 3)
(3,)
()
6
>>> summation(1, 2, 3, 4, 5)
(1, 2, 3, 4, 5)
(2, 3, 4, 5)
(3, 4, 5)
(4, 5)
(5,)
()
15
>>>
```

Another, more elegant implementation:

```python
>>> def summation(first, *rest):
...     print(first, rest)
...     if not rest: return 0
...     return first if not rest else first + summation(*rest)
...
>>>
>>> summation(1, 2, 3, 4, 5)
1 (2, 3, 4, 5)
2 (3, 4, 5)
3 (4, 5)
4 (5,)
5 ()
15
>>>
```

* Recursion can be direct, as the above example, or indirect (when one function calls another that calls the caller back):

```python
>>> def summation(l):
...     if not l: return 0
...     return summation_step(l)
...
>>>
>>> def summation_step(l):
...     return l[0] + summation(l[1:])
...
>>>
>>> summation([1, 2, 3, 4, 5])
15
>>>
```

* In Python recursion is not the best way to do things. Simpler loops are recommended.

* But recursion is perfect ofr handling arbitrary strucutres. Example: summation of a list of lists `[1, [2, [3, 4], 5], 6, [7, 8]]`:

```python
>>> def summation(lst):
...     tot = 0
...     for item in lst:
...         if isinstance(item, list):
...             tot += summation(item)
...         else:
...             tot += item
...     return tot
...
>>>
>>> summation([1, [2, [3, [4, [5]]]]])
15
>>> summation([[[[[1], 2], 3], 4], 5])
15
>>>
```

* Internally, recursion is implemented as a stack. So you can achieve the same results with your own stack or queue:

```python
>>> # queue, first in, first out - breadth first
>>> def summation(lst):
...     total = 0
...     items = list(lst)
...     while items:
...         item = items.pop(0)
...         if isinstance(item, list):
...             items.extend(item)
...         else:
...             total += item
...     return total
...
>>>
>>> summation([1, [2, [3, [4, [5]]]]])
15
>>> summation([[[[[1], 2], 3], 4], 5])
15
>>>
```

Or, more accurately, as a stack last-in first-out:

```python
>>> # stack, last-in, first-out, depth first
>>> def summation(lst):
...     total = 0
...     items = list(lst)
...     while items:
...         item = items.pop()
...         if isinstance(item, list):
...             items[:0] = item
...         else:
...             total += item
...     return total
...
>>> summation([1, [2, [3, [4, [5]]]]])
15
>>> summation([[[[[1], 2], 3], 4], 5])
15
>>>
```

* Python limits the number of recursive call (1000 calls) to avoid infinite loops, to increase this limit:

```python
>>> sys.getrecursionlimit()         # 1000 calls deep default
1000
>>> sys.setrecursionlimit(10000)    # Allow deeper nesting
```

* Python function are full-featured objects, supporting attributes assignment and annotations.

* Function name are just references to function objects, thus they can be reassigned, returned, etc. Just like any other reference:

```python
>>> def echo(msg):
...     print(msg)
...
>>>
>>> output = echo
>>> output("name")
name
>>>
```

* You can pass function as arguments:

```python
>>> def apply(fx, obj):
...     return fx(obj)
...
>>>
>>> apply(str.upper, "spam!")
'SPAM!'
>>>
>>> apply(str.lower, "SPAM!")
'spam!'
>>>
```

* Function objects can be used in data strucutres:

```python
>>> actions = [str.upper, str.lower, str.title]
>>>
>>> message = "Hello world"
>>>
>>> for action in actions:
...     print( action(message) )
...
HELLO WORLD
hello world
Hello World
>>>
```

* The only thing special about a function object is that it respond to a function call expression: **refence()** trought a method named `__call__()`.

* And, lastly, functions can be created from inside another function and return. This is named as a "closure".
Remember that the returned function mantains the scope of the enclosing scope (state of the functions enclosing it):

```python
>>> def a(_a):
...     def b(_b):
...         def c():
...             print(_a, _b)
...         return c
...     return b
...
>>>
>>> b = a(10)
>>> c = b(20)
>>> c()
10 20
>>>
>>> b2 = a(100)
>>> c2 = b2(200)
>>> c2()
100 200
>>>
```

* Function are object and these objecs contain some interesting attributes:

`__code__` attribute

```python
>>> def fx(a, b=10, *args, c=30, **kwargs):
...     print(a, b, args, c, kwargs)
...
>>>
>>> fx.__code__ # function code object
<code object fx at 0x7ff07f33d810, file "<ipython-input-27-f1c153566186>", line 1>
>>>
>>> fx.__code__.co_argcount
2
>>> fx.__code__.co_code
b't\x00|\x00|\x01|\x03|\x02|\x04\x83\x05\x01\x00d\x00S\x00'
>>> fx.__code__.co_consts
(None,)
>>> fx.__code__.co_filename
'<ipython-input-27-f1c153566186>'
>>> fx.__code__.co_firstlineno
1
>>> fx.__code__.co_consts
(None,)
>>> fx.__code__.co_freevars
()
>>> fx.__code__.co_nlocals
5
>>> fx.__code__.co_varnames
('a', 'b', 'c', 'args', 'kwargs')
>>> fx.__code__.co_name
'fx'
>>>
```

* Function attributes: you can attach attributes to function objects, just like any other object:

```python
>>> def fx():
...     print(fx.counter)
...
...
>>>
>>> fx.counter = 0
>>> fx()
0
>>>
>>> fx.counter += 1
>>> fx()
1
>>>
```

Its a way to mantain state between function calls, but to do this properly, you need to use a factory function, so a new function object is created each time.

* You can annotate function signatures in Python 3. But this information is not used by the interpreter, that only attachs it to an `__annotations__` attribute, usually used by other tools:

```python
>>> def add(a:int=0, b:int=0) -> int:
...     return a + b
...
>>> add()
0
>>>
>>> add(10)
10
>>> add(10, 20)
30
>>>
>>> add.__annotations__
{'a': int, 'b': int, 'return': int}
>>>
```

Annotations can be any valid Python expression:

```python
>>> def fx(a:"spam", b:2+2, c:3/3) -> "spam".upper():
...     pass
...
>>>
>>> fx.__annotations__
{'a': 'spam', 'b': 4, 'c': 1.0, 'return': 'SPAM'}
>>>
```

* You can annotate and use defaults:

```python
>>> def fx(a:"first parameter"=0, b:"second param"=10) -> "spam".upper():
...     print(a, b)
...     return "SPAM"
...
...
>>>
>>> fx.__annotations__
{'a': 'first parameter', 'b': 'second param', 'return': 'SPAM'}
>>> fx()
0 10
'SPAM'
>>>
```

> Annotations cant be used in lambda expressions.

* **lambdas** create anonymous functions and return this object. Are expressions and can be used pretty much everywhere in Python code.

* `lambda` general form:

`lambda arg1, arg2, ...: expression_which_result_is_returned`

The expression can make use of the passed arguments. Remember that the LEGB rule for name scope resolution still applies.

* `lambda` are expressions, thus can appear in places where the `def` statement cannot: inside lists declarations, etc.

* `lambda` should be a single expression, not a block.

* `lambda` can have defaults too:

```python
>>> f = lambda a=1, b=2: print(a, b)
>>>
>>> f()
1 2
>>>
>>> f(10, 20)
10 20
>>>
```

* `lambda` follow the LEGB rule also:

```python
>>> global_var = "spam"
>>>
>>> def enclosing(enclosing_var):
...     inner = lambda local_var: print(global_var, enclosing_var, local_var)
...     return inner
...
>>>
>>> inner = enclosing("eggs")
>>> inner("bacon")
spam eggs bacon
>>>
```

* `lambda` accept all the parameters definition techniques and arguments passing:

```python
>>> f = lambda a, *b, **c: print(a, b, c)
>>>
>>> f(1, 2, 3, x=10, y=20)
1 (2, 3) {'x': 10, 'y': 20}
>>>
>>> f(1, *[2, 3], **{"x":10, "y":20})
1 (2, 3) {'x': 10, 'y': 20}
>>>
```

* `lambda` are useful for multiway branche switches:

```python
>>> incrementer_table = {
...     "two": lambda x: x + 2,
...     "three": lambda x: x + 3,
...     "four": lambda x: x + 4,
...     "five": lambda x: x + 5
... }
>>>
>>> two_incrementer = incrementer_table["two"] # the index could be given by the user, dinamically
>>>
>>> two_incrementer(10)
12
>>>
```

* You can implement selection logic using the `if` ternary operator inside lambdas:

```python
>>> lower = lambda a, b: a if a < b else b
>>>
>>> lower(3, 5)
3
>>> lower(30, 5)
5
>>>
```

* `lambda` can have loops using functional tools like `map()`, `filter()` or list comprehensions:

```python
>>> upper_all = lambda lst: map(str.upper, lst)
>>> list( upper_all(["spam", "eggs", "bacon"]) )
['SPAM', 'EGGS', 'BACON']
>>>
```

* Remember: `lambdas`, when created inside other function, follow the LEGB rule, thus having access to the enclosing state:

```python
>>> def greeter_maker(greet):
...     return lambda name: print(greet, name)
...
>>>
>>> bazinga_greeter = greeter_maker("Bazinga!")
>>> bazinga_greeter("John")
Bazinga! John
>>>
```

* `lambda` are very common in Gui toolkits api usage. An example with `tkinter`:

```python
>>> import tkinter
>>>
>>> # When the button is pressed, a message is print
>>> x = tkinter.Button(text="Press me", command=lambda: print("Pressed!"))
>>> x.pack()
>>>
>>> tkinter.mainloop()
Pressed!
Pressed!
>>>
```

* Functional tools:

1. `map()` applies a function to each item of the sequence and collect the results in a list:

```python
>>> lst = [1, 2, 3]
>>>
>>> incremented_lst = list( map(lambda x: x + 10, lst) )
>>> incremented_lst
[11, 12, 13]
>>>
```

2. `map()`, if given multiple sequences and the function supports multiple arguments, it takes one from each sequence:

```python
>>> list( map(lambda a, b, c: print(a, b, c), [1, 2, 3], [4, 5, 6], [7, 8, 9]) )
1 4 7
2 5 8
3 6 9
[None, None, None]
>>>
```

The sequence with the smaller size determines the end of the iteration:

```python
>>> list( map(lambda a, b, c: print(a, b, c), [1, 2, 3], [4, 5, 6], [7, 8]) )
1 4 7
2 5 8
[None, None]
>>>
```

3. `filter()` applies a function to a list and collects the values for which the function returns `True`:

```python
>>> list( filter(str.isdigit, ["10", "30", "40", "spam", "55", "3.14"]) )
['10', '30', '40', '55']
>>>
```

4. `functools.reduce(fx, seq)` takes the first and second argument from a sequence and executes an expression.
The result is applied in the same expression with the third argument, and so on, result with fourth, until the seq is exhausted:

```python
>>> from functools import reduce
>>>
>>> reduce(lambda x, y: x + y, [1, 2, 3, 4]) # 1 + 2 = 3 / 3 + 3 = 6 / 6 + 4 = 10
10
>>>
```

5. Lastly, you should check the `operator` module. It brings functions that correspond to some expressions in Python and are useful for functional programming techniques:

```python
>>> import operator
>>>
>>> operator.add(2, 3)
5
>>> operator.mul(2, 3)
6
>>> index_2 = operator.itemgetter(2)
>>>
>>> index_2(["a", "b", "c"])
'c'
>>>
>>> name_getter = operator.itemgetter("name")
>>> name_getter({"age": 10, "name": "John"})
'John'
>>>
```

* Remember that list comprehensions can have nested for loops and if statements:

```python
>>> [(x, y, x+y) for x in range(11) if x % 2 == 0 for y in range(11) if y % 2 != 0]
[(0, 1, 1),
 (0, 3, 3),
 (0, 5, 5),
 (0, 7, 7),
 (0, 9, 9),
 (2, 1, 3),
 (2, 3, 5),
 (2, 5, 7),
 (2, 7, 9),
 (2, 9, 11),
 (4, 1, 5),
 (4, 3, 7),
 (4, 5, 9),
 (4, 7, 11),
 (4, 9, 13),
 (6, 1, 7),
 (6, 3, 9),
 (6, 5, 11),
 (6, 7, 13),
 (6, 9, 15),
 (8, 1, 9),
 (8, 3, 11),
 (8, 5, 13),
 (8, 7, 15),
 (8, 9, 17),
 (10, 1, 11),
 (10, 3, 13),
 (10, 5, 15),
 (10, 7, 17),
 (10, 9, 19)]
>>>
```

Is the same as:

```python
>>> res = []
>>>
>>> for x in range(11):
...     if x % 2 == 0:
...         for y in range(11):
...             if y % 2 != 0:
...                 res.append( (x, y, x+y) )
...
>>> res
[(0, 1, 1),
 (0, 3, 3),
 (0, 5, 5),
 (0, 7, 7),
 (0, 9, 9),
 (2, 1, 3),
 (2, 3, 5),
 (2, 5, 7),
 (2, 7, 9),
 (2, 9, 11),
 (4, 1, 5),
 (4, 3, 7),
 (4, 5, 9),
 (4, 7, 11),
 (4, 9, 13),
 (6, 1, 7),
 (6, 3, 9),
 (6, 5, 11),
 (6, 7, 13),
 (6, 9, 15),
 (8, 1, 9),
 (8, 3, 11),
 (8, 5, 13),
 (8, 7, 15),
 (8, 9, 17),
 (10, 1, 11),
 (10, 3, 13),
 (10, 5, 15),
 (10, 7, 17),
 (10, 9, 19)]
>>>
```

* You can have a list comprehension nested in a list comprehension:

```python
>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]
>>>
>>> squared_matrix = [[col * col for col in row] for row in matrix]
>>> squared_matrix
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
>>>

```

* Generator example:

```python
>>> def gensquares(n):
...     for i in range(n):
...         yield i ** 2
...
>>>
>>> iterator = gensquares(3)
>>>
>>> iterator
<generator object gensquares at 0x7f54f0a02728>
>>>
>>> next(iterator)
0
>>> next(iterator)
1
>>> next(iterator)
4
>>> next(iterator)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-14-4ce711c44abc> in <module>
----> 1 next(iterator)

StopIteration:
>>>
>>>
```


* To end the generation of values generator functions should use an empty `return` or let control reach the end of the function body:

```python
>>> def gensquares2(n):
...     for i in range(n):
...         if i > 5: return # end generation
...         yield i ** 2
...
>>>
>>> for sq in gensquares2(10):
...     print(sq)
...
0
1
4
9
16
25 # Stops at 5 square
>>>
```

* `iter()` calls on `generators` are unecessary, as generators are their own iterators, supporting `next()` themselves:

```python
>>> def gensquares(n):
...     for i in range(n):
...         yield i ** 2
...
>>>
>>> g = gensquares(10)
>>>
>>> g is iter(g) # The same object ?
True
>>>
>>> next(g) # call next directly on g
0
>>> next(g)
1
>>> next(g)
4
>>> next(g)
9
>>> next(g)
16
>>> next(g)
25
>>> next(g)
36
>>> next(g)
49
>>> next(g)
64
>>> next(g)
81
>>> next(g)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-32-e734f8aca5ac> in <module>
----> 1 next(g)

StopIteration:
>>>
```

* Being iterables, generator functions can be used wherever iterators can be used:

```python
>>> def upper(s):
...     for letter in s:
...         yield letter.upper()
...
>>>
>>> list( upper("spam") )
['S', 'P', 'A', 'M']
>>>
>>> a, b, c, d = upper("spam")
>>> a, b, c, d
('S', 'P', 'A', 'M')
>>>
>>>
>>> for i, l in enumerate(upper("spam")):
...     print(i, l)
...
0 S
1 P
2 A
3 M
>>>
```

* Communicating with a `generator` using the `send` protocol:

Since Python 2.5 the `yield` is both an statement as an expression, meaning you can use:

`yield val...` or `sent_value = yield val...`

But how we pass `sent_value` ? Calling the `generator.send(value)` method, which acts like a `next()` call, but allows argument passing:

```python
>>> def gen():
...     while True:
...         message = yield
...         print(message)
...
>>>
>>> g = gen() # Creates the generator
>>>
>>> # The generator has not executed yet, so a next() call is necessary
>>> next(g)
>>>
>>> # Now we can send informations
>>> g.send("Hello")
Hello
>>>
>>> g.send("World")
World
>>>
```

* **Generator Expressions**

Just like list comprehensions but surrounded by parenthesis, given origin to generator objects:

```python
>>> lst_squares = [x ** 2 for x in range(10)]
>>> lst_squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>>
>>> gen_squares = (x ** 2 for x in range(10))
>>> gen_squares
<generator object <genexpr> at 0x7f54f096e728>
>>>
>>> for s in gen_squares: print(s)
0
1
4
9
16
25
36
49
64
81
>>>
```

Generator expressions give birth to generator objects that support the iterator protocol:

```python
>>> gen_squares = (x ** 2 for x in range(10))
>>>
>>> iter_g = iter(gen_squares) # unecessary, remember the generator itself is the iterator
>>>
>>> iter_g is gen_squares
True
>>>
>>> next(iter_g)
0
>>> next(iter_g)
1
>>> next(iter_g)
4
>>> next(iter_g)
9
>>> next(iter_g)
16
>>> next(iter_g)
25
>>> next(iter_g)
36
>>> next(iter_g)
49
>>> next(iter_g)
64
>>> next(iter_g)
81
>>> next(iter_g)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-72-f4e87cccdfc6> in <module>
----> 1 next(iter_g)

StopIteration:
>>>
```

Of course you rarely will need to use the iterator protocol directly, as the language constructs, such as `for` and `while`, do this automatically:

```python
>>> for s in  (x ** 2 for x in range(10)): print(s)
0
1
4
9
16
25
36
49
64
81
>>>
>>>
```

* If the generator expression is the only thing between a pair of parenthesis of a function call, another pair of parenthesis is dismised, otherwise, required:

```python
>>> # Not required
>>> ', '.join(w.upper() for w in 'spam')
'S, P, A, M'
>>>
>>> # Required
>>> sorted((x * 2 for x in range(3)), reverse=True)
[4, 2, 0]
>>>
```

* Generators x Maps

```python
>>> list(map(abs, [-1, -3, 2]))
[1, 3, 2]
>>>
>>> list(abs(num) for num in [-1, -3, 2])
[1, 3, 2]
>>>
>>> list(map(lambda x: x * 2, [1, 2, 3]))
[2, 4, 6]
>>>
>>> list(x * 2 for x in [1, 2, 3])
[2, 4, 6]
>>>
```

If the operation is not a simple function call, you should use a generator, it is usually simpler.

With text processing operations generators shine too:

```python
>>> line = 'john, mary, peter'
>>>
>>> ' '.join(word * 2 for word in line.split(','))
'johnjohn  mary mary  peter peter'
>>>
```

* Generators comprehensions can be nested:

```python
>>> list(x * 2 for x in (abs(x) for x in [-1, -2, -3, 4]))
[2, 4, 6, 8]
>>>
```

* Generators can be mixed with `map()` calls:

```python
>>> import math
>>> list( map(math.sqrt, (x ** 2 for x in range(4))) )
[0.0, 1.0, 2.0, 3.0]
>>>
```

* Generators versus `filter`

Generators can act as the `filter` built-in using `if` clauses:

```python
>>> list( filter(lambda x: x > 10, [1, 3, 22, 41, 8, 19]) )
[22, 41, 19]
>>>
>>> list( x for x in [1, 3, 22, 41, 8, 19] if x > 10 )
[22, 41, 19]
>>>
```


* Remember that `generators` are `one-shot iterators`:

```python
>>> g = (c * 2 for c in 'spam')
>>> list( g ) # uses
['ss', 'pp', 'aa', 'mm']
>>>
>>> list( g ) # exhausted
[]
>>>
>>> # To reuse, create another
>>> g = (c * 2 for c in 'spam')
>>> list( g )
['ss', 'pp', 'aa', 'mm']
>>>
```

* Generators are their own iterator, there is only one copy each time:

```python
>>> g = (char * 2 for char in 'spam')
>>>
>>> i1 = iter(g)
>>> i2 = iter(g)
>>>
>>> next(i1)
'ss'
>>> next(i1)
'pp'
>>>
>>> next(i2)
'aa'
>>> next(i2)
'mm'
>>>
>>> next(i1) # exhausted
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-8-982b006512c9> in <module>
----> 1 next(i1) # exhausted

StopIteration:
>>>
>>> next(i2) # exhausted also, same iterator
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-9-deb51dae6b35> in <module>
----> 1 next(i2) # exhausted also, same iterator

StopIteration:
>>>
```

* This exhaustion behavior also happens with function generators:

```python
>>> def repeat_letters(word):
...     for letter in word:
...         yield letter * 2
...
>>>
>>> g = repeat_letters('spam')
>>>
>>> i1, i2 = iter(g), iter(g)
>>>
>>> next(i1)
'ss'
>>> next(i1)
'pp'
>>>
>>> next(i2)
'aa'
>>> next(i2)
'mm'
>>> next(i2)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-17-c8d45a197b20> in <module>
----> 1 next(i2)

StopIteration:
>>>
>>> # Also exhausted
>>> next(i1)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-19-cc9ef6da1ea7> in <module>
----> 1 next(i1)

StopIteration:
>>>
```

* This behavior differs from some built-ins, which create a different iterator each time `iter()` is called:

```python
>>> l = [1, 2, 3, 4]
>>>
>>> i1 = iter(l)
>>> i2 = iter(l)
>>>
>>> next(i1)
1
>>> next(i1)
2
>>>
>>> next(i2) # different iterator
1
>>> next(i2)
2
>>> next(i2)
3
>>>
>>> next(i1) # back to the first iterator
3
>>>
```

These built-in objects also reflect their changes in the existent iterators:

```python
>>> l = [1, 2]
>>>
>>> i = iter(l)
>>>
>>> next(i)
1
>>> next(i)
2
>>>
>>> l.append(3)
>>>
>>> next(i) # Gets 3
3
>>>
```

* You can make a generator delegate to another generator with the `yield ... from ...` syntax:

```python
>>> def outer_fx(text):
...     yield from (letter.upper() for letter in text)
...
>>>
>>> g = outer_fx("spam")
>>>
>>> next(g)
'S'
>>> next(g)
'P'
>>> next(g)
'A'
>>> next(g)
'M'
>>> next(g)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-41-e734f8aca5ac> in <module>
----> 1 next(g)

StopIteration:
>>>
```

* One example of generator in the Python library reference is the `os.walk` function,
which returns the `current directory`, its `subdirectories` and its `files` for each tree level:

```python
>>> import os
>>>
>>> g = os.walk('.')
>>> g
<generator object walk at 0x7f197f76f0a0>
>>>
>>> next(g)
('.',
 ['tracker-extract-files.1000',
  'systemd-private-219506a7a2404f89b3098037c69a3f9f-systemd-timesyncd.service-j6qFn5',
  'systemd-private-219506a7a2404f89b3098037c69a3f9f-redis-server.service-rcP2Mq',
  '.ICE-unix',
  'tmppshv7_w2',
  'upd',
  'systemd-private-219506a7a2404f89b3098037c69a3f9f-systemd-resolved.service-1blPLE',
  'ssh-loZCQ0C57dcS',
  'VSCode Crashes',
  'systemd-private-219506a7a2404f89b3098037c69a3f9f-rtkit-daemon.service-rnpfpv',
  '.XIM-unix',
  '.X11-unix',
  '.wsdl',
  '.Test-unix',
  'tmpv1l0_2kr',
  '.font-unix',
  '.com.google.Chrome.AvTlWO',
  'systemd-private-219506a7a2404f89b3098037c69a3f9f-ModemManager.service-VeHBvw'],
 ['sddm-:0-DYaxeG',
  'sddm-auth3f187f5a-c28a-4b59-a06b-50299ee02d92',
  '.X1001-lock',
  'xauth-1000-_0'])
>>>
>>> next(g)
('./tracker-extract-files.1000', [], [])
>>>
>>> next(g)
('./.ICE-unix', [], ['1916'])
>>>
```

* A scramble creator as a generator function:

```python
>>> def scrambler(word):
...     for i in range(len(word)):
...         word = word[1:] + word[0]
...         yield word
...
>>>
>>> for option in scrambler("spam"):
...     print(option)
...
pams
amsp
mspa
spam
>>>
```

* A permutation generator function:

```python
>>> def permute(seq):
...     if not seq: yield seq
...     for i in range(len(seq)):
...         rest = seq[:i] + seq[i + 1:]
...         for rest_perm in permute(rest):
...             yield seq[i] + rest_perm
...
>>>
```

* Both `zip()` and `map()` are appliable to multiple iterators at the same time:

```python
>>> a = 'spam'
>>> b = 'bacon'
>>>
>>> list( zip(a, b) )
[('s', 'b'), ('p', 'a'), ('a', 'c'), ('m', 'o')]
>>>
>>> # if you apply zip to a single sequence
>>> list( zip([1, 2, 3, 4, 5]) )
[(1,), (2,), (3,), (4,), (5,)]
>>>
>>> # if you apply to n sequences, you get a list of tuples with n elements each
>>> a
'spam'
>>> b
'bacon'
>>>
>>> list( zip(a, b) )
[('s', 'b'), ('p', 'a'), ('a', 'c'), ('m', 'o')]
>>>
>>> # with map(), an element from each sequence is used as an argument
>>> list( map(pow, [1, 2, 3], [4, 5, 6]) ) # pow(1, 4), pow(2, 5), pow(3, 6)
[1, 32, 729]
>>>
>>>
```

* `all(seq)` returns `True` if all elements from `seq` have a `True` value. While `any(seq)` returns `True` if some element from `seq` is `True`:

```python
>>> all([ "spam", [1, 2, 3], ('a', 'b') ])
True
>>>
>>> any([ (), "", 0 ])
False
>>>
```

* Custom `zip()`:

```python
>>> def myzip(*seqs):
...     while all(seqs):
...         yield tuple(seq.pop(0) for seq in seqs)
...
>>>
>>> list( myzip([1, 2, 3], [10, 20, 30], [100, 200, 300]) )
[(1, 10, 100), (2, 20, 200), (3, 30, 300)]
>>>
```

* Custom `map()`:

```python
>>> def mymap(fx, *seqs):
...     while all(seqs):
...         yield fx(*tuple(seq.pop(0) for seq in seqs))
...
>>>
>>> list( mymap(print, [1, 2, 3], [4, 5, 6], [7, 8, 9]) )
1 4 7
2 5 8
3 6 9
[None, None, None]
>>>
```

* Caution. Always remember that some built-in iterators in Python are exhausted after used:

```python
>>> def myzip(*seqs, debug=False):
...     iters = map(iter, seqs)
...     if debug: print( iters )
...     while iters:
...         res = [next(i) for i in iters]
...         if debug: print( res )
...         yield tuple(res)
...         input()
...
>>>
>>> list( myzip(['a', 'b', 'c'], ['d', 'e', 'f'], debug=True) )
<map object at 0x7f60dbe4a668>
['a', 'd']

[]

[]
```

`iters` returns a `map()` object which has an always `True` value, but becomes exhausted.
After this exhaustion the loop keeps running and `res` always generates an empty list.

* Comprehensions localize the local variables, creating an unshared scope:

```python
>>> (x for x in range(5))
<generator object <genexpr> at 0x7f60dbeb56d0>
>>>
>>> print( x ) # ?
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-47-5047d901a4e9> in <module>
----> 1 print( x ) # ?

NameError: name 'x' is not defined
>>>
>>> # list comprehensions (in fact, all comprehensions) have the same behavior
>>> [y for y in range(5)]
[0, 1, 2, 3, 4]
>>> y
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-50-9063a9f0e032> in <module>
----> 1 y

NameError: name 'y' is not defined
>>>
>>> # but for loops share the scope where they are included
>>> for z in range(5): pass
>>> print(z) # defined in the local scope
4
>>>
>>>
```

* Comprehensions are an exception for the LEGB rule, as they create an specific namespace. But the remainding lookup follows the LEGB (Local, Enclosing, Global and Built-in) rule:

```python
>>> global_var = 'spam'
>>>
>>> def fx():
...     enclosing_var = 'eggs'
...     print( ','.join(local_var for local_var in global_var + enclosing_var) )
...
>>>
>>> fx()
s,p,a,m,e,g,g,s
>>>
```

* So, Python 3 has an special scope (non-sharing) for comprehensions expressions, besides the LEGB rule.

* Set and dict comprehensions are syntatic sugar for passing a generator for the type names:

```python
>>> {x * x for x in range(5)}
{0, 1, 4, 9, 16}
>>>
>>> # the same as
>>> set(x * x for x in range(5))
{0, 1, 4, 9, 16}
>>>
>>> {x: x * x for x in range(5)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
>>>
>>> dict(( (x, x * x) for x in range(5) )) # dict( (0, 0), (1, 1), (2, 4)... )
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
>>>
```

> Remember that `set` and `dict` comprehensions produce all the values at once, if you need lazy generation, a generator is still your best option.

* As any comprehensions, `set` and `dict` comprehensions also support `if` clauses and nested `for` loops:

```python
>>> {x for x in range(10) if x % 2 == 0}
{0, 2, 4, 6, 8}
>>>
>>> {x: x * x for x in range(10) if x % 2 == 0}
{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
>>>
>>> # nested for loops and if clauses
>>> {x + y for x in range(10) for y in range(10) if x % 2 == 0 and y % 2 == 0}
{0, 2, 4, 6, 8, 10, 12, 14, 16}
>>>
>>> {(x, y): x + y for x in range(10) for y in range(10) if x % 2 == 0 and y % 2 == 0}
{(0, 0): 0,
 (0, 2): 2,
 (0, 4): 4,
 (0, 6): 6,
 (0, 8): 8,
 (2, 0): 2,
 (2, 2): 4,
 (2, 4): 6,
 (2, 6): 8,
 (2, 8): 10,
 (4, 0): 4,
 (4, 2): 6,
 (4, 4): 8,
 (4, 6): 10,
 (4, 8): 12,
 (6, 0): 6,
 (6, 2): 8,
 (6, 4): 10,
 (6, 6): 12,
 (6, 8): 14,
 (8, 0): 8,
 (8, 2): 10,
 (8, 4): 12,
 (8, 6): 14,
 (8, 8): 16}
>>>
```

## Benchmarking interlude

* You can do your own benchmark using the `time.clock()` function:

```python
>>> import time
>>>
>>> def benchmark(fx, *args, **kwargs):
...     start = time.clock()
...     fx(*args, **kwargs)
...     elapsed = time.clock() - start
...     print(fx, " run in ", elapsed, " seconds")
...
>>>
>>> def add(a, b):
...     return a + b
...
>>>
>>> benchmark(add, 10, 20)
<function add at 0x7f60e0035268>  run in  2.9999999995311555e-06  seconds
>>>
>>> benchmark(str.upper, 'spam')
<method 'upper' of 'str' objects>  run in  4.0000000041118255e-06  seconds
>>>
>>> benchmark(str.upper, 'spam eggs spam eggs')
<method 'upper' of 'str' objects>  run in  5.999999999062311e-06  seconds
>>>
```

* From Python 3.3 beyond newtime tracking function are avaiable:

`time.perf_counter()` return a tick in seconds that takes into consideration the time the process was sleeping and so it is system-wide:

```python
>>> import time
>>>
>>> start = time.perf_counter()
>>> fx()
s,p,a,m,e,g,g,s
>>> elapsed = time.perf_counter() - start
>>> elapsed
13.342552814001465
>>>
```

While `time.process_time()` returns a tick in seconds (float) that takes into account only the time the process was actually running:

```python
>>> import time
>>>
>>> start = time.process_time()
>>> fx()
s,p,a,m,e,g,g,s
>>> elapsed = time.process_time() - start
>>>
>>> elapsed
0.6284703069999935
>>>
```

### `timeit` module

* `timeit` module supports callables and code strings.

To measure a cycle of tests (`number`) use the `timeit` function. It takes a `number` parameters that defines the number of times the `stmt` is run, then the time average is returned:

```python
>>> timeit.timeit(stmt="[x ** 2 for x in range(1000)]", number=1000)
0.2875530249999656
```

If you want multiple time averages, use the `repeat()` method. It performs `repeat` cycles, and in each cycle averages the `stmt` execution time for `number` executions:

```python
>>> timeit.repeat(stmt="[x ** 2 for x in range(1000)]", number=1000, repeat=5)
[0.28816614900006243,
 0.28122328899996774,
 0.27856260500004737,
 0.2780457700000625,
 0.2791460249999318]
>>>
```

### Function gotchas

* You cant use the same name for a local variable in a function and a global one. To have a local and still have access to the global variable, import the `__main__` (current module) and use it as prefix for access:

```python
>>> x = 99
>>>
>>> def example():
...     import __main__
...     x = 100
...     __main__.x = 88
...
>>> print(x)
99
>>>
>>> example()
>>>
>>> print(x)
88
>>>
```

* Remember that local variables in function are resolved statically:

```python
>>> def ex():
...     print(z)
...     z = 100 # after usage
...
>>>
>>> ex()
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
<ipython-input-14-70ab1ac0b8ad> in <module>
----> 1 ex()

<ipython-input-13-21440486dcf0> in ex()
      1 def ex():
----> 2     print(z)
      3     z = 100 # after usage
      4

UnboundLocalError: local variable 'z' referenced before assignment
>>>
>>>
```

* Avoid mutable objects as defaults, as they save state and are created only during definition, thus being uniques:

```python
>>> def example(lst=[]):
...     lst.append(1)
...     return lst
...
>>>
>>> example()
[1]
>>> example()
[1, 1]
>>> example()
[1, 1, 1]
>>>
>>> # Avoid it passing a new list explictly
>>> example([])
[1]
>>> example([])
[1]
>>> example([])
[1]
>>> # If any is defined, the list created during 'def' is used
>>> example()
[1, 1, 1, 1]
>>> example()
[1, 1, 1, 1, 1]
>>> example()
[1, 1, 1, 1, 1, 1]
>>>
```

To avoid this shared state behavior, move the default initialization to the function body:

```python
>>> def example(lst=None):
...     if lst is None:
...         lst = []
...     lst.append(1)
...     return lst
...
>>>
>>> example()
[1]
>>> example()
[1]
>>> example()
[1]
>>>
```

* Today, the best way to preserve state between function executions is using its attributes:

```python
>>> def example():
...     if not hasattr(example, 'lst'):
...         example.lst = []
...     example.lst.append(1)
...     return example.lst
...
...
>>>
>>> example()
[1]
>>> example()
[1, 1]
>>> example()
[1, 1, 1]
>>>
```

## Modules and packages

* A Python program is composed, at least, by a top level file and auxiliary module files.

* `import` and `from ... import ...` execute and load modules to provide access to its attributes.

* `import` are only established when the interpreter runs them. Their net effect is to assign a variable, usually the module name,
to the loaded module object.

* `import` and `from ... import ...` really executes the statements from the module to create the module object and its attributes.

* A module import is a three step process:

1. find it
2. compile to bytecode (if needed)
3. run the module code to create the module object attributes

* Modules are imported only once per process and are registered in the `sys.modules` dict.
Subsequent imports ignore the three steps and directly fetch the module object from this dict.

* Python uses a module search path during import operations, instead of specifying the absolute path.

* Compilation happens only during `import` operations, so the top-level module/file of your program will leave no `.pyc` file behind.

* If your module has a `print` statement, for example, it will be execute when the module is imported. Again, it will be execute only once and, then, cached in `sys.modules`.

* The default module search path is composed of:

1. Directory containing the top level script being executed or the dir where the Python shell was open;
2. `PYTHONPATH` dirs, if defined;
3. Standard library;
4. `.pth` files, if present;
5. `site-packages`, home of third party extensions.

These five sources become the `sys.path` list of paths in the Python process.

`sys.path` is mutable, so you can change it and look for modules in other, arbitrary, folders.

* Some Python setups also include the current working dir as the first item of the `sys.path` list.
Mind that the working dir can be **different** from the top-level script dir.

* Given a module named `module1.py`:

```python
# module1.py
def printer(x):
    print(x)
```

You can use this module in two ways:

1. `import`

```python
import module1

module1.printer('spam')
```

You have access through the `module1` variable/object.

2. `from ... import ...`

```python
from module1 import printer
printer('spam')
```

You create a local reference `printer` that actually links to `module1.printer`.

> The `from` statement is just an extension. A syntatic sugar. It executes the three `import` steps as usual.

3. `from ... import *`

Import all top level names defined in the module:

```python
from module1 import *

printer('spam')
```

> Caution: this can lead to name shadowing.

> This form cant be used inside a function. But, anyway, you should list your imports in the top, start, of the script.

* Remember: modules are loaded once per process, so they can act as singletons:

```python
>>> import sys
>>>
>>> # append /tmp to sys.path
>>> sys.path.append('/tmp')
>>> sys.path
['/home/rnetonet/.local/bin',
 '/usr/lib/python36.zip',
 '/usr/lib/python3.6',
 '/usr/lib/python3.6/lib-dynload',
 '',
 '/home/rnetonet/.local/lib/python3.6/site-packages',
 '/usr/local/lib/python3.6/dist-packages',
 '/usr/lib/python3/dist-packages',
 '/home/rnetonet/.local/lib/python3.6/site-packages/IPython/extensions',
 '/home/rnetonet/.ipython',
 '/tmp']
>>>
>>> # execute another import, but the cached version is used
>>> import sys
>>>
>>> # the module attribute is changed still, the module was not executed again
>>> sys.path
['/home/rnetonet/.local/bin',
 '/usr/lib/python36.zip',
 '/usr/lib/python3.6',
 '/usr/lib/python3.6/lib-dynload',
 '',
 '/home/rnetonet/.local/lib/python3.6/site-packages',
 '/usr/local/lib/python3.6/dist-packages',
 '/usr/lib/python3/dist-packages',
 '/home/rnetonet/.local/lib/python3.6/site-packages/IPython/extensions',
 '/home/rnetonet/.ipython',
 '/tmp']
>>>
```

* If you `from ... import ...` a mutable object, it will be subject to side effects:

```python
>>> from sys import path
>>> path.append('/tmp')
>>>
>>> # load the module object
>>> import sys
>>> sys.path # the object was altered before
['/home/rnetonet/.local/bin',
 '/usr/lib/python36.zip',
 '/usr/lib/python3.6',
 '/usr/lib/python3.6/lib-dynload',
 '',
 '/home/rnetonet/.local/lib/python3.6/site-packages',
 '/usr/local/lib/python3.6/dist-packages',
 '/usr/lib/python3/dist-packages',
 '/home/rnetonet/.local/lib/python3.6/site-packages/IPython/extensions',
 '/home/rnetonet/.ipython',
 '/tmp']
>>>
```

Remember that `from ...` in fact imports the module and creates the module object in `sys.modules`, it just dont create the local reference for the module.

* But references created with `from ... import` syntax to non-mutable objects dont affect the module when reassigned:

```python
>>> from sys import platform
>>> platform
'linux'
>>>
>>som> platform = 'ubuntu'
>>>
>>> import sys
>>> sys.platform # unchanged
'linux'
>>>
>>>
```

To change you have to use the module object name explictly:

```python
>>> import sys
>>>
>>> sys.platform = 'unix'
>>>
>>> sys.platform
'unix'
>>>
```

* You can import attributes from modules using an alias:

 `from module import var as alias`

It also works with the `import` statement:

```python
import module as alias
```

* Some notes about module scopes and loading:

1. Module code is executed on the first import;
2. During this execution, Python intercepts top-level assignments (remember that `def` and `class` definitions perform implicit assignments), which originate the module attributes.
3. Modules attributes (namespace) can be accessed through `.__dict__` attr or using `dir(module)`.
4. Module becomes the global scope for all non-top-level code it contains. Unlike functions, which namespace live only during execution, module scopes live while the module is loaded in memory (it becomes the `__dict__` attribute).

* Python creates some attributes automatically for modules:

`__name__`, the original module name:

```python
>>> import sys
>>>
>>> sys.__name__
'sys'
>>>
>>> import os as super_os_lib
>>> super_os_lib.__name__
'os'
>>>
```

`__file__`, the module path:

```python
>>> from ldap_backend import ifbaiano_ldap_manager
>>> ifbaiano_ldap_manager.__file__
'/home/rnetonet/Workspace/suap/ldap_backend/ifbaiano_ldap_manager.py'
>>>
```

* The `__dict__` attribute is present in `modules` and `objects`. In both, it intermediates the attribute access:

```python
>>> import sys
>>>
>>> sys.platform
'linux'
>>>
>>> sys.__dict__['platform']
'linux'
>>>
```

* Qualification: `object.attribute` provides an unified way to acess objects attributes through Python.

* The LEGB rule **does not** applies to qualification operations, only to bare name lookups:

1. Bare, unqualified, name lookup. Follows the LEGB rule:

```python
print(x)
```

2. Qualification: Looks for `x` using the LEGB rule, then look for `y` in the `x` object `__dict__`.

```python
print(x.y)
```

> Qualification works on all objects with attributes: modules, classes, C extension types, etc.

* The global scope is always of the surrounding file:

```python
# mod_a.py
X = 99

def change():
    global X
    X = 100
```

```python
# mod_b.py
X = 'a'

import mod_a
mod_a.change()

print(mod_a.X)

print(X)
```

Executing `mod_b.py`:

```python
➜ python mod_b.py
100 # the 'global' clause refers to 'mod_a' scope
a   # mod_b scope is not changed
```

> Remember: a module can only access attributes from another module explicitly, using one of the `import` forms.

> Remember 2: Python scope is determined by the position where the code is. **Lexical scoping.**.

* Modules can nest downwards:

```python
# c.py

X = 'x in c'
```

```python
# b.py

X = 'x in b'

import c
```

```python
# a.py

X = 'x in a'


import __main__
print("a.X (__main__.X)", __main__.X)

import b
print("b.X", b.X)
print("b.c.X", b.c.X)
```

Executing `a.py`:

```bash
➜ python a.py
('a.X (__main__.X)', 'x in a')
('b.X', 'x in b')
('b.c.X', 'x in c')
```

* To reload a module, use `imp.reload(module_object)` function.

It reloads (reruns and recreates the object) in place:

```python
# b.py
value = 'initial'
```

```python
import b

# b 'initial' value
print(b.value)

# changes b object value
b.value = 'altered'
print(b.value) # altered...

# reloads, back to initial value
import imp
imp.reload(b)

# initial
print(b.value)
```

```bash
rnetonet on T440s in /tmp/sample via 🐍 v2.7.17
➜ python a.py
initial
altered
initial
```

* `reload` reruns the module code. It dosent deletes the previous object and recreates, instead, it morphs:

```python
# b.py
value = 'initial'
```

```python
# a.py
import b

# creates a new attr in the module object
b.new_value = 'new_value'
print(b.new_value)

# reloads, morphing
import imp
imp.reload(b)

print(b.new_value) # still there
```

```bash
➜ python /tmp/sample/a.py
new_value
new_value
```

* Reloads affect all `import` uses. But only future `from ... import` uses.

## Module packages

* A package import converts a directory into a module object, which attributes are other modules it contains and subdirectories.
Both also handled as module objects.

* Instead of a module name, you can import a path:

```python
import dir1.subdir.module
```

or

```python
from di1.subdir.module import attr
```

Both statements indicate that there is a 'dir1' folder in your PYTHONPATH, which includes a 'subdir' folder with a `module.py` file.

* Until Python 3.3, each dir in a package must contain a `__init__.py` file, even if its empty.

In the prior example, tree would show something like:

```bash
project_folder/
  main.py # which contains the import
  dir1/
    __init__.py
    subdir/
      __init__.py
      module.py
```

`__init__.py` files are executed when their package path is imported:

given the structure below:

```bash
➜ tree sample/
sample/
├── a
│   ├── b
│   │   ├── __init__.py
│   ├── __init__.py
└── main.py

4 directories, 5 files
```

And the following codes:

```python
# a / __init__.py
print('a imported')
```

```python
# a / b / __init__.py
print('b imported')
```

```python
# main.py
import a.b
```

Running `main.py`:

```bash
> python /tmp/sample/main.py
a imported
b imported
```

* When you do a package import as:

```python
import dir_a.dir_b.module
```

Python creates three module objects in memory, but make only the left-most avaiable. To access the inner modules, you need to qualify.

The `dir_a.__init__.py` file will be interpreted and originate the `dir_a` module.

The same happens with `dir_b.__init__.py` file, which is run and originates the `dir_b` module object.

Back to our example:

```bash
├── a
│   ├── b
│   │   ├── __init__.py
│   ├── __init__.py
└── main.py
```

If we change the `__init__.py` files to:

```python
# a / __init__.py
print('a imported')
var = 'a var!'
```

```python
# b / __init__.py
print('b imported')
var = 'b var!'
```

And import in the shell:

only `a`

```python
>>> import a # a module is executed
a imported
>>> a.var    # and is accessible
'a var!'
>>>
>>>
```

`b` from inside `a`:

```python
# Creates each module
>>> import a.b
a imported
b imported
>>>
# The top is accessible
>>> a.var
'a var!'
>>>
# To access nested modules, you need to qualify the top level
>>> a.b.var
'b var!'
>>>
>>> # you cant go directly to b
>>> b.var
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-5-a8930fce5e02> in <module>
----> 1 b.var

NameError: name 'b' is not defined
>>>
```

Another example, importing the `os.path` package:

```python
>>> import os.path
>>>
>>> os # module imported
<module 'os' from '/usr/lib/python3.6/os.py'>
>>>
>>> os.path # to access the nested module, you need to qualify
<module 'posixpath' from '/usr/lib/python3.6/posixpath.py'>
>>>
```

But if you use `from ...` only the specified names become avaiable:

```python
>>> from os.path import sep
>>>
>>> os
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-2-15f5e96fdb7b> in <module>
----> 1 os

NameError: name 'os' is not defined
>>>
>>> path
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-3-012ab3a6b187> in <module>
----> 1 path

NameError: name 'path' is not defined
>>>
>>> # but sep is accessible
>>> sep
'/'
>>>
```

Remember that `from` also executes each directory `__init__.py` file:

```python
>>> from a.b import var
a imported
b imported
>>>
>>> var
'b var!'
>>>
```

* Relative imports work for packages structures.

* import in packages in Python 3:

1. module import search ignore the package own directory. it looks only in `sys.path`. these are the absolute imports.

2. added the relative syntax to `from ...` to import from the package directory structure explicitly, using dots to specify the level.
these are the new `relative` imports.

So in Python 3 you have two major kinds of imports:

`absolute`, which look in the `sys.path` only.

and

`relative`, using `from ...` and dots to import from the module current package structure.

* Examples:

```python
from . import mod
```

Imports a module named `mod` in the current importer dir.

```python
from .spam import spamassassin
```

Imports an object or module named `spamassassin` from the subfolder `spam` inside the current importer dir.

To achieve this behavior in Python 2, which performs a `relative-then-absolute` import, even without the dots:

```python
from __future__ import  absolute_import
```

Remember: relative imports work only with the `from ...` syntax.
In Python 3 `import ....` are always absolute imports.

Some other relative examples:

```python
from .spam import name1, name2 # import name1 and name2 from a module spam in the current importer dir
from . import string # imports a string.py module from the current importer dir
from .. import string # from the folder above the current importer dir, import a module named string
```

* `import` are always absolute in Python 3. `relative` imports are only possible using `from ..path import ...` . **The dots before the `.path` are required for relative imports**.

* `from something import otherthing` without dots are absolute also, looking in `sys.path`

* To make a relative `import` to the current package, use:

```python
from . import module # import module from the current dir
```

* You can import specific names from in a relative import:

```python
from .module import a, b
```

* The dots reference work like most Linux shells:

1. Current dir:

```python
from . import module
```

```python
from .module import a, b
```

2. Parent dir

```python
from .. import module
```

```python
from ..module import a, b
```

3. Grandparent dir


```python
from ... import module
```

```python
from ...module import a, b
```

* Absolut imports from packages:

If your package folder is in `sys.path`, you can name it explictly and perform an absolute import using the package:

```python
from mypkg.subpkg import string
```

Mind that `mypkg` should be present in some of the `sys.path` directories.

* Module lookup rules summary:

1.`import module` or `from module import a, b` where `module` has no dot as prefix are absolute import and traverse `sys.path` searching the module file. This also applies for package imports without leading dots: `import mypkg.module` or `from mypkg.module import a, b`.

2. Python packages are directories with `__init__.py` files. When you import a package like:

```python
import a.b.c
```

Python executes `a.__init__.py`, `b.__init__.py` and `c.__init__.py` files.

Then, it creates the `a` module object. The `b` module becomes an attribute in the `a` module object. And the `c` module object becomes an attribute in the `b` object.

The module object of each dir corresponds to its `__init__.py` file execution.

To import a module inside some of the packages, you need to be explicit. You can, for example, import an `utils.py` module that resides inside the `c` folder:

```python
import a.b.c.utils
print( a.b.c.utils.some_var )
```

or

```python
form a.b.c import utils
print( utils.some_var )
```

3. By default, Python 3 always performs `absolute` imports, which traverse the `sys.path` folders.
To perform `relative` import, you need to use the `from .dir import module` where the `dir` has one or more leading dots.

* Let's see some examples to clear up possible doubts:

1. Sometimes the `import` seems to perform relative imports.

Remember that relative imports are executed only when the dir is prefixed with leading dots.

But, also remember, that the first item in `sys.path` is always the folder where the top-level/executing script is.

So, if you have in your folder two modules: `main.py` and `string.py` and in `main.py` you `import` a `string` module:

```python
import string
```

The folder `string.py` module will be loaded, as it is the first match in `sys.path`.

2. I cant `from . import module` from my running script.

Your running script is not considerated a `package` code, so you can perform relative imports:

Given the structure:

```bash
├── main.py
└── utils.py
```

```python
# utils.py
def uprint(msg):
    print(msg.upper())
```

```python
# main.py
from . import utils

utils.uprint("Hello World")
```

if you run `main.py`:

```bash
➜ python main.py
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    from . import utils
ValueError: Attempted relative import in non-package
```

* **Remember:** the home directory of the running Python module is always set as the first folder in `sys.path`.

* `Relative imports` search only the package!

```bash
sample/
├── main.py
└── pkg
    ├── example.py
    ├── __init__.py
    ├── string.py
```

```python
# pkg/example.py
from . import string # tries to do a relative import, but there is no string.py file. no absolute import is tried automatically.
```

```python
# sample/main.py
import sys
print("sys.path=", sys.path)

import pkg.example
```

Running `main.py`:

```python
sys.path= ['/tmp/sample', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/rnetonet/.local/lib/python3.8/site-packages', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    import pkg.example
  File "/tmp/sample/pkg/example.py", line 1, in <module>
    from . import string
ImportError: cannot import name 'string' from 'pkg' (/tmp/sample/pkg/__init__.py)
```

* **Remember** the folder where the running script is, is always the first item in `sys.path`.

Dir structure:

```bash
sample/
└── main.py
```

```python
# main.py
import sys
print("sys.path=", sys.path)
```

Running from the `sample` folder:

```bash
rnetonet on ThinkPad-T440s in /tmp/sample via 🐍 v2.7.18rc1
➜ pwd
/tmp/sample
rnetonet on ThinkPad-T440s in /tmp/sample via 🐍 v2.7.18rc1
➜ python3 main.py
sys.path= ['/tmp/sample', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/rnetonet/.local/lib/python3.8/site-packages', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']
```

From outside the folder:

```python
➜ python3 sample/main.py
sys.path= ['/tmp/sample', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/rnetonet/.local/lib/python3.8/site-packages', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']
```

* Caution. If your CWD (dir of the running script) has some module name as a built-in module, `string.py` for example, absolute imports will use it. Remember: the running script home folder is always the first dir in `sys.path`.


* In both Python 2 and 3, using relative imports binds the file to the package and precludes it from being used in other ways.

* In Python 3, modules that use relative imports cant be used as top level running scripts.

* In a nutshell, Python 3 modules that use relative import cant be executed as top-level scripts.
To create modules that can act as package modules or top-level scripts, you need to use full package path imports and assume the package container folder is in the `sys.path`:

```python
from pkg.audio.syntetizer import Syntetizer
```

* An example of this issue:

```bash
pkg/
├── main.py
├── midway.py
├── mod.py
```

```python
# main.py
import midway
```

```python
# midway.py
import mod
```

```python
# mod.py
print('module!')
```

Running as script works, as all files are in the `sys.path`:

```bash
➜ python3 main.py
module!
```

But you cant import it as a package, as it is an absolute import:

```python
>>> import pkg.midway
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-1-24126b11b284> in <module>
----> 1 import pkg.midway

/tmp/sample/pkg/midway.py in <module>
----> 1 import mod

ModuleNotFoundError: No module named 'mod'
>>>
```

Another example. Now using the same structure but relative imports:

```python
# main.py
import midway
```

```python
# midway.py
from . import mod
```

```python
# mod.py
print('module!')
```

You cant execute as top-level scripts. Remembem that relative imports can be used by running scripts:

```bash
➜ python pkg/main.py
Traceback (most recent call last):
  File "pkg/main.py", line 1, in <module>
    import midway
  File "/tmp/sample/pkg/midway.py", line 1, in <module>
    from . import mod
ValueError: Attempted relative import in non-package

➜ python pkg/midway.py
Traceback (most recent call last):
  File "pkg/midway.py", line 1, in <module>
    from . import mod
ValueError: Attempted relative import in non-package
```

But package imports work:

```python
>>> import pkg.midway
module!
```

* Fix 1: put all the acessory packages modules into a subdirectory and the main, running files, in parent folder:

```bash
sample/
├── main.py
└── pkg
    ├── __init__.py
    ├── midway.py
    ├── mod.py
```

```python
# main.py
import pkg.midway
```

```python
# pkg/midway.py
from . import mod
```

```python
# pkg/mod.py
print('module!')
```

Now running as script works:

```bash
➜ python3 main.py
module!
```

And package import also works:

```python
>>> %pwd
'/tmp/sample'
>>>
>>> import pkg.midway
module!
>>>
```

* Fix 2: use full package import paths

```bash
sample/
└── pkg
    ├── __init__.py
    ├── main.py
    ├── midway.py
    ├── mod.py
```

```python
# main.py
import pkg.midway
```

```python
# pkg/midway.py
import pkg.mod
```

```python
# pkg/mod.py
print('module!')
```

If you put the `pkg` parent folder in the `sys.path`, running and package imports will work:

```bash
rnetonet on ThinkPad-T440s in /tmp/sample
➜ export PYTHONPATH=/tmp/sample/
rnetonet on ThinkPad-T440s in /tmp/sample
➜
rnetonet on ThinkPad-T440s in /tmp/sample
➜ python3 pkg/main.py
['/tmp/sample/pkg', '/tmp/sample', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/rnetonet/.local/lib/python3.8/site-packages', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']
module!
rnetonet on ThinkPad-T440s in /tmp/sample
➜
rnetonet on ThinkPad-T440s in /tmp/sample
➜ ipython
Python 3.8.2 (default, Mar 13 2020, 10:14:16)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.
>>> import pkg.midway
module!
>>>
```

Using full package imports, modules can be tested being run directly:

```bash
rnetonet on ThinkPad-T440s in /tmp/sample
➜ export PYTHONPATH=/tmp/sample/

rnetonet on ThinkPad-T440s in /tmp/sample took 1m19s
➜ python3 pkg/midway.py
module!
```

> **Important!** To a folder to be considerated as a package, it needs to have an `__init__.py` file.

`__init__.py` files are still necessary!!!

* You can make instances of any of the classes in the hierarchy. Remember that lookups will start from this class, then.

* Names assigned in the main body of a classe become attributes of the class object and are shared among all instances.

* Functions declared in the body of classes become methods and receive, when called, the instance where it was called as the first argument.
This first argument is usually defined as `self`:

```python
>>> class Example:
...     message_prefix = '-> '
...     data = 'default' # will be overriden by set_data() in the instances
...
...     def set_data(self, value):
...         self.data = value
...
...     def get_data(self):
...         return self.data
...
...     def display(self):
...         print(f'{self.message_prefix} {self.get_data()}') # self.message_prefix can be replaced by Example.message_p
... refix
...
>>>
>>> e1 = Example()
>>> # use the default (class) data
>>> e1.display()
->  default
>>>
>>> e1.set_data('spam') # create a data attribute in the instance
>>> e1.display() # the object data will be used instead
->  spam
>>>
```

* Objects namespace are implemented as a `__dict__` attribute:

```python
>>> class Test:
...     x = 1
...     y = 2
...
>>>
>>> Test.__dict__
mappingproxy({'__module__': '__main__',
              'x': 1,
              'y': 2,
              '__dict__': <attribute '__dict__' of 'Test' objects>,
              '__weakref__': <attribute '__weakref__' of 'Test' objects>,
              '__doc__': None})
>>>
>>> t1 = Test()
>>> t1.x = 10
>>>
>>> t2 = Test() # wont have any object attribute
>>>
>>> t1.__dict__
{'x': 10}
>>>
>>> t2.__dict__
{}
>>>
```

* The `vars(object)` built-in returns the `object.__dict__`:

```python
>>> vars(Test)
mappingproxy({'__module__': '__main__',
              'x': 1,
              'y': 2,
              '__dict__': <attribute '__dict__' of 'Test' objects>,
              '__weakref__': <attribute '__weakref__' of 'Test' objects>,
              '__doc__': None})
>>> vars(t1)
{'x': 10}
>>> vars(t2)
{}
>>>
```

* Caution: qualification triggers an inheritance search, but `__dict__` access dosent:

```python
>>> class Example:
...     var = 42
...
>>>
>>> t1 = Example()
>>>
>>> # Acessing Example object
>>> Example.var
42
>>> Example.__dict__['var']
42
>>>
>>> # Accessing t1 object
>>> t1.var # does inheritance lookup
42
>>> t1.__dict__['var'] # does not trigger inheritance name lookup
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-23-b2326f61e87c> in <module>
----> 1 t1.__dict__['var'] # does not trigger inheritance name lookup

KeyError: 'var'
>>>
```

* Instance objects keep a link to its class object in the `__class__` attribute:

```python
>>> class Dog:
...     says = 'bark!'
...
>>> class Cat:
...     says = 'Meow!'
...
>>>
>>> animal = Dog()
>>> animal.__class__
__main__.Dog
>>>
>>> animal.says
'bark!'
>>>
>>> # You can, but should not, change the __class__ in runtime
>>> animal.__class__ = Cat
>>> animal
<__main__.Cat at 0x7f49f2a00588>
>>>
>>> animal.says
'Meow!'
>>>
```

* Class object have a `__bases__` attribute linking their superclasses:

```python
>>> class Father:
...     hair = 'brown'
...
>>> class Mother:
...     eyes_color = 'blue'
...
>>> class Baby(Father, Mother): pass
>>>
>>> Baby.__bases__
(__main__.Father, __main__.Mother)
>>>
>>> b = Baby()
>>> b.hair
'brown'
>>> b.eyes_color
'blue'
>>>
```

* Classes and instances are just namespace objects, thus attributes can be created on the fly. Even methods:

```python
>>> class Calculator:
...     pass
...
>>>
>>> # Sets default values
>>> Calculator.a = 1
>>> Calculator.b = 2
>>>
>>> # Create a method outside
>>> def add(self):
...     return self.a + self.b
...
>>>
>>> Calculator.add = add
>>>
>>> # Use the attributes defined in an instance object
>>> c1 = Calculator()
>>> c1.add()
3
>>>
>>> c1.a = 10
>>> c1.b = 30
>>> c1.add()
40
>>>
```

* You can even add methods dinamically to pre-existent instances:

```python
>>> class Dog:
...     def bark(self):
...         print(f'bark {self}')
...
>>>
>>> def jump(self):
...     print(f'jump {self}')
...
>>>
>>> d1 = Dog()
>>> d1.bark()
bark <__main__.Dog object at 0x7f49f249d898>
>>> d1.jump() # ops!
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-74-ba2a952f416d> in <module>
----> 1 d1.jump() # ops!

AttributeError: 'Dog' object has no attribute 'jump'
>>>
>>> Dog.jump = jump
>>>
>>> d1.jump()
jump <__main__.Dog object at 0x7f49f249d898>
>>>
```

* Python has two methods responsible for displaying an object: `__str__` and `__repr__`.

`__str__` is prefered by `print()` and `str()`.

if `__str__` is not present, `__repr__` is used instead.

Python provides a default `__repr__` for all objects.

But have in mind why both exist:

`__str__` provides a more friendly, user focused, string representation.

`__repr__` provides a more technical, developer focused, representation.

* In Python 3 built-ins lookups, like `__repr__` skip the instance and go directly to the class. So you are forced to overload it to change its behavior:

```python
>>> class Father:
...     def __repr__(self):
...         return f'Fathers'
...
...
>>> class Son(Father):
...     def __getattribute__(self, attr):
...         print(attr)
...
>>>
>>> s = Son()
__class__
__class__
__class__
__class__
>>> s.x = 10
>>> s.x
x
>>>
>>> repr(s)
'Fathers'
>>>

>>> class Daughter(Father):
...     def __getattribute__(self, attr):
...         print(attr)
...     def __repr__(self):
...         return 'daughter'
...
>>>
>>> d = Daughter()
>>> d.x = 10
>>> d.x
x
>>> repr(d)
'daughter'
>>>
```

---

Instances have a `__class__` attribute that points to the class it was originated.

Classes have a `__name__` attribute and a `__bases__` (superclasses).

Objects commonly also have a `__dict__` object, representing their namespace.

```python
>>> class Person: pass
>>>
>>> bob = Person()
>>> bob.__class__
__main__.Person
>>> bob.__class__.__name__
'Person'
>>> bob.__class__.__bases__
(object,)
>>>
>>> bob.name = 'Bob'
>>> bob.__dict__
{'name': 'Bob'}
>>>
```

---

To create a "mixin" to display all attributes from a class:

```python
class RichDisplay:
    def __attrs(self):
        attrs = []
        for attr in sorted(self.__dict__):
            attrs.append(f'{attr}={getattr(self, attr)}')
        return ', '.join(attrs)

    def __repr__(self):
        return f'{self.__class__.__name__} | {self.__attrs()}'

class Person(RichDisplay):
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    bob = Person('Bob', 32)
    print(bob)
```

output:

```bash
$ python /tmp/demo.py
Person | age=32, name=Bob
```

---

If you want to list all attributes, including the inherited by the instance from its classes, use `dir`:

```python
>>> class Person:
...     person_attr = 1
...
>>> class Manager(Person):
...     def __init__(self):
...         self.manager = True
...
>>>
>>> m = Manager()
>>> dir(m)
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'manager',
 'person_attr']
>>>
>>>
```

While `vars(object)` has the same effect as `object.__dict__`:

```python
>>> vars(m)
{'manager': True}
>>> m.__dict__
{'manager': True}
>>>
```

---

To avoid name collisions in classes, prefix methods or attributes not meant to be overloaded with an underscore:

```python
class RichDisplay:
    def _get_attrs(self):
        attrs = []
        for attr in sorted(self.__dict__):
            attrs.append(f'{attr}={getattr(self, attr)}')
        return ', '.join(attrs)

    def __repr__(self):
        return f'{self.__class__.__name__} | {self._get_attrs()}'

class Person(RichDisplay):
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    bob = Person('Bob', 32)
    print(bob)
```

---

You can use `shelve` to persist Python objects leveraging the `pickle` and `dbm` modules:

```python
import shelve


class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __repr__(self):
        return f'{self.__class__.__name__} - {self.name}, {self.age}, {self.job}'

if __name__ == "__main__":
    bob = Person("Bob", 32, "dev")
    paul = Person("Paul", 44, "mgr")

    # persist. shelve are like dicts.
    db = shelve.open('db')
    db['bob'] = bob
    db['paul'] = paul
    db.close()

    # retrieve
    db = shelve.open('db')
    for reg_key in db: # just like a dict.keys()
        print(db[reg_key])
    db.close()
```

The `pickle` module, use by `shelve`, can persist any kind of Python object. Even the one we create. Their classes are automatically imported when the *pickled objects* are loaded, thus they should be *importable* from `sys.path` in this moment.

> pickleable classes must be coded at the top level of a module file accessible from a directory listed on the sys.path module search path

---

To modify class attributes, you need to use the class name.

```python
>>> # You can access class attributes through instances or classes
>>> a.x, a.y
(11, 99)
>>> b.x, b.y
(11, 99)
>>> SharedData.x, SharedData.y
(11, 99)
>>>
>>> # But, to change you need to use the class name
>>> SharedData.x = 'x'
>>> SharedData.y = 'y'
>>>
>>> a.x, a.y
('x', 'y')
>>> b.x, b.y
('x', 'y')
>>> SharedData.x, SharedData.y
('x', 'y')
>>>
>>>
>>> # If you change in an instance, you create a new attribute _in the instance_ only:
>>> a.x = 'xxx'
>>>
>>> a.x, a.y
('xxx', 'y')
>>> b.x, b.y
('x', 'y')
>>> SharedData.x, SharedData.y
('x', 'y')
>>>
>>>
```

Example:

```python
>>> class MixedData:
...     data = 'a'
...     def __init__(self, value):
...         self.data = value
...     def __repr__(self):
...         return "self.data={}, MixedData.data={}".format(self.data, MixedData.data)
...
>>>
>>> m = MixedData(10)
>>> m
self.data=10, MixedData.data=a
>>>
```

---

Calling superclass constructors

When an object is created Python calls only one `__init__` method.
If this method is found in one of the subclasses, just this version is called.

If the superclass `__init__` method needs to be called, the method needs to call it explictly using the class name:

```python
>>> class Super:
...     def __init__(self, x):
...         print('super __init__')
...
>>>
>>> class Sub(Super):
...     def __init__(self, x, y):
...         Super.__init__(self, x)
...         print('sub __init__')
...
>>>
>>> s = Sub(10, 20)
super __init__
sub __init__
>>>
```

You can also call perform this action using `super()`. In this case `self` is passed automatically:

```python
>>> class Super:
...     def __init__(self, x):
...         print('super __init__')
...
>>> class Sub(Super):
...     def __init__(self, x, y):
...         super().__init__(x)
...         print('sub __init__')
...
>>>
>>> s = Sub(10, 20)
super __init__
sub __init__
>>>
```

---

Methods are created in the class scope and shared, through inheritance search, with all instances.

These methods can be called through the `instance`:

```python
>>> class AnotherExample:
...     def printer(self, text):
...         self.message = text
...         print(self.message)
...
>>>
>>> ae = AnotherExample()
>>> ae.printer('Hello World')
Hello World
>>> ae.message
'Hello World'
>>>
>>>
```

You can call directly from the class:

```python
>>> AnotherExample.printer(ae, 'Bye!') # you need to pass the 'self' parameter, as Python dosent pass it implictly when
... the method is called from a class
Bye!
>>>
```

---

The four usages of superclasses:

1. Super class - The super class:

```python
>>> class Super:
...     def method(self):
...         print('in Super.method')
...     def delegate(self):
...         self.action() # expects the subclass to implement it
...
>>>
>>>
```

2. A simple Inheritor, that is just an alias to the superclass:

```python
>>> class Inheritor(Super):
...     pass
...
>>> i = Inheritor()
>>> i.method()
in Super.method
>>>
```

3. `Replacer`: overrides one of the superclass methods:

```python
>>> class Replacer(Super):
...     # overrides
...     def method(self):
...         print('in Replacer method =)')
...
>>>
>>> r = Replacer()
>>> r.method()
in Replacer method =)
>>>
```

4. `Extender`: overrides superclass methods, but call them in the overriden methods

```python
>>> class Extender(Super):
...     def method(self):
...         print('before logic in Extender')
...         Super.method(self) # call superclass method
...         print('after login in Extender')
...
>>>
>>> e = Extender()
>>> e.method()
before logic in Extender
in Super.method
after login in Extender
>>>
```

5. `Provider` implements the delegated methods from the superclass:

```python
>>> class Super:
...     def method(self):
...         print('in Super.method')
...     def delegate(self):
...         self.action() # expects the subclass to implement it
...
>>>
>>> class Provider(Super):
...     def action(self):
...         print('action implemented in Provider')
...
>>> p = Provider()
>>> p.delegate()
action implemented in Provider
>>>
>>>
```

---

Abstract superclasses

You can force a superclass method to be provided (implemented) by a superclass creating an abstract method (a method with no body) with the help of the `assert` statement:

```python
>>> class Super:
...     def method(self):
...         print('in Super.method')
...     def action(self):
...         assert False, 'action() should be implemented in a subclass'
...     def delegate(self):
...         self.action() # if subclass dosent override, will use Super.action() raising an AssertionError
...
...
>>> class SubclassWithoutOverriding(Super): pass
>>>
>>> obj = SubclassWithoutOverriding()
>>> obj.delegate() # ops!
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-18-cf2b460b665c> in <module>
----> 1 obj.delegate() # ops!

<ipython-input-15-165b7544cdb3> in delegate(self)
      5         assert False, 'action() should be implemented in a subclass'
      6     def delegate(self):
----> 7         self.action() # if subclass dosent override, will use Super.action() raising an AssertException
      8
      9

<ipython-input-15-165b7544cdb3> in action(self)
      3         print('in Super.method')
      4     def action(self):
----> 5         assert False, 'action() should be implemented in a subclass'
      6     def delegate(self):
      7         self.action() # if subclass dosent override, will use Super.action() raising an AssertException

AssertionError: action() should be implemented in a subclass
>>>
```

A more elegant way to achieve the same behavior is to `raise` the built-in `NotImplementedError`:

```python
>>> class Super:
...     def method(self):
...         print('in Super.method')
...     def action(self):
...         raise NotImplementedError('action() should be overriden by a subclass')
...     def delegate(self):
...         self.action() # if subclass dosent override, will use Super.action() raising a NotImplementedError
...
...
...
>>>
>>> class SubclassWithoutOverriding(Super): pass
>>>
>>> obj = SubclassWithoutOverriding()
>>> obj.delegate()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-25-86842646d907> in <module>
----> 1 obj.delegate()

<ipython-input-22-bb7757248df6> in delegate(self)
      5         raise NotImplementedError('action() should be overriden by a subclass')
      6     def delegate(self):
----> 7         self.action() # if subclass dosent override, will use Super.action() raising a NotImplementedError
      8
      9

<ipython-input-22-bb7757248df6> in action(self)
      3         print('in Super.method')
      4     def action(self):
----> 5         raise NotImplementedError('action() should be overriden by a subclass')
      6     def delegate(self):
      7         self.action() # if subclass dosent override, will use Super.action() raising a NotImplementedError

NotImplementedError: action() should be overriden by a subclass
>>>
```

---

> Abstract superclasses using the `abc` module

The `abc` module and its mixins enforce a more strict policy. Subclasses can be created only if the implement all abstract methods:

```python
>>> from abc import ABCMeta, abstractmethod
>>>
>>> class Super(metaclass=ABCMeta): # you have to specify the metaclass
...     def delegate(self):
...         self.action()
...     @abstractmethod
...     def action(self): pass
...
>>>
>>> class Subclass(Super): pass # action was not overriden
>>> s = Subclass() # exception! action was not overriden
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-29-645f4b392e9e> in <module>
----> 1 s = Subclass() # exception! action was not overriden

TypeError: Can't instantiate abstract class Subclass with abstract methods action
>>>
```

---

> Namespaces: review

- Unqualified (`variable`) and Qualified (`object.attribute`) are treated differently.

- Unqualified (`variable`) lookups deal with scopes.

- Qualified (`object.attribute`) deal with objects namespaces and inheritance search.

- Some scopes initialize objects namespaces: `modules` and `classes`.

- These concepts usually are mixed. Example:

`object.variable` performs a scope lookup for `object` and a `namespaces search` for `variable.`

> Simple names: LEGB

- Assignemnts `var = value` create a local name, unless explicited using `global` or `nonlocal`.

- References: `var` follow the LEGB lookup rule:

1. Local (inside the current function)
2. Enclosing (any enclosing FUNCTION)
3. Global (module where the code is located globals)
4. Built-ins

**Enclosing classes are not checked in the LEGB lookup**.

> Attributes: navigate object and classes namespaces

- Assignemnts (`object.var = value`) creates the name in the object namespace.

- References (`object.var`) perform an inheritance search:

1. Instance
2. Class
3. Superclasses

Modules dont have class or superclass, so the attribute is looked only in the Instance.

An example summarizing these rules:

```python
# manynames.py
X = 11


def print_global_x():
    print(X)


def print_local_x():
    X = 22  # LEGB. Shadows the global X.
    print(X)


class Example:
    X = 33  # Class attribute: Example.X, shared with all instances through objects namespace search

    def method(self):
        X = 44  # local function scope X
        self.X = 55  # changes X in the object (self) namespace
        print(Example.X, X, self.X)  # 33, 44, 55


if __name__ == "__main__":
    print_global_x()

    print_local_x()

    e = Example()
    e.method()
```

output:

```bash
11
22
33 44 55
```

If you import this module you can access some of the names defined:

```python
import manynames

X = 99 # This X does not interfer with the manynames module lookups

print(manynames.X) # 11: manynames global X

manynames.print_global_x() # 11: the LEGB. Global is looked in the module where the function was defined.ArithmeticError

manynames.print_local_x()  # 22: prints the Local X, declared inside the function body

e = manynames.Example()
e.method() # 33, 44, 55...
```

output:

```bash
11
11
22
33 44 55
```

To change variables in the `global` or `nonlocal` from inside a fuction, you have to *declare* them using one of theses prefixs...

---

LEGB should be LEfGB: Local, Enclosing Functions, Global and Built-ins.

Enclosing classes are not looked:

```python
>>> def factory(enclosing_fx_value):
...     class Klass:
...         klass_value = enclosing_fx_value * 2
...         def method(self):
...             print(enclosing_fx_value) # ok! LEfGB
...             # print(klass_value) # Fails! Enclosing does not consided class
...             # correct way:
...             print(self.klass_value)
...     return Klass
...
>>>
>>> instance = factory(5)()
>>> instance
<__main__.factory.<locals>.Klass at 0x7f53ebba70f0>
>>>
>>> instance.method()
5
10
>>>
```

Another example:

```python
>>> X = 99
>>>
>>> class Klass:
...     X = 95 # local class scope
...     def method(self):
...         print(X) # global, dosent check the class namespace
...         print(self.X) # through inheritance search we see the class value
...
>>>
>>> k = Klass()
>>> k.method()
99
95
>>>
```

In order to access class attributes we have to qualify the class or use `self` (an instance):

```python
>>> class Klass:
...     X = 95
...     def method(self):
...         print(Klass.X, self.X)
...
>>>
>>> k = Klass()
>>> k.method()
95 95
>>>
```

---

Namespaces in objects, classes and modules are implemented as dicts in the objects `__dict__` attribute.

Instances `__dict__` s have links to their classes, in the `__class__` attr, and classes have links to their superclasses in the `__bases__`.

```python
>>> class Super:
...     def a(self):
...         self.super = 'a'
...
>>> class Sub(Super):
...     def b(self):
...         self.sub = 'b'
...
>>>
>>> sup = Super()
>>> sup.__dict__
{}
>>> sup.a()
>>> sup.__dict__
{'super': 'a'}
>>>
>>> sup.__class__
__main__.Super
>>> sup.__class__.__dict__
mappingproxy({'__module__': '__main__',
              'a': <function __main__.Super.a(self)>,
              '__dict__': <attribute '__dict__' of 'Super' objects>,
              '__weakref__': <attribute '__weakref__' of 'Super' objects>,
              '__doc__': None})
>>>
>>> sub = Sub()
>>> sub.__dict__
{}
>>> sub.b()
>>> sub.__dict__
{'sub': 'b'}
>>> sub.__class__
__main__.Sub
>>>
>>> sub.__class__.__bases__
(__main__.Super,)
>>>
```

Namespaces being dictionaries, you can access/change their through qualification or indexing:

```python
>>> class Person:
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
...
>>>
>>> p = Person('john', 33)
>>> p.name
'john'
>>> p.__dict__['name']
'john'
>>>
>>> vars(p) # same as p.__dict__
{'name': 'john', 'age': 33}
>>> p.__dict__
{'name': 'john', 'age': 33}
>>>
>>> p.__dict__['age'] = 100
>>> p.age
100
>>>
```

**Inheritance search just works with qualification, though:**

```python
>>> class Dog:
...     sound = 'raw'
...     def bark(self):
...         print(self.sound)
...
>>>
>>> class SmallDog(Dog): pass
>>>
>>> s = SmallDog()
>>> s.__dict__['sound'] # does not work
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-77-6d5f52ab7191> in <module>
----> 1 s.__dict__['sound'] # does not work

KeyError: 'sound'
>>>
>>> s.sound
'raw'
>>>
```

---

You can use `__class__` and `__bases__` attributes to print a class tree, for example:

```python
def class_tree(klass, indent=0):
    print("." * indent, klass.__name__)
    for superklass in getattr(klass, "__bases__", []):
        class_tree(superklass, indent + 4)


if __name__ == "__main__":

    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    class E:
        pass

    class F(D, E):
        pass

    class_tree(F)

```

output:

```bash
 F
.... D
........ B
............ A
................ object
........ C
............ A
................ object
.... E
........ object
```

---

### Operator Overloading

> Indexing and Slicing

`__getitem__(self, key_or_index)` is the method called in indexing operations: `instance[key_or_index]`, where `self` is `instance`:

```python
>>> class DoubleIndex:
...     def __getitem__(self, number):
...         return number * 2
...
>>>
>>> d = DoubleIndex()
>>> d['spam']
'spamspam'
>>> d[10]
20
>>>
```

Slicing is also handled by `__getitem__`, receiving a `slice()` object:

```python
>>> class SliceHandler:
...     def __getitem__(self, s):
...         print('start: ', s.start, 'stop: ', s.stop, 'step: ', s.step)
...
...
>>>
>>> s = SliceHandler()
>>> s[0:11:2]
start:  0 stop:  11 step:  2
>>>
```

`__getitem__` can check the type of the argument to perform the correct action:

```python
>>> class Indexer:
...     def __getitem__(self, i):
...         if isinstance(i, int):
...             print('index[i]')
...         elif isinstance(i, slice):
...             print('slice[a:b:c]')
...         else:
...             print('cant index by other types')
...
>>>
>>> ind = Indexer()
>>> ind[0:11:2]
slice[a:b:c]
>>> ind[10]
index[i]
>>> ind['spam']
cant index by other types
>>>
```

The assignment variant is the `__setitem__(self, i, val)` method:

```python
>>> class Example:
...     def __getitem__(self, ind):
...         print('getitem->{}'.format(ind))
...     def __setitem__(self, ind, val):
...         print('setitem->{} = {}'.format(ind, val))
...
...
>>> e = Example()
>>> e['a']
getitem->a
>>> e['a'] = 10
setitem->a = 10
>>>
```

Caution! The `__index__` returns an integer representation when the object is used in an indexing operation.

```python
>>> class Example:
...     def __index__(self):
...         return 42
...
>>>
>>> r = range(0, 101)
>>> e = Example()
>>> r[e] # e is converted to an int
42
>>>
```

It is kind obscure.

`__getitem__` is also used in `for` loops when there is no iteration protocol methods implemented. It starts indexing the first, `0`, position and goes up until an `IndexError` is issued (which is handled by the `for`):

```python
>>> class Example:
...     def __init__(self, text):
...         self.text = text
...     def __getitem__(self, index):
...         return self.text[index]
...
>>>
>>> e = Example('spam')
>>> for letter in e: print(letter)
s
p
a
m
>>>
```

You get more than the `for` loop. You also get support for the membership operator `in`, comprehensions, and so on:

```python
>>> class Example:
...     def __init__(self, text):
...         self.text = text
...     def __getitem__(self, index):
...         return self.text[index]
...
>>>
>>> e = Example('bacon')
>>> for l in e: print(l, )
b
a
c
o
n
>>> 'b' in e
True
>>> 'x' in e
False
>>>
>>> [l.upper() for l in e]
['B', 'A', 'C', 'O', 'N']
>>>
>>> list(e)
['b', 'a', 'c', 'o', 'n']
>>> tuple(e)
('b', 'a', 'c', 'o', 'n')
>>> map(str.upper, e)
<map at 0x7fc518c01208>
>>> list( map(str.upper, e) )
['B', 'A', 'C', 'O', 'N']
>>>
```

### Iterable objects: `__iter__` and `__next__`

Today, the iterator protocol recommends the usage of `__iter__` and `__next__` methods instead of relying in the `__getitem__`:

```python
>>> class Squares:
...     def __init__(self, start, stop):
...         self.start = start
...         self.stop = stop
...         self.current = 0
...     def __iter__(self):
...         return self
...     def __next__(self):
...         if self.current >= self.stop:
...             raise StopIteration
...         item = self.current * 2
...         self.current += 1
...         return item
...
>>>
>>> s = Squares(0, 10)
>>> for i in s: print(i)
0
2
4
6
8
10
12
14
16
18
>>>
```

Remember: `yield` is used only in functions, turning them into generators.

The previous iterator example is a single shot iterator, as `__iter__` always return `self`:

```python
>>> class Squares:
...     def __init__(self, start, stop):
...         self.start = start
...         self.stop = stop
...         self.current = 0
...     def __iter__(self):
...         return self
...     def __next__(self):
...         if self.current >= self.stop:
...             raise StopIteration
...         item = self.current * 2
...         self.current += 1
...         return item
...
>>>
>>> s = Squares(1, 3)
>>> for i in s: print(i)
0
2
4
>>>
>>> # Exhausted
>>> for i in s: print(i)
>>>
```

This last iterator could be created with generator functions or comprehensions:

```python
>>> def gsquares(start, end):
...     current = start
...     while current < end:
...         yield current
...         current += 1
...
>>>
>>> gsquares(1, 3)
<generator object gsquares at 0x7fc518efffc0>
>>> list( gsquares(1, 3) )
[1, 2]
>>>
>>> start = 1; end = 3; list( (current * 2 for current in range(start,end) ) )
[2, 4]
>>>
```

---

Multiple iterators for the same object

To allow multiple iterators for the same object, just return a stateful object from `__iter__`:

```python
>>> class Example:
...     def __init__(self, text):
...         self.text = text
...     def __iter__(self):
...         return ExampleIterator(self)
...
>>> class ExampleIterator:
...     def __init__(self, instance):
...         self.instance = instance
...         self.current = 0
...     def __next__(self):
...         if self.current >= len(self.instance.text): raise StopIteration
...
...         response = self.instance.text[self.current]
...         self.current += 1
...
...         return response
...
>>>
>>> e1 = iter(e)
>>> e2 = iter(e)
>>>
>>> next(e1)
's'
>>> next(e1)
'p'
>>>
>>> next(e2)
's'
>>>
>>> next(e1)
'a'
>>> next(e1)
'm'
>>> next(e1)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-27-6c9ada9e2824> in <module>
----> 1 next(e1)

<ipython-input-19-6a168ddea4e3> in __next__(self)
      4         self.current = 0
      5     def __next__(self):
----> 6         if self.current >= len(self.instance.text): raise StopIteration
      7
      8         response = self.instance.text[self.current]

StopIteration:
>>>
```

Remember: your `__next__` method should raise `StopIteration` when exhausted. **Always.**

---

`__iter__` and `yield`

Functions that return values with yield automatically become generators with an `__iter__` method that returns the automatically
created generator and a `__next__` method that resumes the original function execution until the next `yield` or exhaustion:

```python
>>> class Example:
...     def __init__(self, text):
...         self.text = text
...         self.current = 0
...     def __iter__(self):
...         while self.current < len(self.text):
...             yield self.text[self.current]
...             self.current += 1
...
>>> e = Example('spam')
>>> for letter in e: print(letter)
s
p
a
m
>>> iter(e)
<generator object Example.__iter__ at 0x7f82e8dda6d0>
>>>
```

This method allows multiple iterators for a same object at the same time:

```python
>>> class Squares:
...     def __init__(self, start, stop):
...         self.start = start
...         self.stop = stop
...     def __iter__(self):
...         for i in range(self.start, self.stop):
...             yield i ** 2
...
>>>
>>> s = Squares(1, 11)
>>>
>>> i1 = iter(s)
>>> i2 = iter(s)
>>>
>>> next(i1)
1
>>> next(i1)
4
>>> next(i1)
9
>>> next(i2)
1
>>> next(i1)
16
>>>
```

Methods using `yield` create a different generator each time they are called.

But remember that generators are single scan iterators. They exhaust.

This can be done using an additional class and the traditional `__iter__` `__next__` approach too:

```python
>>> class Squares:
...     def __init__(self, start, stop):
...         self.start = start
...         self.stop = stop
...
...     def __iter__(self):
...         return SquaresIterator(self)
...
...
>>> class SquaresIterator:
...     def __init__(self, instance):
...         self.instance = instance
...         self.range = list( range(self.instance.start, self.instance.stop) )
...         self.current_position = 0
...
...     def __next__(self):
...         if self.current_position == len(self.range): raise StopIteration
...
...         response = self.range[self.current_position] ** 2
...         self.current_position += 1
...
...         return response
...
>>>
>>> s = Squares(1, 11)
>>> list(s)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> list(s)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>>
>>> i1 = iter(s)
>>> next(i1)
1
>>> next(i1)
4
>>>
>>> i2 = iter(s)
>>> next(i2)
1
>>> next(i2)
4
>>> next(i2)
9
>>>
```

You can create a skipable iterator using the yield approach and save some lines of code:

```python
>>> class Skip:
...     def __init__(self, wrapped):
...         self.wrapped = wrapped
...     def __iter__(self):
...         current = 0
...         while current < len(self.wrapped):
...             yield self.wrapped[current]
...             current += 2
...
...
>>> s = Skip("spam")
>>> for l in s: print(l)
s
a
>>>
```

---

Membership: `__contains__`, `__iter__` and `__getitem__`

Some operations are performed in layers. That is, they can be handled by a generic or more specific methods.

For example: the `in` membership operator is, in order, handled by (if present): `__contains__`, `__iter__` or `__getitem__`.
Being `__contains__` the more specific and `__getitem__` the more generic.

Examples:

Using `__contains__`:

```python
>>> class Squares:
...     def __init__(self, start, stop):
...         self.start = start
...         self.stop = stop
...
...     def __contains__(self, squared_value):
...         current = self.start
...         while current <= self.stop:
...             if current ** 2 == squared_value: return True
...             current += 1
...         return False
...
...
>>> s = Squares(1, 10)
>>>
>>> 100 in s
True
>>> 101 in s
False
>>>
```

---

> Intercept **undefined** attributes qualification with `__getattr__(self, attrname)`

Called only when the attribute is **not** found in the inheritance search.

```python
>>> class Example:
...     class_attr = 'A'
...
...     def __init__(self, value):
...         self.instance_attr = value
...
...     def __getattr__(self, name):
...         print('you tried to access "{}" but i could not find it anywhere'.format(name))
...
>>>
>>> e = Example('B')
>>>
>>> e.class_attr
'A'
>>> e.instance_attr
'B'
>>>
>>> e.inexistent_attr
you tried to access "inexistent_attr" but i could not find it anywhere
>>>
>>> e.another_inexistent
you tried to access "another_inexistent" but i could not find it anywhere
>>>
```

You can trigger an `AttributeError(name)` if you want too:

```python
>>> class Example:
...     def __getattr__(self, name):
...         if name in ('age', 'years', 'old'):
...             return 42
...         else:
...             raise AttributeError(name)
...
>>> e = Example()
>>> e.age
42
>>> e.years
42
>>> e.name
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-111-c517efffb09b> in <module>
----> 1 e.name

<ipython-input-107-0bb81d697dca> in __getattr__(self, name)
      4             return 42
      5         else:
----> 6             raise AttributeError(name)
      7

AttributeError: name
>>>
```

---

> Intercept **all** attribute assignments with `__setattr__(sef, attrname, value)`

Example:

```python
>>> class Example:
...     def __setattr__(self, attrname, value):
...         if attrname in ('name', 'age', 'job'):
...             self.__dict__[attrname] = value
...         else:
...             raise AttributeError(attrname)
...
>>>
>>> e = Example()
>>> e.name = 'John'
>>> e.age = 42
>>> e.job = 'dev'
>>>
>>> vars(e)
{'name': 'John', 'age': 42, 'job': 'dev'}
>>>
>>> e.nickname = 'Big John'
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-118-2ff33198739d> in <module>
----> 1 e.nickname = 'Big John'

<ipython-input-112-ccfad0c6ebc3> in __setattr__(self, attrname, value)
      4             self.__dict__[attrname] = value
      5         else:
----> 6             raise AttributeError(attrname)
      7

AttributeError: nickname
>>>
```

Caution! You cant perform a normal assignment inside a `__setattr__` method, it will cause an infinite loop.
To avoid that, assign directly to the `__dict__` attribute.

**The best way to avoid this loop is using `__dict__`.**.

You can also use superclasses implementations of `__setattr__`, but its a little more obscure:

```python
>>> class Example:
...     def __setattr__(self, attrname, value):
...         if attrname in ('name', 'age', 'job'):
...             object.__setattr__(self, attrname, value)
...         else:
...             raise AttributeError(attrname)
...
>>>
>>> e = Example()
>>> e.name = 'paul'
>>> e.age = 33
>>> e.job = 'mgr'
>>>
>>> vars(e)
{'name': 'paul', 'age': 33, 'job': 'mgr'}
>>>
>>> e.nickname = 'mr paul'
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-125-748d9886b96b> in <module>
----> 1 e.nickname = 'mr paul'

<ipython-input-119-e143744b24cc> in __setattr__(self, attrname, value)
      4             object.__setattr__(self, attrname, value)
      5         else:
----> 6             raise AttributeError(attrname)
      7

AttributeError: nickname
>>>
```

Remember that `getattr(object, attr)` is the same as: `object.attr` and `setattr(object, attr, value)` is the same as `object.attr = value`.

---

> Intercept **all** attributes deletion implementing `__delattr__`

Its called in all deletions: of existent and non-existent attributes:

```python
>>> class Example:
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
...     def __delattr__(self, attrname):
...         if attrname in ('age'):
...             del object.__delattr__(self, attrname)
...         else:
...             raise AttributeError(attrname)
...
>>>
>>> e = Example('john', 33)
>>> vars(e)
{'name': 'john', 'age': 33}
>>>
>>> del e.age # ok
>>> vars(e)
{'name': 'john'}
>>> del e.name
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-131-94fabb642c6c> in <module>
----> 1 del e.name

<ipython-input-126-5304c3ab627c> in __delattr__(self, attrname)
      7             del self.__dict__[attrname] # you have to use __dict__ to avoid infinite loops or object.__delattr__
      8         else:
----> 9             raise AttributeError(attrname)
     10

AttributeError: name
>>> del e.job # non-existent
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-132-802d15ff2081> in <module>
----> 1 del e.job # non-existent

<ipython-input-126-5304c3ab627c> in __delattr__(self, attrname)
      7             del self.__dict__[attrname] # you have to use __dict__ to avoid infinite loops or object.__delattr__
      8         else:
----> 9             raise AttributeError(attrname)
     10

AttributeError: job
>>>
```

As `__setattr__`, inside the `__delattr__` method you have to access `__dict__` directly or use a superclass implementation `object.__delattr__...`

---

> Supporting `__slots__` and properties:

If you want to override `__setattr__` and `__delattr__` and support slots and propertis, leverage superclasses `__setattr__` and `__delattr__` in the overloads.

---

> Intercepting **all** (existent and non-existent) attribute access with `__getattribute__`

```python
>>> class Example:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...     def __getattribute__(self, attrname):
...         if attrname in object.__getattribute__(self, '__dict__'):
...             return object.__getattribute__(self, attrname)
...         else:
...             print('cound not find "{}"'.format(attrname))
...
>>>
>>> e = Example(10, 20)
>>> e.x
10
>>> e.y
20
>>> e.z
cound not find "z"
>>>
```

---

# A correction: avoid __dict__, use the `object` superclass implementation when overloading `__getattr__`, `__setattr__`, `__delattr__` and `__getattribute__`.

---

If `__getattribute__` and `__getattr__` are both present in a class, `__getattr__` is called only when `__getattribute__` raises an `AttributeError` exception.

```python
>>> class Example:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...     def __getattribute__(self, attrname):
...         if attrname not in object.__getattribute__(self, '__dict__'):
...             print('getattribute: "{}" was not found'.format(attrname))
...             raise AttributeError(attrname)
...         else:
...             print('getattribute: "{}" found:'.format(attrname))
...             return object.__getattribute__(self, attrname)
...     def __getattr__(self, attrname):
...         print('getattr: "{}" was not found'.format(attrname))
...
>>>
>>> e = Example(10, 20)
>>> e.x
getattribute: "x" found:
10
>>> e.y
getattribute: "y" found:
20
>>> e.z
getattribute: "z" was not found
getattr: "z" was not found
>>>
```

---


Creating a `Private` mixin class:

```python
>>> class Private:
...     def __getattribute__(self, attrname):
...         if attrname in object.__getattribute__(self, '__privates__'):
...             raise AttributeError('{} is private'.format(attrname))
...         else:
...             return object.__getattribute__(self, attrname)
...
>>>
>>> class Person(Private):
...     __privates__ = ['salary']
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
...         self.salary = age * 1_000
...
>>>
>>> p = Person('john', 33)
>>> p.name
'john'
>>> p.age
33
>>> p.salary
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-34-39e0cbaef282> in <module>
----> 1 p.salary

<ipython-input-29-04fec670b934> in __getattribute__(self, attrname)
      2     def __getattribute__(self, attrname):
      3         if attrname in object.__getattribute__(self, '__privates__'):
----> 4             raise AttributeError('{} is private'.format(attrname))
      5         else:
      6             return object.__getattribute__(self, attrname)

AttributeError: salary is private
>>>
```

---

> String representation: `__repr__` and `__str__`

`print()` and `str()` look for the `__str__` method first. if not found, `__repr__` is used.

`repr()` looks for `__repr__` first.

`__str__` should return a human friendly representation.

`__repr__` is meant for developers. it should return a code-like representation or a detailed one for devs.

```python
>>> class Person:
...     def __init__(self, name, age, job):
...         self.name = name
...         self.age = age
...         self.job = job
...     def __str__(self):
...         return '{}, {} years old, works as {}'.format(self.name, self.age, self.job)
...     def __repr__(self):
...         return 'Person("{}", {}, "{}")'.format(self.name, self.age, self.job)
...
>>>
>>> p = Person("John", 33, "mgr")
>>> repr(p)
'Person("John", 33, "mgr")'
>>> str(p)
'John, 33 years old, works as mgr'
>>>
```

But caution, objects nested inside other objects usually will have their `__repr__` called, not their `__str__`:

```python
>>> class Person:
...     def __init__(self, name, age, job):
...         self.name = name
...         self.age = age
...         self.job = job
...     def __str__(self):
...         return '{}, {} years old, works as {}'.format(self.name, self.age, self.job)
...     def __repr__(self):
...         return 'Person("{}", {}, "{}")'.format(self.name, self.age, self.job)
...
>>>
>>> lst = [Person('john', 33, 'dev'), Person('paul', 22, 'mgr')]
>>> lst
[Person("john", 33, "dev"), Person("paul", 22, "mgr")]
>>> print(lst)
[Person("john", 33, "dev"), Person("paul", 22, "mgr")]
>>>
>>> print( lst[0], lst[1] )
john, 33 years old, works as dev paul, 22 years old, works as mgr
>>>
```

---

> `__call__`

Allows instances to answer to the "function call syntax":

```python
>>> class Example:
...     def __call__(self, *args, **kwargs):
...         print(args)
...         print(kwargs)
...
>>>
>>> e = Example()
>>> e(1, 2, 3, a=10, b=20, c=30)
(1, 2, 3)
{'a': 10, 'b': 20, 'c': 30}
>>>
```

```python
>>> class Product:
...     def __init__(self, factor):
...         self.factor = factor
...     def __call__(self, value):
...         return value * self.factor
...
>>>
>>> p3 = Product(3)
>>> p3(10)
30
>>>
>>> p2 = Product(2)
>>> p2(10)
20
>>> p2(99)
198
>>>
```

---

> Comparision operators: `__eq__`, `__lt__`, `__gt__`, `__ne__`

* There is no implicit relation between these operators. You need to define `__eq__` and `__ne__`, for example. `__eq__` being `True` does not imply `__ne__` being `False`.

---

> Boolean tests: `__bool__` and `__len__`

All objects have an inherent boolean value in Python.

First Python checks for the `__bool__` method, which should return `True` or `False`.

If `__bool__` is not present, it checks for `__len__` and infers the boolean value from the length of the object. Nonzero meaning `True`.

If neither method is present, Python assumes the object is `True`.

```python
>>>  class Truth1:
...     def __bool__(self):
...        return False
...
>>> t1 = Truth1()
>>> bool( t1 )
False
>>>
>>> class Truth2:
...     def __len__(self):
...         return 42
...
>>> t2 = Truth2()
>>> len(t2)
42
>>> bool(t2)
True
>>>
>>> class Truth3: pass
>>>
>>> t3 = Truth3()
>>> bool(t3)
True
>>>
```

---

> Object destruction (garbage collection): `__del__`

Called when the object is garbage collected:

```python
>>> class Person:
...     def __init__(self, name):
...         self.name = name
...     def __del__(self):
...         print('{} died'.format(self.name))
...
>>>
>>> p = Person('john')
>>> p = Person('paul') # john will be gc
john died
>>>
```

---

An example using inheritance and the `is-a` relation:

```python
class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def raise_salary(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(f"{self.name} does something")

    def __repr__(self):
        return f"<Employee name={self.name}, salary={self.salary}>"

class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, salary=50_000)

    def work(self):
        print(f'{self.name} cooks')

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, salary=40_000)

    def work(self):
        print(f'{self.name} serves')


class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(f'{self.name} makes pizza and serve and never complains')


if __name__ == '__main__':
    bob = PizzaRobot('bob')
    print(bob)
    bob.work()
    bob.raise_salary(0.25)
    print(bob)
    print()

    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        print(obj)
        obj.work()
```

`PizzaRobot` **is-a** `Chef` which also **is-a** an `Employee`.
Therefore, `PizzaRobot` **is-a** `Chef` and an `Employee`.

---

Composition or Aggregation is a way to designate _parts of a whole_, forming `has-a` relationships.

You create a container object formed by other objects.

Lets expand our Pizza Shop example:

```python
class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def raise_salary(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(f"{self.name} does something")

    def __repr__(self):
        return f"<Employee name={self.name}, salary={self.salary}>"

class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, salary=50_000)

    def work(self):
        print(f'{self.name} cooks')

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, salary=40_000)

    def work(self):
        print(f'{self.name} serves')


class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(f'{self.name} makes pizza')


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(f'{self.name} orders from {server}')

    def pay(self, server):
        print(f'{self.name} pays to {server}')


class Oven:
    def bake(self):
        print(f'Oven-{id(self)} bakes')


class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def place_order(self, customer_name):
        customer = Customer(customer_name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        self.server.work()
        customer.pay(self.server)

if __name__ == '__main__':
    pizza_shop = PizzaShop()
    pizza_shop.place_order('John')
```

---

Another composition example: a `Pipe` class:

```python
class Pipe:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.read()
            if not data: break
            data = self.convert(data)
            self.writer.write(data)

    def convert(self, data):
        raise NotImplementedError('You must overload the convert method')
```

Composition, `has-a` `reader` and `has-a` `writer`.

An example:

```python
class Pipe:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.convert(data)
            self.writer.write(data)

        self.writer.flush()

        self.reader.close()
        self.writer.close()

    def convert(self, data):
        raise NotImplementedError('You must overload the convert method')


class UpperPipe(Pipe):
    def convert(self, data):
        return data.upper()


if __name__ == '__main__':
    reader = open('/etc/hosts', 'rt')
    writer = open('/tmp/hosts_upper', 'wt')

    pipe = UpperPipe(reader, writer)
    pipe.process()
```

---

Wrapppers / Proxy objects - Delegation

Controllers composed by other objects, to which the received actions requests are delegated.

The wrapper retains most of the wrapped object interface, but adds some functionality before or after the action is performed by the wrapped obj.

A good example uses `__getattribute__`, creating a sort of tracer:

```python
class Tracer:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __getattribute__(self, name):
        print(f"Trace: {name=}")
        return getattr(object.__getattribute__(self, "wrapped"), name)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    p = Person("john", 33)
    traced_p = Tracer(p)

    print(traced_p.name)
    print(traced_p.age)

    lst = [1, 2, 3]
    traced_l = Tracer(lst)

    traced_l.append(4)

    traced_l += 5
    print(f'{traced_l=})
```

output:

```bash
Trace: name='name'
john
Trace: name='age'
33
Trace: name='append'
```

But caution, since Python 3 operators dont trigger `__getattribute__` or `__getattr__` anymore:

```python
class TracedList(list):
    def __getattribute__(self, name):
        print(f'Trace: {name=}')
        return super().__getattribute__(name)

    def __iadd__(self, value):
        print(f"__iadd__({value=})")
        return super().__iadd__(value)


if __name__ == "__main__":
    t = TracedList()
    t.append(10) # calls getattribute
    t += [11]      # does not trigger getattribute
    print(t)
```

```bash
Trace: name='append'
__iadd__(value=[11])
[10, 11]
```

---

Pseudoprivate classes attributes

Class attributes prefixed with an underscore `_` are a convention, meaning they should not be changed.

Name mangling happens inside the `class` statement (all of it, including the method bodies).

Basically, it transforms every name/variable prefixed with two underscores, for example: `__name` into `_ClassName__name`.

The following class:

```python
class Example:
    __spam = 'spam'

    def __method(self):
        self.__eggs = 'eggs'
        self.__spam = 'spam!'

        return 'bacon'

if __name__ == '__main__':
    e = Example()

    print()
    print(f'{dir(e)=}')
    print()

    print(f'{e._Example__method()=}')

```

output:

```bash
dir(e)=['_Example__method', '_Example__spam', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

e._Example__method()='bacon'
```

The mangled class is, internally, something like:

```python
class Example:
    _Example__spam = 'spam'

    def __method(self):
        self._Example__eggs = 'eggs'
        self._Example__spam = 'spam!'

        return 'bacon'

if __name__ == '__main__':
    e = Example()

    print()
    print(f'{dir(e)=}')
    print()

    print(f'{e._Example__method()=}')
```

producing the same output:

```bash
dir(e)=['_Example__method', '_Example__spam', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

e._Example__method()='bacon'
```

---

Methods are objects: bound vs unbound

Python has two ways to access class methods. Through classes (without a `self`) and through instances (with a defined `self`):

* Unbound (class methods) no `self`: you must pass `self` yourself:

```python
In [8]: class Example:
   ...:     def __init__(self, message):
   ...:         self.message = message
   ...:
   ...:     def up(self):
   ...:         print(self.message.upper())
   ...:

In [9]: e = Example("spam")

In [10]: # Unbound method, needs to pass self

In [11]: Example.up(self=e)
SPAM

In [12]:
```

* Bound method: `self` is passed automagically.

```python
In [12]: class Example:
    ...:     def __init__(self, message):
    ...:         self.message = message
    ...:
    ...:     def up(self):
    ...:         print(self.message.upper())
    ...:

In [13]: e = Example("spam")

In [14]:

In [14]: # Bound method

In [15]: e.up() # self is passed magically
SPAM

In [16]:
```

Both ways return full-fledged objects, which can be passed around.

But **bound methods** have an advantage. They can replace common functions, as they already have the `self` pre-defined:

```python
In [29]: class Button:
    ...:     def __init__(self, handler):
    ...:         self.handler = handler
    ...:     def clicked(self):
    ...:         self.handler(self) # call the handler passing the button as argument
    ...:

In [30]: class ButtonHandler:
    ...:     def click(self, btn):
    ...:         print(f'{id(btn)=}')
    ...:

In [31]:

In [31]: handler = ButtonHandler()

In [32]: btn = Button(handler.click)

In [33]: btn.clicked()
id(btn)=139840076663728
```

Another bound method example:

```python
In [34]: class Person:
    ...:     def __init__(self, name):
    ...:         self.name = name
    ...:     def greet(self):
    ...:         print(f'{self.name} says hi!')
    ...:

In [35]: p = Person('John')

In [36]:

In [36]: john_greeting = p.greet

In [37]: john_greeting()
John says hi!

In [38]: john_greeting()
John says hi!

In [39]:
```

The John example with an unbound method:

```python
In [39]: class Person:
    ...:     def __init__(self, name):
    ...:         self.name = name
    ...:     def greet(self):
    ...:         print(f'{self.name} says hi!')
    ...:

In [40]:

In [40]: p = Person('John')

In [41]: Person.greet(p) # we have to pass self
John says hi!
```

Note that `self.method` are bounds methods. `self` is the instance and is passed automagically as `self` =):

```python
In [42]: class Banner:
    ...:     def __init__(self, message):
    ...:         self.message = message
    ...:
    ...:     def draw(self):
    ...:         header = '-' * (len(self.message) + 2)
    ...:         footer = header
    ...:         return header + '\n' + self.message + '\n' + footer + '\n'
    ...:
    ...:     def output(self):
    ...:         draw_fx = self.draw # self.draw is a bound method, self being self again =)
    ...:         banner = draw_fx()
    ...:         print(banner)
    ...:

In [43]: b = Banner('spam')

In [44]: b.output()
------
spam
------

In [45]:
```

---

In Python 3 you can declare methods (actually, regular functions) inside classes witch dont expect the `self` parameter:

```python
In [45]: class Banner:
    ...:     def b1(message):
    ...:         print('*' * len(message))
    ...:         print(message)
    ...:         print('*' * len(message))
    ...:

In [46]: Banner.b1("Hello!")
******
Hello!
******

In [47]:
```

But caution. If you call it from an instance, Python still tries to pass the instance a `self`, what raises an exception:

```python
In [47]: b = Banner()

In [48]: b.b1("Spam!")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-48-03a170eeb5a4> in <module>
----> 1 b.b1("Spam!")

TypeError: b1() takes 1 positional argument but 2 were given

In [49]:
```

Bound methods behave just like any other function as full-fledged objects:

```python
In [13]: class Number:
    ...:     def __init__(self, n):
    ...:         self.n = n
    ...:     def double(self):
    ...:         return self.n ** 2
    ...:

In [14]: lst = [n1.double, n2.double, n3.double] # list of bound methods

In [15]: for method in lst:
    ...:     print( method() )
    ...:
    ...:
1
4
9
```

Bound methods have attributes, `__self__` indicating the instance and `__func__` referencing the class (unbound) method linked:

```python
In [19]: class Number:
    ...:     def __init__(self, n):
    ...:         self.n = n
    ...:     def double(self):
    ...:         return self.n ** 2
    ...:

In [20]: n = Number(10)

In [21]: bound_method = n.double

In [22]: bound_method.__self__
Out[22]: <__main__.Number at 0x7f9d576269d0>

In [23]: bound_method.__func__
Out[23]: <function __main__.Number.double(self)>

In [24]:
```

---

Classes are objects: generic object factories

The factory pattern is trivial to implement in Python. Remember that classes are first-class objects too:

```python
In [26]: class Person: pass

In [27]: class Manager: pass

In [28]: class Customer: pass

In [29]:

In [29]: def factory(klass_name):
    ...:     mapping = {'Person': Person, 'Manager': Manager, 'Customr': Customer}
    ...:     klass = mapping.get(klass_name)
    ...:     if klass:
    ...:         return klass()
    ...:

In [30]: person = factory('Person')

In [31]: person
Out[31]: <__main__.Person at 0x7f9d560f70d0>
```

---

Multiple inheritance - Mix-in classes

Example 1: ListInstance

```python
In [1]: class ListInstance:
   ...:     def __attrnames(self):
   ...:         result = []
   ...:         for attr in sorted(self.__dict__):
   ...:             result.append("{}={}".format(attr, self.__dict__[attr]))
   ...:         return " ".join(result)
   ...:     def __str__(self):
   ...:         return "<Instance of {}, memory address {}>[{}]".format(self.__class__.__name__, id(self), self.__attrnames())
   ...:

In [2]: class Person(ListInstance):
   ...:     def __init__(self, name, age):
   ...:         self.name = name
   ...:         self.age = age
   ...:

In [3]: p = Person("John", 33)

In [4]: p
Out[4]: <__main__.Person at 0x7f1bc2ea09e8>

In [5]: print(p)
<Instance of Person, memory address 139757210962408>[age=33 name=John]

In [6]:
```

An example listing the inherited attributes also (uses `dir()` instead of `__dict__`):

```python
In [10]: class ListInherited:
    ...:     def __attrnames(self):
    ...:         result = []
    ...:         for attr in sorted(dir(self)):
    ...:             result.append("{}={}".format(attr, getattr(self, attr)))
    ...:         return " ".join(result)
    ...:     def __str__(self):
    ...:         return "<Instance of {}, memory address {}>[{}]".format(self.__class__.__name__, id(self), self.__attrnames())
    ...:

In [11]: class Person(ListInherited):
    ...:     def __init__(self, name, age):
    ...:         self.name = name
    ...:         self.age = age
    ...:

In [12]: p = Person("John", 33)

In [13]: print(p)
<Instance of Person, memory address 139757215536296>[_ListInherited__attrnames=<bound method ListInherited.__attrnames of <__main__.Person object at 0x7f1bc32fd4a8>> __class__=<class '__main__.Person'> __delattr__=<method-wrapper '__delattr__' of Person object at 0x7f1bc32fd4a8> __dict__={'name': 'John', 'age': 33} __dir__=<built-in method __dir__ of Person object at 0x7f1bc32fd4a8> __doc__=None __eq__=<method-wrapper '__eq__' of Person object at 0x7f1bc32fd4a8> __format__=<built-in method __format__ of Person object at 0x7f1bc32fd4a8> __ge__=<method-wrapper '__ge__' of Person object at 0x7f1bc32fd4a8> __getattribute__=<method-wrapper '__getattribute__' of Person object at 0x7f1bc32fd4a8> __gt__=<method-wrapper '__gt__' of Person object at 0x7f1bc32fd4a8> __hash__=<method-wrapper '__hash__' of Person object at 0x7f1bc32fd4a8> __init__=<bound method Person.__init__ of <__main__.Person object at 0x7f1bc32fd4a8>> __init_subclass__=<built-in method __init_subclass__ of type object at 0x3334a98> __le__=<method-wrapper '__le__' of Person object at 0x7f1bc32fd4a8> __lt__=<method-wrapper '__lt__' of Person object at 0x7f1bc32fd4a8> __module__=__main__ __ne__=<method-wrapper '__ne__' of Person object at 0x7f1bc32fd4a8> __new__=<built-in method __new__ of type object at 0x9d17a0> __reduce__=<built-in method __reduce__ of Person object at 0x7f1bc32fd4a8> __reduce_ex__=<built-in method __reduce_ex__ of Person object at 0x7f1bc32fd4a8> __repr__=<method-wrapper '__repr__' of Person object at 0x7f1bc32fd4a8> __setattr__=<method-wrapper '__setattr__' of Person object at 0x7f1bc32fd4a8> __sizeof__=<built-in method __sizeof__ of Person object at 0x7f1bc32fd4a8> __str__=<bound method ListInherited.__str__ of <__main__.Person object at 0x7f1bc32fd4a8>> __subclasshook__=<built-in method __subclasshook__ of type object at 0x3334a98> __weakref__=None age=33 name=John]

In [14]:
```

---

Extending types by composition

A Set class that 'has-a' a list:

```python
class Set:
    def __init__(self, data):
        self.data = []
        self.data.extend(data)

    def __iter__(self):
        for item in self.data:
            yield item

    def intersect(self, other):
        result = []
        for item in self.data:
            if item in other:
                result.append(item)

        return Set(result)

    def __repr__(self):
        return repr(self.data)


if __name__ == "__main__":
    s1 = Set([1, 2, 3])
    s2 = Set([3, 4, 5])

    print(s1.intersect(s2))

```

Much of the functionality is achieved through delegation.

---

Extending type throug subclassing

You can extend any of the core types: `str`, `int`, etc, like any other class.

An example: a LuaList, a list which indexing starts in 1.

```python
In [7]: class LuaList(list):
   ...:     def __getitem__(self, offset):
   ...:         return list.__getitem__(self, offset - 1)
   ...:

In [8]:

In [8]: lst = LuaList(["a", "b", "c"])

In [9]: lst[1]
Out[9]: 'a'

In [10]: lst[2]
Out[10]: 'b'

In [11]: lst[3]
Out[11]: 'c'

In [12]: lst
Out[12]: ['a', 'b', 'c']

In [13]: type(lst)
Out[13]: __main__.LuaList

In [14]:
```

---

New Style Class Model

Differences:

1. In Python 3, operators dont trigger `__getattr__` or `__getattribute__`:

```python
>>> class PlusOne:
...     def __getattr__(self, attr):
...         print("not found {}".format(attr))
...
...     def __add__(self, other):
...         return other + 1
...
>>> p = PlusOne()
>>> p.non_existent # non existent attribute, will trigger getattr
not found non_existent
>>> p + 1          # existent operator (__add__) called directly
2
>>> p - 1          # non existent operator (__sub__), but dosent trigger __getattr__
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-18-f3102d908cb7> in <module>
----> 1 p - 1          # non existent operator (__sub__), but dosent trigger __getattr__

TypeError: unsupported operand type(s) for -: 'PlusOne' and 'int'
>>>
```

```python
>>> class PlusOne:
...     def __getattribute__(self, attr):
...         print("accessing {}".format(attr))
...
...     def __add__(self, other):
...         return other + 1
...
>>> p = PlusOne()
>>> p.non_existent # non existent attribute, will trigger getattr
accessing non_existent
>>> p + 1          # existent operator (__add__) called directly
2
>>> p - 1
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-26-1f4b0c9221f8> in <module>
----> 1 p - 1

TypeError: unsupported operand type(s) for -: 'PlusOne' and 'int'
>>>
```

This happens because the search beings in the class, not in the instance.

Therefore, to delegate operator calls to wrapped objects you need to redefine those methods in the wrapper class, because
you cant use `__getattr__` or `__getattribute__` tricks:

```python
>>> class WrappedNumber:
...     def __init__(self, number):
...         self.number = number
...     def __getattr__(self, attr):
...         return getattr(self.number, attr)
...
>>> w = WrappedNumber(10)
>>> w + 3
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-33-f3f51bf85a2a> in <module>
----> 1 w + 3

TypeError: unsupported operand type(s) for +: 'WrappedNumber' and 'int'
>>>
```

Correct way:

```python
>>> class WrappedNumber:
...     def __init__(self, number):
...         self.number = number
...     def __add__(self, other):
...         return self.number.__add__(other)
...
>>> w = WrappedNumber(10)
>>> w + 3
13
>>>
```

This happens because operators search start in the class, skipping the instance.


2. Types and classes are the same now:

```python
>>> num = 10
>>> type( num )
int
>>> type( num ) is int
True
>>> type( num ) is num.__class__
True
>>>
```

3. All classes now implictly inherit from `object`, thus having some default methods as: `__repr__()`

---

Slots

Limit the possible variables that can be assigned to an instance.

```python
>>> class Example:
...     __slots__ = ["name", "age"]
...
>>> e = Example()
>>> e.name # you still need to assign before
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-3-044cc9756e8a> in <module>
----> 1 e.name # you still need to assign before

AttributeError: name
>>>
>>> e.name = "John"
>>> e.age = 23
>>> e.job = "mgr" # not possible
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-6-f613016262a4> in <module>
----> 1 e.job = "mgr" # not possible

AttributeError: 'Example' object has no attribute 'job'
>>>
```

Slots are a memory optimization and should be used only when strictly necessary.

Instances of classes declared with `__slots__` do not have a `__dict__` as storage:

```python
>>> class Person:
...     __slots__ = ("name", "age")
...
>>>
>>> p = Person()
>>> p.name = "John"
>>> p.age = 32
>>>
>>> p.__dict__ # ops
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-5-223115104e02> in <module>
----> 1 p.__dict__ # ops

AttributeError: 'Person' object has no attribute '__dict__'
>>> vars(p)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-0c35495ab569> in <module>
----> 1 vars(p)

TypeError: vars() argument must have __dict__ attribute
```

* To access slots or dict attributes in instances in a neutral form, use `getattr()` and `setattr()`:

```python
>>> class Person:
...     __slots__ = ("name", "age")
...
>>> p = Person()
>>> p.name = "John"
>>>
>>> getattr(p, 'name')
'John'
>>>
>>> setattr(p, 'age', 33)
>>>
>>> p.age
33
>>>
```

* To list attributes in a neutral way, that works for `__dict__` and `__slots__` based instances, use `dir(obj)`:

```python
>>> class Person:
...     __slots__ = ("name", "age")
...
>>>
>>> p = Person()
>>> p.name = "John"
>>> setattr(p, 'age', 33)
>>>
>>> dir(p)
['__class__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__slots__',
 '__str__',
 '__subclasshook__',
 'age',
 'name']
>>>
```

* Slots restrict the possible names in instances:

```python
>>> class Person:
...     __slots__ = ("name", "age")
...
>>> p = Person()
>>> p.name = 'john'
>>> p.age = 33
>>> p.job = 'mgr' # not possible, 'job' is not in __slots__
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-23-22b95480f42d> in <module>
----> 1 p.job = 'mgr' # not possible, 'job' is not in __slots__

AttributeError: 'Person' object has no attribute 'job'
>>>
```

* You can mix both mechanisms including `__dict__` in `__slots__`:

```python
>>> class Person:
...     __slots__ = ("name", "age", "__dict__")
...
>>> p = Person()
>>> p.name = "john"
>>> p.age = 33
>>> p.job = "mgr"
>>>
>>> vars(p)
{'job': 'mgr'}
>>>
>>> p.name, p.age, p.job
('john', 33, 'mgr')
>>>
```

* Caution: `__slots__` are subject to the inheritance search, so when you fetch it from an instance, you get the least defined.
But Python automatically merges the `__slots__` of the class and its superclasses.

```python
>>> class Employee:
...     __slots__ = ("name", "age", "job")
...
>>> class Developer(Employee):
...     __slots__ = ("language", )
...
>>> class Manager(Developer):
...     __slots__ = ("nice_or_annoying", )
...
>>> # You can use superclasse slots also
>>> d = Developer()
>>> d.name = 'John'
>>> d.age = 33
>>> d.language = 'Python'
>>>
>>> # You can use all attributes, but if you require '__slots__' you get only the least defined
>>> d.__slots__
('language',)
>>>
```

* If you use `__slots__` in an inheritace, you should include it in every class.
When ommited, the class generates a `__dict__`, thus negating the memory optimization benefit:

```python
>>> class A: pass # no slots
>>> class B(A): __slots__ = ("x", "y") # will create dict because of A
>>>
>>> b = B()
>>> b.x = 1
>>> b.y = 2
>>> b.z = 3
>>>
>>> b.__dict__
{'z': 3}
>>>
>>> b.x, b.y, b.z
(1, 2, 3)
>>>
```

* `hasattr()` works with `__slots__` too:

```python
>>> class Point: __slots__ = ("x", "y")
>>>
>>> p = Point()
>>> p.x = 10
>>> hasattr(p, 'x')
True
>>> hasattr(p, 'z')
False
>>>
```

---

Properties

The magic is implemented throug the `property()` built-in.

`help(property)`:

```python
Init signature: property(self, /, *args, **kwargs)
Docstring:
property(fget=None, fset=None, fdel=None, doc=None) -> property attribute

fget is a function to be used for getting an attribute value, and likewise
fset is a function for setting, and fdel a function for del'ing, an
attribute.  Typical use is to define a managed attribute x:

class C(object):
    def getx(self): return self._x
    def setx(self, value): self._x = value
    def delx(self): del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

Decorators make defining new properties or modifying existing ones easy:

class C(object):
    @property
    def x(self):
        "I am the 'x' property."
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x
Type:           type
Subclasses:     abstractproperty
```

If you skip any of the arguments, the operation will no be supported.

An example:

```python
>>> class Person:
...     def _get_age(self):
...         print("_get_age()")
...         return self._age
...
...     def _set_age(self, value):
...         print("_set_age()")
...         self._age = value
...
...     age = property(fget=_get_age, fset=_set_age, fdel=None)
...
>>>
>>> p = Person()
>>> p.age = 42
_set_age()
>>> p.age
_get_age()
42
>>>
```

Properties can also be created using decorators:

```python
>>> class Person:
...     # The getter must come first
...     @property
...     def age(self):
...         print("age-getter")
...         return self._age
...
...     @age.setter
...     def age(self, value):
...         print("age-setter")
...         self._age = value
...
>>>
>>> p = Person()
>>> p.age = 42
age-setter
>>> p.age
age-getter
42
>>>
```

---

Descriptors: classes with `__get__` and `__set__` that behave as an attribute.

```python
>>> class SimpleAgeDescriptor:
...     def __get__(self, instance, owner):
...         print("__get__(self={}, instance={}, owner={})".format(self, instance, owner))
...         if hasattr(instance, '_age'):
...             return instance._age
...         else:
...             return 42
...
...     def __set__(self, instance, value):
...         print("__set__(self={}, instance={}, value={})".format(self, instance, value))
...         instance._age = value
...
...
...
>>> class Person:
...     age = SimpleAgeDescriptor()
...
>>>
>>> p = Person()
>>> p.age
__get__(self=<__main__.SimpleAgeDescriptor object at 0x7f1214f2d898>, instance=<__main__.Person object at 0x7f1214f050b8>, owner=<class '__main__.Person'>)
42
>>> p.age = 33
__set__(self=<__main__.SimpleAgeDescriptor object at 0x7f1214f2d898>, instance=<__main__.Person object at 0x7f1214f050b8>, value=33)
>>> p.age
__get__(self=<__main__.SimpleAgeDescriptor object at 0x7f1214f2d898>, instance=<__main__.Person object at 0x7f1214f050b8>, owner=<class '__main__.Person'>)
33
>>>
```

---

Static and class methods

`@staticmethod`

Define methods inside classes that do not require instances. So Python dosent passes the `self` argument.

> In Python 3 you can create functions inside classes that do not receive any argument (class or self/instance).
Simple functions, really. But mind that these methods will fail if you call them from an instance: Python will try to pass
the `self` argument:

```python
>>> class InstanceCounter:
...     counter = 0
...
...     def __init__(self):
...         InstanceCounter.counter += 1
...
...     def print_counter(): # simple function defined in the class.
...         print("InstanceCounter instances: {}".format(InstanceCounter.counter))
...
>>>
>>> i1 = InstanceCounter()
>>> i2 = InstanceCounter()
>>>
>>> InstanceCounter.print_counter() # from the class, works fine
InstanceCounter instances: 2
>>>
>>> # But from the instances, fails, as Python tries to pass 'self'
>>> i1.print_counter()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-109-79f9b2f4a3d1> in <module>
----> 1 i1.print_counter()

TypeError: print_counter() takes 0 positional arguments but 1 was given
>>>
```

To solve it, always use the `@staticmethod` built-in:

```python
>>> class InstanceCounter:
...     counter = 0
...
...     def __init__(self):
...         InstanceCounter.counter += 1
...
...     @staticmethod
...     def print_counter():
...         print("InstanceCounter instances: {}".format(InstanceCounter.counter))
...
>>>
>>> i1 = InstanceCounter()
>>> i2 = InstanceCounter()
>>> i3 = InstanceCounter()
>>>
>>> # Class call works
>>> InstanceCounter.print_counter()
InstanceCounter instances: 3
>>>
>>> # Instance call also works
>>> i3.print_counter()
InstanceCounter instances: 3
>>>
```

`@classmethod`

Define methods inside classes that should receive the class (or the class of the instance) where it was called as first argument.

The previous example could be coded as a class method too:

```python
>>> class InstanceCounter:
...     counter = 0
...
...     def __init__(self):
...         InstanceCounter.counter += 1
...
...     @classmethod
...     def print_counter(cls):
...         print("{} instances: {}".format(cls, getattr(cls, 'counter', 0)))
...
...
>>> i1 = InstanceCounter()
>>> i2 = InstanceCounter()
>>> i3 = InstanceCounter()
>>>
>>> # Class call works
>>> InstanceCounter.print_counter()
<class '__main__.InstanceCounter'> instances: 3
>>>
>>> # Instance call works too
>>> i3.print_counter()
<class '__main__.InstanceCounter'> instances: 3
>>>
```

But mind that class methods receive the most specific (lowest) class of the call subject.
So caution with inheritance:

```python
>>> class InstanceCounter:
...     counter = 0
...
...     def __init__(self):
...         InstanceCounter.counter += 1
...
...     @classmethod
...     def print_counter(cls): # simple function defined in the class.
...         print("{} instances: {}".format(cls, getattr(cls, 'counter', 0)))
...
...
>>>
>>> class EnhancedInstanceCounter(InstanceCounter):
...     @classmethod
...     def print_counter(cls):
...         print("*** Enhanced ***: {} has instances {} ***".format(cls, getattr(cls, 'counter', 0)))
...
>>>
>>> i1 = InstanceCounter()
>>> i2 = InstanceCounter()
>>> i3 = InstanceCounter()
>>>
>>> InstanceCounter.print_counter()
<class '__main__.InstanceCounter'> instances: 3
>>> i3.print_counter()
<class '__main__.InstanceCounter'> instances: 3
>>>
>>> e1 = EnhancedInstanceCounter()
>>> e2 = EnhancedInstanceCounter()
>>>
>>> EnhancedInstanceCounter.print_counter()
*** Enhanced ***: <class '__main__.EnhancedInstanceCounter'> has instances 5 ***
>>> e2.print_counter()
*** Enhanced ***: <class '__main__.EnhancedInstanceCounter'> has instances 5 ***
>>>
```

Works because `getattr()` finds `counter` using inheritance search.

But if the method assigns something to the generically passed class, issues can occour.

Lets create an instance counter per class:

```python
>>> class GenericInstanceCounter:
...     def __init__(self):
...         if 'counter' in vars(self.__class__):
...             self.__class__.counter += 1
...         else:
...             self.__class__.counter = 1
...     @classmethod
...     def get_counter(klass):
...         if 'counter' in vars(klass):
...             return klass.counter
...         else:
...             return 0
...
>>>
>>> class A(GenericInstanceCounter): pass
>>> class B(GenericInstanceCounter): pass
>>>
>>> a1 = A()
>>> a2 = A()
>>> a3 = A()
>>>
>>> A.get_counter()
3
>>> a1.get_counter()
3
>>>
>>> # No instances
>>> B.get_counter()
0
>>>
>>> # Inheritance example
>>> class C(A): pass
>>>
>>> # C has no instances, but A has three
>>> C.get_counter()
0
>>>
```

---

Function Decorators

Example:

```python
@metafunction
def func_or_method(...):
    pass
```

Is the same as:

```python
def func_or_method(...):
    pass

# name rebiding
func_or_method = metafunction(func_or_method)
```

A simple decorator that traces how many times a function was called:

```python
>>> class tracer:
...     def __init__(self, fx):
...         self.fx = fx
...         self.counter = 0
...     def __call__(self, *args, **kwargs):
...         self.counter += 1
...         print(self.counter, "times")
...         return self.fx(*args, **kwargs)
...
>>>
>>> @tracer
... def add(a, b):
...     return a + b
...
>>> add(10, 20)
1 times
30
>>> add(4, 3)
2 times
7
>>>
```

> Remember that `__init__` is called to initialize the object. The object is returned implictly by Python.

It is the same as:

```python
>>> def sub(a, b):
...     return a - b
...
>>> sub = tracer(sub)
>>> sub(10, 5)
1 times
5
>>> sub(10, 4) # triggers tracer.__call__
2 times
6
>>>
```

This implementation fails with class methods:

```python
>>> class tracer:
...     def __init__(self, fx):
...         self.fx = fx
...         self.counter = 0
...     def __call__(self, *args, **kwargs):
...         print("self: {}".format(self))
...         print("*args: {}".format(args))
...         print("**kwargs: {}".format(kwargs))
...
...         self.counter += 1
...         print(self.counter, "times")
...
...         return self.fx(*args, **kwargs)
...
>>>
>>> class Math:
...     @tracer
...     def add(self, a, b):
...         return a + b
...
>>>
>>> m = Math()
>>> m.add(10, 20)
self: <__main__.tracer object at 0x7f1214651ef0>
*args: (10, 20)
**kwargs: {}
1 times
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-169-a3aaa252df11> in <module>
----> 1 m.add(10, 20)

<ipython-input-166-062f9424e1ef> in __call__(self, *args, **kwargs)
     11         print(self.counter, "times")
     12
---> 13         return self.fx(*args, **kwargs)
     14

TypeError: add() missing 1 required positional argument: 'b'
>>>
```

Because `self` is mapped to the `tracer` instance, thus passing the firt argument as `self` to the wrapped method.

To solve this, you can use another common coding pattern: function wrapping

```python
>>> def tracer(fx):
...     def wrap(*args, **kwargs):
...         wrap.times += 1
...         print("Called {} times".format(wrap.times))
...         return fx(*args, **kwargs)
...     wrap.times = 0
...     return wrap
...
>>>
>>> class Math:
...     @tracer
...     def add(self, a, b):
...         return a + b
...
>>>
>>> m = Math()
>>> m.add(10, 20)
Called 1 times
30
>>> m.add(1, 2)
Called 2 times
3
>>>
```

This version works because `self` is not mapped, so the instance is passed as a regular positional argument.

---

Class decorators

```python
def decorator(klass): return enchanced_klass # must return a callable

@decorator
class Klass: pass
```

is mapped to:

```python
def decorator(klass): return enchanced_klass # must return a callable

class Klass: pass

Klass = decorator(Klass)
```

Class decorators can enhance and return the received class or wrap it and intercep all instance construction calls.

Example: decorator classes that count instances.

```python
>>> def countable(klass):
...     klass.counter = 0
...
...     original_init = klass.__init__
...     def new_init(self, *args, **kwargs):
...         self.__class__.counter += 1
...         original_init(self, *args, **kwargs)
...
...     klass.__init__ = new_init
...
...     return klass
...
>>> @countable
... class Spam: pass
>>>
>>> s1 = Spam()
>>> s2 = Spam()
>>>
>>> Spam.counter
2
>>> s1.counter
2
>>>
```

You can use class decorator to create fully featured proxies:

```python
>>> def upcase(klass):
...     class Proxy:
...         def __init__(self, *args, **kwargs):
...             self.wrapped = klass(*args, **kwargs)
...         def __getattr__(self, attr):
...             return getattr(self.wrapped, attr, "").upper()
...     return Proxy
...
>>>
>>> @upcase
... class Person:
...     def __init__(self, name, job):
...         self.name = name
...         self.job = job
...
>>> p = Person("john", "dev")
>>> p.name
'JOHN'
>>> p.job
'DEV'
>>>
```

---

Exceptions

You can capture exceptions with `try/except` blocks:

```python
>>> arr = ['a', 'b', 'c']
>>> arr[4] # ops!
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-2-311f5b4cae56> in <module>
----> 1 arr[4] # ops!

IndexError: list index out of range
>>>
>>> try:
...     print(arr[4])
... except IndexError:
...     print('out of bounds')
...
out of bounds
>>>
```

`IndexError` is one of the many built-ins exceptions already defined in the language.

You can use the `assert` statement to check conditions and trigger the `AssertException` if these are no meet:

```python
In [7]: value = 10

In [8]: assert value < 5, "Value is too small"
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-8-bea9a853b341> in <module>
----> 1 assert value < 5, "Value is too small"

AssertionError: Value is too small

In [9]:
```

And you can `raise` exceptions:

```python
In [9]: def fetch(arr, index):
   ...:     if index >= len(arr):
   ...:         raise IndexError
   ...:     else:
   ...:         return arr[index]
   ...:

In [10]: fetch(['a', 'b', 'c'], 2)
Out[10]: 'c'

In [11]: fetch(['a', 'b', 'c'], 3)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-11-2bc2bb757ecf> in <module>
----> 1 fetch(['a', 'b', 'c'], 3)

<ipython-input-9-d9ad47945398> in fetch(arr, index)
      1 def fetch(arr, index):
      2     if index >= len(arr):
----> 3         raise IndexError
      4     else:
      5         return arr[index]

IndexError:

In [12]:
```

Exception are just classes. You can create your own, inheriting from `Exception`:

```python
>>> class EvenException(Exception): pass
>>> class OddException(Exception): pass
>>>
>>> def handle(number):
...     if number % 2 == 0:
...         raise EvenException
...     else:
...         raise OddException
...
>>> handle(10)
---------------------------------------------------------------------------
EvenException                             Traceback (most recent call last)
<ipython-input-6-d1c2b8d10fe0> in <module>
----> 1 handle(10)

<ipython-input-5-72415a662d97> in handle(number)
      1 def handle(number):
      2     if number % 2 == 0:
----> 3         raise EvenException
      4     else:
      5         raise OddException

EvenException:
>>>
>>> handle(33)
---------------------------------------------------------------------------
OddException                              Traceback (most recent call last)
<ipython-input-7-b8de1288a416> in <module>
----> 1 handle(33)

<ipython-input-5-72415a662d97> in handle(number)
      3         raise EvenException
      4     else:
----> 5         raise OddException
      6

OddException:
>>>
```

And you can catch them the same way as built-in exceptions:

```python
>>> try:
...     handle(10)
... except EvenException:
...     print('Even!')
...
Even!
>>>
```

You can customize the exceptions messages defining the `__str__` method.

```python
>>> class EvenException(Exception):
...     def __str__(self):
...         return 'EVEN'
...
>>> handle(10)
---------------------------------------------------------------------------
EvenException                             Traceback (most recent call last)
<ipython-input-10-d1c2b8d10fe0> in <module>
----> 1 handle(10)

<ipython-input-5-72415a662d97> in handle(number)
      1 def handle(number):
      2     if number % 2 == 0:
----> 3         raise EvenException
      4     else:
      5         raise OddException

EvenException: EVEN
>>>
```

The except clause can have an `as` statement to access the exception object:

```python
>>> try:
...     handle(10)
... except EvenException as ex:
...     print(repr(ex)) # print
...     print(type(ex)) # ex type
...     print(id(ex))   # ex memory address
...
EvenException()
<class '__main__.EvenException'>
139802552693864
>>>
```

Important:

```python
raise Exception
```

is automatically translated by Python to:

```python
raise Exception()
```

`try` statements can have `finally` blocks, which are executed always, when an exception happens or not:

```python
# No exception happens
>>> try:
...     assert 10 > 1
... except AssertionError:
...     print('handled exception')
... finally:
...     print('executed after')
...
executed after
>>>

# Exception is handled
>>> try:
...     assert 10 > 11
... except AssertionError:
...     print('handled exception')
... finally:
...     print('executed after')
...
handled exception
executed after
>>>

# Exception happens and is not handled
>>> try:
...     assert 10 > 11
... except IndexError:
...     print('handled exception')
... finally:
...     print('executed after')
...
executed after
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-23-934b07f42374> in <module>
      1 try:
----> 2     assert 10 > 11
      3 except IndexError:
      4     print('handled exception')
      5 finally:

AssertionError:
>>>
```

In a similar way as `for` and `while` loops, `try` statements can have an `else` clause that is run if no `exception` (`break` in loops) happens:

`else` in loops. run only if no `break` is issued:

```python
# no-breaks
>>> for i in range(3):
...     print(i)
... else:
...     print('ok')
...
0
1
2
ok

# break
>>> for i in range(3):
...     print(i)
...     if i % 2 == 0: break
... else:
...     print('ok')
...
0

# else still runs if a continue is issued
>>> for i in range(3):
...     print(i)
...     if i % 2 == 0: continue
... else:
...     print('ok')
...
0
1
2
ok
>>>
```

In the `try` statement the `else` clause is run only if **no** exceptions happen in the `try` block, be them handled or not:

```python
>>> arr = ['a', 'b', 'c']
>>> index = 2
>>>
>>> try:
...     print(arr[index])
... except IndexError:
...     print('array out of bounds')
... else:
...     print('no exceptions. index is inside array bounds')
...
c
no exceptions. index is inside array bounds
>>>
```

Handled or non handled exceptions both stop `else` execution:

```python
# handled
>>> try:
...     raise IndexError
... except IndexError:
...     print('handled IndexError')
... else:
...     print('no exceptions! else is running')
...
handled IndexError
>>>

# non-handled
>>> try:
...     raise IndexError
... except AttributeError:
...     print('handled AttributeError')
... else:
...     print('no exceptions! else is running')
...
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-37-99dc79166c45> in <module>
      1 try:
----> 2     raise IndexError
      3 except AttributeError:
      4     print('handled AttributeError')
      5 else:

IndexError:
>>>
```

You can match all exceptions with an empty `except` block:

```python
>>> try:
...     raise NotImplementedError
... except IndexError:
...     print('IndexError')
... except AttributeError:
...     print('AttributeError')
... except:
...     print('Generic Exception Handler')
...
Generic Exception Handler
>>>
```

Exceptions propagate up until they are handled by Python's default exception handler, which prints the exceptions and exit.

```python
>>> def inner():
...     raise NotImplementedError
...
>>> def outer():
...     inner()
...
>>>
>>> try:
...     outer()
... except NotImplementedError:
...     print('handled the inner-launched exception')
...
handled the inner-launched exception
>>>
```

You can handle multiple exceptions types in the same `except` clause:

```python
>>> try:
...     if int(random.random() * 10) % 2 == 0: # even
...         raise NotImplementedError
...     else: # odd
...         raise AttributeError
... except (NotImplementedError, AttributeError) as e:
...     print("Exception handled: {}".format(repr(e)))
...
Exception handled: AttributeError()
>>>
>>> try:
...     if int(random.random() * 10) % 2 == 0: # even
...         raise NotImplementedError
...     else: # odd
...         raise AttributeError
... except (NotImplementedError, AttributeError) as e:
...     print("Exception handled: {}".format(repr(e)))
...
Exception handled: NotImplementedError()
>>>
```

Caution. The empty `except` clause also catches system exceptions, not meant to be handled by your code.
To mitigate it, use `except Exception:` which has almost the same effect, but ignores system-meant exceptions.

```python
>>> try:
...     raise NotImplementedError
... except IndexError:
...     print('IndexError')
... except AttributeError:
...     print('AttributeError')
... except Exception:
...     print('Generic Exception Handler')
...
Generic Exception Handler
>>>
```

`finally` is always executed. Even if the `except` or `else` clauses raises exceptions:

```python
>>> try:
...     raise NotImplementedError
... except Exception:
...     raise IndexError
... finally:
...     print('Executed before the IndexError exception is propagated')
...
Executed before the IndexError exception is propagated
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-76-0ded7e148e2e> in <module>
      1 try:
----> 2     raise NotImplementedError
      3 except Exception:

NotImplementedError:

During handling of the above exception, another exception occurred:

IndexError                                Traceback (most recent call last)
<ipython-input-76-0ded7e148e2e> in <module>
      2     raise NotImplementedError
      3 except Exception:
----> 4     raise IndexError
      5 finally:
      6     print('Executed before the IndexError exception is propagated')

IndexError:
>>>
>>> try:
...     print('no exceptions raised in try!')
... except Exception:
...     raise IndexError
... else:
...     print('no exceptions. running else. will raise and exception')
...     raise AttributeError
... finally:
...     print('Executed before the AttributeError exception in else clause is propagated')
...
...
no exceptions raised in try!
no exceptions. running else. will raise and exception
Executed before the AttributeError exception in else clause is propagated
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-77-b16cd8a637eb> in <module>
      5 else:
      6     print('no exceptions. running else. will raise and exception')
----> 7     raise AttributeError
      8 finally:
      9     print('Executed before the AttributeError exception in else clause is propagated')

AttributeError:
>>>
```

`raise` triggers exceptions in Python. It comes in three forms:

```python
raise ExceptionClass      # raise ExceptionClass. Python automatically converts it to: raise ExceptionClass()
raise ExceptionInstance() # raise an instance of ExceptionClass
raise                     # reraise the last triggered exception, propagating it
```

The `raise ExceptionClass` is converted to `raise ExceptionClass` actually:

```python
raise IndexError             # Class (instance created)
raise IndexError()           # Instance (created in statement)
```

You can instatiate the exception object before too:

```python
>>> error = IndexError()
>>>
>>> raise error
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-79-a2e21a396f4d> in <module>
----> 1 raise error

IndexError:
>>>
```

You can access the exception instances using the `as` statement in the `except` clauses:

```python
>>> error = IndexError()
>>> id(error)
139802552020136
>>>
>>> try:
...     raise error
... except IndexError as e:
...     print(e.__class__)
...     print(id(e))
...
<class 'IndexError'>
139802552020136
>>>
```

Another example, using user-defined exceptions:

```python
>>> class MyError(Exception):
...     def __init__(self, value):
...         self.value = value
...
>>>
>>> try:
...     raise MyError(42)
... except MyError as e:
...     print(e.value)
...
42
>>>
```

Caution: the `as` statement in `except` clauses localizes the variable to the `except` block below it and, after the block execution, performs a
`del` in the reference, even if it was existent before the `try` statement:

```python
>>> e = 3.14
>>> print(e)
3.14
>>>
>>>
>>> try:
...     raise NotImplementedError
... except NotImplementedError as e:
...     print(repr(e))
...
NotImplementedError()
>>>
>>> print(e) # ops!
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-88-f193e723d7bd> in <module>
----> 1 print(e) # ops!

NameError: name 'e' is not defined
>>>
```

Hence, avoid reutilizing names in `except-as` clauses.

To propagate an exception, use `raise` alone:

```python
>>> try:
...     raise NotImplementedError
... except NotImplementedError:
...     print('handled. propagating: ')
...     raise
...
handled. propagating:
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-89-de724c44c7b2> in <module>
      1 try:
----> 2     raise NotImplementedError
      3 except NotImplementedError:
      4     print('handled. propagating: ')
      5     raise

NotImplementedError:
>>>
```

When an exception is raised because of another exception you can use the `raise CurrentException from PreviousException` statement.
Python will output both exceptions and mark the `PreviosException` instance in the `__cause__` attribute of the `CurrentException` instance.


```python
>>> try:
...     1 / 0
... except ZeroDivisionError as e:
...     raise NotImplementedError("Zero div is not implemented") from e
...
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-90-13af6a8b1218> in <module>
      1 try:
----> 2     1 / 0
      3 except ZeroDivisionError as e:

ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

NotImplementedError                       Traceback (most recent call last)
<ipython-input-90-13af6a8b1218> in <module>
      2     1 / 0
      3 except ZeroDivisionError as e:
----> 4     raise NotImplementedError("Zero div is not implemented") from e
      5

NotImplementedError: Zero div is not implemented
>>>
```

Simalarly, if an exception is triggered in an `except` block, the exception which was being handle is set as the `__context__` attribute of
the new exception and both are print:

```python
>>> try:
...     1 / 0
... except ZeroDivisionError:
...     typo # not defined
...
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-91-cba524358743> in <module>
      1 try:
----> 2     1 / 0
      3 except ZeroDivisionError:

ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

NameError                                 Traceback (most recent call last)
<ipython-input-91-cba524358743> in <module>
      2     1 / 0
      3 except ZeroDivisionError:
----> 4     typo # not defined
      5

NameError: name 'typo' is not defined
>>>
```

`assert` is an `if` with a `raise`:

```python
>>> value = 10
>>>
>>> if value >= 10:
...     raise ValueError("Greater or equal to 10")
...
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-93-b2c9386f0062> in <module>
      1 if value >= 10:
----> 2     raise ValueError("Greater or equal to 10")
      3

ValueError: Greater or equal to 10
>>>
```

Is the same as:

```python
>>> value = 10
>>> assert value < 10, "Greater or equal to 10"
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-95-0446de4b4d1a> in <module>
----> 1 assert value < 10, "Greater or equal to 10"

AssertionError: Greater or equal to 10
>>>
```

The syntax is:

```python
asset test, data
```

If `test` is `False` an `AssertionError` is raised and `data` is passed as argument:

```python
if not test:
    raise AssertionError(data)
```

You can disable asserts in code running Python in optimized mode: `-o`.
In this mode, the global `__debug__` will be set to `False`.

---

`with expr [as var]:` Context Managers

`expr` should return an object that implements the context management interface defined by Python.

optionaly, you can create a reference to this in object `as var` and use it in the block below.

The object returned by `expr` can run code before or after the `with` code block, regardless of any exceptions that happen.

The expression should return a context manager object to execute actions before and/or after the with block, but can also
return a different object to be assigned to `var`.

An example is the file object, which returns a context manager aware object that closes the file automatically after the `with` block,
even if exceptions happen inside the block:

```python
>>> with open('/etc/hosts', 'r') as fp:
...     data = fp.read()
...     while data:
...         print(data)
...         data = fp.read()
...
...
127.0.0.1	localhost
127.0.1.1	ThinkPad-T440s

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

>>> # file closed automatically
>>>
```

The context manager protocol:

1. The expression must return an object with `__enter__` and `__exit__` methods.

2. The `__enter__` method is called in the object. The return object is assigned to the variable in the `as` clause, if present, or discarded.

3. Code in the `with` block is executed.

4. After the `with` block executes sucessfully or raises an exception, the `__exit__` method is called.

If an exception happened, its details are passed to the `__exit__` method.

If the `__exit__` method returns a `False` value, the received exception is automatically reraised (this is the most common and desired behavior).

If `__exit__` returns a `True` value, the received exception is terminated and not propagated.


A simple context manager example:

```python
>>> class CManager:
...     def message(self, arg):
...         print('***')
...         print(arg)
...         print('***')
...     def __enter__(self):
...         print('starting the block execution')
...         return self # return the CManager instance to be assigned to a possible as clause
...     def __exit__(self, exc_type, exc_value, exc_tb):
...         if exc_type is None:
...             print('No exception! Went fine')
...         else:
...             print('An exception was raised: {}'.format(repr(exc_type)))
...             return False # forces propagation. can be ommited, remember that methods return None (false) by default
...
>>>
>>> with CManager() as manager:
...     print('Doing my work')
...
starting the block execution
Doing my work
No exception! Went fine
>>>
>>> with CManager() as manager:
...     print('Doing my work')
...     raise NotImplementedError
...
starting the block execution
Doing my work
An exception was raised: <class 'NotImplementedError'>
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-8-c1e9de99a2e1> in <module>
      1 with CManager() as manager:
      2     print('Doing my work')
----> 3     raise NotImplementedError
      4

NotImplementedError:
>>>
```

You can list multiple context managers separated by commas in `with` statements.
To read multiple files simultaneously, for example:

```python
>>> with open('/etc/hosts') as hosts, open('/etc/protocols') as protocols:
...     data = hosts.readline(), protocols.readline()
...     while all(data):
...         print(data)
...         data = hosts.readline(), protocols.readline()
...
('127.0.0.1\tlocalhost\n', '# Internet (IP) protocols\n')
('127.0.1.1\tThinkPad-T440s\n', '#\n')
('\n', '# Updated from http://www.iana.org/assignments/protocol-numbers and other\n')
('# The following lines are desirable for IPv6 capable hosts\n', '# sources.\n')
('::1     ip6-localhost ip6-loopback\n', '# New protocols will be added on request if they have been officially\n')
('fe00::0 ip6-localnet\n', '# assigned by IANA and are not historical.\n')
('ff00::0 ip6-mcastprefix\n', '# If you need a huge list of used numbers please install the nmap package.\n')
('ff02::1 ip6-allnodes\n', '\n')
('ff02::2 ip6-allrouters\n', 'ip\t0\tIP\t\t# internet protocol, pseudo protocol number\n')
>>>
```

---

`except` clausses perform an `isinstance()` check.

It is, if you set a superclass in the `except` clause but raises a `subclass`, the match will occur:

```python
>>> class TopError(Exception): pass
>>> class SubError(TopError): pass
>>>
>>> try:
...     raise SubError
... except TopError as e:
...     print('type(e) = {}'.format(repr(type(e))))
...     print('isinstance(e, TopError) = {}'.format(isinstance(e, TopError)))
...
type(e) = <class '__main__.SubError'>
isinstance(e, TopError) = True
>>>
```

---

Python exceptions hierarchy has classes that give birth to categories of exceptions:

BaseException          # Superclass of all exceptions, provides default constructor (save arguments in `args` and provides a default `__str__`)
-- Exception           # User-defined exceptions should inherit from Exception
------ ArithmeticError # Superclass to all number related exceptions: OverflowError, ZeroDivisionError, FloatingPointError...
------ LookupError     # Superclass to all indexing related exceptions: IndexError, KeyError

Example of the functionality provided by `BaseException`:

```python
>>> be = BaseException("Erro!", 1, 2, 3)
>>> print(be)
('Erro!', 1, 2, 3)
>>> print(repr(be))
BaseException('Erro!', 1, 2, 3)
>>>
>>> be.args
('Erro!', 1, 2, 3)
>>>
>>> raise be
---------------------------------------------------------------------------
BaseException                             Traceback (most recent call last)
<ipython-input-24-2b6c74aeba29> in <module>
----> 1 raise be

BaseException: ('Erro!', 1, 2, 3)
>>>
```

Unless you redefine the class constructor, any argument passed to an `Exception` constructor is saved in the `args` attribute and is
displayed when the instance is printed (`__str__`).

If you pass no arguments, an empty string is used.

If you pass only one argument, it is treated as an string and is used.

If you pass more than one argument, args is treated as a tuple.

Example:

```python
>>> raise IndexError() # no arg
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-25-0cf668fc6142> in <module>
----> 1 raise IndexError() # no arg

IndexError:
>>>
>>>
>>> raise IndexError('simple single string') # single arg
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-26-cd3cfa1c53d7> in <module>
----> 1 raise IndexError('simple single string') # single arg

IndexError: simple single string
>>>
>>>
>>> raise IndexError('multiple', 'messages', 1, 2, 3, 'as', 'arguments') # multiple arguments
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-27-fb9fa3bbe6cb> in <module>
----> 1 raise IndexError('multiple', 'messages', 1, 2, 3, 'as', 'arguments') # multiple arguments

IndexError: ('multiple', 'messages', 1, 2, 3, 'as', 'arguments')
>>>
```

This holds for user-defined classes too:

```python
>>> raise CustomError() # no arg
---------------------------------------------------------------------------
CustomError                               Traceback (most recent call last)
<ipython-input-29-d91347c6bc75> in <module>
----> 1 raise CustomError() # no arg

CustomError:
>>>
>>> raise CustomError('error message') # single arg
---------------------------------------------------------------------------
CustomError                               Traceback (most recent call last)
<ipython-input-30-9ca7d3bd6409> in <module>
----> 1 raise CustomError('error message') # single arg

CustomError: error message
>>>
>>> raise CustomError('roses', 'are', 'red') # multiple args
---------------------------------------------------------------------------
CustomError                               Traceback (most recent call last)
<ipython-input-31-006d4b9ea527> in <module>
----> 1 raise CustomError('roses', 'are', 'red') # multiple args

CustomError: ('roses', 'are', 'red')
>>>
```

If you want to customize the exception instance representation, override the `__str__` method:

```python
>>> class MyTimedError(Exception):
...     def __str__(self):
...         from datetime import datetime
...         return 'MyTimedError raised at {}'.format(datetime.now())
...
...
>>> raise MyTimedError
---------------------------------------------------------------------------
MyTimedError                              Traceback (most recent call last)
<ipython-input-33-9365682d870e> in <module>
----> 1 raise MyTimedError

MyTimedError: MyTimedError raised at 2020-06-07 03:08:50.502359
>>>
```

---

The last raised `Exception` is always disponible in the `sys.exc_info()[0]` variable.

Actually, `sys.exc_info()` returns a tuple with `type, instance, traceback`.

---

`try` blocks are stacked in Python. Exceptions propagate until the top.
When handled by one `except` clause, the exception is terminated. It does not propagate anymore.

```python
>>> class Error(Exception): pass
>>>
>>> # most outer
>>> def most_outer():
...     try:
...         outer()
...     except Error:
...         print('Handle in most_outer')
...
>>>
>>> def outer():
...     inner()
...
>>> def inner():
...     raise Error
...
>>>
>>> most_outer() # Exception will be raise in inner() but caught in most_outer()
Handle in most_outer
>>>
```

To force the propagation, you shoud 'reraise' with a empty `raise` statement or raising the exception instance: `raise exception_object`.

```python
>>> class Error(Exception): pass
>>>
>>> def most_outer():
...     try:
...         outer()
...     except Error as e:
...         print('Handle in most_outer and reraised')
...         raise # or raise e
...
>>> def outer():
...     inner()
...
>>> def inner():
...     raise Error
...
>>>
>>> most_outer()
Handle in most_outer and reraised
---------------------------------------------------------------------------
Error                                     Traceback (most recent call last)
<ipython-input-11-d278f8fbf6b3> in <module>
----> 1 most_outer()

<ipython-input-8-7ea98f06a745> in most_outer()
      1 def most_outer():
      2     try:
----> 3         outer()
      4     except Error as e:
      5         print('Handle in most_outer and reraised')

<ipython-input-9-d5e3f7c43260> in outer()
      1 def outer():
----> 2     inner()
      3

<ipython-input-10-57f17d0929e1> in inner()
      1 def inner():
----> 2     raise Error
      3

Error:
>>>
```

Remember that you can handle the exception a raise a different one using the `raise ... from ...` syntax:

```python
>>> class OriginalError(Exception): pass
>>> class CustomError(Exception): pass
>>>
>>> def most_outer():
...     try:
...         outer()
...     except Error as e:
...         print('Handle in most_outer and raises another customized exception')
...         raise CustomError from e
...
>>> def outer():
...     inner()
...
>>> def inner():
...     raise Error
...
>>> most_outer()
Handle in most_outer and raises another customized exception
---------------------------------------------------------------------------
Error                                     Traceback (most recent call last)
<ipython-input-20-991f9aba106d> in most_outer()
      2     try:
----> 3         outer()
      4     except Error as e:

<ipython-input-21-d5e3f7c43260> in outer()
      1 def outer():
----> 2     inner()
      3

<ipython-input-22-57f17d0929e1> in inner()
      1 def inner():
----> 2     raise Error
      3

Error:

The above exception was the direct cause of the following exception:

CustomError                               Traceback (most recent call last)
<ipython-input-23-d278f8fbf6b3> in <module>
----> 1 most_outer()

<ipython-input-20-991f9aba106d> in most_outer()
      4     except Error as e:
      5         print('Handle in most_outer and raises another customized exception')
----> 6         raise CustomError from e
      7

CustomError:
>>>
```

Different from `except` clauses, `finally` clauses don't kill the exception. They are executed in each level, but the exception still is propagated:

```python
>>> class Error(Exception): pass
>>>
>>> def most_outer():
...     try:
...         outer()
...     finally:
...         print('most_outer')
...
>>> def outer():
...     try:
...         inner()
...     finally:
...         print('outer')
...
>>>
>>> def inner():
...     try:
...         raise Error
...     finally:
...         print('inner')
...
>>>
>>> most_outer()
inner
outer
most_outer
---------------------------------------------------------------------------
Error                                     Traceback (most recent call last)
<ipython-input-29-d278f8fbf6b3> in <module>
----> 1 most_outer()

<ipython-input-25-0035eb2efd4d> in most_outer()
      1 def most_outer():
      2     try:
----> 3         outer()
      4     finally:
      5         print('most_outer')

<ipython-input-26-6c926f16e278> in outer()
      1 def outer():
      2     try:
----> 3         inner()
      4     finally:
      5         print('outer')

<ipython-input-27-08c0e92ce514> in inner()
      1 def inner():
      2     try:
----> 3         raise Error
      4     finally:
      5         print('inner')

Error:
>>>
```

---

Breaking out of multiple nested loops (go-to) using exceptions

Also note that variables declared inside `try` blocks are mantained after the `try` is executed (launching or not exceptions).

```python
>>> class ExitLoop(Exception): pass
>>>
>>> try:
...     while True:
...         while True:
...             for i in range(10):
...                 if i > 3: raise ExitLoop
...                 print('looping3: ', i)
...             print('looping2')
...         print('looping1')
... except ExitLoop:
...     print('ok. exited.')
...
looping3:  0
looping3:  1
looping3:  2
looping3:  3
ok. exited.
>>>
>>> print('i stopped at: ', i)
i stopped at:  4
>>>
```

---


Sometimes exceptions are just signals, not errors per se. `KeyboardInterrupt` for example:

```python
>>> while True:
...     try:
...         command = input('Enter command or CTRL + C to exit: ')
...         print(command.upper())
...     except KeyboardInterrupt:
...         print('Ok! Bye')
...         break
...
Enter command or CTRL + C to exit: echo
ECHO
Enter command or CTRL + C to exit: cd
CD
Enter command or CTRL + C to exit: del
DEL
Enter command or CTRL + C to exit: ^COk! Bye
>>>
```

---

Signaling conditions with exceptions

```python
>>> lst = ['spam', 'eggs', 'bacon']
>>>
>>> class SearchFound(Exception): pass
... class SearchNotFound(Exception): pass
...
... def search(lst, item):
...     if item in lst:
...         raise SearchFound
...     else:
...         raise SearchNotFound
...
>>>
>>> try:
...     search(lst, 'bacon')
... except SearchFound:
...     print('Ok! Found it.')
... except SearchNotFound:
...     print('oh! not found')
...
Ok! Found it.
>>>
```

---

You can use the variables defined in the `try` block in the clauses below:

```python
>>> try:
...     item = 10
...     raise IndexError
... except:
...     print(item)
...     print('exception handled')
...
10
exception handled
>>>

>>> try:
...     item = 10
... except:
...     print('exception handled')
... else:
...     print(item)
...     print('else: no exceptions happened')
...
...
10
else: no exceptions happened
>>>
```

---

`sys.exc_info()` returns the most recently raised exception. Its useful for empty `except` blocks.

```python
import random
import sys

exceptions = (AttributeError, IndexError, NotImplementedError)

try:
    raise random.choice(exceptions)
except:
    exc_class, exc_obj, _ = sys.exc_info()
    print(f'{exc_class} / {exc_obj}')
```

Output:

```bash
rnetonet on ThinkPad-T440s in /tmp via 🐍 v2.7.17
❯ python3 sample.py
<class 'AttributeError'> /
rnetonet on ThinkPad-T440s in /tmp via 🐍 v2.7.17
❯ python3 sample.py
<class 'NotImplementedError'> /
rnetonet on ThinkPad-T440s in /tmp via 🐍 v2.7.17
❯ python3 sample.py
<class 'IndexError'> /
rnetonet on ThinkPad-T440s in /tmp via 🐍 v2.7.17
❯
```

Mind that using `sys.exc_info` for getting the exception type from category excepts is overkill:

```python
>>> class Parent(Exception): pass
>>> class Sub(Parent): pass
>>> class SubSub(Sub): pass
>>>
>>> try:
...     raise SubSub
... except Parent:
...     import sys
...     print( sys.exc_info()[0] ) # overkill!
...
<class '__main__.SubSub'>
>>>
```

Correct way:

```python
>>> class Parent(Exception): pass
>>> class Sub(Parent): pass
>>> class SubSub(Sub): pass
>>>
... try:
...     raise SubSub
... except Parent as e:
...     print( e.__class__ )
...
...
<class '__main__.SubSub'>
>>>
```

This is valid for generic `except` clauses:

```python
>>> class Parent(Exception): pass
>>> class Sub(Parent): pass
>>> class SubSub(Sub): pass
>>>
>>>
... try:
...     raise SubSub
... except Exception as e:
...     print( e.__class__ )
...
...
<class '__main__.SubSub'>
>>>
```

---

Avoid empty `except` and `except Exception` clauses.

They will catch most of the errors, even programming errors that should be handled by the Python interpreter.

The difference between an empty `except:` and `except Exception:` is that the first catch even `SystemExit` exceptions, while the other, don´t.

```python
>>> mydic = {"name": "John"}
>>>
>>> try:
...     print( mydi["name"] ) # you could wait for a KeyError, but a NameError is launched because the var name is wrong: should be mydic, not mydi.
... except:
...     print("-")
...
-
>>> try:
...     print( mydi["name"] ) # you could wait for a KeyError, but a NameError is launched because the var name is wrong: should be mydic, not mydi.
... except Exception:         # also shadows the exception
...     print("-")
...
-
>>>
>>> # Be specific instead
>>> try:
...     print( mydi["name"] )
... except KeyError:
...     print("-")
...
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-13-80c9800f4ea1> in <module>
      1 try:
----> 2     print( mydi["name"] )
      3 except KeyError:
      4     print("-")
      5

NameError: name 'mydi' is not defined
>>>
```

---

Unicode and byte strings

Python 2 types: `str` and `unicode` have become, respectivily, `bytes` and `str` in Python 3.

The mutable `bytearray` type was also included.

Convert a character to its byte representation using `ord()` and back using `chr()`:

```python
In [1]: ord('ç')
Out[1]: 231

In [2]:

In [2]: chr(231)
Out[2]: 'ç'

In [3]:
```

1 byte can have (256 - 1^8) different values.

**encoding**: convert a unicode string into a sequence of bytes.

**decoding**: translate a sequence of bytes back into a string.

**encode**: string -> raw bytes.
**decode**: raw bytes -> string.

The encode/decode process is based on a defined *encoding* scheme.

Some encodings are trivial, such as ASCII and Latin-1, as they map each char to a single byte.
But other encodings are more complex, mapping some chars to more than a single byte, having UTF-8 as the most famous.

In UTF-8, the first 128 character codes are represented as single bytes.
Codes between 128 and 2047 (ox7ff) use two bytes with value between 128 and 255.
And codes above 2047 have three ou four bytes with value between 128 and 255.

Thus ASCII is a valid subset of both latin-1 and utf-8.

You see this in the example below:

```python
In [1]: s = 'spam'

In [2]: s.encode('ascii') # each char, one byte
Out[2]: b'spam'

In [3]: s.encode('latin-1') # each char, one byte
Out[3]: b'spam'

In [4]: s.encode('utf-8') # each char, one byte
Out[4]: b'spam'

In [5]:

In [5]: # Now, a string with special chars

In [6]: s = 'ação'

In [7]: s.encode('latin-1') #
Out[7]: b'a\xe7\xe3o'

In [8]: s.encode('utf-8')
Out[8]: b'a\xc3\xa7\xc3\xa3o'

In [9]:
```

Note that Python prints the first 128 character points as real characters, even in byte strings.

These and all the others (utf-16, utf-32) compose the 'unicode' standard.

Python performs the encoding decoding process only when data is transferred externally: files, network.
In Python, strings are stored in a encoding-neutral format in memory and string operations are performed in this format.

Python 3 has three types for strings and alike:

`str`: for decoded (unicode) strings;
`bytes`: for encoded (bytes) string and binary data;
`bytearray`: a mutable sequence of bytes.

The `bytes` type is a sequence of bytes / small integers (0 up to 255). If you index a position of a bytes object, it returns an integer:

```python
>>> ustr = "acentuação"
>>>
>>> ustr_as_bytes = ustr.encode("utf-8") # utf-8 is also the Python 3 default, thus you can omit.
>>>
>>> ustr_as_bytes
b'acentua\xc3\xa7\xc3\xa3o'
>>>
>>> ustr_as_bytes[3]
110
>>> ustr_as_bytes[4]
116
>>>
```

If you slice it, you get a `bytes` object. If you pass it to a `list()` you get a list of integers:

```python
>>> ustr_as_bytes[2:5]
b'ent'
>>>
>>> list( ustr_as_bytes )
[97, 99, 101, 110, 116, 117, 97, 195, 167, 195, 163, 111]
>>>
```

The `bytes` type has many string operations, in these, the bytes are treated as ascii characters:

```python
>>> ustr = "acentuação"
>>> ustr_as_bytes = ustr.encode()
>>>
>>> ustr_as_bytes
b'acentua\xc3\xa7\xc3\xa3o'
>>>
>>> print( ustr_as_bytes.upper() )
b'ACENTUA\xc3\xa7\xc3\xa3O'
>>>
```

When printed, `bytes` are replaced by ascii chars whenever possible.

---

Unicode and text files

In Py 3, when you open a file in text mode it is automatically decoded, becoming a neutral-memory-only string of the `str` type.

And when you write a `str` to a file opened in text mode, it is automatically _encoded_.

You can explictly specify the encoding to be used, if not, the default, utf-8, is used.

End-of-line translation is also automatically handled by Python in text mode.

---

Binary mode and files

To open a file in binary mode, you need to a `b` to the mode string.
In this mode no encoding or decoding is performed. Python reads `bytes` and writes `bytes` or `bytearray`.

---

In Python 3, `str` and `bytes` can never be mixed. You must explictly convert from one to the other.

Remember that `str` strings while in memory in Python are `unicode-agnostic`.

To convert an `str` to `bytes`, use: `str.encode([encoding])` or `bytes(str, encoding)`.

In `str.encode()` if you not provide the `encoding`, the default `utf-8` is used.
While `bytes()` requires you to define the encoding.

To convert from `bytes` to `str` use `bytes.decode([encoding])` or `str(bytes, encoding)`:

```python
>>> b
b'acentua\xc3\xa7\xc3\xa3o'
>>>
>>> b.decode()
'acentuação'
>>>
>>> b.decode("utf-8")
'acentuação'
>>>
>>> # Caution! str(b) requires an encoding
>>> str(b)
"b'acentua\\xc3\\xa7\\xc3\\xa3o'"
>>>
>>> str(b, "utf-8")
'acentuação'
>>>
```

Caution with the `str()` method. You should pass an encoding, otherwise the result can be not what you expect.

---

You can unicode chars in literal strings using:

`\uNNNN` or `\uNNNNNNNN`

Mind that you need to fill the four or the eight `N` positions, filling left empty positions with `0`.

```python
>>> print('\u2705')
✅
>>> print("\U0001F601") # Filled with zeros
😁
>>>
```

---

`bytes` type in Python 3

Imutable sequence of small integers between 0 and 255 (1 byte).

Python prints them as ASCII characters whenever possible.

`bytes` support almost all operations supported by the `str` type, except formating methods.

`bytes` and `str` can not be mixed.

```python
>>> bs = b'spam'
>>> bs.index(b'p') # you must pass bytes arguments
1
>>>
>>> bs.upper()
b'SPAM'
>>>
>>> bs.split(b'p')
[b's', b'am']
>>>
>>> bs[3]
109
>>>
>>>
```

`bytes` also supports indexing and slicing operations:

```python
>>> bs = b'spam'
>>> bs
b'spam'
>>> repr(bs)
"b'spam'"
>>> str(bs)
"b'spam'"
>>>
>>> bs[3] # indexing returns an integer
109
>>>
>>> chr(bs[3]) # use chr to convert to a char
'm'
>>>
>>> list(bs) # returns a list of integers
[115, 112, 97, 109]
>>>
>>> bs[2:4] # slicing returns another bytes object
b'am'
>>>
>>> len(bs) # number of elements
4
>>>
>>> bs + bs
b'spamspam'
>>>
```

---

`str` operations are unicode-aware. They work with unicode code points, not bytes.

```python
>>> s = 'ação'
>>>
>>> len(s) # unicode code points
4
>>>
>>> s.upper()
'AÇÃO'
>>>
>>> bs = s.encode()
>>> bs
b'a\xc3\xa7\xc3\xa3o'
>>>
>>> len(bs) # num of bytes
6
>>>
>>> bs.upper()
b'A\xc3\xa7\xc3\xa3O'
>>>
```

---

Other ways to create `bytes` objects:

```python
>>> b = b'abc' # literal
>>> b
b'abc'
>>>
>>> b = bytes('abc', 'utf8') # constructor with encoding name
>>> b
b'abc'
>>>
>>> b = bytes([97, 98, 99])  # integer sequence
>>> b
b'abc'
>>>
>>> b = 'abc'.encode() # similar to bytes(str, 'utf8')
>>> b
b'abc'
>>>
>>> s = b.decode() # or str(bytes, 'utf8')
>>> s
'abc'
>>>
```

---

Mixing string types is not possible in Python 3:

```python
>>> # must convert
>>> b'ab'.decode() + 'cd'
'abcd'
>>>
>>> # or encode the other
>>> b'ab' + 'cd'.encode()
b'abcd'
>>>
>>> # which is the same as
>>> b'ab' + bytes('cd', 'ascii')
b'abcd'
>>>
```

---

`bytearray`

To create and modify:

```python
>>> s = 'spam'
>>> c = bytearray(s, 'utf8')
>>> c
bytearray(b'spam')
>>> print(c)
bytearray(b'spam')
>>>
>>> c[3] = 32
>>> print(c)
bytearray(b'spa ')
>>>
>>> c[3] = 90
>>> c
bytearray(b'spaZ')
>>>
>>> c[3] = ord('X')
>>> c
bytearray(b'spaX')
>>>
>>> c[3] = b'Y'[0]
>>> c
bytearray(b'spaY')
>>>
```

`bytearray` provide many methods from `str` and `bytes` types:

```python
>>> c = bytearray('spam', 'utf8')
>>> c
bytearray(b'spam')
>>>
>>> c.append( ord('A') )
>>> c
bytearray(b'spamA')
>>>
>>> c.extend( b'XYZ' )
>>> c
bytearray(b'spamAXYZ')
>>>
>>> c.replace(b'XYZ', b'ZYX')
bytearray(b'spamAZYX')
>>> c
bytearray(b'spamAXYZ')
>>>
>>> c * 2
bytearray(b'spamAXYZspamAXYZ')
>>>
```

---

To sum up:

`str` for textual data.

`bytes` for binary data.

`bytearray` for mutable binary data.

---

Reading and writing text files with the default encoding in Python 3 look the same:

```python
>>> file = open('/tmp/dump', 'w') # w is the same as wt
>>> file.write('acentuação\n')
11
>>> file.close()
>>>
>>> file = open('/tmp/dump') # defaults to reading text, rt
>>> print( file.read() ) # python decodes automatically
acentuação

>>> file.close()
>>>
```

---

To write encoded (bytes) strings, you can encode beforehand or define the encoding in the `open()` call

This:

```python
>>> # Writing the encoded strings (bytes)
>>> data = "acentuação"
>>> data_enc = data.encode("latin-1")
>>> data_enc
b'acentua\xe7\xe3o'
>>>
>>> file = open("/tmp/data", "wb")
>>> file.write(data_enc)
10
>>> file.close()
>>>
>>> # Reading and decoding
>>> file = open("/tmp/data", "rb")
>>> data_enc = file.read()
>>> data = data_enc.decode("latin-1")
>>> data
'acentuação'
>>>
```

Is the same as:

```python
>>> data = "acentuação"
>>> file = open("/tmp/data", "w", encoding="latin-1")
>>> file.write(data) # encoding is performed automatically
10
>>> file.close()
>>>
>>> file = open("/tmp/data", "r", encoding="latin-1")
>>> data = file.read() # decoding is performed automatically
>>> data
'acentuação'
>>>
```

---

Some modules were adjusted to work with `str`, `bytes` and `bytearray` such as: `re`, `xml`, `json`...

```python
>>> import re
>>>
>>> s = "The king is naked!"
>>> bs = b"The king is naked!"
>>>
>>> # Handling str types. The pattern and the text should have the same type.
>>> re.findall("(k[a-z]*)", s)
['king', 'ked']

>>> # The pattern and the text must have the same type
>>> re.findall("(k[a-z]*)", bs)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-50-4a90812ebea1> in <module>
----> 1 re.findall("(k[a-z]*)", bs)

/usr/lib/python3.6/re.py in findall(pattern, string, flags)
    220
    221     Empty matches are included in the result."""
--> 222     return _compile(pattern, flags).findall(string)
    223
    224 def finditer(pattern, string, flags=0):

TypeError: cannot use a string pattern on a bytes-like object

>>> # It works with bytes too
>>> re.findall(b"(k[a-z]*)", bs)
[b'king', b'ked']
>>>
```

The `pickle` module in Python 3 needs a file opened in binary mode to work properly:

```python
>>> import pickle
>>>
>>> f = open('/tmp/dump', 'w') # text mode
>>>
>>> data = "spam!"
>>>
>>> pickle.dump(data, f)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-56-3f22c8cea0f7> in <module>
----> 1 pickle.dump(data, f)

TypeError: write() argument must be str, not bytes
>>>
>>>
>>> # In binary mode
>>> f = open('/tmp/dump', 'wb')
>>> pickle.dump(data, f)
>>> f.close()
>>>
>>> # Reading also requires binary mode
>>> f = open('/tmp/dump', 'r')
>>> pickle.load(f) # ops
---------------------------------------------------------------------------
UnicodeDecodeError                        Traceback (most recent call last)
<ipython-input-64-7a3e7c481918> in <module>
----> 1 pickle.load(f) # ops

/usr/lib/python3.6/codecs.py in decode(self, input, final)
    319         # decode input (taking the buffer into account)
    320         data = self.buffer + input
--> 321         (result, consumed) = self._buffer_decode(data, self.errors, final)
    322         # keep undecoded input until the next call
    323         self.buffer = data[consumed:]

UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
>>>
>>> # Reading also requires binary mode
>>> f = open('/tmp/dump', 'rb')
>>> pickle.load(f) # ops
'spam!'
>>>
```

---

# Managed Attributes

## Properties

- Created using as class attributes assignments to the `property(fget, fset, fdel, doc)` built-in function:

- All `property` arguments are optional and default to `None`, meaning the opeartion is not allowed.
Producing `AttributeError` exceptions when attemped.

- The arguments can be any callable that accept an instance as first argument.

- `fget` is the getter, `fset` is the setter, `fdel` is the deletion handler (should return `None`) and `doc` is optional.
If `doc` is not provided, `fget.__doc__` is used.

- Example:

```python
>>> class Person:
...     def __init__(self, name):
...         self._name = name
...     def get_name(self):
...         print('*fetch*')
...         return self._name
...     def set_name(self, value):
...         print('*change*')
...         self._name = value
...     def del_name(self):
...         print('removing!')
...         del self._name
...     name = property(get_name, set_name, del_name, "name property example")
...
>>>
>>> bob = Person('bob smith')
>>> print( bob.name ) # get
*fetch*
bob smith
>>>
>>> bob.name = "Robert Smith" # set
*change*
>>> print( bob.name ) # get
*fetch*
Robert Smith
>>>
>>> del bob.name # deleting
removing!
>>>
```

- Usually properties are used to compute a value while accessing:

```python
>>> class Square:
...     def __init__(self, width, height):
...         self.width = width
...         self.height = height
...     def get_area(self):
...         return self.width * self.height
...     area = property(get_area)
...
>>> s = Square(10, 20)
>>> s.area
200
>>>
```

- You can code properties using decorators. The previous example using decorators:

```python
>>> class SquaredNumber:
...     def __init__(self, number):
...         self._number = number
...     @property
...     def number(self):
...         return self._number ** 2
...     @number.setter
...     def number(self, value):
...         self._number = value
...     @number.deleter
...     def number(self):
...         print('bye')
...         self.number = 0
...
>>>
>>> s = SquaredNumber(5)
>>> s.number
25
>>> s.number = 10
>>> s.number
100
>>>
>>> del s.number
bye
>>> s.number
0
>>>
```

---

# Descriptors

- Properties are syntax sugar for descriptors, which are classes/objects that implement a protocol to intercept
  the reading, writing and deletion of an attribute.

- Descriptors have their proper state (being objects) and have access to the `instance` state.
  The `instance` is received as an argument of the protocol methods.

- The descriptor protocol has three methods:
    - `__get__(self, instance, owner)`, that returns the attr value;
    - `__set__(self, instance, value)`, that sets the attr value;
    - `__delete__(self, instance)`, that deletes the attr value;

- Descriptors can implement all or none of these. If not implemented, the operation will not be allowed by the interpreter.

- **Caution:** If you dont implement `__set__` the assignment operation will be performed in the origin instance, thus overriding the descriptor.
  To implement a readonly descriptor, you must implement `__get__` and `__set__`.

- All descriptor methods receive the descriptor instance (`self`) and the client-instance which attribute points to a descriptor instance (`instance`).

    - The `__get__` method also receives an `owner` argument, that refers to the class where the descriptor was defined and called.
      Remember that descriptor are class attributes, hence they can be accessed directly from the class (`MyDescriptorClass.descriptor`)
      In this case, the `instance` argument will be empty and only the `owner` will be avaiable, with the class: `MyDescriptorClass`.

- An example:

```python
>>> class Descriptor:
...     def __get__(self, instance, owner):
...         print('Accessing descriptor: self={}, instance={}, owner={}'.format(self, instance, owner))
...         return instance.value ** 2
...
...
>>> class Number:
...     squared = Descriptor()
...     def __init__(self, value):
...         self.value = value
...
>>>
>>> n = Number(10)
>>> n.squared
Accessing descriptor: self=<__main__.Descriptor object at 0x7fadb33cb2e8>, instance=<__main__.Number object at 0x7fadb345ac18>, owner=<class '__main__.Number'>
100
>>>
```

Adding a setter and deleter:

```python
>>> import math
>>>
>>> class Descriptor:
...     def __get__(self, instance, owner):
...         print('Accessing descriptor: self={}, instance={}, owner={}'.format(self, instance, owner))
...         return instance.value ** 2
...     def __set__(self, instance, value):
...         print('Setting descriptor: self={}, instance={}, value={}'.format(self, instance, value))
...         instance.value = math.sqrt(value)
...     def __delete__(self, instance):
...         print('Setting descriptor: self={}, instance={}'.format(self, instance))
...         instance.value = 0
...
>>>
>>> class Number:
...     squared = Descriptor()
...     def __init__(self, value):
...         self.value = value
...
>>>
>>> n = Number(10)
>>> n.value
10
>>> n.squared
Accessing descriptor: self=<__main__.Descriptor object at 0x7fadb259ddd8>, instance=<__main__.Number object at 0x7fadb259dac8>, owner=<class '__main__.Number'>
100
>>>
>>> n.squared = 81
Setting descriptor: self=<__main__.Descriptor object at 0x7fadb259ddd8>, instance=<__main__.Number object at 0x7fadb259dac8>, value=81
>>> n.value
9.0
>>>
>>> del n.squared
Setting descriptor: self=<__main__.Descriptor object at 0x7fadb259ddd8>, instance=<__main__.Number object at 0x7fadb259dac8>
>>> n.value
0
>>>
```

- To create read-only descriptors you should implement the `__set__` method, otherwise the descriptor can be overriden:

```python
>>> class SquaredDescriptor:
...     def __get__(self, instance, owner):
...         return instance.value ** 2
...
>>>
>>> class Number:
...     squared = SquaredDescriptor()
...     def __init__(self, n):
...         self.value = n
...
>>> n = Number(10)
>>> n.squared
100
>>>
>>> # If you dont implement __set__, the descriptor can be overriden in the instance
>>> n.squared = 81
>>> n.value
10
>>> n.squared
81
>>>
```

Implementing `__set__` solves it:

```python
>>> class SquaredDescriptor:
...     def __get__(self, instance, owner):
...         return instance.value ** 2
...     def __set__(self, instance, value):
...         raise AttributeError('Cannot set')
...
>>> class Number:
...     squared = SquaredDescriptor()
...     def __init__(self, n):
...         self.value = n
...
>>>
>>> n = Number(10)
>>> n.squared
100
>>>
>>> n.squared = 81 # cant!
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-50-1d325a88e5e9> in <module>
----> 1 n.squared = 81 # cant!

<ipython-input-46-8117b3f88984> in __set__(self, instance, value)
      3         return instance.value ** 2
      4     def __set__(self, instance, value):
----> 5         raise AttributeError('Cannot set')
      6

AttributeError: Cannot set
>>>
>>> # Change value to get correct squared
>>> n.value = 9
>>> n.squared
81
>>>
```

- **Caution:** descriptor protocol deletion method is named `__delete__`, not `__del__`, which is the default destructor method in Python objects.

- You can implement your own `property` using descriptors:

```python
class p:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, owner):
        print("p.__get__(self={}, instance={}, owner={})".format(self, instance, owner))

        # if called without instance, the descriptor is being called directly
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("no access")
        else:
            return self.fget(instance)  # instance as self

    def __set__(self, instance, value):
        print("p.__set__(self={}, instance={})".format(self, instance))

        if self.fset is None:
            raise AttributeError("no writing access")

        self.fset(instance, value)  # delegates the assignment

    def __delete__(self, instance):
        print("p.__delete__(self={}, instance={})".format(self, instance))

        if self.fdel is None:
            raise AttributeError("no deletion access")

        self.fdel(instance)  # delegates deletion


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("name getter")
        return self._name

    def set_name(self, value):
        print("name setter")
        self._name = value

    def del_name(self):
        print("name deletion")
        self._name = "John Doe"

    name = p(get_name, set_name, del_name)  # could be used as decorator also

if __name__ == "__main__":
    p = Person("Bob Smith")
    print(p.name)

    p.name = "Paul Peterson"
    print(p.name)

    del p.name
    print(p.name)
```

Output:

```bash
p.__get__(self=<__main__.p object at 0x7fa1cf14d9e8>, instance=<__main__.Person object at 0x7fa1cf14da20>, owner=<class '__main__.Person'>)
name getter
Bob Smith
p.__set__(self=<__main__.p object at 0x7fa1cf14d9e8>, instance=<__main__.Person object at 0x7fa1cf14da20>)
name setter
p.__get__(self=<__main__.p object at 0x7fa1cf14d9e8>, instance=<__main__.Person object at 0x7fa1cf14da20>, owner=<class '__main__.Person'>)
name getter
Paul Peterson
p.__delete__(self=<__main__.p object at 0x7fa1cf14d9e8>, instance=<__main__.Person object at 0x7fa1cf14da20>)
name deletion
p.__get__(self=<__main__.p object at 0x7fa1cf14d9e8>, instance=<__main__.Person object at 0x7fa1cf14da20>, owner=<class '__main__.Person'>)
name getter
John Doe
```

---

# `__getattr__` and `__getattribute__`

- `__getattr__(self, attr)` handle *undefined* attributes that are accessed.

- `__getattribute__(self, attr)` is run for **every** attribute access. **Undefined and defined**:

```python
>>> class Demo:
...     def __getattribute__(self, attr):
...         print("__getattribute__({}, {})".format(self, attr))
...
>>> d = Demo()
>>> d.name
__getattribute__(<__main__.Demo object at 0x7ff4996d19e8>, name)
>>>
>>> d.age = 45
>>> d.age
__getattribute__(<__main__.Demo object at 0x7ff4996d19e8>, age)
>>>
```

- The attribute interception protocol can be summarized as:

```
def __getattr__(self, attr):        # Called when __getattribute__ is not defined and an undefined attribute is accesed
def __getattribute__(self, attr):   # Called for all attribute reading access (even undefined) (obj.attr)
def __setattr__(self, attr, value): # Called for every assignment (obj.attr = )
def __delattr__(self, attr):        # Called on deletion (del obj.attr)
```

---

# Avoiding loops when using `__getattribute__` and `__setattr__`

- These methods are called for all attributes readings and assignments.
  If you perform some of these options inside their body, you end up in an infinite loop:

```python
>>> class Tracer:
...     def __init__(self, wrapped):
...         self.wrapped = wrapped
...     def __getattribute__(self, attr):
...         print('trace: .{}'.format(attr))
...         return self.wrapped.attr # loop!
...
...
...
>>> f = 3.14
>>> t = Tracer(f)
>>> t.real
trace: .real
trace: .wrapped
trace: .wrapped
trace: .wrapped
trace: .wrapped
trace: .wrapped
trace: .wrapped
trace: .wrapped
```

- To avoid the loop, route the fetch through a superclass (usually `object`):

```python
>>> class Tracer:
...     def __init__(self, wrapped):
...         self.wrapped = wrapped
...     def __getattribute__(self, attr):
...         print('trace: ', attr)
...         return getattr( object.__getattribute__(self, 'wrapped'), attr )
...
...
>>> f = 3.14
>>> t = Tracer(f)
>>> t.real
trace:  real
3.14
>>>
```

- `__setattr__` is also susceptible to loops, hence assignments inside `__setattr__` blocks should also
  go through a superclass.

    - Loop:

    ```python
    >>> class SetTracer:
    ...     def __init__(self, wrapped):
    ...         self.wrapped = wrapped
    ...     def __setattr__(self, attr, value):
    ...         print('set:', attr, 'value:', value)
    ...         setattr(self, attr, value) # loop!
    ...
    >>>
    >>> class Struct: pass
    >>>
    >>> s = Struct()
    >>> st = SetTracer(s)
    set: wrapped value: <__main__.Struct object at 0x7f7de7df4630>
    set: wrapped value: <__main__.Struct object at 0x7f7de7df4630>
    set: wrapped value: <__main__.Struct object at 0x7f7de7df4630>
    set: wrapped value: <__main__.Struct object at 0x7f7de7df4630>
    set: wrapped value: <__main__.Struct object at 0x7f7de7df4630>
    set: wrapped value: <__main__.Struct object at 0x7f7de7df4630>
    set: wrapped value: <__main__.Struct object at 0x7f7de7df4630>
    ```

    - No-loop

    ```python
    >>> class SetTracer:
    ...     def __init__(self, wrapped):
    ...         self.wrapped = wrapped
    ...     def __setattr__(self, attr, value):
    ...         print('set:', attr, 'value:', value)
    ...         object.__setattr__(self, attr, value)
    ...
    ...
    >>> class Struct: pass
    >>>
    >>> s = Struct()
    >>> ts = SetTracer(s)
    set: wrapped value: <__main__.Struct object at 0x7f7de6682fd0>
    >>>
    >>> ts.answer = 42
    set: answer value: 42
    >>>
    ```

- Coding `managed` attr using these interception methods:

```python
class Person:
    _managed = ("name", "age")

    def __getattribute__(self, attr):
        _managed = object.__getattribute__(self, "_managed")
        if attr in _managed:
            print('get', attr)

        return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value):
        _managed = object.__getattribute__(self, "_managed")
        if attr in _managed:
            print('set', attr, 'value', value)

        object.__setattr__(self, attr, value)

if __name__ == '__main__':
    p = Person()

    p.name = 'John'
    p.age = 42
    p.job = 'devops'

    print(p.name)
    print(p.age)
    print(p.job)
```

output:

```bash
set name value John
set age value 42
get name
John
get age
42
devops
```

---

# Intercepting built-in operations

- Language operations like addition `+`, subtraction `-`, among others, are not passed to `__getattr__` or `__getattribute__` handlers.
  To wrap acess to these methods, the class must reimplement them:

```python
>>> class MyFloat(float):
...     def __getattribute__(self, attr):
...         print('get: ', attr)
...         return object.__getattribute__(self, attr)
...
>>>
>>> m = MyFloat(3.14)
>>> m
3.14
>>>
>>> m.real
get:  real
3.14
>>>
>>> m + 10 # calls __add__, but does not trigger __getattribute__
13.14
>>>
```

- To intercept operator calls, you must reimplement them in the wrapper class:

```python
>>> class WrappedFloat:
...     def __init__(self, f):
...         self.f = f
...
...     def __getattribute__(self, attr):
...         print('get', attr)
...
...         if attr == 'f':
...             return object.__getattribute__(self, 'f')
...
...         return getattr( object.__getattribute__(self, 'f'), attr )
...
...     def __add__(self, other):
...         print('add', other)
...         return self.f + other
...
>>>
>>> w = WrappedFloat(3.14)
>>> w.real
get real
3.14
>>>
>>> w + 10
add 10
get f
13.14
>>>
```

- The printing operation skips `__getattribute__` also:

```python
>>> class WrappedFloat:
...     def __init__(self, f):
...         self.f = f
...
...     def __getattribute__(self, attr):
...         print('get', attr)
...
...         if attr == 'f':
...             return object.__getattribute__(self, 'f')
...
...         return getattr( object.__getattribute__(self, 'f'), attr )
...
...     def __add__(self, other):
...         print('add', other)
...         return self.f + other
...
>>> w = WrappedFloat(3.14)
>>> print(w) # w.__str__ does not trigger getattribute
<__main__.WrappedFloat object at 0x7f7de666bb00>
>>>
```

To intercept, reimplement:

```python
>>> class WrappedFloat:
...     def __init__(self, f):
...         self.f = f
...
...     def __getattribute__(self, attr):
...         print('get', attr)
...
...         if attr == 'f':
...             return object.__getattribute__(self, 'f')
...
...         return getattr( object.__getattribute__(self, 'f'), attr )
...
...     def __add__(self, other):
...         print('add', other)
...         return self.f + other
...
...     def __str__(self):
...         print('printing')
...         return "***{}***".format(self.f)
...
...
>>> w = WrappedFloat(3.14)
>>> print(w)
printing
get f
***3.14***
>>>
```

---

# Decorators

- **Decorators** manage or augment functions or classes

- Decorators are callable that receive other callables and return callables.

- Decorators can be implemented as functions or classes (implementing `__call__()`).

- Decorators can be **applied** to functions and classes statements.
  In practice, they are additional code executed just after the function or class statement block.

- Decorators can return a wrapper object, thus serving as a proxy object, or the original object after augmenting it.

- **Function decorators** are syntatic sugar that runs one function through another after the `def` statement block,
  rebinding the original to the return value.

- Function decorator basic struct:

```python
>>> def meta_function(wrapped_function):
...     def wrapper_function(*args, **kwargs):
...         print('Called!')
...         return wrapped_function(*args, **kwargs) # delegates the call
...     return wrapper_function
...
>>> @meta_function
... def banner(name):
...     print('***', name, '***')
...
>>>
>>> banner('john')
Called!
*** john ***
>>>
```

- The decorator syntax is similar to a rebind just after the `def` or `class` statement:

```python
>>> def meta_function(wrapped_function):
...     def wrapper_function(*args, **kwargs):
...         print('Called!')
...         return wrapped_function(*args, **kwargs) # delegates the call
...     return wrapper_function
...
>>>
>>> def banner(name):
...     print('*' * 50)
...     print(name)
...     print('*' * 50)
...
>>> banner = meta_function(banner) # equivalente to @meta_function decorator
>>> banner('john')
Called!
**************************************************
john
**************************************************
>>>
```

- Function decorators can be implemented as classes too.
  In this case, the `__call__()` method act as the returned callable in function decorators:

```python
>>> class logger:
...     def __init__(self, fx):
...         self.fx = fx
...     def __call__(self, *args, **kwargs):
...         print('calling {}'.format(self.fx))
...         return self.fx(*args, **kwargs)
...
>>>
>>> @logger
... def banner(name):
...     print('***', name, '***')
...
>>>
>>> banner('john')
calling <function banner at 0x7fbb5cb9f510>
*** john ***
>>>
```

- **Caution:** class-based decorators dont work with class methods (oh, the irony) because the automatically passed `self` instance will be
  decorator class instance, not the wrapped class instance:

```python
>>> class logger:
...     def __init__(self, fx):
...         self.fx = fx
...     def __call__(self, *args, **kwargs):
...         print('calling {}'.format(self.fx))
...         return self.fx(*args, **kwargs)
...
>>>
>>> class Example:
...     def __init__(self, number):
...         self.number = number
...
...     @logger
...     def squared(self):
...         return self.number ** 2
...
>>>
>>> e = Example(10)
>>> e.squared()
calling <function Example.squared at 0x7fbb5cf9ad08>
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-14-c3710e24f3d9> in <module>
----> 1 e.squared()

<ipython-input-11-a7b30b19ce72> in __call__(self, *args, **kwargs)
      4     def __call__(self, *args, **kwargs):
      5         print('calling {}'.format(self.fx))
----> 6         return self.fx(*args, **kwargs)
      7

TypeError: squared() missing 1 required positional argument: 'self'
>>>
```

This happens because only one automatic `self` is passed by the Python interpreter.
In the `e.squared()` call the object being called is of the `logger()` type, thus only the `logger` instance as `self` to `logger.__call__` method.
`Example` instance is not passed.

To create decorators appliable to functions and class methods, create `function decorators`:

```python
>>> def logger(f):
...     def f_with_log(*args, **kwargs):
...         print('{}({}, {})'.format(f, args, kwargs))
...         return f(*args, **kwargs)
...     return f_with_log
...
>>>
>>> class Example:
...     def __init__(self, number):
...         self.number = number
...
...     @logger
...     def squared(self):
...         return self.number ** 2
...
>>>
>>> e = Example(10)
>>> e.squared()
<function Example.squared at 0x7fbb5cbb7840>((<__main__.Example object at 0x7fbb57e5fe10>,), {})
100
>>>
>>> # works with functions too
>>> @logger
... def banner(name):
...     print('*' * 50)
...     print(name)
...     print('*' * 50)
...
>>>
>>> banner('john')
<function banner at 0x7fbb57e062f0>(('john',), {})
**************************************************
john
**************************************************
>>>
```

- **Class decorators** work very similar to function decorators, they are declared just before the class statement and return a callable:

```python
>>> def wrap(cls):
...     class Wrapper:
...         def __init__(self, *args, **kwargs):
...             self.wrapped = cls(*args, **kwargs)
...         def __getattr__(self, attr):
...             print('get:', attr)
...             return getattr(self.wrapped, attr)
...     return Wrapper
...
>>>
>>> @wrap
... class Person:
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
...
>>>
>>> p = Person("john", 42)
>>> p.name
get: name
'john'
>>> p.age
get: age
42
>>>
```

- Class decorators are singletons, so be careful. There is only one namespace. You can end up overriding it in subsequent `__call__` executions:

```python
>>> class decorator:
...     #
...     # @decorator
...     # class Example:
...     # ...
...     # is the same as:
...     # Example = decorator(Example) # calls decorator.__init__ method and returns a decorator instance
...     #
...     def __init__(self, cls):
...         self.cls = cls
...
...     #
...     # Example is now a decorator instance.
...     # When you try to instatiate a new Example instance, through Example(...) call,
...     # you are really calling the __call__ method below, that creates an instance and returns it.
...     #
...     # CAUTION: Every time a new instance is created, the Example.wrapped  is overwritten.
...     # Remember that Example is now a "decorator" instance.
...     #
...     def __call__(self, *args, **kwargs):
...         self.wrapped = self.cls(*args, **kwargs)
...         return self
...
...     #
...     # Intercepts attributes access in Decorator and delegates to the self.wrapped
...     #
...     def __getattr__(self, attr):
...         print('get', attr)
...         return getattr(self.wrapped, attr)
...
>>>
>>> @decorator
... class Struct:
...     def __init__(self, value):
...         self.value = value
...
>>>
>>> s1 = Struct(10)
>>> s1.value
get value
10
>>>
>>> isinstance(Struct, decorator) # Struct is an instance of decorator
True
>>>
>>> s2 = Struct(99) # will replace the decorator wrapped attribute
>>> s2.value
get value
99
>>>
>>> s1.value # was overwritten
get value
99
>>>
```

- Decorators can be nested:

```python
@A
@B
@C
def example(...): pass
```

Is the same as:

```python
def example(...): pass
example = A(B(C(example)))
```

This is also true for class decorators:

```python
@spam
@eggs
@bacon
class Pizza: pass
```

Is the same as:

```python
class Pizza: pass
Pizza = spam(eggs(bacon(Pizza)))
```

**The closest decorator is always executed first, up to the top.**

- An example of nesting:

```python
>>> def arity(f):
...     def wrapper(*args, **kwargs):
...         print("arity", len(args) + len(kwargs))
...         return f(*args, **kwargs)
...     return wrapper
...
>>>
>>> def trace(f):
...     def wrapper(*args, **kwargs):
...         print('trace: ({}, {})'.format(args, kwargs))
...         return f(*args, **kwargs)
...     return wrapper
...
>>>
>>> @arity
... @trace
... def sum(a, b): return a + b
>>>
>>> sum(10, 20)
arity 2
trace: ((10, 20), {})
30
>>>
```

- You can pass arguments to decoratos, provided that you create first a "decorator factory".
  A function or class that receives these arguments and returns a callable, which is then used to decorate the
  class or function:

```python
>>> def debug_factory(arity=False, trace=False):
...     # Creates and returns a custom decorator, based on the received arguments
...     def decorator(f):
...         def wrapper(*args, **kwargs):
...             if arity:
...                 print('arity:', len(args) + len(kwargs))
...             if trace:
...                 print('trace:', args, kwargs)
...             return f(*args, **kwargs)
...         return wrapper
...
...     return decorator
...
>>>
>>> @debug_factory(arity=True, trace=True)
... def sum(a, b): return a + b
>>>
>>> sum(10, 20)
arity: 2
trace: (10, 20) {}
30
>>>
```

- Remember that class decorators cant be used to decorate other class methods ? Because when called, Python passes only one `self` argument ?
  Which is the decorator instance. To circumvent it, you can leverage the descriptor protocol:

```python
class count_calls:
    # Creates a decorator instance and saves the wrapped function as an instance attribute
    def __init__(self, f):
        self.f = f
        self.calls = 0

    # the init returns an instance, that responds as a function. this syntax is handled by this method.
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("{} called {} times".format(self.f, self.calls))
        return self.f(*args, **kwargs)

    # to allow the decorator to be applied to class methods, we leverage the descriptor protocol, that receives
    # the instance and its class as arguments when accessed.
    # then, we create another callable instance (wrapper) concatenating the decorator instance (self) and the object instance (instance).
    # this callable calls the descriptor passing the object instance as the first positional arg.
    # in face, two selfes are passed to the descriptor. the descriptors's self and the object instance as the first positional arg.
    def __get__(self, instance, owner):
        class wrapper:
            def __init__(self, descriptor, subject):
                self.descriptor = descriptor
                self.subject = subject

            def __call__(self, *args, **kwargs):
                return self.descriptor(self.subject, *args, **kwargs)

        return wrapper(self, instance)

if __name__ == '__main__':
    @count_calls
    def first_test(): pass

    class Test:
        @count_calls
        def second_test(self):
            pass

        @count_calls
        def third_test(self):
            pass

    first_test()

    t = Test()
    t.second_test()
    t.third_test()

    first_test()

    t.second_test()
    t.second_test()

    t.third_test()
    t.third_test()
    t.third_test()
```

output:

```bash
<function first_test at 0x7fb741658488> called 1 times
<function Test.second_test at 0x7fb74166a8c8> called 1 times
<function Test.third_test at 0x7fb74166a950> called 1 times
<function first_test at 0x7fb741658488> called 2 times
<function Test.second_test at 0x7fb74166a8c8> called 2 times
<function Test.second_test at 0x7fb74166a8c8> called 3 times
<function Test.third_test at 0x7fb74166a950> called 2 times
<function Test.third_test at 0x7fb74166a950> called 3 times
<function Test.third_test at 0x7fb74166a950> called 4 times
```

- The `wrapper` class in the last example can be replaced with a function:

```python
class count_calls:
    # Creates a decorator instance and saves the wrapped function as an instance attribute
    def __init__(self, f):
        self.f = f
        self.calls = 0

    # the init returns an instance, that responds as a function. this syntax is handled by this method.
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("{} called {} times".format(self.f, self.calls))
        return self.f(*args, **kwargs)

    # to allow the decorator to be applied to class methods, we leverage the descriptor protocol, that receives
    # the instance and its class as arguments when accessed.
    # then, we create another callable instance (wrapper) concatenating the decorator instance (self) and the object instance (instance).
    # this callable calls the descriptor passing the object instance as the first positional arg.
    # in face, two selfes are passed to the descriptor. the descriptors's self and the object instance as the first positional arg.
    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)

        return wrapper

if __name__ == '__main__':
    @count_calls
    def first_test(): pass

    class Test:
        @count_calls
        def second_test(self):
            pass

        @count_calls
        def third_test(self):
            pass

    first_test()

    t = Test()
    t.second_test()
    t.third_test()

    first_test()

    t.second_test()
    t.second_test()

    t.third_test()
    t.third_test()
    t.third_test()
```

same output:

```bash
<function first_test at 0x7f7e09241d08> called 1 times
<function Test.second_test at 0x7f7e092718c8> called 1 times
<function Test.third_test at 0x7f7e09271950> called 1 times
<function first_test at 0x7f7e09241d08> called 2 times
<function Test.second_test at 0x7f7e092718c8> called 2 times
<function Test.second_test at 0x7f7e092718c8> called 3 times
<function Test.third_test at 0x7f7e09271950> called 2 times
<function Test.third_test at 0x7f7e09271950> called 3 times
<function Test.third_test at 0x7f7e09271950> called 4 times
```

- Usefull class decorator: `singleton`

```python
>>> def singleton(klass):
...     instance = None
...     def wrapper(*args, **kwargs):
...         nonlocal instance
...         if instance is None:
...             instance = klass(*args, **kwargs)
...         return instance
...     return wrapper
...
>>>
>>> @singleton
... class Example: pass
>>>
>>> e1 = Example()
>>> e1
<__main__.Example at 0x7fbb57b30898>
>>>
>>> e2 = Example()
>>> e2
<__main__.Example at 0x7fbb57b30898>
>>>
>>> id(e1), id(e2)
(140442606962840, 140442606962840)
>>>
>>> @singleton
... class AnotherExample: pass
>>>
>>> a1 = AnotherExample()
>>> a1
<__main__.AnotherExample at 0x7fbb57d69b00>
>>>
>>> a2 = AnotherExample()
>>> a2
<__main__.AnotherExample at 0x7fbb57d69b00>
>>>
>>> @singleton
... class Person:
...     def __init__(self, name):
...         self.name = name
...
>>>
>>> p1 = Person("john")
>>> p1.name
'john'
>>>
>>> p2 = Person("paul")
>>> p2.name
'john'
>>>
```

- The singleton decorator can be implemented as a class too:

```python
>>> class singleton:
...     def __init__(self, klass):
...         self.klass = klass
...         self.instance = None
...
...     def __call__(self, *args, **kwargs):
...         if self.instance is None:
...             self.instance = self.klass(*args, **kwargs)
...         return self.instance
...
>>>
>>> @singleton
... class Test: pass
>>>
>>> t1 = Test()
>>> t2 = Test()
>>>
>>> id(t1), id(t2)
(140442608276704, 140442608276704)
>>>
```

- Creating a `trace` decorator using classes:

```python
>>> class trace:
...     def __init__(self, klass):
...         self.klass = klass
...     def __call__(self, *args, **kwargs):
...         class wrapper:
...             def __init__(self, delegate):
...                 self.delegate = delegate
...             def __getattr__(self, attr):
...                 print('trace:', attr)
...                 return getattr(self.delegate, attr)
...
...         return wrapper( self.klass(*args, **kwargs) )
...
>>>
>>> @trace
... class Person:
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
...
>>>
>>> p1 = Person("john", 42)
>>> p1.name
trace: name
'john'
>>> p1.age
trace: age
42
>>> @trace
... class Math:
...     def __init__(self, a, b):
...         self.a = a
...         self.b = b
...     def add(self):
...         return self.a + self.b
...
>>>
>>> m = Math(10, 2)
>>> m.add()
trace: add
12
>>>
```

- The following example creates a class decorator to implement `private`-like access for class attributes.
  They can be accessed only from inside the class.

```python
def private(*attributes):
    def decorator(klass):
        class wrapper:
            def __init__(self, *args, **kwargs):
                self.klass = klass
                self.instance = self.klass(*args, **kwargs)

            def __getattr__(self, attr):
                if attr in attributes:
                    raise AttributeError("private attribute")

                return getattr(self.instance, attr)

            def __setattr__(self, attr, value):
                if attr in attributes:
                    raise AttributeError("private")

                if attr in ("klass", "instance"):
                    return object.__setattr__(self, attr, value)

                setattr(self.instance, attr, value)

        return wrapper

    return decorator


@private("name", "age")
class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job


if __name__ == "__main__":
    p = Person("john", 42, "manager")

    print(p.job)

    # raise exception, is private
    try:
        print(p.name)  # ops!
    except AttributeError as e:
        print(e)

    p.job = "dev"  # ok! public attr
    print(p.job)

    # raises exp! its private
    try:
        p.name = "paul"
    except AttributeError as e:
        print(e)

```

- Decorators can be used to test arguments validity too:

```python
def range_check(**checks):
    for check in checks:
        assert len(checks[check]) == 2, "{}={} argument is invalid"

    def decorator(f):
        def wrapper(*args, **kwargs):
            if "all" in checks:
                for arg in args:
                    assert (
                        checks["all"][0] <= arg <= checks["all"][1]
                    ), "{} is bigger than 'all' constraint: ({}, {})".format(
                        arg, checks["all"][0], checks["all"][1]
                    )

            for check in checks:
                if check in kwargs:
                    assert (
                        checks[check][0] <= kwargs[check] <= checks[check][1]
                    ), "{} argument is bigger thant ({}, {})".format(
                        kwargs[check], checks[check][0], checks[check][1]
                    )

            return f(*args, **kwargs)
        return wrapper
    return decorator

if __name__ == "__main__":
    @range_check(all=(0.0, 1.0))
    def sum(a, b):
        return a + b

    print( sum(0.1, 0.1) )

    try:
        print( sum(1, 3) )
    except AssertionError as e:
        print(e)

    @range_check(percent=(0, 100))
    def give_raise(salary=0, percent=0):
        return salary * (1 + (percent/100))

    print( give_raise(salary=1000, percent=25) )

    try:
        print( give_raise(salary=1000, percent=200) )
    except AssertionError as e:
        print(e)
```

Output:

```bash
0.2
3 is bigger than 'all' constraint: (0.0, 1.0)
1250.0
200 argument is bigger thant (0, 100)
```

---

# Function annotations

- The previous range test example can be implement using function annotations, which include expressions
  to the funcion signature header and associate them to the parameters and the function return value.
  This association is saved as a function attribute named `__annotations__`:

```python
>>> def sum(a: (0.0, 1.0), b: (0.0, 1.0)) -> (0.0, 2.0):
...     return a + b
...
>>> sum.__annotations__
{'a': (0.0, 1.0), 'b': (0.0, 1.0), 'return': (0.0, 2.0)}
>>>
```

- The previous, range checking, decorator can leverage these annotations:

```python
def range_check(f):
    checks = f.__annotations__

    for check in checks:
        assert check != "return" and len(checks[check]) == 2, "{}={} check is invalid"

    def wrapper(*args, **kwargs):

        # checking args
        argnames = f.__code__.co_varnames
        checks_list = list(checks.values())

        for index, arg in enumerate(args):
            assert (
                checks_list[index][0] <= args[index] <= checks_list[index][1]
            ), "{}={} argument is invalid ({}, {})".format(
                argnames[index],
                args[index],
                checks_list[index][0],
                checks_list[index][1]
            )

        # checking kwargs
        for check in checks:
            if check in kwargs:
                assert (
                    checks[check][0] <= kwargs[check] <= checks[check][1]
                ), "{}={} argument is invalid ({}, {})".format(
                    check,
                    kwargs[check],
                    checks[check][0],
                    checks[check][1]
                )

        return f(*args, **kwargs)

    return wrapper


if __name__ == "__main__":

    @range_check
    def sum(a: (0.0, 1.0), b: (0.0, 1.0)):
        return a + b

    print(sum(0.1, 0.1))

    try:
        print(sum(1, 3))
    except AssertionError as e:
        print(e)

    @range_check
    def give_raise(salary:(0, 10_000)=0 , percent:(1, 100)=0):
        return salary * (1 + (percent / 100))

    print(give_raise(salary=1000, percent=25))

    try:
        print(give_raise(salary=1000, percent=200))
    except AssertionError as e:
        print(e)

```

- The previous examples can be modified to check for argument class types too:

```python
def type_check(f):
    annotations = f.__annotations__

    def wrapper(*args, **kwargs):

        # check args
        args_names = f.__code__.co_varnames
        for index, arg in enumerate(args):
            arg_name = args_names[index]
            annotation = annotations[arg_name]

            assert isinstance(arg, annotation), "{} ({}) has not the expected type {}".format(arg_name, type(arg), annotation)

        # check kwargs
        for kwarg in kwargs:
            arg_name = kwarg
            arg = kwargs[kwarg]
            annotation = annotations[kwarg]
            assert isinstance(arg, annotation), "{} ({}) has not the expected type {}".format(arg_name, type(arg), annotation)

        return f(*args, **kwargs)

    return wrapper


if __name__ == "__main__":
    @type_check
    def sum(a: int, b: int):
        return a + b

    print( sum(2, 2) )

    try:
        print( sum(2, 3.0) )
    except AssertionError as e:
        print(e)

    @type_check
    def sub(a:float=0.0, b:float=0.0):
        return a - b

    print( sub(3.0, 1.0) )

    try:
        print( sub(3.0, 1) )
    except AssertionError as e:
        print(e)
```

---

# Metaclasses

- Metaclasses allow the programmer define code to be automatically run after a class creation.
  Differently from decorators, there is no rebound. The metaclass does not need to return another object.

- Metaclasses and decorators share many similarities. There is a time difference: metaclasses are run during
  class creation, while decorators are run after the class is already created and perform name rebinding.

- A simple example of a metaclass that augments the class `__str__` method:

```python
class BetterStr(type):
    def better_str(self):
        attrs = [attr for attr in dir(self) if not attr.startswith("_")]
        return "{}: {}".format(self.__class__, attrs)

    def __init__(klass, klass_name, superclasses, klass_dict):
        print(
            "klass={}, klass_name={}, superclasses={}, klass_dict={}".format(
                klass, klass_name, superclasses, klass_dict
            )
        )

        klass.__str__ = BetterStr.better_str

class Person(metaclass=BetterStr):
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    p = Person("john", 42)
    print(p)
```

output:

```bash
klass=<class '__main__.Person'>, klass_name=Person, superclasses=(), klass_dict={'__module__': '__main__', '__qualname__': 'Person', '__init__': <function Person.__init__ at 0x7fc9d4d1e620>}
<class '__main__.Person'>: ['age', 'name']
```

- Metaclasses should inherit from `type`. Their __init__ method does not receive a `self` instance, but a `klass` instance
  and its data as parameters.

- In Python 3, classes are objects of the type `type`:

```python
>>> class E: pass
>>> type( E )
type
>>> E.__class__
type
>>> E
__main__.E
>>>
```

This is True for the built-in classes too:

```python
>>> type( list )
type
>>> type( tuple )
type
>>> type( float )
type
>>> type( int )
type
>>>
```

- To understand metaclasses you need to grasp the following concepts:

    - Classes are instances of the `type` class.
      Classes statements are, in fact, a syntatic sugar for `type()` instantiation.

    - Metaclasses are subclasses of `type` (they must be!) that overwrite the `__init__` or other methods.

    - When we specify `metaclass=CustomMetaClass` we are indicating that the class should be created instantiating `CustomMetaClass`,
      instead of `type`.

- The class creation protocol:

1. Execute the class statement block code, creating a namespace dictionary (`attribute_dict`).

2. After the block execution and namespace creation, call the `type` (default metaclass) `__call__` method:

```python
type(classname, superclasses, attribute_dict)
```

3. The `type` `__call__` method makes two calls. One to the `__new__` method, that creates and returns the class object,
   and `__init__` that initialize this class object:

```python
type.__new__(typeclass, classname, superclasses, attributedict)
type.__init__(class, classname, superclasses, attributedict)
```

Example: given the following class:

```python
class Eggs: ...

class Spam(Eggs):
    data = 1
    def meth(self, arg):
        return self.data + arg
```

Python will internally execute:

```python
Spam = type(classname="Spam", superclasses=("Eggs",), attribute_dict={"data": 1})
```

In fact, you can create a class calling type directly:

```python
>>> class Super:
...     a = 1
...     def out(self):
...         print(self.a)
...
>>>
>>> Sub = type("Sub", (Super,), {"b": 2})
>>> Sub
__main__.Sub
>>>
>>> s = Sub()
>>> s.out()
1
>>>
>>> s.b
2
>>>
```

- Metaclasses are just subclasses of `type` and to use them in your user classes you
  simple a `metaclass` keyword argument to the class header statement:

```python
>>> class Meta(type):
...     # def __new__ ...
...     def __init__(self, *args, **kwargs):
...         print(args, kwargs)
...         type.__init__(self, *args, **kwargs)
...
>>>
>>> class Spam(metaclass=Meta): pass
('Spam', (), {'__module__': '__main__', '__qualname__': 'Spam'}) {}
>>>
```

- The `metaclass` keyword argument should be the last in the class statement declaration.

- One of the simplest metaclasses you can create is one that simple intercepts and delegates the object creation to the default:

```python
class LogMeta(type):
    def __new__(meta, classname, supers, classdict):
        print("meta={}, classname={}, supers={}, classdict={}".format(meta, classname, supers, classdict))
        return type.__new__(meta, classname, supers, classdict)

class Person(metaclass=LogMeta):
    banner_top = "***" + "\n"
    banner_bottom = "***"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        response = ""
        response += self.banner_top
        response += "{} - {}\n".format(self.name, self.age)
        response += self.banner_bottom
        return response

if __name__ == "__main__":
    p = Person("john", 42)
    print( p )
```

output:

```bash
meta=<class '__main__.LogMeta'>, classname=Person, supers=(), classdict={'__module__': '__main__', '__qualname__': 'Person', 'banner_top': '***\n', 'banner_bottom': '***', '__init__': <function Person.__init__ at 0x7ffb7c33c620>, '__str__': <function Person.__str__ at 0x7ffb7c33c6a8>}
***
john - 42
***
```

- The metaclass protocol really is a call to the `type.__call__` which calls `__new__` and `__init__` implementations.
  Thus, it can be implemented as a simple function:

```python
>>> def meta(classname, supers, classdict):
...     print('***', classname, supers, classdict, '***')
...     return type(classname, supers, classdict) # type.__call__
...
>>>
>>> class Person(metaclass=meta):
...     job = 'dev'
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
...
*** Person () {'__module__': '__main__', '__qualname__': 'Person', 'job': 'dev', '__init__': <function Person.__init__ at 0x7f14c494d510>} ***
>>>
```

- Classes (but not their instances) have access to metaclass attributes:

```python
>>> class Meta(type):
...     attr = 42
...
>>>
>>> class Example(metaclass=Meta): pass
>>>
>>> Example.attr # class has access to metaclass
42
>>>
>>> # But, instance does not
>>> e = Example()
>>> e.attr
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-6-cf12a7ae060f> in <module>
----> 1 e.attr

AttributeError: 'Example' object has no attribute 'attr'
>>>
```

This attribute can be a `classmethod`, `staticmethod`.

- Metaclass are propagated in inheritance:

```python
class Meta(type):
    def __new__(meta, classname, supers, classdict):
        print(meta, classname, supers, classdict)
        return type.__new__(meta, classname, supers, classdict)

class Super(metaclass=Meta): pass

class Sub(Super): pass

if __name__ == "__main__":
    s = Sub()
```

Output:

```python
class Meta(type):
    def __new__(meta, classname, supers, classdict):
        print(meta, classname, supers, classdict)
        return type.__new__(meta, classname, supers, classdict)

class Super(metaclass=Meta): pass

class Sub(Super): pass

if __name__ == "__main__":
    s = Sub()
```

Note that both class instances are created and passed to the same metaclass:

```bash
<class '__main__.Meta'> Super () {'__module__': '__main__', '__qualname__': 'Super'}
<class '__main__.Meta'> Sub (<class '__main__.Super'>,) {'__module__': '__main__', '__qualname__': 'Sub'}
```

- Thus, subclasses also have access to metaclass attributes:

```python
class Meta(type):
    def __new__(meta, classname, supers, classdict):
        print(meta, classname, supers, classdict)
        return type.__new__(meta, classname, supers, classdict)

    @classmethod
    def toast(klass):
        print(klass, 'toast')

class Super(metaclass=Meta): pass

class Sub(Super): pass

if __name__ == "__main__":
    s = Sub()
    Sub.toast()
```

- Metaclass methods accessed through one of its classes are bound to the class:

```python
>>> class Meta(type):
...     def __new__(meta, classname, supers, classdict):
...         print(meta, classname, supers, classdict)
...         return type.__new__(meta, classname, supers, classdict)
...
...     @classmethod
...     def toast(klass):
...         print(klass, 'toast')
...
... class Super(metaclass=Meta): pass
...
... class Sub(Super): pass
<class '__main__.Meta'> Super () {'__module__': '__main__', '__qualname__': 'Super'}
<class '__main__.Meta'> Sub (<class '__main__.Super'>,) {'__module__': '__main__', '__qualname__': 'Sub'}
>>>
>>> Sub.toast
<bound method Meta.toast of <class '__main__.Meta'>>
>>>
```

- While **class** methods when accessed through the class are unbound:

```python
>>> class Meta(type):
...     def __new__(meta, classname, supers, classdict):
...         print(meta, classname, supers, classdict)
...         return type.__new__(meta, classname, supers, classdict)
...
...     @classmethod
...     def toast(klass):
...         print(klass, 'toast')
...
... class Super(metaclass=Meta): pass
...
... class Sub(Super):
...     def spam(self):
...         print('spam')
...
<class '__main__.Meta'> Super () {'__module__': '__main__', '__qualname__': 'Super'}
<class '__main__.Meta'> Sub (<class '__main__.Super'>,) {'__module__': '__main__', '__qualname__': 'Sub', 'spam': <function Sub.spam at 0x7f484bfa7b70>}
>>>
>>> Sub.spam # unbound
<function __main__.Sub.spam(self)>
>>>
```

- But class methods referenced from an instance are **bound** to the instance:

```python
>>> class Meta(type):
...     def __new__(meta, classname, supers, classdict):
...         print(meta, classname, supers, classdict)
...         return type.__new__(meta, classname, supers, classdict)
...
...     @classmethod
...     def toast(klass):
...         print(klass, 'toast')
...
... class Super(metaclass=Meta): pass
...
... class Sub(Super):
...     def spam(self):
...         print('spam')
...
<class '__main__.Meta'> Super () {'__module__': '__main__', '__qualname__': 'Super'}
<class '__main__.Meta'> Sub (<class '__main__.Super'>,) {'__module__': '__main__', '__qualname__': 'Sub', 'spam': <function Sub.spam at 0x7f484bde41e0>}
>>>
>>> s = Sub()
>>> s.spam # bound to s
<bound method Sub.spam of <__main__.Sub object at 0x7f484bde86a0>>
>>>
```

- Remember: a metaclass is a class that produces classes. Thus, their methods receive the "class instance" as the first argument `self`:

```python
>>> class Meta(type):
...     def add(self, a, b):
...         print('self={}'.format(self))
...         return a + b
...
>>> class Example(metaclass=Meta): pass
>>>
>>> Example.add(5, 3)
self=<class '__main__.Example'>
8
>>>
```

- Remember2: All metaclasses should inherit from `type`.

- Metaclass methods have access only to the class data (they have no access to this class instances and are not accessible from them).
  Hence, don't need the application of a `@classmethod` decorator.

- Therefore, you should write metaclass methods with a `cls` or `klass` as first argument, instead of `self`:

```python
>>> class Meta(type):
...     def add(cls, a, b):
...         print('cls={}'.format(cls))
...         return a + b
...
...
>>> class Example(metaclass=Meta): pass
>>>
>>> Example.add(5, 3)
cls=<class '__main__.Example'>
8
>>>
```

- You can define operator-methods in metaclasses, making the operations supported by the classes that are based in
  this metaclass:

```python
>>> class Meta(type):
...     def __add__(cls, other):
...         print('cls={}, other={}'.format(cls, other))
...         return cls.value + other.value
...
...
...
>>> class A(metaclass=Meta):
...     value = 10
...
>>> class B(metaclass=Meta):
...     value = 50
...
>>>
>>> A + B
cls=<class '__main__.A'>, other=<class '__main__.B'>
60
>>>
```

Mind that the classes instance have no access to these implementations:

```python
>>> a = A()
>>> b = B()
>>>
>>> a + b
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-bd58363a63fc> in <module>
----> 1 a + b

TypeError: unsupported operand type(s) for +: 'A' and 'B'
>>>
```

- You can use metaclasses to augment the future-created-classes with new methods or attributes:

```python
>>> class Meta(type):
...     def __new__(meta, classname, supers, classdict):
...         print("meta={}, classname={}, supers={}, classdict={}".format(meta, classname, supers, classdict))
...         classdict["add"] = lambda self, a, b: a + b
...         return type.__new__(meta, classname, supers, classdict)
...
>>>
>>> class Example(metaclass=Meta): pass
meta=<class '__main__.Meta'>, classname=Example, supers=(), classdict={'__module__': '__main__', '__qualname__': 'Example'}
>>>
>>> e1 = Example()
>>> e1.add(10, 20)
30
>>>
```

- Adding a new attribute:

```python
>>> class PrefixMeta(type):
...     def __new__(meta, classname, supers, classdict):
...         classdict["prefix"] = "__"
...         return type.__new__(meta, classname, supers, classdict)
...
>>>
>>> class Example(metaclass=PrefixMeta): pass
>>>
>>> e = Example()
>>> e.prefix
'__'
>>>
>>> Example.prefix
'__'
>>>
```

- Decorators are best suited to handle 'instances', while metaclasses are better suited for class creations.
  A Tracer example:

As a decorator:

```python
>>> def trace(klass):
...     class Wrapper:
...         def __init__(self, *args, **kwargs):
...             self.wrapped = klass(*args, **kwargs)
...
...         def __getattr__(self, attr):
...             print("get: ", attr)
...             return getattr(self.wrapped, attr)
...
...     return Wrapper
...
>>>
>>> @trace
... class Person:
...     def __init__(self, name):
...         self.name = name
...
>>>
>>> p = Person("john")
>>> p.name
get:  name
'john'
>>>
```

As a metaclass:

```python
class Tracer(type):
    def __new__(cls, name, bases, namespace):
        class Wrapper:
            def __init__(self, *args, **kwargs):
                self.wrapped = type(name, bases, namespace)(*args, **kwargs)

            def __getattr__(self, attr):
                print("get:", attr)
                return getattr(self.wrapped, attr)

        return Wrapper


class Person(metaclass=Tracer):
    def __init__(self, name):
        self.name = name


class Job(metaclass=Tracer):
    def __init__(self, description):
        self.description = description


if __name__ == "__main__":
    p = Person("john")
    print(p.name)

    p2 = Person("paul")
    print(p2.name)

    j1 = Job("dev")
    print(j1.description)

    j2 = Job("mgr")
    print(j2.description)
```

output:

```bash
get: name
john
get: name
paul
get: description
dev
get: description
mgrget: name
john
get: name
paul
get: description
dev
get: description
mgr
```

- One last metaclass usage example: decorate all methods of a class automatically:

```python
import types


def counter_decorator(func):
    ncalls = 0

    def wrapper_func(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1

        print("{} called {} times".format(func.__name__, ncalls))

        return func(*args, **kwargs)

    return wrapper_func

class CounterMeta(type):
    def __init__(klass, klass_name, klass_bases, klass_namespace):
        for key in klass_namespace:
            if isinstance(klass_namespace[key], types.FunctionType):
                setattr(klass, key, counter_decorator(klass_namespace[key]))

class Person(metaclass=CounterMeta):
    def __init__(self, name):
        self.name = name

    def banner(self):
        print('*' * 10)
        print(self.name)
        print('*' * 10)

if __name__ == "__main__":
    p1 = Person("John")
    p2 = Person("Paul")

    p1.banner()
    p1.banner()

    p2.banner()
```

output:

```bash
__init__ called 1 times
__init__ called 2 times
banner called 1 times
**********
John
**********
banner called 2 times
**********
John
**********
banner called 3 times
**********
Paul
**********
```