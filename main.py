# =========================================
# RPN Classroom Practice
# 逆ポーランド記法の練習
# =========================================
# Goal / 目標:
# 1. Split expression into tokens
#    expression を tokens に分ける
# 2. Use stack
#    stack を使う
# 3. Calculate only "+"
#    今回は "+" だけ計算する
# 4. Find simple errors
#    簡単なエラーを見つける
#
# This file has TODO parts.
# このファイルには、未完成の TODO があります。


# =========================================
# Calculate function / 計算する関数
# =========================================

def calculate(a, b, operator):
    """
    Calculate a and b.
    a と b を計算する。
    This time, only + is supported.
    今回は + だけ対応。
    """

    if operator == "+":
        # TODO:
        # Return a + b.
        # a + b を返す。
        #
        # Hint / ヒント:
        # return a + b

        print("TODO: write + calculation / + の計算を書く")
        return 0

    print("Error: unsupported operator / エラー: 未対応の演算子:", operator)
    return None


# =========================================
# Operators / 使用できる演算子
# =========================================

# TODO:
# Use set for operators.
# 演算子を set で書く。
#
# Hint / ヒント:
# operators = {"+"}

operators = set()


# =========================================
# Expressions / 入力する式
# =========================================
# Write your prediction before running.
# 実行する前に予想を書く。
#
# Example / 例:
# "3 4 +"      # Prediction / 予想: 7
# "3 +"        # Prediction / 予想: Error. Not enough numbers.
# "5 a +"      # Prediction / 予想: Error. "a" is not a number.
# "3 4 5 +"    # Prediction / 予想: Error. Too many numbers.

expressions = [
    "3 4 +",      # Prediction / 予想:
    "10 20 +",    # Prediction / 予想:
    "3 +",        # Prediction / 予想:
    "5 a +",      # Prediction / 予想:
    "3 4 5 +",    # Prediction / 予想:
]


# =========================================
# RPN logic / RPN の処理
# =========================================
# Read first. Then complete TODO parts.
# まず読む。そのあと TODO を完成させる。

for expression in expressions:
    print("-----")
    print("expression:", expression)

    # TODO:
    # Split expression into tokens.
    # expression を空白で区切って tokens にする。
    #
    # Hint / ヒント:
    # tokens = expression.split()

    tokens = []
    print("tokens:", tokens)

    stack = []
    error = False

    for token in tokens:
        print("token:", token)
        print("stack before:", stack)

        # -----------------------------------------
        # Operator token / 演算子の場合
        # -----------------------------------------
        if token in operators:

            # TODO:
            # Need 2 numbers in stack.
            # stack に数字が2つ必要。
            #
            # If stack has fewer than 2 numbers, it is an error.
            # stack の中に数字が2つ未満ならエラー。
            #
            # Hint / ヒント:
            # if len(stack) < 2:
            #     print(expression, "= Error: not enough numbers / エラー: 数字が足りません")
            #     error = True
            #     break

            pass

            # TODO:
            # Pop 2 numbers from stack.
            # stack から数字を2つ取り出す。
            #
            # First pop is b.
            # 先に取り出したものを b にする。
            #
            # Second pop is a.
            # 次に取り出したものを a にする。
            #
            # Hint / ヒント:
            # b = stack.pop()
            # a = stack.pop()

            print("TODO: pop 2 numbers / 数字を2つ取り出す")
            continue

            # TODO:
            # Calculate using calculate().
            # calculate() を使って計算する。
            #
            # Hint / ヒント:
            # result = calculate(a, b, token)

            print("TODO: calculate / 計算する")

            # TODO:
            # Push result back to stack.
            # 結果を stack に戻す。
            #
            # Hint / ヒント:
            # stack.append(result)

            print("TODO: push result / 結果を戻す")

        # -----------------------------------------
        # Number token / 数字の場合
        # -----------------------------------------
        elif token.isdigit():

            # TODO:
            # Convert token to int, then push to stack.
            # token を int に変換して stack に入れる。
            #
            # Hint / ヒント:
            # stack.append(int(token))

            print("TODO: push number / 数字を入れる")
            pass

        # -----------------------------------------
        # Invalid token / 不正な文字の場合
        # -----------------------------------------
        else:
            print(expression, "= Error: invalid token / エラー: 不正な文字があります:", token)
            error = True
            break

        print("stack after:", stack)

    # =========================================
    # Result / 結果表示
    # =========================================

    if not error:
        # TODO:
        # If calculation is correct, stack has only 1 value.
        # 正しく計算できたら、stack の中身は1つだけ。
        #
        # Hint / ヒント:
        # if len(stack) == 1:
        #     print(expression, "=", stack[0])
        # else:
        #     print(expression, "= Error: too many numbers / エラー: 数字が余っています")

        print("TODO: check final stack / 最後の stack を確認する")
        print("stack:", stack)