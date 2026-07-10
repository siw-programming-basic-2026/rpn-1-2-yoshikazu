from pathlib import Path


def main():
    filepath = (
        Path(__file__).resolve().parent
        / "rpn_expressions_1000_float_mixed.txt"
    )

    try:
        with filepath.open("r", encoding="utf-8") as file:
            for line in file:
                expression = line.strip()

                if expression == "":
                    continue

                print(expression)

    except FileNotFoundError:
        print("ERROR:ファイルが見つかりません")
        print("探した場所:", filepath)


if __name__ == "__main__":
    main()