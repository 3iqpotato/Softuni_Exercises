def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def set_queen(r, c,rows, cols, l_d, r_d):
    matrix[r][c] = '*'
    rows.add(r)
    cols.add(c)
    l_d.add(r-c)
    r_d.add(r+c)


def remove_queen(r, c, rows, cols, l_d, r_d):
    matrix[r][c] = '-'
    rows.remove(r)
    cols.remove(c)
    l_d.remove(r-c)
    r_d.remove(r+c)


def can_place_queen(r, c, rows, cols, l_d, r_d):
    if r in rows:
        return False
    if c in cols:
        return False
    if r - c in l_d:
        return False
    if r + c in r_d:
        return False
    return True


def place_queen(row, board, rows, cols, l_diagonal, r_diagonal):
    if row == 8:
        print_board(board)
        return
    for col in range(8):
        if can_place_queen(row, col, rows, cols, l_diagonal, r_diagonal):
            set_queen(row, col, rows, cols, l_diagonal, r_diagonal)
            place_queen(row+1, board, rows, cols, l_diagonal, r_diagonal)
            remove_queen(row, col, rows, cols, l_diagonal, r_diagonal)


matrix = [['-']* 8for _ in range(8)]
place_queen(0, matrix, set(), set(), set(), set())
