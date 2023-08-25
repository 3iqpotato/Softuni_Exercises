my_list = [int(x) for x in input().split()]

is_sorted = False
counter = 0
while not is_sorted:
    is_sorted = True
    for idx in range(1, len(my_list) - counter):
        if my_list[idx] < my_list[idx-1]:
            my_list[idx], my_list[idx-1] = my_list[idx-1], my_list[idx]
            is_sorted = False
    counter += 1





print(*my_list, sep=' ')