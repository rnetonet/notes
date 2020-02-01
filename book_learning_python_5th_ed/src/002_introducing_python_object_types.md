* Modules, classes and functions are objects too. Thus, can be passed as any other object in code.

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

## Unicode Strings

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


## Lists

