from math import floor


def find_player():
    for r in range(size):
        for c in range(size):
            if field[r][c] == 'P':
                field[r][c] = 0
                return [[r, c]]


def player_moving(direction):
    row = player_moves[-1][0] + moves[direction][0]
    col = player_moves[-1][1] + moves[direction][1]

    if row < 0:
        row = size - 1
    if col < 0:
        col = size - 1
    if row > size - 1:
        row = 0
    if col > size - 1:
        col = 0
    return [row, col]


size = int(input())

field = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size) ]

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

coins = 0
player_moves = find_player()
player_died = False

while coins < 100:
    command = input()

    if command not in moves.keys():
        continue

    player_new_coordinates = player_moving(command)

    if player_new_coordinates:
        player_moves.append(player_new_coordinates)
        if field[player_new_coordinates[0]][player_new_coordinates[1]] == 'X':
            coins = floor(coins / 2)
            player_died = True
            break

        else:
            coins += field[player_new_coordinates[0]][player_new_coordinates[1]]
            field[player_new_coordinates[0]][player_new_coordinates[1]] = 0

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
if player_died:
    print(f"Game over! You've collected {coins} coins.")

print('Your path:')
[print(el) for el in player_moves]
