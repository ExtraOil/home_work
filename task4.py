
print('Input figure: ')
figure = input()

if figure == 'circle':
    print('Input radius: ')
    side_c_radius = int(input())
    area = 3.14 * side_c_radius**2
    print(area)
elif figure == 'rectangle':
    print('Input side a and b: ')
    side_a = int(input())
    side_b = int(input())
    area = side_a * side_b
    print(area)
elif figure == 'triangle':
    print('Input side a,b,c: ')
    side_a = int(input())
    side_b = int(input())
    side_c = int(input())
    p = (side_a + side_b + side_c)/2
    area = (p * (p - side_a) * (p - side_b) * (p - side_c))**0.5
    print(area)
