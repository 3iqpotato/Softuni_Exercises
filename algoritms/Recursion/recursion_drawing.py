def drowing(n):
    if n == 0:
        return
    print('*' * n)
    drowing(n-1)
    print('#' * n)

num = int(input())

drowing(num)