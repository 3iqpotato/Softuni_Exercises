def check_valid_indices(curr_row, curr_col):
    return 0 <= curr_row < size_of_matrix and 0 <= curr_col < size_of_matrix


def find_santa():
    for r in range(size_of_matrix):
        for c in range(size_of_matrix):
            if matrix[r][c] == 'S':
                return [r, c]


def moving_santa(direction):
    r = santa_coordinates[0] + moves[direction][0]
    c = santa_coordinates[1] + moves[direction][1]
    if check_valid_indices(r, c):
        return [r, c]
    return False


def eating_cookie():
    gifted_presents = 0
    nice_kids_with_present = 0

    for m in moves:
        r = santa_new_position[0] + moves[m][0]
        c = santa_new_position[1] + moves[m][1]
        if check_valid_indices(r, c):
            if matrix[r][c] == 'X':
                gifted_presents += 1
                matrix[r][c] = '-'
            elif matrix[r][c] == 'V':
                gifted_presents += 1
                nice_kids_with_present += 1
            matrix[r][c] = '-'
            if total_count_presents - gifted_presents == 0:
                break
    return gifted_presents, nice_kids_with_present


total_count_presents = int(input())
size_of_matrix = int(input())
nice_kids_count = 0
matrix = []


for row in range(size_of_matrix):
    matrix.append(input().split())
    nice_kids_count += matrix[row].count('V')

santa_coordinates = find_santa()
happy_kids = 0


moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while total_count_presents > 0 and nice_kids_count != happy_kids:
    command_move = input()

    if command_move == 'Christmas morning':
        break

    if command_move in moves.keys():
        santa_new_position = moving_santa(command_move)
        if santa_new_position:
            matrix[santa_coordinates[0]][santa_coordinates[1]] = '-'
            under_santa_is = matrix[santa_new_position[0]][santa_new_position[1]]
            if under_santa_is == 'X':
                santa_coordinates = santa_new_position
                matrix[santa_new_position[0]][santa_new_position[1]] = 'S'

            elif under_santa_is == 'V':
                happy_kids += 1
                total_count_presents -= 1
                # nice_kids_count -= 1
                santa_coordinates = santa_new_position
                matrix[santa_new_position[0]][santa_new_position[1]] = 'S'

            elif under_santa_is == 'C':
                presents_gift, nice_kids_with_presents = eating_cookie()
                santa_coordinates = santa_new_position
                matrix[santa_new_position[0]][santa_new_position[1]] = 'S'
                total_count_presents -= presents_gift
                happy_kids += nice_kids_with_presents
                # nice_kids_count -= nice_kids_with_presents

            else:
                matrix[santa_new_position[0]][santa_new_position[1]] = 'S'
                santa_coordinates = santa_new_position


matrix[santa_coordinates[0]][santa_coordinates[1]] = 'S'

if total_count_presents == 0 and nice_kids_count > happy_kids:
    print(f'Santa ran out of presents!')

if nice_kids_count == happy_kids:
    [print(*w) for w in matrix]
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")

else:
    [print(*w) for w in matrix]
    print(f"No presents for {abs(nice_kids_count - happy_kids)} nice kid/s.")
