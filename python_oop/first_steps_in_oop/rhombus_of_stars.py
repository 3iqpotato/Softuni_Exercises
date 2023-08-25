def print_upper_part(num):
    for count in range(1, num + 1):
        printing(num, count)


def print_lower_part(num):
    for count in range(num - 1, 0, -1):
        printing(num, count)

def printing(num, count):
    print(" " * (num - count), end='')
    print(*['*'] * count)


def print_rhombus(num):
    print_upper_part(num)
    print_lower_part(num)




n = int(input())

print_rhombus(n)