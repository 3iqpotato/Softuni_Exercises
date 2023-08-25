def sum_num(num1, num2):
    return num1 + num2


def substract_num(num1, num2):
    return num1 - num2

num1 = int(input())
num2 = int(input())
num3 = int(input())

sum_num(num1, num2)
print(substract_num(sum_num(num1, num2), num3))
