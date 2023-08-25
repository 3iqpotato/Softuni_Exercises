def adding(mat, nums):
    r = nums[0]
    c = nums[1]
    if 0 <= r < size and 0 <= c < size:
        mat[r][c] += nums[2]
        return True
    return False


def substacting(mat, nums):
    r = nums[0]
    c = nums[1]
    if 0 <= r < size and 0 <= c < size:
        mat[r][c] -= nums[2]
        return True
    return False

size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

while True:
    command, *digits = [int(el) if not el.isalpha() else el for el in input().split()]
    if command == 'END':
        break
    if command == 'Add':
        added = adding(matrix, digits)
        if not added:
            print('Invalid coordinates')
    elif command == 'Subtract':
        subtracted = substacting(matrix, digits)
        if not subtracted:
            print('Invalid coordinates')

[print(*el) for el in matrix]

# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END