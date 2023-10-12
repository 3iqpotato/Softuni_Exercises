# import copy
#
#
# def find_sublists():
#     for idx in range(len_nums):
#         curr_list = [list_nums[idx]]
#
#         if sum(curr_list) <= target_sum:
#             found_sublists.append(copy.deepcopy(curr_list))
#
#         else:
#             continue
#
#         starting_idx = idx + 1
#         end_idx = len_nums
#         for idx_1 in range(starting_idx, end_idx):
#             curr_list.append(list_nums[idx_1])
#
#             if sum(curr_list) <= target_sum:
#                 found_sublists.append(copy.deepcopy(curr_list))
#             else:
#                 break
#
#             for idx_2 in range(idx_1 + 1, end_idx):
#                 curr_list.append(list_nums[idx_2])
#                 if sum(curr_list) <= target_sum:
#                     found_sublists.append(copy.deepcopy(curr_list))
#                 else:
#                     break
#
#             curr_list = curr_list[:1]
#
#
list_nums = [int(x) for x in input().split(', ')]


target_sum = int(input())
# len_nums = len(list_nums)
#
# found_sublists = []
# find_sublists()
# for x in found_sublists:
#
#     print(*x, sep=' ')


# A Python program to count all subsets with given sum.

# dp[i][j] is going to store True if sum j is
# possible with array elements from 0 to i.


def get_subsets(items, target):
    items = sorted(items)
    def helper(i, t, acc):
        if i >= len(items): # no more items
            return
        elif items[i] > t: # all remaining items are too big
            yield acc
        else:
            yield from helper(i+1, t - items[i], (*acc, items[i])) # include item[i]
            yield from helper(i+1, t, acc)                  # do not include item[i]
    yield from helper(0, target, ())

answers = list(get_subsets(list_nums, target_sum))

for i in list_nums:
    for el in answers:
        if len(el) == 1 and el[0] == i:
            break
    else:
        answers.append([i])
for x in answers:
    print(*x, sep=' ')