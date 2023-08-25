from collections import deque

def fill_the_box(a, b, c, *args):
    cub_area = a * b * c
    things = deque(args)
    while cub_area > 0:
        cube = things.popleft()
        if cube == 'Finish':
            break
        cub_area -= cube

    if cub_area > 0:
        return f"There is free space in the box. You could put {cub_area} more cubes."
    else:
        return f"No more free space! You have {abs(cub_area) + sum([el for el in things if el != 'Finish'])} more cubes."

print(fill_the_box(2, 8,
2, 2, 1, 7, 3, 1, 5,
"Finish"))
