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

## Numbers

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

## Dictionaries

