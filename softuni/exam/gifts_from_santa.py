n = int(input())
m = int(input())
s = int(input())

for num1 in range(m, n - 1, -1):
    if num1 % 2 == 0 and num1 % 3 == 0:
        if num1 == s:
            break
        else:
            print(num1, end=' ')
