num = int(input())
current = 1
dali = False
for row in range(1, num + 1):
    for col in range(1, row + 1):
        if current > num:
            dali = True
            break
        print(str(current) + ' ', end='')
        current += 1
    if dali:
        break
    print()
