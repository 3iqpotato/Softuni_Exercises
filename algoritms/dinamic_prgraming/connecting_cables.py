cables = [int(c) for c in input().split()]
size = len(cables) + 1
positions = [x for x in range(1, size)]


matrix = [[0] * size for _ in range(size)]

for row in range(1, size):
    for column in range(1, size):
        if cables[row - 1] == positions[column - 1]:
            matrix[row][column] = matrix[row - 1][column - 1] + 1
        else:
            matrix[row][column] = max(matrix[row - 1][column], matrix[row][column - 1])


print(f'Maximum pairs connected: {matrix[size-1][size-1]}')