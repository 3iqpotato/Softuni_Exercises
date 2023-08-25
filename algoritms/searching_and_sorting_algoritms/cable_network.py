from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.weight = weight
        self.second = second
        self.first = first

    def __gt__(self, other):
        return self.weight > other.weight


budget = int(input())
nodes = int(input())
edges = int(input())

tree = set()
graph = [[] for _ in range(nodes)]
budget_used = 0

for _ in range(edges):
    line = input().split()
    first, second, weight = int(line[0]), int(line[1]), int(line[2])
    edge = Edge(first, second, weight)
    if len(line) == 4:
        tree.add(edge)
    else:
        graph[first].append(edge)
        graph[second].append(edge)


def find_parent(node):
    while node != parents[node]:
        node = parents[node]
    return node


parents = [n for n in range(nodes + 1)]

pq = PriorityQueue()
for edge in tree:
    start = edge.first
    end = edge.second
    parents[start] = parents[end]
    for x in graph[start]:
        pq.put(x)
    for y in graph[end]:
        pq.put(y)

while not pq.empty():
    edge = pq.get()
    first_root = find_parent(edge.first)
    second_root = find_parent(edge.second)
    if first_root != second_root:
        if budget_used + edge.weight > budget:
            break
        budget_used += edge.weight

        parents[second_root] = parents[first_root]
        tree.add(edge)
        for x in graph[first_root]:
            if x not in tree:
                pq.put(x)
        for y in graph[second_root]:
            if y not in tree:
                pq.put(y)

        

print(f'Budget used: {budget_used}')
