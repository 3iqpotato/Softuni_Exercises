import math

car_times = input().split()
first_car_times = math.floor(len(car_times) / 2)
first_car = 0
second_car = 0
for time in range(len(car_times)):
    if time < first_car_times:
        first_car += int(car_times[time])
        if car_times[time] == '0':
            first_car *= 0.8

        second_car += int(car_times[-time + (-1)])
        if car_times[-time + (-1)] == '0':
            second_car *= 0.8

if first_car < second_car:
    print(f'The winner is left with total time: {first_car:.1f}')
else:
    print(f'The winner is right with total time: {second_car:.1f}')
