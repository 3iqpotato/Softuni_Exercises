from collections import deque

def best_list_pureness(nums, n):
    rotation = 0
    max_sum = 0
    nums = deque(nums)
    for rotatio in range(n + 1):
        pureness = 0
        for x in nums:
            m = x
            m *= nums.index(x)
            pureness += m
        if pureness > max_sum:
            max_sum = pureness
            rotation = rotatio
        nums.appendleft(nums.pop())

    return f'Best pureness {max_sum} after {rotation} rotations'





test = ([0, 0, 0, 0], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
