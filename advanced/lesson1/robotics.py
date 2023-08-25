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


while products:
    factory_time += timedelta(0, 1)
    free_robots = deque()

    for robot, times in robot_dict.items():
        if times[1] > 0:
            times[1] -= 1
        if times[1] == 0:
            free_robots.append(robot)

    if not free_robots:
        products.rotate(-1)
    else:
        first_free_bot = free_robots.popleft()
        robot_dict[first_free_bot][1] = robot_dict[first_free_bot][0]
        print(f'{first_free_bot} - {products.popleft()} [{factory_time.time()}]')




    #     if time[1] > 0:
    #         time[1] -= 1
    #
    #
    #     if time[1] == 0:
    #         free_robots.append(robot, time)
    #
    # if not free_robots:
    #     products.rotate(-1)
    # else:
    #     for _ in range(len(free_robots)):
    #
    #         robot = free_robots.popleft()
    #         print(f'{robot} - {products.popleft()} [{factory_time.time()}]')
    #         factory_time += timedelta(0, 1)
    #         robot_dict[robot][1] = robot_dict[robot][0]



