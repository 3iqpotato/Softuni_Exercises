import sys

num = int(input())

full_sum_even = 0
full_sum_od = 0
max_od_num = -sys.maxsize
min_od_num = sys.maxsize
max_even_num = -sys.maxsize
min_even_num = sys.maxsize

for i in range(1, num + 1):
    number = float(input())
    if i % 2 == 0:
        full_sum_even += number
        if number > max_even_num:
            max_even_num = number
        if number < min_even_num:
            min_even_num = number
    else:
        full_sum_od += number
        if number > max_od_num:
            max_od_num = number
        if number < min_od_num:
            min_od_num = number

if max_od_num == - sys.maxsize:
    max_even_num = 'No'
    max_od_num = 'No'
    min_even_num = 'No'
    min_od_num = 'No'
elif max_even_num == -sys.maxsize:
    max_even_num = 'No'
    max_od_num = f'{max_od_num:.2f}'
    min_even_num = 'No'
    min_od_num = f'{min_od_num:.2f}'
else:
    max_even_num = f'{max_even_num:.2f}'
    max_od_num = f'{max_od_num:.2f}'
    min_even_num = f'{min_even_num:.2f}'
    min_od_num = f'{min_od_num:.2f}'

print(f'OddSum={full_sum_od:.2f},')
print(f'OddMin={min_od_num},')
print(f'OddMax={max_od_num},')
print(f'EvenSum={full_sum_even:.2f},')
print(f'EvenMin={min_even_num},')
print(f'EvenMax={max_even_num}')