from math import floor


def closer(x, y):
    return abs(x) + abs(y)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
first = [floor(x1), floor(y1)]
second = [floor(x2), floor(y2)]
uno = closer(x1, y1)
dos = closer(x2, y2)

if closer(x1, y1) < closer(x2, y2):
    print(f'({first[0]}, {first[1]})')
else:
    print(f'({second[0]}, {second[1]})')




