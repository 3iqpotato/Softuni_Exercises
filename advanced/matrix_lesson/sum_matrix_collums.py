matrix = [[int(el) for el in input().split()] for _ in range([int(el) for el in input().split(', ')][0])]

for col in range(len(matrix[0])):
    sum_els = 0
    sum_els += sum(matrix[row][col] for row in range(len(matrix)))
    print(sum_els)
