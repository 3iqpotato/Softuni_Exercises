def check_valid_indices(curr_row, curr_col):
    return 0 <= curr_row < SIZE and 0 <= curr_col < SIZE


def find_alice(field):
    for r in range(SIZE):
        for c in range(SIZE):
            if field[r][c] == 'A':
                field[r][c] = '*'
                return [r, c]


def alice_move(direction, alice_place):
    r = alice_place[0] + moves[direction][0]
    c = alice_place[1] + moves[direction][1]
    return [r, c]


def what_did_she_find(field, coordinates):
    find = field[coordinates[0]][coordinates[1]]
    field[coordinates[0]][coordinates[1]] = '*'
    return find



SIZE = int(input())
matrix = [[int(el) if el.isdigit() else el for el in input().split()] for _ in range(SIZE)]
alice_coordinates = find_alice(matrix)
tea_bags_collected = 0

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


while True:
    move_direction = input()
    alice_coordinates = alice_move(move_direction, alice_coordinates)

    if not check_valid_indices(alice_coordinates[0], alice_coordinates[1]):
        print("Alice didn't make it to the tea party.")
        break

    she_find = what_did_she_find(matrix, alice_coordinates)

    if she_find == 'R':
        print("Alice didn't make it to the tea party.")
        break

    if str(she_find).isdigit():
        tea_bags_collected += she_find
        if tea_bags_collected >= 10:
            print("She did it! She went to the party.")
            break
[print(*line) for line in matrix]