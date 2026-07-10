# How to Receive Data from a File

## Objective

In this document, you will learn how to read data from a file in Python and process it line by line.

In this program, we read RPN (Reverse Polish Notation) expressions from a file and display the calculation results.

---

## Input, Processing, and Output

A program generally works in the following flow.

```text
Input -> Processing -> Output
```

The key point this time is changing how input is provided.

- Previously, we wrote expressions directly in the program or entered them using `input()`.
- This time, we write expressions in a file and read that file from Python.

## Files Used

For example, use the following structure.

```text
rpn_file_io/
├── run_rpn_file.py
├── rpn_calculator.py
├── expressions.txt
└── results.txt
```

The role of each file is as follows.

- `run_rpn_file.py`: Reads the file and executes RPN calculations
- `rpn_calculator.py`: Contains functions for RPN calculation
- `expressions.txt`: Input file that stores RPN expressions
- `results.txt`: Output file that stores calculation results

### Example of `expressions.txt`

```text
3 4 +
10 2 /
10 0 /
5 a +
3 4 5 +
```

Write one RPN expression per line.

`3 4 +` means `3 + 4` in normal notation.

## Basic File-Opening Pattern

Use `open()` when reading a file in Python.

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  for line in file:
    print(line)
```

This code opens `expressions.txt` and prints it line by line.

### Meaning of `open()`

`open("expressions.txt", "r", encoding="utf-8")`

- `"expressions.txt"`: The file name to open
- `"r"`: Means read mode
- `encoding="utf-8"`: Character encoding setting

### Why Use `with`

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  ...
```

Using `with` automatically closes the file after use.

So, in most cases, you should open files with `with open(...)`.

## Read Line by Line

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  for line in file:
    print(line)
```

`for line in file:` reads the file one line at a time.

For example, if `expressions.txt` contains:

```text
3 4 +
10 2 /
```

Then `line` receives these values in order.

- 1st time: `"3 4 +\n"`
- 2nd time: `"10 2 /\n"`

## Remove Newlines with `strip()`

Each line read from a file includes a trailing newline.

So use `strip()` as follows.

```python
expression = line.strip()
```

Example:

```python
line = "3 4 +\n"
expression = line.strip()

print(expression)
```

Result:

```text
3 4 +
```

`strip()` removes extra whitespace and newlines before and after the text.

## Calculate Each Line

If you have an RPN function called `calculate_rpn()`, you can pass each expression directly.

```python
from rpn_calculator import calculate_rpn

with open("expressions.txt", "r", encoding="utf-8") as file:
  for line in file:
    expression = line.strip()

    if expression == "":
      continue

    result = calculate_rpn(expression)

    print(expression, "=>", result)
```

### Ignore Blank Lines

If the file has blank lines, the program may try to calculate an empty expression.

So add this condition.

```python
if expression == "":
  continue
```

This means: if the line is blank, skip it and move to the next line.

## Write Results to a File

Besides showing results on screen, you can also save them to a file.

```python
from rpn_calculator import calculate_rpn

with open("expressions.txt", "r", encoding="utf-8") as input_file:
  with open("results.txt", "w", encoding="utf-8") as output_file:
    for line in input_file:
      expression = line.strip()

      if expression == "":
        continue

      result = calculate_rpn(expression)

      print(expression, "=>", result)
      output_file.write(f"{expression} => {result}\n")
```

### Difference Between `print()` and `write()`

```python
print(expression, "=>", result)
output_file.write(f"{expression} => {result}\n")
```

- `print()`: Outputs to the terminal
- `write()`: Writes to a file

### Meaning of `\n`

`output_file.write(f"{expression} => {result}\n")`

The final `\n` means a newline.

Without it, all results would be written on one line.

## Write Mode

Use `"w"` when writing to a file.

```python
open("results.txt", "w", encoding="utf-8")
```

`"w"` means write mode.

Be careful: `"w"` overwrites the file each time you run the program.

### If You Want to Append

If you want to keep previous results and add new ones at the end, use `"a"`.

```python
open("results.txt", "a", encoding="utf-8")
```

`"a"` means append mode.

However, in this lesson, we use `"w"` to create fresh results each time.

## Summary

Key points in this lesson:

- Open files with `open()`
- Use `"r"` for read mode
- Use `"w"` for write mode
- Read one line at a time with `for line in file:`
- Remove newlines with `strip()`
- Write to files with `write()`
- Use `\n` for line breaks

## Complete Example

```python
from rpn_calculator import calculate_rpn

input_filename = "expressions.txt"
output_filename = "results.txt"

with open(input_filename, "r", encoding="utf-8") as input_file:
  with open(output_filename, "w", encoding="utf-8") as output_file:
    for line in input_file:
      expression = line.strip()

      if expression == "":
        continue

      result = calculate_rpn(expression)

      print(expression, "=>", result)
      output_file.write(f"{expression} => {result}\n")
```

## Record It on GitHub

After changing your program to read from a file, record the change on GitHub.

```bash
git status
git add .
git commit -m "Read RPN expressions from file"
git push
```

If you want a Japanese commit message, this is also fine.

```bash
git commit -m "RPN式をファイルから読み込む"
```
