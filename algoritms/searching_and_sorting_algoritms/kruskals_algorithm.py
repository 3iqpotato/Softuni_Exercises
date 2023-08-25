times = int(input())


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


def find_parent(node):
    while node != parents[node]:
        node = parents[node]
    return node

forest = []
graph = []

max_num = float('-inf')
for _ in range(times):
    start, end, weight = [int(x) for x in input().split(', ')]
    graph.append(Edge(start, end, weight))

    max_num = max(start, end, max_num)

parents = [n for n in range(max_num + 1)]

for edge in sorted(graph, key=lambda e: e.weight):

    first_root = find_parent(edge.start)
    second_root = find_parent(edge.end)
    if first_root != second_root:
        parents[second_root] = parents[first_root]
        forest.append(edge)

for edge in forest:
    print(f"{edge.start} - {edge.end}")

# 11
# 0, 3, 9
# 0, 5, 4
# 0, 8, 5
# 1, 4, 8
# 1, 7, 7
# 2, 6, 12
# 3, 5, 2
# 3, 6, 8
# 3, 8, 20
# 4, 7, 10
# 6, 8, 7