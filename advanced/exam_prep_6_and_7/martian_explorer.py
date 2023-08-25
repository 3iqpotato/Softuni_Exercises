from collections import deque


def we_found(coords):
    return field[coords[0]][coords[1]]


moves = {
    'left': lambda x, y: [x, (y - 1) % SIZE],
    'up': lambda x, y: [(x - 1) % SIZE, y],
    'right': lambda x, y: [x, (y + 1) % SIZE],
    'down': lambda x, y: [(x + 1) % SIZE, y]
}


SIZE = 6

rover_coordinates = []
field = []
for row in range(SIZE):
    line = input().split()

    if 'E' in line:
        idx = line.index('E')
        rover_coordinates = [row, idx]
        line[idx] = '-'

    field.append(line)

commands = deque(input().split(', '))
deposits = {'W': 0, "M": 0, 'C': 0}
is_suitable = False

while commands:
    if all(deposits.values()):
        is_suitable = True

    move = commands.popleft()
    new_pos = moves[move](rover_coordinates[0], rover_coordinates[1])
    what_we_found = we_found(new_pos)

    if what_we_found.isalpha():

        if what_we_found in deposits:
            deposits[what_we_found] += 1

            if what_we_found == 'W':
                print(f'Water deposit found at ({", ".join(str(x) for x in new_pos)})')

            elif what_we_found == 'M':
                print(f'Metal deposit found at ({", ".join(str(x) for x in new_pos)})')

            else:
                print(f'Concrete deposit found at ({", ".join(str(x) for x in new_pos)})')

        else:
            print(f'Rover got broken at ({", ".join(str(x) for x in new_pos)})')

    rover_coordinates = new_pos

if not is_suitable:
    print(f'Area not suitable to start the colony.')
else:
    print('Area suitable to start the colony.')

# R - - - - -
# - - C - - -
# - - - - M -
# - - W - - -
# - E - W - R
# - - - - - -
# up, right, down, right, right, right
