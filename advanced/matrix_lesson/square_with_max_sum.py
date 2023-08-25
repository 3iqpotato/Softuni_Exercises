import sys

matrix = [[int(el) for el in input().split(', ')] for _ in range([int(el) for el in input().split(', ')][0])]

max_sum_square = -sys.maxsize
square_nums = []

for row in range(len(matrix) - 1):
    for col in range(len(matrix[row]) - 1):
        number = matrix[row][col]
        left_num = matrix[row][col + 1]
        down_num = matrix[row + 1][col]
        diagonal_num = matrix[row + 1][col + 1]
        sum_nums = number + left_num + diagonal_num + down_num
        if sum_nums > max_sum_square:
            square_nums = [[number, left_num], [down_num, diagonal_num]]
            max_sum_square = sum_nums

print(*square_nums[0])
print(*square_nums[1])
print(max_sum_square)

