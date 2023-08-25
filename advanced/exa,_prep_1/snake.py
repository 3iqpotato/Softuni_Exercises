def check_valid_indices(curr_row, curr_col):
    return 0 <= curr_row < size and 0 <= curr_col < size


def find_snake():
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'S':
                matrix[r][c] = '.'
                return [r, c]


def snake_move(direction, alice_place):
    r = alice_place[0] + moves[direction][0]
    c = alice_place[1] + moves[direction][1]
    return [r, c]


def what_did_she_find(coordinates):
    find = matrix[coordinates[0]][coordinates[1]]
    matrix[coordinates[0]][coordinates[1]] = '.'
    return find

def teleporting(pos):
    row = pos[0]
    col = pos[1]
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'B':
                if r != row or c != col:
                    matrix[row][col] = '.'
                    matrix[r][c] = '.'
                    return [r, c]


size = int(input())
matrix = [list(input()) for _ in range(size)]

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

snake_position = find_snake()
food_eaten = 0
snake_dead = False

while not snake_dead and food_eaten < 10:
    moving_direction = input()
    snake_is_moving_to = snake_move(moving_direction, snake_position)
    if not check_valid_indices(snake_is_moving_to[0], snake_is_moving_to[1]):
        snake_dead = True
    else:
        snake_position = snake_is_moving_to
        she_find = what_did_she_find(snake_position)
        if she_find == "B":
            snake_position = teleporting(snake_position)
        if she_find == '*':
            food_eaten += 1

if snake_dead:
    print('Game over!')

else:
    matrix[snake_position[0]][snake_position[1]] = 'S'
    print('You won! You fed the snake.')

print(f'Food eaten: {food_eaten}')
[print(''.join(w)) for w in matrix]