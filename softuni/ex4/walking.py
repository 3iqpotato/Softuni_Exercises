steps = input()
all_steps = 0
while all_steps < 10000:
    if steps == 'Going home':
        break
    steps = int(steps)
    all_steps += steps
    if all_steps >= 10000:
        break

    steps = input()
if steps == 'Going home':
    steps_home = int(input())
    all_steps += steps_home
diff = abs(10000 - all_steps)
if all_steps < 10000:
    print(f'{diff} more steps to reach goal.')
else:
    print(f'Goal reached! Good job!\n{diff} steps over the goal!')