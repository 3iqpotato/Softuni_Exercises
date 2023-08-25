rows, cols = [int(el) for el in input().split(', ')]
matrix = []
sum_mat = 0


for rol in range(rows):
    col = [int(el) for el in input().split(', ')]
    matrix.append(col)
    sum_mat += sum(col)

print(sum_mat)
print(matrix)