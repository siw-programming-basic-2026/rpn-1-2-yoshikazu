# ファイルからデータを受け取る方法

## 目的

この資料では、Python でファイルからデータを読み込み、1 行ずつ処理する方法を確認します。

今回のプログラムでは、RPN（逆ポーランド記法）の式をファイルから読み込み、計算結果を表示します。

---

## 入力・処理・出力

プログラムは基本的に、次の流れで動きます。

```text
入力 → 処理 → 出力
```

今回のポイントは、入力の方法を変えることです。

- これまでは、プログラムの中に直接式を書いたり、`input()` で入力したりしていました。
- 今回は、計算式をファイルに書いておき、そのファイルを Python で読み込みます。

## 使用するファイル

例として、次のような構成にします。

```text
rpn_file_io/
├── run_rpn_file.py
├── rpn_calculator.py
├── expressions.txt
└── results.txt
```

それぞれの役割は次の通りです。

- `run_rpn_file.py`: ファイルを読み込み、RPN 計算を実行するファイル
- `rpn_calculator.py`: RPN 計算用の関数を書くファイル
- `expressions.txt`: 入力用ファイル。RPN の式を書く
- `results.txt`: 出力用ファイル。計算結果を書き出す

### `expressions.txt` の例

```text
3 4 +
10 2 /
10 0 /
5 a +
3 4 5 +
```

1 行に 1 つの RPN 式を書きます。

`3 4 +` は、通常の計算式では `3 + 4` を意味します。

## ファイルを開く基本形

Python でファイルを読むときは、`open()` を使います。

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  for line in file:
    print(line)
```

このコードは、`expressions.txt` を開いて、1 行ずつ表示します。

### `open()` の意味

`open("expressions.txt", "r", encoding="utf-8")`

- `"expressions.txt"`: 開きたいファイル名
- `"r"`: read の意味。読み込みモード
- `encoding="utf-8"`: 文字コードの指定

### `with` を使う理由

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  ...
```

`with` を使うと、ファイルを使い終わったあとに自動で閉じてくれます。

そのため、基本的にはファイルを開くときは `with open(...)` を使います。

## 1行ずつ読み込む

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  for line in file:
    print(line)
```

`for line in file:` と書くと、ファイルの中身を 1 行ずつ取り出せます。

たとえば、`expressions.txt` に次のように書かれているとします。

```text
3 4 +
10 2 /
```

この場合、`line` には順番に次の値が入ります。

- 1 回目: `"3 4 +\n"`
- 2 回目: `"10 2 /\n"`

## `strip()` で改行を取り除く

ファイルから読み込んだ 1 行には、最後に改行が含まれます。

そのため、次のように `strip()` を使います。

```python
expression = line.strip()
```

例:

```python
line = "3 4 +\n"
expression = line.strip()

print(expression)
```

結果:

```text
3 4 +
```

`strip()` を使うことで、前後の余分な空白や改行を取り除くことができます。

## 1行ずつ計算する

RPN 計算用の関数 `calculate_rpn()` がある場合、ファイルから読み込んだ式をそのまま渡すことができます。

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

### 空行を無視する

ファイルの中に空行があると、何もない式を計算しようとしてしまいます。

そのため、次の処理を入れます。

```python
if expression == "":
  continue
```

これは「もし空行だったら、その行は処理せずに次の行へ進む」という意味です。

## 結果をファイルに書き出す

結果を画面に表示するだけでなく、ファイルに保存することもできます。

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

### `print()` と `write()` の違い

```python
print(expression, "=>", result)
output_file.write(f"{expression} => {result}\n")
```

- `print()`: ターミナルに出力する
- `write()`: ファイルに書き込む

### `\n` の意味

`output_file.write(f"{expression} => {result}\n")`

最後の `\n` は改行を意味します。

これを書かないと、結果がすべて 1 行につながってしまいます。

## 書き込みモード

ファイルを書き込むときは、`"w"` を使います。

```python
open("results.txt", "w", encoding="utf-8")
```

`"w"` は write の意味です。

注意点として、`"w"` は実行するたびにファイルの中身を上書きします。

### 追記したい場合

前の結果を残したまま、後ろに追加したい場合は `"a"` を使います。

```python
open("results.txt", "a", encoding="utf-8")
```

`"a"` は append の意味です。

ただし、今回の授業では、毎回新しく結果を作るために `"w"` を使います。

## まとめ

今回のポイントは次の通りです。

- `open()` でファイルを開く
- `"r"` で読み込みモード
- `"w"` で書き込みモード
- `for line in file:` で 1 行ずつ読み込む
- `strip()` で改行を取り除く
- `write()` でファイルに書き込む
- `\n` で改行する

## 完成例

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

## GitHubに記録する

ファイルから読み込めるように変更できたら、GitHub に記録します。

```bash
git status
git add .
git commit -m "Read RPN expressions from file"
git push
```

日本語でコミットメッセージを書くなら、次のようにしてもよいです。

```bash
git commit -m "RPN式をファイルから読み込む"
```