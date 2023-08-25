def check_valid_indices(curr_row, curr_col):
    return 0 <= curr_row < size and 0 <= curr_col < size


def place_bomb(coordinates):
    r = coordinates[0]
    c = coordinates[1]
    if check_valid_indices(r, c):
        matrix[r][c] = '*'


def calculating_sums(row, col):
    bomb_in_range = 0
    for move in moves_dict.values():
        r = row + move[0]
        c = col + move[1]
        if check_valid_indices(r, c):
            if matrix[r][c] == '*':
                bomb_in_range += 1
    return bomb_in_range


moves_dict = {
    1: (1, 0),
    2: (1, 1),
    3: (0, 1),
    4: (-1, 0),
    5: (-1, -1),
    6: (0, -1),
    7: (1, -1),
    8: (-1, 1),
}

size = int(input())
matrix = [[0] * size for _ in range(size)]
num_bombs = int(input())
bombs_positions = [input() for _ in range(num_bombs)]


for bomb in bombs_positions:
    bomb = bomb[1:-1]
    bomb = [int(x) for x in bomb.split(', ')]
    place_bomb(bomb)


for r in range(size):
    for c in range(size):
        if matrix[r][c] == 0:
            matrix[r][c] = calculating_sums(r, c)

[print(*w) for w in matrix]