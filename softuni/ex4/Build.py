floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    for room in range(rooms):
        if floor == floors:
            pr = f'L{floor}{room}'
            print(pr, end=' ')

        else:
            if floor % 2 == 0:
                pr = f'O{floor}{room}'
                print(pr, end=' ')

            else:
                pr = f'A{floor}{room}'
                print(pr, end=' ')
    print()




