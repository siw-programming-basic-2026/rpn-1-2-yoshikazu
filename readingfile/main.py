def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "ERROR: 0では割れません"
        return a / b
    else:
        return "ERROR: 不明な演算子です"


def calculate_rpn(expression):
    stack = []

    tokens = expression.split()

    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            if len(stack) < 2:
                return "ERROR: 数字が足りません"

            b = stack.pop()
            a = stack.pop()

            result = calculate(a, b, token)

            if isinstance(result, str) and result.startswith("ERROR"):
                return result

            stack.append(result)

        else:
            try:
                number = float(token)
                stack.append(number)
            except ValueError:
                return "ERROR: 数字または演算子ではありません"

    if len(stack) != 1:
        return "ERROR: 演算子が足りません"

    return stack[0]


def main():
    expression = input("逆ポーランド記法の式を入力してください: ")
    result = calculate_rpn(expression)
    print(result)


main()