rows,  cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]
times = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        ch = matrix[row][col]
        if ch == matrix[row + 1][col] and \
            matrix[row + 1][col + 1] == matrix[row][col + 1] and \
                ch == matrix[row][col + 1]:
            times += 1

print(times)


