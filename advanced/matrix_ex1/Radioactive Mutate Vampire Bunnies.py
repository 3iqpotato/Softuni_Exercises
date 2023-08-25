from collections import deque


def check_valid_indices(curr_row, curr_col):
    return 0 <= curr_row < rows and 0 <= curr_col < cols


def find_player_position():
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'P':
                matrix[r][c] = '.'
                return [r, c]


def player_is_moving_to(direction):
    r = player_position[0] + moves[direction][0]
    c = player_position[1] + moves[direction][1]
    if check_valid_indices(r, c):
        if matrix[r][c] != 'B':
            return 'player_moved', [r, c]
        else:
            return 'Player_stepped_on_rabbit', [r, c]
    return 'player_escaped', player_position


def where_are_the_rabbits():
    coords = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'B':
                coords.append([r, c])
    return coords


def rabbits_spreading(r_pos):
    player_stepped = False
    for rabbit in r_pos:
        for moving in moves:
            r = rabbit[0] + moves[moving][0]
            c = rabbit[1] + moves[moving][1]
            if check_valid_indices(r, c):
                if r == player_position[0] and c == player_position[1]:
                    matrix[r][c] = 'B'
                    player_stepped = True
                else:
                    matrix[r][c] = 'B'
    return player_stepped


rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]
directions = deque(list(input()))

moves = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

player_position = find_player_position()
player_is_alive = True
player_escaped = False

while player_is_alive and not player_escaped:
    move = directions.popleft()

    where_did_player_go, coordinates = player_is_moving_to(move)

    if where_did_player_go == 'player_moved':
        player_position = coordinates
    elif where_did_player_go == 'Player_stepped_on_rabbit':
        player_position = coordinates
        player_is_alive = False
    else:
        player_escaped = True

    rabbits_positions = where_are_the_rabbits()

    did_the_rabbits_eat_the_player = rabbits_spreading(rabbits_positions)
    if did_the_rabbits_eat_the_player:
        player_is_alive = False

[print(*w, sep='') for w in matrix]
if player_escaped:
    print(f'won: {" ".join(str(el) for el in player_position)}')
else:
    print(f'dead: {" ".join(str(el) for el in player_position)}')



