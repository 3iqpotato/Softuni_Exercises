num1 = int(input())
num2 = int(input())
bonus1 = int(input())
bonus2 = int(input())
max1 = num1 + bonus1
max2 = num2 + bonus2
del1 = num1
del2 = num2
for first in range(num1, max1 + 1):
    times = 0
    for n in range(1, max1 + 1):
        core = first % n
        if core == 0:
            times += 1
    if times <= 2:
        for second in range(num2, max2 + 1):
            times = 0
            for m in range(1, max2 + 1):
                cor = second % m
                if cor == 0:
                    times += 1
            if times <= 2:
                print(f'{first}{second}')
