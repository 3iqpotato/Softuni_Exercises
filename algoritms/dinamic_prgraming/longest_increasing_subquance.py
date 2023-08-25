from collections import deque

nums = [int(x) for x in input().split(' ')]

len_nums = [0] * len(nums)
parent = [None] * len(nums)

best_len = 0
best_idx = 1

for curr_idx in range(len(nums)):
    curr_num = nums[curr_idx]
    curr_len = 1
    curr_parent = -1

    for prev_idx in range(curr_idx -1, -1, -1):
        prev_number = nums[prev_idx]
        prev_len = len_nums[prev_idx]
        if curr_num > prev_number and prev_len + 1 >= curr_len:
            curr_len = prev_len + 1
            curr_parent = prev_idx

    len_nums[curr_idx] = curr_len
    parent[curr_idx] = curr_parent

    if curr_len > best_len:
        best_len = curr_len
        best_idx = curr_idx

path = deque()
idx = best_idx

while idx != -1:
    path.appendleft(nums[idx])
    idx = parent[idx]

print(*path, sep=' ')