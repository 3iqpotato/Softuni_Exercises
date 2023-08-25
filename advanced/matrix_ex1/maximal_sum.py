rows, cols = [int(x) for x in input().split()]
matrix = [[int(el) for el in input().split()] for _ in range(rows)]

max_sum = float('-inf')
biggest_sum_mat = []
for row in range(rows - 2):
    for col in range(cols - 2):
        mini_matrix = [matrix[row][col:col+3] for row in range(row, row + 3)]
        sum_mat = sum(sum(l) for l in mini_matrix)
        if sum_mat > max_sum:
            max_sum = sum_mat
            biggest_sum_mat = mini_matrix

print(f'Sum = {max_sum}')
[print(*l) for l in biggest_sum_mat]
