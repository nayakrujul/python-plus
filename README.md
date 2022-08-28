# python-plus
Shorten your Python code with shorter syntax.

## Installation

From PIP:

```
$ pip install shorter-python
```

## Running code

Use the `pythonplus` command, followed by a filename

```
$ pythonplus my_file.py
```

Note: the file can have any extension, not just `.py`

## Syntax

Here is a table to show the difference between Python and Python+

|Python|Python+|Examples|Characters saved|
|-|-|-|-|
|`print`|`$`|`print(x)` -> `$(x)`|4|
|`input`|`§`|`input(x)` -> `§(x)`|4|
|`for` ... `in`|`£` ... `:`*|`for x in y:` -> `£x:y`|7|

\* Colons are not needed at the end of a line in Python+
