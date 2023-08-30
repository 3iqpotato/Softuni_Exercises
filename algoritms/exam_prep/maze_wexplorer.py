size = int(input())
matrix = []

def find_path(r, c, moves, matrix):
    if r < 0 or c < 0 or r >= size or c >= size:
        return float('inf')
    if matrix[r][c] == '#':
        return float('inf')
    if matrix[r][c] == 'E':
        moves_list.append(moves)
        return 0

    matrix[r][c] = '#'
    moves += 1

    find_path(r + 1, c, moves, matrix),
    find_path(r - 1, c, moves, matrix),
    find_path(r, c + 1, moves, matrix),
    find_path(r, c - 1, moves, matrix)
    matrix[r][c] = '.'





for i in range(size):
    matrix.append(list(input()))

moves_list = []
steps = find_path(0, 0, 0, matrix)

print(min(moves_list))
# print(find_path(0 , 0, 0))