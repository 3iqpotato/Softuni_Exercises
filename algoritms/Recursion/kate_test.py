def find_kate():
    for row in range(rows):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'k':
                return row, col


def calculate_kate_moves(r, c, count_moves):
    if 0 > r or r >= rows or 0 > c or c >= cols:
        return count_moves + 1

    if matrix[r][c] == '#':
        return 0

    matrix[r][c] = '#'
    count_moves += 1
    res1 = calculate_kate_moves(r + 1, c, count_moves)
    res2 = calculate_kate_moves(r - 1, c, count_moves)
    res3 = calculate_kate_moves(r, c + 1, count_moves)
    res4 = calculate_kate_moves(r, c - 1, count_moves)
    res = max([res1, res2, res3, res4])

    return res


rows = int(input())

matrix = [list(input()) for _ in range(rows)]
cols = len(matrix[0])
k_r, k_c = find_kate()

moves = calculate_kate_moves(k_r, k_c, 0)
if moves == 0:
    print('Kate cannot get out')
else:
    print(f'Kate got out in {moves - 1} moves')

