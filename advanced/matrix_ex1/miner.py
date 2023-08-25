from collections import deque


def find_position(ground):
    for r in range(size):
        for c in range(size):
            if ground[r][c] == 's':
                return (r, c)


def move_miner(miner_pos, move, ground):
    row_pos = miner_pos[0] + moves[move][0]
    col_pos = miner_pos[1] + moves[move][1]

    if 0 <= row_pos < size and 0 <= col_pos < size:
        ground[miner_pos[0]][miner_pos[1]] = '*'
        if ground[row_pos][col_pos] == 'e':
            return {'end': (row_pos, col_pos)}
        ground[row_pos][col_pos] = 's'
    return ground


def how_much_coal(ground):
    coal = 0
    for r in range(size):
        for c in range(size):
            if ground[r][c] == 'c':
                coal += 1
    return coal


size = int(input())
commands = deque(input().split())
matrix = [input().split() for _ in range(size)]
coal = how_much_coal(matrix)
is_over = False
moves = {
    'left': (0, -1),
    'right': (0, 1),
    'down': (1, 0),
    'up': (-1, 0)
}
while commands and coal > 0:
    command = commands.popleft()
    miner_position = find_position(matrix)
    matrix = move_miner(miner_position, command, matrix)
    if type({'a': 0}) == type(matrix):
        print(f'Game over! {matrix["end"]}')
        is_over = True
        break
    coal = how_much_coal(matrix)
if not is_over:
    if coal == 0:
        print(f'You collected all coal! {find_position(matrix)}')
    else:
        print(f'{coal} pieces of coal left. {find_position(matrix)}')