from collections import deque

num_pumps = int(input())
stations_and_liters = deque([[int(x) for x in input().split()] for _ in range(num_pumps)])
idx = 0
fuel = 0
stations_and_liters_copy = stations_and_liters.copy()

while stations_and_liters_copy:
    station = stations_and_liters_copy.popleft()
    fuel += station[0]
    km = station[1]
    if fuel < km:
        fuel = 0
        idx += 1
        stations_and_liters.rotate(-1)
        stations_and_liters_copy = stations_and_liters.copy()
    else:
        fuel -= km

print(idx)
