matrix = [list(input()) for _ in range(int(input()))]
searched_symbol = input()
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == searched_symbol:
            print((row, col))
            exit(0)

print(f'{searched_symbol} does not occur in the matrix')