# 如何从文件读取数据

## 目的

本文将学习如何在 Python 中从文件读取数据，并按行进行处理。

在这次程序中，我们会从文件读取 RPN（逆波兰表示法）表达式，并显示计算结果。

---

## 输入、处理、输出

程序基本按照以下流程运行。

```text
输入 -> 处理 -> 输出
```

这次的重点是改变输入方式。

- 以前我们是在程序中直接写表达式，或者用 `input()` 输入。
- 这次我们把表达式写到文件里，再由 Python 读取该文件。

## 使用的文件

例如，目录结构如下。

```text
rpn_file_io/
├── run_rpn_file.py
├── rpn_calculator.py
├── expressions.txt
└── results.txt
```

各文件作用如下。

- `run_rpn_file.py`：读取文件并执行 RPN 计算
- `rpn_calculator.py`：编写 RPN 计算函数
- `expressions.txt`：输入文件，写入 RPN 表达式
- `results.txt`：输出文件，写入计算结果

### `expressions.txt` 示例

```text
3 4 +
10 2 /
10 0 /
5 a +
3 4 5 +
```

每行写一个 RPN 表达式。

`3 4 +` 在普通中缀表达式中表示 `3 + 4`。

## 打开文件的基本写法

在 Python 中读取文件时使用 `open()`。

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  for line in file:
    print(line)
```

这段代码会打开 `expressions.txt`，并逐行显示内容。

### `open()` 的含义

`open("expressions.txt", "r", encoding="utf-8")`

- `"expressions.txt"`：要打开的文件名
- `"r"`：read，读取模式
- `encoding="utf-8"`：字符编码设置

### 为什么使用 `with`

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  ...
```

使用 `with` 可以在处理完成后自动关闭文件。

因此，通常建议用 `with open(...)` 打开文件。

## 逐行读取

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  for line in file:
    print(line)
```

写成 `for line in file:` 就可以一次取出一行。

例如，`expressions.txt` 中有以下内容：

```text
3 4 +
10 2 /
```

此时 `line` 会依次得到：

- 第 1 次：`"3 4 +\n"`
- 第 2 次：`"10 2 /\n"`

## 用 `strip()` 去掉换行

从文件读出的每一行末尾通常包含换行符。

因此可使用 `strip()`。

```python
expression = line.strip()
```

示例：

```python
line = "3 4 +\n"
expression = line.strip()

print(expression)
```

结果：

```text
3 4 +
```

`strip()` 可以去掉字符串前后的多余空白和换行。

## 按行计算

如果有 RPN 计算函数 `calculate_rpn()`，就可以把每一行表达式直接传入。

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

### 忽略空行

如果文件中有空行，程序可能会尝试计算空表达式。

因此加入以下处理。

```python
if expression == "":
  continue
```

含义是：如果该行为空，就跳过并处理下一行。

## 将结果写入文件

除了在屏幕显示结果，也可以把结果保存到文件。

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

### `print()` 和 `write()` 的区别

```python
print(expression, "=>", result)
output_file.write(f"{expression} => {result}\n")
```

- `print()`：输出到终端
- `write()`：写入文件

### `\n` 的含义

`output_file.write(f"{expression} => {result}\n")`

最后的 `\n` 表示换行。

如果不写，结果会连在同一行。

## 写入模式

写文件时使用 `"w"`。

```python
open("results.txt", "w", encoding="utf-8")
```

`"w"` 表示 write（写入）模式。

注意：`"w"` 每次执行都会覆盖原文件内容。

### 如果想追加

如果想保留原结果并在末尾追加，使用 `"a"`。

```python
open("results.txt", "a", encoding="utf-8")
```

`"a"` 表示 append（追加）模式。

不过本次课程中，为了每次重新生成结果，我们使用 `"w"`。

## 总结

本次要点如下。

- 使用 `open()` 打开文件
- 用 `"r"` 作为读取模式
- 用 `"w"` 作为写入模式
- 用 `for line in file:` 逐行读取
- 用 `strip()` 去掉换行
- 用 `write()` 写入文件
- 用 `\n` 表示换行

## 完整示例

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

## 在 GitHub 上记录

当你完成“从文件读取”改造后，可以记录到 GitHub。

```bash
git status
git add .
git commit -m "Read RPN expressions from file"
git push
```

如果想用日文提交信息，也可以这样写。

```bash
git commit -m "RPN式をファイルから読み込む"
```
