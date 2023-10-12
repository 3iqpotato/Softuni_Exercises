import sys
num_numbers = int(input())

min_num = sys.maxsize
max_num = -sys.maxsize
for num in range(num_numbers):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    if current_num < min_num:
        min_num = current_num

print(f'Max number: {max_num}\nMin number: {min_num}')


