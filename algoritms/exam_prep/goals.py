from collections import deque

goals = [int(x) for x in input().split(', ')]
lenght = [0] * len(goals)
parent = [0] * len(goals)

best_len, best_idx = 0, 0

for curr_idx in range(len(goals)):
    curr_num, curr_len, curr_parent = goals[curr_idx], 1, -1
    for prev_idx in range(curr_idx-1, -1 , -1):
        prev_num, prev_len = goals[prev_idx], lenght[prev_idx]
        if curr_num >= prev_num and prev_len + 1>= curr_len:
            curr_len = prev_len + 1
            curr_parent = prev_idx

    lenght[curr_idx] = curr_len
    parent[curr_idx] = curr_parent
    if curr_len > best_len:
        best_len = curr_len
        best_idx = curr_idx

lis = deque()
idx = best_idx

while idx != -1:
    lis.appendleft(goals[idx])
    idx = parent[idx]

print(*lis)