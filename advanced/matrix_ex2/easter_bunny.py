def bunny_way(field, direction, bunny_place):
    r = bunny_place[0] + moves[direction][0]
    c = bunny_place[1] + moves[direction][1]
    collected_eggs = 0
    coords = []
    while 0 <= r < size and 0 <= c < size:
        if field[r][c] == 'X':
            break
        collected_eggs += field[r][c]
        coords.append([r, c])
        r += moves[direction][0]
        c += moves[direction][1]
    return [collected_eggs, coords]


def bunny_coords(field):
    for r in range(size):
        for c in range(size):
            if field[r][c] == 'B':
                return [r, c]


size = int(input())
matrix = [[int(el) if not el.isalpha() else el for el in input().split()] for _ in range(size)]

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

bunny_coordinates = bunny_coords(matrix)


most_eggs = float('-inf')
way = ''
way_coords = []
for move in moves:
    eggs, steps = bunny_way(matrix, move, bunny_coordinates)
    if eggs >= most_eggs:
        most_eggs = eggs
        way = move
        way_coords = steps

print(way)
[print(w) for w in way_coords]
print(most_eggs)

# 8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22
