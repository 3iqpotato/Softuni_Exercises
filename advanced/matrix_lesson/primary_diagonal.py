matrix = [[int(el) for el in input().split()] for _ in range(int(input()))]
# sum_diagonal = 0
# for row in range(len(matrix)):
#     sum_diagonal += matrix[row][row]
# print(sum_diagonal)
print(sum([matrix[row][row] for row in range(len(matrix))]))