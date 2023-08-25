def is_valid_coords(r, c):
    return 0 <= r < row and 0 <= c < col


def moving_mouse(rw, cl, m):
    r = rw + moves[m][0]
    c = cl + moves[m][1]
    if is_valid_coords(r, c):
        return [r, c]
    else:
        return False


row, col = [int(x) for x in input().split(',')]


field = []
mouse_position = []
full_cheese_count = 0

for i in range(row):
    input_line = list(input())

    if "M" in input_line:
        mouse_position = [i, input_line.index('M')]

    full_cheese_count += input_line.count('C')
    field.append(input_line)

mouse_state = 'alive'

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while mouse_state == 'alive':
    command = input()

    if command == "danger":

        break

    mouse_is_going_to = moving_mouse(mouse_position[0], mouse_position[1], command)

    if not mouse_is_going_to:
        mouse_state = 'dead'
        break
    else:
        m_r, m_c = mouse_is_going_to
        if field[m_r][m_c] == '@':
            continue

        field[mouse_position[0]][mouse_position[1]] = "*"

        if field[m_r][m_c] == "C":
            full_cheese_count -= 1
            mouse_position = [m_r, m_c]
            if full_cheese_count == 0:
                break

        elif field[m_r][m_c] == 'T':
            mouse_position = [m_r, m_c]
            mouse_state = 'Trapped'

        else:
            mouse_position = [m_r, m_c]


if mouse_state == 'alive':
    if full_cheese_count == 0:
        print("Happy mouse! All the cheese is eaten, good night!")
    else:
        print("Mouse will come back later!")
elif mouse_state == 'dead':
    print("No more cheese for tonight!")
else:
    print("Mouse is trapped!")
field[mouse_position[0]][mouse_position[1]] = "M"
[print(''.join(w)) for w in field]

