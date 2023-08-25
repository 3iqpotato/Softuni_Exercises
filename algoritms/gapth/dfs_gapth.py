def dfs(node):
    if visited_graphs[node]:
        return
    visited_graphs[node] = True
    for child in graphs[node]:
        dfs(child)
    component.append(node)


number = int(input())

graphs = []
for _ in range(number):
    line = input()
    graphs.append([] if line == '' else [int(el) for el in line.split()])


visited_graphs = [False] * number

for graph in range(len(graphs)):
    if visited_graphs[graph]:
        continue
    component = []
    dfs(graph)
    print(f'Connected component: {" ".join(str(x) for x in component)}')



# 9
# 3 6
# 3 4 5 6
# 8
# 0 1 5
# 1 6
# 1 3
# 0 1 4
#
# 2