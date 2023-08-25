from math import pi
fig = input()

if fig == 'square':
    a = float(input())
    area = a ** 2

elif fig == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b

elif fig == 'circle':
    r = float(input())
    area = pi * (r ** 2)

elif fig == 'triangle':
    a = float(input())
    b = float(input())
    area = a * b * 1 / 2

print(f'{area:.3f}')
