def tibona(x):
    list_tibon = [1, 1, 2]
    listoo = [1, 1, 2]
    if x >= 3:
        for idx in range(3, x):
            list_tibon.append(listoo[-1] + listoo[-2] + listoo[-3])
            listoo.append(list_tibon[idx])
    elif x == 2:
        return [1, 1]
    elif x == 1:
        return [1]
    elif x == 0:
        return []
    return list_tibon


times = int(input())
print(f"{' '.join(str(x) for x in tibona(times))}")