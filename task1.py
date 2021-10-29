
print('enter value arg_1 and arg_2 ')
arg_1 = input()
arg_2 = input()

if arg_1.isdigit() and arg_2.isdigit():
    if (float(arg_1) >= 3 and float(arg_1) <= 21) and (float(arg_2) >= 3 and float(arg_2) <= 21):
        print(abs(float(arg_1)-float(arg_2)))
    else:
        print(arg_1 + arg_2)
else:
    print(arg_1+arg_2)
