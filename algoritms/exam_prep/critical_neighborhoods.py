from queue import PriorityQueue

number_of_edges = int(input())

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = int(weight)

graph = {}
distance = {}
parent = {}
for _ in range(number_of_edges):
    start, end, weight = [x for x in input().split(' - ')]
    if start not in graph:
        graph[start] = []
        distance[start] = float('inf')
        parent[start] = None
    if end not in graph:
        graph[end] = []
        distance[end] = float('inf')
        parent[end] = None

    graph[start].append(Edge(start, end, weight))


bad_roads = input().split(',')
other_roads = []
for road in bad_roads:
    other_roads.append(f'{road[2]}-{road[0]}')

bad_roads.extend(other_roads)

for key, value in graph.items():
    for road in value:
        road_path = f"{road.source}-{road.destination}"
        if road_path in bad_roads:
            value.remove(road)


start = input()
end = input()

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

    path = []
    s = end
    while s is not None:
        path.append(s)
        s = parent[s]
    path.reverse()
    print(*path, sep=' - ')
    print(distance[end])


