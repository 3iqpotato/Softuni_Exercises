rows = int(input())
columns = int(input())

matrix = []
new_matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))
    new_matrix.append([0] * columns)

new_matrix[0][0] = matrix[0][0]


for col in range(1, columns):
    new_matrix[0][col] = new_matrix[0][col-1] + matrix[0][col]

for row in range(1, rows):
    new_matrix[row][0] = new_matrix[row-1][0] + matrix[row][0]

for row in range(1, rows):
    for col in range(1, columns):
        new_matrix[row][col] = max(new_matrix[row-1][col], new_matrix[row][col-1]) + matrix[row][col]

path = []
curr_row = rows-1
curr_column = columns-1
flag = True

while flag:
    if curr_column == 0 and curr_row == 0:
        flag = False
    path.append([curr_row, curr_column])
    if new_matrix[curr_row][curr_column-1] < new_matrix[curr_row-1][curr_column]:
        curr_row -= 1
        if curr_row < 0:
            curr_row = 0
            curr_column -= 1
    else:
        curr_column -= 1
        if curr_column < 0:
            curr_column = 0
            curr_row -=1

path.reverse()
print(*path, sep=" ")
# 3
# 3
# 1 0 6
# 8 3 7
# 2 4 9