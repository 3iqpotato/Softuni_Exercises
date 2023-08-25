num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    hund_thou = i // 100000
    ten_thou = (i // 10000) % 10
    thou = (i // 1000) % 10
    hun = (i // 100) % 10
    ten = (i // 10) % 10
    units = (i // 1) % 10
    sum_even = ten_thou + hun + units
    sum_odd = hund_thou + thou + ten
    if sum_odd == sum_even:
        print(i, end=' ')
