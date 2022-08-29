# python-plus
Shorten your Python code with concise syntax.

## Installation

From PIP:

```
$ pip install shorter-python
```

## Running code from command line

### Use the `pythonplus` command, followed by a filename

```
$ pythonplus my_file.py
```

Note: the file can have any extension, not just `.py`

### To debug your program, use `-d 1`

```
$ pythonplus my_file.py -d 1
```

The output will look like this:

```
Python+ Code:
n=100
$([i£i:range(1,n+1)?~~n%i])

Python3 Code:
n=100
print([i for i in range(1,n+1) if  not n%i])

Output:
[1, 2, 4, 5, 10, 20, 25, 50, 100]
```

## Running code from Python

Use the `convert` function to convert a string of Python+ code to Python:

```python
from python_plus import convert
exec(convert(PYTHON_PLUS_CODE_HERE))
```

## Syntax

Here is a table to show the difference between Python and Python+

|Python|Python+|Examples|Characters saved|
|-|-|-|-|
|`print`|`$`|`print(x)` -> `$(x)`|4|
|`input`|`§`|`input(x)` -> `§(x)`|4|
|`for` ... `in`|`£` ... `:`\*|`for x in y:` -> `£x:y`|7|
|`in`|`:`|`x in y` -> `x:y`|3|
|`while`|`€`\*|`while x` -> `€x`|5|
|`if`|`?`\*|`if x:` -> `?x`|3|
|`else`|`!`\*|`else:` -> `!`|4|
|`elif`|`±`\*|`elif x:` -> `±x`|5|
|`and`|`&&`|`x and y` -> `x&&y`|3|
|`or`|`\|\|`|`x or y` -> `x\|\|y`|2|
|`not`|`~~`|`not x` -> `~~x`|2|

\* Colons are not needed at the end of a line in Python+

## Example

This Python script to get the factors of a given number, n, is 43 characters:

```python
print([i for i in range(1,n+1) if not n%i])
```

The equivalent Python+ code is 27 characters (a 37% reduction)

```python
$([i£i:range(1,n+1)?~~n%i])
```

Python+ can save you time and characters.
