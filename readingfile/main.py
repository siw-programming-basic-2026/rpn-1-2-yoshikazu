def calculate(a, b, operator):
    if operator == "+":
        return a + b
    

operators = {"+"}



with open("expressions.txt", "r", encoding="utf-8") as file:
    for line in file:
        expression = line.strip()
        print("expression:", expression)

        print(expression.split())






    # TODO:
    # expression を split して tokens にしましょう。

        tokens = expression.split()
        stack = []

        print("tokens:",tokens)
        print("stack:",stack)

        for token in tokens:
            print("token:", token)
            print("stack before:", stack)

            if token in operators:
                # TODO:
                # stack から2つ取り出しましょう。
                #
                # b = stack.pop()
                # a = stack.pop()
                if len(stack) < 2:
                    print("値が足りません")
                    break
                
                else:
                    print("TODO: stackから2つ取り出す")
                    b = stack.pop()
                    a = stack.pop()

                # TODO:
                # calculate() で計算しましょう。
                #
                # result = calculate(a, b, token)

                    print("TODO: calculate()で計算する")
                    result=calculate(a,b,token)

                # TODO:
                # 計算結果を stack に戻しましょう。
                #
                # stack.append(result)

                    print("TODO: 結果をstackに戻す")
                    stack.append(result)

            else:
                # TODO:
                # token を整数に変換して stack に入れましょう。
                #
                # stack.append(int(token))
                if token.isdigit():
                    print("TODO: 数字をstackに入れる")
                    stack.append(int(token))
                else:
                    print("不正な入力です。計算を止めます。")
                    break
                

            print("stack after:", stack)
            print("-----")
        if len(stack)!=1:
            print("値が2つ以上あるので演算子が足りません。")
        else:    
            print("最後のstack:", stack)
            print()