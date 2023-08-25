def is_valid_coords(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE


def sum_column(c):
    p = 0
    for r in range(SIZE):
        if not matrix[r][c].isalpha():
            p += int(matrix[r][c])
    return p


buckets_hit = []
SIZE = 6
matrix = [[x for x in input().split()] for _ in range(SIZE)]
points = 0

for _ in range(3):
    coords = [int(x) for x in input()[1:-1].split(', ')]
    row, col = coords

    if is_valid_coords(row, col):
        if matrix[row][col] == 'B':
            points += sum_column(col)
            matrix[row][col] = 0


if points < 100:
    print(f'Sorry! You need {100-points} points more to win a prize.')
else:
    if points < 200:
        print(f"Good job! You scored {points} points, and you've won Football.")
    elif points < 300:
        print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
    else:
        print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")