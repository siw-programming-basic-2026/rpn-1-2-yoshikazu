from pathlib import Path

def calculate(a, b, operator):
    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":
        if b == 0:
            return "ERROR:0では割れません"
        return a / b

    else:
        return "ERROR:不明な演算子です"


operators = {"+", "-", "*", "/"}


def calculate_rpn(expression):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token in operators:
            if len(stack) < 2:
                return "ERROR:値が足りません"

            b = stack.pop()
            a = stack.pop()

            result = calculate(a, b, token)

            if isinstance(result, str):
                return result

            stack.append(result)

        else:
            try:
                number = float(token)
                stack.append(number)
            except ValueError:
                return "ERROR:数字または演算子ではありません"

    if len(stack) == 1:
        return stack[0]

    elif len(stack) > 1:
        return "ERROR:演算子が足りません"

    else:
        return "ERROR:式が空です"