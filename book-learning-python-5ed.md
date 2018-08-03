
# Modules

* Every `.py` file is a module.

* Each module constitutes a namespace. You can access attributes from other modules, namespaces, by **importing**.

* Two ways to import: `import module_name` or `from module import attribute`

* Module imports are cached per process. After the first import, the cache is used.

* If you need to reload an already imported module, explicitlly do it: `imp.reload(modulename)`

* The module code is fully executed when imported. 
This happens when you do `import ...` or `from ... import ...`.

* **Caution:** `from module import a, b, c` will insert `a, b, c` into the importer namespace (*creating a copy*), overwriting if already defined.

---
* **Tip:** You can open an interpreter after the script execution (even if it fails) using the `python -i module.py` option. The interpreter will have access to the attributes defined in *module.py*.
---

# Types and Operations

## Introducing Python Object Types

* Everything is an object. 

* Objects = data + associated operations.

* Python Hierarchy:

`Programs -> Modules -> Statements -> Expressions (objects)`

* Python core types and literals (special syntax for creation):

|Type            |Literal                                          |
|----------------|-------------------------------------------------|
|Booleans        |`True, False`                                    |
|Numbers         |`2, 3.14, Decimal(), Fraction()`                 |
|Strings         |`'spam', "Bob´s"`                                |
|Lists           |`[1, 'two', 3], list(), []`                      |
|Dictionaries    |`{'age': 15, 'name': 'John'}, dict(hours=2)`     |
|Tuples          |`(1, 'spam', 4), tuple('spam'), namedtuple`      |
|Sets            |`{1, 2, 3}, set('abc')`                          |
|Others          |`Modules, Functions, Classes`                    |

---
* **Note:** Modules, Functions and Classes are objects also!
---

* Python is **dynamically typed**: the interpreter keeps tabs on the types of the objects, no need to declare.

* Python is also **strongly typed**: you can only perform operations on an object that are valid for its type.

---
* **Note:** `repr(object)` outputs the precise representation of the object. `print(object)` outputs the friendly version.
---

## Numbers

* Python supports integers, floats, complex numbers and sets:

```python
>>> # Integer
... 2 + 2
4
>>> 
>>> # Float, has a decimal part
... 2.2 - 0.5
1.7000000000000002
>>> 
>>> # Basic opperations with integers
... 2 + 2
4
>>> 3 - 1
2
>>> 4 * 9
36
>>> 10/5
2.0
>>> 2 ** 3
8
>>> # Float operations
... 5.4 - 3.2
2.2
>>> 
>>> 5.5 + 1.2
6.7
>>> 
>>> 6.7 * 2 # You can use floats with integers
13.4
>>> 
```