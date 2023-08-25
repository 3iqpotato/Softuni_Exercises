def explosion(power, row1, col1):
    if power > 0:
        for r in range(row1 - 1, row1 + 2):
            if 0 <= r < n:
                for c in range(col1 - 1, col1 + 2):
                    if 0 <= c < n:
                        if matrix[r][c] > 0:
                            matrix[r][c] -= power


def alive_cells(mat):
    allive = 0
    sum_cells = 0
    for r in range(n):
        for c in range(n):
            if matrix[r][c] > 0:
                allive += 1
                sum_cells += matrix[r][c]
    return [allive, sum_cells]


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

bomb_coordinates = [[int(x) for x in l.split(',')] for l in input().split()]

for bomb in bomb_coordinates:
    row, col = bomb
    bomb_power = matrix[row][col]
    explosion(bomb_power, row, col)

alive, sum_alive = alive_cells(matrix)
print(f'Alive cells: {alive}')
print(f'Sum: {sum_alive}')
[print(*line, sep=' ') for line in matrix]

