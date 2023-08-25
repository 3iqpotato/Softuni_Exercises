from collections import deque

my_string = deque(input().split())
all_colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
sec_colors = {'orange': ['red', 'yellow'], 'purple': ['red', 'blue'], 'green': ['yellow', 'blue']}
found_colors = []

while my_string:
    first_half = my_string.popleft()
    second_half = my_string.pop() if my_string else ''

    if f'{first_half}{second_half}' in all_colors:
        found_colors.append(f'{first_half}{second_half}')
    elif f'{second_half}{first_half}' in all_colors:
        found_colors.append(f'{second_half}{first_half}')
    else:
        first_half = first_half[:len(first_half) - 1]
        if first_half:
            my_string.insert(len(my_string) // 2, first_half)
        if second_half:
            second_half = second_half[:len(second_half) - 1]
            if second_half:
                my_string.insert(len(my_string) // 2, second_half)


for color in found_colors:
    if color in sec_colors.keys():
        if set(sec_colors[color]).issubset(found_colors):
            continue
        else:
            found_colors.remove(color)

print(found_colors)