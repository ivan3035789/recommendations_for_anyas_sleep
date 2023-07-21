a = int(input())
b = int(input())
h = int(input())
if a <= 24 and a <= h <= b and h <= 24:
    print('Это нормально')
elif 24 >= a >= h and h < b and h <= 24:
    print('Недосып')
elif a <= 24 and h >= a and b < h <= 24:
    print('Пересып')
