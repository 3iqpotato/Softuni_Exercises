def valid_coordinates(list_coordinates):
    if len(list_coordinates) == 4:
        if 0 <= list_coordinates[0] <= rows and 0 <= list_coordinates[2] <= rows and \
                0 <= list_coordinates[1] <= cols and 0 <= list_coordinates[3] <= cols:
            return True
    return False

rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

while True:
    command, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

    if command == 'END':
        break
    if command == 'swap':
        if valid_coordinates(coordinates):
            row1, col1, row2, col2 = coordinates
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*l) for l in matrix]
            continue

    print('Invalid input!')

