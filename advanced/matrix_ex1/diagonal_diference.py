matrix = [[int(el) for el in input().split()] for _ in range(int(input()))]

sum_first_diagonal = 0
sum_sec_diagonal = 0
for row in range(len(matrix)):
    sum_first_diagonal += (matrix[row][row])
    sum_sec_diagonal += (matrix[row][len(matrix[0]) - row - 1])

print(abs(sum_sec_diagonal - sum_first_diagonal))

