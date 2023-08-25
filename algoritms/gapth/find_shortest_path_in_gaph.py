from collections import deque

number_of_nodes = int(input())
edges = int(input())

graph = [[] for _ in range(100+1)]

for _ in range(edges):
    destination, source = [int(x) for x in input().split()]
    graph[destination].append(source)

start = int(input())
end = int(input())

visited = [False] * (number_of_nodes+1)
parent = [None] * (number_of_nodes+1)

visited[start] = True
queue = deque([start])

while queue:
    node = queue.popleft()
    if node == end:
        break
    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = node

path = []
father = end
while father:
    path.append(father)
    father = parent[father]

path.reverse()
print(f"Shortest path length is: {len(path) - 1}")
print(*path, sep=' ')

# 8
# 10
# 1 2
# 1 4
# 2 3
# 4 5
# 5 8
# 5 6
# 5 7
# 5 8
# 6 7
# 7 8
# 1
# 7