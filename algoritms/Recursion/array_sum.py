
def sum_array(my_array_list, idx):
    if idx >= len(my_array_list):
        return 0
    return my_array_list[idx] + sum_array(my_array_list, idx+1)



my_array = [int(x) for x in input().split()]
print(sum_array(my_array, 0))