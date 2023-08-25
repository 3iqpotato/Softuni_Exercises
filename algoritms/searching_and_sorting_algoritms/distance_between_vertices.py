from collections import deque

nodes = int(input())
num_of_pears = int(input())


max_number = float('-inf')
graph = {}

for _ in range(nodes):
    start, *childs = input().split(':')
    start = int(start)
    childs = [int(x) for x in childs[0].split()]
    graph[start] = childs
    max_number = max(start, *childs if len(childs) > 1 else childs, max_number)


for _ in range(num_of_pears):
    start, end = [int(x) for x in input().split('-')]

    visited = {start}
    parent = {}

    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == end:
            break
        for child in graph[node]:
            if child in visited:
                continue
            visited.add(child)
            queue.append(child)
            parent[child] = node

    path = []
    father = end
    while True:
        path.append(father)
        try:
            father = parent[father]
        except KeyError:
            break

    if len(path) == 1:
        strin = f'{start}, {end}'
        print('{' + strin + '} -> -1')
        continue
    strin = f'{start}, {end}'
    print('{' + strin + '} -> ' + str(len(path) - 1))

# 8
# 4
# 1:4
# 2:4
# 3:4 5
# 4:6
# 5:3 7 8
# 6:
# 7:8
# 8:
# 1-6
# 1-5
# 5-6
# 5-8

