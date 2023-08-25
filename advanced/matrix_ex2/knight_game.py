def check_valid_indices(curr_row, curr_col):
    return 0 <= curr_row < size and 0 <= curr_col < size


def how_many_is_attacking(position):
    att = 0
    for move in all_moves:
        r = position[0] + move[0]
        c = position[1] + move[1]
        if check_valid_indices(r, c):
            if matrix[r][c] == 'K':
                att += 1
    return att



size = int(input())
matrix = [list(input()) for _ in range(size)]
removed_knights = 0



all_moves = (
    (-2, -1),
    (-2, +1),
    (-1, -2),
    (-1, +2),
    (+1, -2),
    (+1, +2),
    (+2, -1),
    (+2, +1)
)


while True:
    max_attacks = 0
    coords = []
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                posit = [row, col]
                attacking = how_many_is_attacking(posit)
                if attacking > max_attacks:
                    coords = posit
                    max_attacks = attacking
    if coords:
        matrix[coords[0]][coords[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)