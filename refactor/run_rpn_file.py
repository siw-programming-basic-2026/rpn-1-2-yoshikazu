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