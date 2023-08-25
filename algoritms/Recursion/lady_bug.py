def calculate_paths(r, c):
    if r > row - 1 or c > col - 1:
        return 0
    if r == row-1 and c == col-1:
        return 1
    res = calculate_paths(r + 1, c) + calculate_paths(r, c+1)
    return res


row = int(input())
col = int(input())

paths = calculate_paths(0, 0)
print(paths)