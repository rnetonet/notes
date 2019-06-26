# Python in a Nutshell, 3rd Edition

## The Python Interpreter

- You run Python programs throught the `python` interpreter.
    - In Windows, we have the `py` launcher

- The intepreter respects some environment variables:
    - `PYTHONHOME` - Python installation directory. A `lib` subdir must exist in it.
    - `PYTHONPATH` - List of directories where Python looks for modules. Extends `sys.path` initial value. In UNIX, separate with **colons**. In Windows, **semicolons**.
    - 