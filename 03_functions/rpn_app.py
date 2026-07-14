from pathlib import Path

from rpn_calculator import calculate_rpn


def run_manual_input():
    while True:
        expression = input(
            "RPNの式を入力してください（qで終了）: "
        ).strip()

        if expression == "q":
            print("手入力を終了します")
            break

        if expression == "":
            continue

        result = calculate_rpn(expression)
        print(expression, "=>", result)


def run_file_input():
    filepath = (
        Path(__file__).resolve().parent
        / "expressions.txt"
    )

    try:
        with filepath.open("r", encoding="utf-8") as file:
            for line in file:
                expression = line.strip()

                if expression == "":
                    continue

                result = calculate_rpn(expression)
                print(expression, "=>", result)

    except FileNotFoundError:
        print("ERROR:ファイルが見つかりません")
        print("探した場所:", filepath)


def main():
    print("入力方法を選んでください")
    print("1: 手入力")
    print("2: ファイル入力")

    choice = input("番号を入力してください: ").strip()

    if choice == "1":
        run_manual_input()
    elif choice == "2":
        run_file_input()
    else:
        print("ERROR:1または2を入力してください")


if __name__ == "__main__":
    main()