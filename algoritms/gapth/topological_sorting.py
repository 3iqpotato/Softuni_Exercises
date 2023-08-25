def fill_graphs_pointed_dict():
    for g in dict_graphs:
        if g not in dict_graphs_pointed:
            dict_graphs_pointed[g] = 0
        for child in dict_graphs[g]:
            if child not in dict_graphs_pointed:
                dict_graphs_pointed[child] = 0
            dict_graphs_pointed[child] += 1


def topological_sorting():
    for g, n in dict_graphs_pointed.items():
        if n == 0:
            return g
    return None


num = int(input())


dict_graphs = {}
dict_graphs_pointed = {}
for _ in range(num):
    graph, mosts = input().strip().split(' ->')
    dict_graphs[graph] = [] if mosts == '' else [x for x in mosts.strip().split(', ')]


fill_graphs_pointed_dict()
res = []
bat = False
while dict_graphs_pointed:
    curr_res = topological_sorting()
    if not curr_res:
        bat = True
        print("Invalid topological sorting")
        break
    res.append(curr_res)
    dict_graphs_pointed.pop(curr_res)
    for child in dict_graphs[curr_res]:
        dict_graphs_pointed[child] -= 1

if not bat:
    print(f'Topological sorting: {", ".join(res)}')







# 6
# A -> B, C
# B -> D, E
# C -> F
# D -> C, F
# E -> D
# F ->