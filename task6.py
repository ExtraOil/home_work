
print("Input values a and b: ")
value_a = int(input())
value_b = int(input())

while value_a != value_b:
    if value_a > value_b:
        value_a -= value_b
    else:
        value_b -= value_a

print(value_a)
