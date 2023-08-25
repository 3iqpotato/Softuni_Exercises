lengh = float(input())
width = float(input())

size = lengh * width
piece = input()

while piece != 'STOP':
    piece = int(piece)


    size -= piece
    if size <= 0:
        break
    piece = input()
if size > 0:
    print(f'{size:.0f} pieces are left.')
else:
    size = abs(size)
    print(f'No more cake left! You need {size:.0f} pieces more.')