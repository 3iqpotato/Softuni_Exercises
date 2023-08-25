num = int(input())
all_num = 0
i = 0
while i < num:
    i += 1
    if i > num:
        break
    num1 = int(input())
    all_num += num1
mdam = all_num / i
print(f'{mdam:.2f}')
