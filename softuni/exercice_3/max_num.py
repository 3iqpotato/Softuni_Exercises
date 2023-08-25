import sys

n = int(input())
total_sum = 0
max_num = -sys.maxsize

for i in range(1, n + 1):
    current_num = int(input())
    if max_num < current_num:
        max_num = current_num

    total_sum += current_num

sum_without_max = total_sum - max_num

if max_num == sum_without_max:
    print("Yes")
    print(f'Sum = {max_num}')
else:
    diff = abs(max_num - sum_without_max)
    print('No')
    print(f'Diff = {diff}')