
arg_1 = input()
arg_2 = input()
arg_3 = input()

if arg_1.isdigit() and arg_2.isdigit():
    if (float(arg_1) >= 3 and float(arg_1) <= 21) and (float(arg_2) >= 3 and float(arg_2) <= 21):
        if arg_3 == '+':
            print(float(arg_1)+float(arg_2))
        elif arg_3 == '-':
            print(float(arg_1) - float(arg_2))
        elif arg_3 == '*':
            print(float(arg_1) * float(arg_2))
        elif arg_3 == '/':
            print(float(arg_1) / float(arg_2))
