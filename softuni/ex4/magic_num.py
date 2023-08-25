low_num = int(input())
max_num = int(input())
magic_num = int(input())
correct = 0
flaf = False
combinations = 0
for a in range(low_num, max_num + 1):
    for b in range(low_num, max_num + 1):
        combinations += 1
        if a + b == magic_num:
            flaf = True
            if flaf:
                break
    if flaf:
        break
if flaf:
    print(f'Combination N:{combinations} ({a} + {b} = {magic_num})')
else:
    print(f'{combinations} combinations - neither equals {magic_num}')