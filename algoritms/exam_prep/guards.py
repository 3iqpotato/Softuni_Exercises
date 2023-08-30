from collections import deque

towns = int(input())
roads = int(input())

parents = {}
visited = [False for x in range(1, towns + 1)]
for _ in range(roads):
    a, b = map(int, input().split())
    if a not in parents:
        parents[a] = []
    if b not in parents:
        parents[b] = []
    parents[a].append(b)

s = int(input())

my_quee = deque()
my_quee.append(s)
while my_quee:
    start = my_quee.popleft()
    if visited[start-1]:
        continue
    visited[start-1] = True
    for child in parents[start]:
        if visited[child-1]:
            continue
        my_quee.append(child)


for x in range(len(visited)):
    if not visited[x]:
        print(x+1, end=' ')
