matrix = [[int(el) for el in input().split(', ')] for _ in range(int(input()))]
flatten = []
for row in range(len(matrix)):
    flatten.extend(matrix[row])

print(flatten)
