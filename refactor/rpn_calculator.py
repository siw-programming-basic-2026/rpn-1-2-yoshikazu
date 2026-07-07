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
    
    
with open("/home/siwuser/repositories/rpn-1-2-yoshikazu/readingfile/rpn_expressions_1000_float_mixed.txt", "r", encoding="utf-8") as file:
    for line in file:
        expression = line.strip()

        if expression == "":
            continue

        result = calculate_rpn(expression)
        print(expression, "=>", result)
        print()


"""        
with open("rpn_expressions_1000_float_mixed.txt", "r", encoding="utf-8") as input_file, \
     open("results.txt", "w", encoding="utf-8") as output_file:

    for line in input_file:
        expression = line.strip()

        if expression == "":
            continue

        result = calculate_rpn(expression)

        print(expression, "=>", result)
        output_file.write(f"{expression} => {result}\n")
"""