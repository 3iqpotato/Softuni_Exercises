from collections import deque

green_light_time = int(input())
free_window_time = int(input())

cars_list = deque()
cars_passed = 0


while True:
    input_Line = input()
    if input_Line == 'END':
        print('Everyone is safe.')
        print(f'{cars_passed} total cars passed the crossroads.')
        break
    elif input_Line == 'green':
        # if cars_list:
        #     car = cars_list.popleft()
        #     car_copy = car
        # else:
        #     continue
        # for sek in range(green_light_time):
        #     if car:
        #
        #     if cars_list:
        #         car = cars_list.popleft()
        #         car_copy = car

        if cars_list:
            car = cars_list.popleft()
            car_copy = car
            cars_passed += 1
        else:
            continue
        for sek in range(green_light_time):
            if car:
                car = car[1:]
            else:
                if cars_list:
                    car = cars_list.popleft()
                    car_copy = car
                    car = car[1:]
                    cars_passed += 1
                else:
                    break
        if car:
            for sek in range(free_window_time):
                if car:
                    car = car[1:]
                else:
                    break
            else:
                if car:
                    print('A crash happened!')
                    print(f'{car_copy} was hit at {car[:1]}.')
                    break
        else:
            continue
        # cars_passed += 1
    else:
        cars_list.append(input_Line)

