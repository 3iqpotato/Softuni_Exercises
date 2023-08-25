def check_valid_indices(curr_row, curr_col):
    return 0 <= curr_row < SIZE and 0 <= curr_col < SIZE


def shooting(shooter_pos, direct):
    r = shooter_pos[0] + moves[direct][0]
    c = shooter_pos[1] + moves[direct][1]
    while check_valid_indices(r, c):
        if matrix[r][c] == 'x':
            matrix[r][c] = '.'
            return [r, c]
        r += moves[direct][0]
        c += moves[direct][1]
    return False


# def move_command(steps_move, d):
#     c_row = player_coords[0] + (moves[d] * steps_move)
#     c_col = player_coords[1] + (moves[d] * steps_move)
#     if not check_valid_indices(c_row, c_col) or matrix[c_row][c_col] == "x":
#         return player_coords
#     return [c_row, c_col]

def walking(direct, steps):
    r = player_coords[0] + (moves[direct][0] * steps)
    c = player_coords[1] + (moves[direct][1] * steps)
    if check_valid_indices(r, c):
        if matrix[r][c] == '.':
            return [r, c]
    return player_coords


SIZE = 5
matrix = []

total_count_targets = 0
shoot_targets = 0
player_coords = []
targets_hit_positions = []

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


for row in range(SIZE):
    line = input().split()
    matrix.append(line)
    total_count_targets += line.count('x')
    if 'A' in line:
        player_coords = row, line.index('A')


for _ in range(int(input())):
    command, direction, *num = input().split() # num ne e int!!!
    if command == 'shoot':
        shoot = shooting(player_coords, direction)
        if shoot:
            shoot_targets += 1
            targets_hit_positions.append(shoot)

    elif command == 'move':
        num = int(*num)
        player_coords = walking(direction, num)
    if total_count_targets - shoot_targets == 0:
        break

if total_count_targets - shoot_targets == 0:
    print(f"Training completed! All {total_count_targets} targets hit.")
else:
    print(f"Training not completed! {total_count_targets - shoot_targets} targets left.")

[print(w) for w in targets_hit_positions]