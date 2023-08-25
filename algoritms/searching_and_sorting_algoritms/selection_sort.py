def reverce_my_list():
    for idx in range(len(my_list)):
        smallest_num_idx = my_list.index(min(my_list[idx::]))
        my_list[idx], my_list[smallest_num_idx] = my_list[smallest_num_idx], my_list[idx]



my_list = [int(x) for x in input().split()]
reverce_my_list()
print(*my_list, sep=' ')