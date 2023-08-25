from collections import deque

list_tasks = [int(x) for x in input().split(', ')]
task_idx = int(input())
clock_cycles = 0
max_num = float('inf')
while True:
    min_task = min(list_tasks)
    idx = list_tasks.index(min_task)
    clock_cycles += min_task
    if idx == task_idx:

        print(clock_cycles)
        break
    list_tasks.remove(list_tasks[idx])
    list_tasks.insert(idx, max_num)

