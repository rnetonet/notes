# Learning Python, 5th Edition

## How Python Runs Programs

* All Python files, modules, are compiled to bytecode.

* Imported modules bytecodes are cached in disk for optimization.

* Python compiles each module once per execution. An explicit reload should be requested if necessary.

* Bytecode files are regenerated if original source changes (compares timestamps) or its imported by a different interpreter.

* Everything in Python happens in runtime: classes, functions creation, modules linkage.
Everything happens in runtime, while the interpreter reads the code.

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

If you call it using the `py` utility, `python3` will be used.

* You can define the version as an argument for `py`:

```bash
py -3.1 script.py
```

```bash
py -3 script.py
```

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

* You can `exec()` some module, as you just typed its concent, using `exec()`:

```python
exec(open('script1.py').read())
```

* Every time you call `exec()` it executes the code as you had just typed it where you called. It is not like an import.

*