def check_valid_indices(curr_row, curr_col):
    return 0 <= curr_row < SIZE and 0 <= curr_col < SIZE


def find_queens():
    queens_coords = []
    for r in range(SIZE):
        for c in range(SIZE):
            if matrix[r][c] == 'Q':
                queens_coords.append([r, c])

    return queens_coords


def find_king():
    for r in range(SIZE):
        for c in range(SIZE):
            if matrix[r][c] == 'K':
                return [r, c]


def is_attacking_up(row, col):
    for idx in range(1, SIZE):
        r1 = row - idx
        if 0 <= r1 < SIZE:
            if matrix[r1][col] == "K":
                return True
            elif matrix[r1][col] == "Q":
                return False
    return False


def is_attacking_down(row, col):
    for idx in range(1, SIZE):
        r2 = row + idx
        if 0 <= r2 < SIZE:
            if matrix[r2][col] == "K":
                return True
            elif matrix[r2][col] == "Q":
                return False
    return False


def is_attacking_diagonal1(row, col):
    for idx in range(1, SIZE):
        r1 = row - idx
        c1 = col - idx
        if check_valid_indices(r1, c1):
            if matrix[r1][c1] == 'K':
                return True
            elif matrix[r1][c1] == 'Q':
                return False

    return False


def is_attacking_diagonal2(row, col):
    for idx in range(1, SIZE):
        r2 = row + idx
        c2 = col + idx
        if check_valid_indices(r2, c2):
            if matrix[r2][c2] == 'K':
                return True
            elif matrix[r2][c2] == 'Q':
                return False
    return False


def is_attacking_diagonal3(row, col):
    for idx in range(1, SIZE):
        r2 = row - idx
        c2 = col + idx
        if check_valid_indices(r2, c2):
            if matrix[r2][c2] == 'K':
                return True
            elif matrix[r2][c2] == 'Q':
                return False
    return False


def is_attacking_diagonal4(row, col):
    for idx in range(1, SIZE):
        r2 = row + idx
        c2 = col - idx
        if check_valid_indices(r2, c2):
            if matrix[r2][c2] == 'K':
                return True
            elif matrix[r2][c2] == 'Q':
                return False
    return False


def attacking_left(row, col):
    for idx in range(1, SIZE):
        c1 = col - idx
        if 0 <= c1 < SIZE:
            if matrix[row][c1] == "K":
                return True
            elif matrix[row][c1] == "Q":
                return False
    return False


def attacking_right(row, col):
    for idx in range(1, SIZE):
        c1 = col + idx
        if 0 <= c1 < SIZE:
            if matrix[row][c1] == "K":
                return True
            elif matrix[row][c1] == "Q":
                return False
    return False


def queen_attack(coordinates):
    row = coordinates[0]
    col = coordinates[1]
    if attacking_left(row, col):
        return coordinates
    if attacking_right(row, col):
        return coordinates
    if is_attacking_up(row, col):
        return coordinates
    if is_attacking_down(row, col):
        return coordinates
    if is_attacking_diagonal1(row, col):
        return coordinates
    if is_attacking_diagonal2(row, col):
        return coordinates
    if is_attacking_diagonal3(row, col):
        return coordinates
    if is_attacking_diagonal4(row, col):
        return coordinates


SIZE = 8
matrix = [input().split() for _ in range(8)]
all_queen_coordinates = find_queens()
king_coordinates = find_king()
danger_queens_coordinates = []


for queen in all_queen_coordinates:
    can_she_kill_the_king = queen_attack(queen)
    if can_she_kill_the_king:
        danger_queens_coordinates.append(queen)


if danger_queens_coordinates:
    [print(w) for w in danger_queens_coordinates]
else:
    print('The king is safe!')
