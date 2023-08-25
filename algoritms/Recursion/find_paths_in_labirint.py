def find_directions(lab, r, c, direction, road):
    if r >= rows or c >= cols or 0 > c or 0 > r:
        return
    if lab[r][c] == '*':
        return
    if lab[r][c] == 'v':
        return

    road.append(direction)
    if lab[r][c] == 'e':
        print(''.join(road))

    else:
        lab[r][c] = 'v'

        find_directions(lab, r+1, c, 'D', road)
        find_directions(lab, r-1, c, 'U', road)
        find_directions(lab, r, c+1, 'R', road)
        find_directions(lab, r, c-1, 'L', road)
        lab[r][c] = '-'
    road.remove(direction)


rows = int(input())
cols = int(input())
matrix = [[x for x in input()] for _ in range(rows)]
find_directions(matrix, 0, 0, '', [])

# 3
# 3
# ---
# -*-
# --e
# 3
# 5
# -**-e
# -----
# *****