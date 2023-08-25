def nested_loops(n, arr, idx=0):
    if idx == len(arr):
        print(*arr)
        return

    for curr_num in range(1, n+1):
        arr[idx] = curr_num
        nested_loops(n, arr, idx+1)



num = int(input())
array = [1]*num
nested_loops(num, array)