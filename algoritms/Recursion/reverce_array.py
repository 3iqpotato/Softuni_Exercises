def reverse_array(arr, idx):
    if idx < 0:
        return
    print(arr[idx], end=' ')
    reverse_array(arr, idx-1)


my_array = [x for x in input().split()]
reverse_array(my_array, len(my_array) -1 )