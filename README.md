# RPN Classroom Practice / 逆ポーランド記法の授業用練習

この教材では、逆ポーランド記法（Reverse Polish Notation, RPN）を題材にして、文字列の分割、stack、関数、簡単なエラーハンドリング、GitHubへの提出を練習します。

In this practice, you will use Reverse Polish Notation (RPN) to learn `split()`, stack, functions, simple error handling, and GitHub submission.

---

## 今日の目標 / Goals

- 文字列を `split()` で分割する  
  Split a string using `split()`.
- 式を `tokens` に分ける  
  Convert an expression into `tokens`.
- `stack` に数字を入れたり取り出したりする  
  Push numbers to a `stack` and pop them from it.
- `+` だけに対応した計算を行う  
  Calculate expressions using only `+`.
- エラーになる入力を予想する  
  Predict inputs that cause errors.
- Gitで変更を記録し、GitHubにpushする  
  Record changes with Git and push them to GitHub.

---

## ファイル / Files

```text
01_rpn_classroom_practice/
├── README.md
├── main.py
└── rpn_practice.ipynb
```

| ファイル | File | 役割 / Purpose |
| --- | --- | --- |
| `README.md` | README | この説明ファイル / This guide |
| `main.py` | Python file | 提出用のPythonコード / Python file for submission |
| `rpn_practice.ipynb` | Notebook | `split()` や `stack` を試す実験ノート / Notebook for trying `split()` and `stack` |

---

## 重要な用語 / Important Terms

| 日本語 | English | 意味 / Meaning |
| --- | --- | --- |
| 式 | expression | 計算したい文字列 / A string to calculate |
| 部品 | token | `split()` で分けた1つ1つの要素 / One part created by `split()` |
| スタック | stack | 数字を一時的に入れておくリスト / A list used to store numbers temporarily |
| 演算子 | operator | `+` などの計算記号 / A calculation symbol such as `+` |
| エラー | error | 正しく処理できない状態 / A state that cannot be processed correctly |

---

## 逆ポーランド記法とは / What is RPN?

通常の式では、足し算を次のように書きます。  
In normal notation, addition is written like this:

```text
3 + 4
```

逆ポーランド記法では、演算子を後ろに書きます。  
In Reverse Polish Notation, the operator comes after the numbers.

```text
3 4 +
```

この式は、次のように読みます。  
Read it like this:

```text
3 と 4 を足す
Add 3 and 4
```

結果は `7` です。  
The result is `7`.

---

## 今日扱う式 / Expressions

`main.py` には、次のような式が入っています。  
`main.py` has expressions like these:

```python
expressions = [
    "3 4 +",      # Prediction / 予想:
    "10 20 +",    # Prediction / 予想:
    "3 +",        # Prediction / 予想:
    "5 a +",      # Prediction / 予想:
    "3 4 5 +",    # Prediction / 予想:
]
```

実行する前に、右側の `Prediction / 予想:` に結果を予想して書きます。  
Before running the program, write your prediction after `Prediction / 予想:`.

例 / Example:

```python
"3 4 +",      # Prediction / 予想: 7
"3 +",        # Prediction / 予想: Error. Not enough numbers. / エラー。数字が足りない。
```

---

## エラーの例 / Error Examples

### 1. 数字が足りない / Not enough numbers

```text
3 +
```

`+` で計算するには、数字が2つ必要です。しかし、この式では数字が1つしかありません。  
The `+` operator needs two numbers. But this expression has only one number.

```text
Error: not enough numbers
エラー: 数字が足りません
```

### 2. 不正な文字がある / Invalid token

```text
5 a +
```

`a` は数字でも演算子でもありません。  
`a` is not a number and not an operator.

```text
Error: invalid token
エラー: 不正な文字があります
```

### 3. 数字が余る / Too many numbers

```text
3 4 5 +
```

計算後に、stack の中に数字が2つ以上残る場合があります。この場合、式として正しくまとまっていません。  
After calculation, more than one number may remain in the stack. In that case, the expression is not complete.

```text
Error: too many numbers
エラー: 数字が余っています
```

---

## 作業手順 / Steps

### 1. 作業場所を確認する / Check your working directory

```bash
pwd
ls
```

### 2. Notebookで練習する / Practice with the notebook

`rpn_practice.ipynb` を開いて、`split()` や `stack` の動きを確認します。  
Open `rpn_practice.ipynb` and check how `split()` and `stack` work.

### 3. `main.py` を編集する / Edit `main.py`

`main.py` の `TODO` を少しずつ完成させます。  
Complete the `TODO` parts in `main.py` step by step.

### 4. 実行する / Run the program

```bash
python main.py
```

または環境によっては次のコマンドを使います。  
Or use this command depending on your environment:

```bash
python3 main.py
```

### 5. Gitで変更を確認する / Check changes with Git

```bash
git status
```

### 6. 変更を記録する / Commit your changes

```bash
git add .
git commit -m "Complete RPN classroom practice"
```

### 7. GitHubに送る / Push to GitHub

```bash
git push
```

### 8. GitHubで確認する / Check on GitHub

GitHubの画面を開いて、`main.py` が更新されていることを確認してください。  
Open GitHub in your browser and check that `main.py` has been updated.

---

## 今日の合言葉 / Key Message

```text
まず予想する。
Then run.
結果を見る。
Then think again.
```

```text
Predict first.
Then run.
Check the result.
Then think again.
```

---

## 注意 / Notes

- 今回は `+` だけに対応します。  
  This time, only `+` is supported.
- `-`, `*`, `/` は次の段階で扱います。  
  `-`, `*`, and `/` will be handled later.
- コードを全部理解できなくても大丈夫です。  
  It is okay if you do not understand all the code yet.
- まずは、`split()`、`tokens`、`stack` の動きを確認しましょう。  
  First, focus on `split()`, `tokens`, and `stack`.
- エラーは失敗ではありません。エラーの理由を考えることが学習です。  
  Errors are not failures. Thinking about why an error happens is part of learning.
