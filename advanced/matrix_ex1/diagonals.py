matrix = [[int(el) for el in input().split(', ')] for _ in range(int(input()))]

sum_first_diagonal = []
sum_sec_diagonal = []
for row in range(len(matrix)):
    sum_first_diagonal.append(matrix[row][row])
    sum_sec_diagonal.append(matrix[row][len(matrix[0]) - row - 1])

print(f'Primary diagonal: {", ".join(str(el) for el in sum_first_diagonal)}. Sum: {sum(sum_first_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(el) for el in sum_sec_diagonal)}. Sum: {sum(sum_sec_diagonal)}')