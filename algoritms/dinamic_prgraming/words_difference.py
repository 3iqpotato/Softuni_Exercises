first_word = input()
second_word = input()

rows = len(first_word) + 1
cols = len(second_word) + 1

matrix = [[0] * cols for _ in range(rows)]

for col in range(1, cols):
    matrix[0][col] = col

for row in range(1, rows):
    matrix[row][0] = row

for row in range(1, rows):
    for col in range(1, cols):
        if first_word[row - 1] == second_word[col - 1]:
            matrix[row][col] = matrix[row - 1][col - 1]
        else:
            matrix[row][col] = min(matrix[row - 1][col] + 1, matrix[row][col - 1] + 1)


print(f'Deletions and Insertions: {matrix[rows-1][cols-1]}')