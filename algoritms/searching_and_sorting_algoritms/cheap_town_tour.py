class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

def find_parent(node):
    while node != parents[node]:
        node = parents[node]
    return node


towns = int(input())
streets = int(input())

forest = []
graph = []

for _ in range(streets):
    start, end, weight = [int(x) for x in input().split(' - ')]
    graph.append(Edge(start, end, weight))

parents = [n for n in range(towns + 1)]

for edge in sorted(graph, key=lambda e: e.weight):

    first_root = find_parent(edge.start)
    second_root = find_parent(edge.end)
    if first_root != second_root:
        parents[second_root] = parents[first_root]
        forest.append(edge)

total_sum = 0
for edge in forest:
    total_sum += edge.weight

print(f'Total cost: {total_sum}')

# 4
# 5
# 0 - 1 - 10
# 0 - 2 - 6
# 0 - 3 - 5
# 1 - 3 - 15
# 2 - 3 - 4