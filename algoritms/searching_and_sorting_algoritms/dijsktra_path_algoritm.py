from queue import PriorityQueue

number_of_edges = int(input())

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

graph = {}
for _ in range(number_of_edges):
    start, end, weight = [int(x) for x in input().split(', ')]
    if start not in graph:
        graph[start] = []
    if end not in graph:
        graph[end] = []
    graph[start].append(Edge(start, end, weight))

start = int(input())
end = int(input())

max_num = max(graph.keys())
distance = [float('inf')] * len(graph)
parent = [None] * len(graph)

pq = PriorityQueue()
pq.put((0, start))

while not pq.empty():
    min_distance, node = pq.get()
    if node == end:
        break
    for child in graph[node]:
        new_distance = min_distance + child.weight
        if new_distance < distance[child.destination]:
            distance[child.destination] = new_distance
            parent[child.destination] = node
            pq.put((new_distance, child.destination))

if distance[end] == float('inf'):
    print('There is no such path.')
else:
    print(distance[end])
    path = []
    s = end
    while s is not None:
        path.append(s)
        s = parent[s]
    path.reverse()
    print(*path, sep=' ')


