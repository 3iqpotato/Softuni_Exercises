number_rooms = int(input())
free_chairs = 0
flag = True
for room in range(1, number_rooms + 1):
    chairs_and_vizitors = input().split()
    chairs = chairs_and_vizitors[0]
    visitors = int(chairs_and_vizitors[1])
    if len(chairs) >= visitors:
        free_chairs += len(chairs) - visitors

    else:
        chairs_needed = visitors - len(chairs)
        print(f"{chairs_needed} more chairs needed in room {room}")
        flag = False

if flag:
    print(f"Game On, {free_chairs} free chairs left")
