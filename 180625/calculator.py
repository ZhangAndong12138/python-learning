print("欢迎使用calculator v1.0")
while True:
    mark = input(
        "请输入运算符号：\n[A]dd = + \n[S]ubtract = -\n[M]ultiply = * \n[D]ivide = /\n[E]xponentiation = ^\n")
    value1 = float(input("请输入值1：\n"))
    value2 = float(input("请输入值2：\n"))
    if mark == "A" or mark == "a":
        print(str(value1) + "+" + str(value2) + "=" + str(value1 + value2))
    elif mark == "S" or mark == "s":
        print(str(value1) + "-" + str(value2) + "=" + str(value1 - value2))
    elif mark == "M" or mark == "m":
        print(str(value1) + "*" + str(value2) + "=" + str(value1 * value2))
    elif mark == "D" or mark == "d":
        if value2 == 0:
            print("除数不可以为0哦。")
        else:
            print(str(value1) + "/" + str(value2) + "=" + str(value1 / value2))
    elif mark == "E" or mark == "e":
        print(str(value1) + "^" + str(value2) + "=" + str(value1 ** value2))
    else:
        print("运算符:["+mark+"]好像不太对哦。")
    res = input("请输入[C]ontinue：继续 或 [Q]uit：退出\n")
    if res == "C" or res == "c":
        continue
    elif res == "Q" or res == "q":
        break
    else:
        print("不可以淘气哦")
        continue
print("拜拜~")
