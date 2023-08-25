def find_target(t):
    start_idx = 0
    end_idx = len(my_list) - 1
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        mid_el = my_list[mid_idx]

        if mid_el == t:
            return mid_idx

        if mid_el > t:
            end_idx = mid_idx - 1

        else:
            start_idx = mid_idx + 1

    return -1

my_list = input().split()
target = input()
print(find_target(target))