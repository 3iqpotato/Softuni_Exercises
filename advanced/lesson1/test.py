from collections import deque
from datetime import datetime, timedelta

robot_dict = {}
products = deque()

robots = [x.split('-') for x in [x for x in input().split(';')]]

for rob in robots:
    robot_dict[rob[0]] = [int(rob[1]), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")

while True:
    product = input()
    if product == 'End':
        break
    else:
        products.append(product)

free_robots = deque()






while products:
    factory_time += timedelta(seconds=1)

    free_robots = deque()
    for name, curr_list in robot_dict.items():
        if curr_list[1] != 0:
            robot_dict[name][1] -= 1
        if curr_list[1] == 0:
            free_robots.append(name)

    if not free_robots:
        products.rotate(-1)
        continue

    first_free_robot = free_robots.popleft()
    robot_dict[first_free_robot][1] = robot_dict[first_free_robot][0]

    print(f"{first_free_robot} - {products.popleft()} [{factory_time.strftime('%H:%M:%S')}]")