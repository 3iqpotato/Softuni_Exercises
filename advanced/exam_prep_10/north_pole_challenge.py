def is_valid_coords(r, c):
    return 0 <= r < row and 0 <= c < col


def move_santa(move, r, c):

    r_and_c = moves[move](r, c)

    return r_and_c


dict_presents ={
    "D": 0,
    "G": 0,
    'C': 0

}


row, col = [int(x) for x in input().split(', ')]

moves = {
    'left': lambda x, y: [x, (y - 1) % col],
    'up': lambda x, y: [(x - 1) % row, y],
    'right': lambda x, y: [x, (y + 1) % col],
    'down': lambda x, y: [(x + 1) % row, y]
}

field = []
santa_coords = []
all_items = 0
collected_items_count = 0
win = False
for i in range(row):
    input_line = input().split()
    if "Y" in input_line:
        santa_coords = [i, input_line.index('Y')]
    all_items += input_line.count('D') + input_line.count('G') + input_line.count('C')
    field.append(input_line)

while not win:

    commands = input().split('-')

    if 'End' in commands:
        break

    command, steps = commands
    steps = int(steps)

    for _ in range(steps):
        field[santa_coords[0]][santa_coords[1]] = "x"

        santa_coords = move_santa(command, santa_coords[0], santa_coords[1])
        place = field[santa_coords[0]][santa_coords[1]]

        if place in dict_presents:
            dict_presents[place] += 1
            collected_items_count += 1

        field[santa_coords[0]][santa_coords[1]] = "Y"

        if all_items == collected_items_count:
            win = True
            break

if all_items == collected_items_count:
    print('Merry Christmas!')
print("You've collected:")
for key, value in dict_presents.items():
    if key == "D":
        print(f"- {value} Christmas decorations")
    elif key == "G":
        print(f"- {value} Gifts")
    else:
        print(f"- {value} Cookies")

[print(*w) for w in field]