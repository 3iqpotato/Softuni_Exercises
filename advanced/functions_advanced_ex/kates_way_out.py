def check_valid_indices(curr_row, curr_col):
    return 0 <= curr_row < size and 0 <= curr_col < len(matrix[0])


def kates_way_out(row, col, moves):
    r = row
    c = col
    if not check_valid_indices(r, c):
        return moves

    if matrix[r][c] == '#':
        return 0

    matrix[r][c] = '#'

    result1 = kates_way_out(r + 1, c, moves+1)
    result2 = kates_way_out(r - 1, c, moves+1)
    result3 = kates_way_out(r, c + 1, moves+1)
    result4 = kates_way_out(r, c - 1, moves+1)

    return max(result4, result3, result2, result1)


def find_kate():
    for r in range(size):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 'k':
                return [r, c]


size = int(input())
matrix = [list(input()) for _ in range(size)]
kate_pos = find_kate()

out_moves = kates_way_out(kate_pos[0], kate_pos[1], 0)

if out_moves:
    print(f"Kate got out in {out_moves} moves")
else:
    print(f'Kate cannot get out')