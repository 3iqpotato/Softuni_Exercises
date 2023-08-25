SIZE = 8


paws_coordinates = {'w': [], 'b': []}
board = []

for row in range(SIZE):
    col = input().split()

    if 'w' in col:
        paws_coordinates['w'] = [row, col.index('w')]
    if 'b' in col:
        paws_coordinates['b'] = [row, col.index('b')]

    board.append(col)

if abs(paws_coordinates['w'][1] - paws_coordinates['b'][1]) != 1 or paws_coordinates['w'][0] <= paws_coordinates['b'][0]:
    white_left = SIZE - (SIZE - paws_coordinates['w'][0])
    black_left = SIZE - paws_coordinates['b'][0]
    if white_left >= black_left:
        print(f'Game over! Black pawn is promoted to a queen at {chr(97 + paws_coordinates["b"][1])}1.')
    else:
        print(
            f'Game over! White pawn is promoted to a queen at {chr(97 + paws_coordinates["w"][1])}8.')

else:
    meet = SIZE - ((paws_coordinates['w'][0] + paws_coordinates['b'][0]) // 2)
    distance = paws_coordinates['w'][0] - paws_coordinates['b'][0]

    if distance % 2 == 0:
        print(f'Game over! Black win, capture on {chr(97 + paws_coordinates["w"][1])}{meet}.')
    else:
        print(f'Game over! White win, capture on {chr(97 + paws_coordinates["b"][1])}{meet}.')

# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# b - - - - - - -
# - - - - - - - -
# - w - - - - - -
# - - - - - - - -