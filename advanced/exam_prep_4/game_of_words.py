def check_valid_indices(curr_row, curr_col):
    return 0 <= curr_row < size and 0 <= curr_col < size


def find_alice():
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'P':
                matrix[r][c] = '-'
                return [r, c]


def player_is_moving_to(direction, alice_place):
    r = alice_place[0] + moves[direction][0]
    c = alice_place[1] + moves[direction][1]
    if not check_valid_indices(r, c):
        return False
    else:
        return [r, c]


def what_he_stepped_on(position):
    place = matrix[position[0]][position[1]]
    if place.isalpha():
        matrix[position[0]][position[1]] = '-'
        return place
    else:
        return False

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

my_string = input()
size = int(input())
matrix = [list(input()) for _ in range(size)]
player_position = find_alice()
for _ in range(int(input())):
    move = input()

    player_new_coords = player_is_moving_to(move, player_position)

    if not player_new_coords:
        my_string = my_string[:-1]
        continue

    player_position = player_new_coords
    stepped_on = what_he_stepped_on(player_position)

    if stepped_on:
        my_string += stepped_on

matrix[player_position[0]][player_position[1]] = 'P'
print(my_string)
[print(*w, sep='') for w in matrix]
