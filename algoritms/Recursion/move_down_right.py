def unicue_paths(r, c, board, paths, r_end, c_end):
    if 0 > r or 0 > c or r >= r_end or c >= c_end:
        return

    if board[r][c] == 'e':
        paths_l.append('k')
        return

    # if board[r][c] == 'v':
    #     return
    # board[r][c] = 'v'
    res1 = unicue_paths(r + 1, c, board, paths, r_end, c_end)
    res2 = unicue_paths(r, c + 1, board,paths, r_end, c_end)

    if res1:
        return res1
    if res2:
        return res2

paths_l = []
rows = int(input())
cols = int(input())

matrix = [['*']*cols for _ in range(rows)]
matrix[rows-1][cols-1]= 'e'
unicue_paths(0, 0, matrix, 0, rows, cols)
print(len(paths_l))


