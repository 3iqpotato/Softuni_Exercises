def calculate_moves(lab, r, c, count_moves):
    if r >= rows or c >= cols or 0 > r or 0 > c:
        return count_moves
    if lab[r][c] == '#':
        return

    lab[r][c] = '#'
    count_moves += 1
    res = calculate_moves(lab, r+1, c, count_moves)
    if res:
        return res
    res = calculate_moves(lab, r-1, c, count_moves)
    if res:
        return res
    res = calculate_moves(lab, r, c+1, count_moves)
    if res:
        return res

    res = calculate_moves(lab, r, c-1, count_moves)
    if res:
        return res

    # return (calculate_moves(lab, r+1, c, count_moves),
    #     calculate_moves(lab, r-1, c, count_moves),
    #     calculate_moves(lab, r, c+1, count_moves),
    #     calculate_moves(lab, r, c-1, count_moves),)


def ketes_pos(lab):
    for r in range(rows):
        for c in range(cols):
            if lab[r][c] == 'k':
                return r, c

rows = int(input())
matrix = [[x for x in input()] for _ in range(rows)]
cols = len(matrix[0])
kates_r, kates_c = ketes_pos(matrix)
moves = calculate_moves(matrix, kates_r, kates_c, 0)
if moves:
    print(f'Kate got out in {moves} moves')

else:
    print('Kate cannot get out')
# 5
# #####
# # k#
# # ###
# #####
# # ###
# 4
# ######
# ## k#
# ## ###
# ## ###