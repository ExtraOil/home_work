
print("Input values Amount of money  and Years: ")
amount = float(input())
years = int(input())
i = 0

if years != 0:
    while i < years:
        amount += amount * 0.1
        i += 1
print(amount)

