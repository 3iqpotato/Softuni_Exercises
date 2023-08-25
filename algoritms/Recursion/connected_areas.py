def calculate_size(r, c):
    if 0 > r or r >= rows or 0 > c or c >= cols:
        return 0

    if matrix[r][c] != '-':
        return 0

    matrix[r][c] = 'v'

    result = 1
    result += calculate_size(r + 1, c)
    result += calculate_size(r - 1, c)
    result += calculate_size(r, c + 1)
    result += calculate_size(r, c - 1)

    return result


class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


rows = int(input())
cols = int(input())

matrix = [list(input()) for _ in range(rows)]


areas = []
for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'v' or matrix[row][col] == '*':
            continue
        size = calculate_size(row, col)
        areas.append(Area(row, col, size))

print(f'Total areas found: {len(areas)}')
count = 0
for area in sorted(areas, key=lambda a: -a.size):
    count += 1
    print(f"Area #{count} at ({area.row}, {area.col}), size: {area.size}")



# 4
# 9
# ---*---*-
# ---*---*-
# ---*---*-
# ----*-*--