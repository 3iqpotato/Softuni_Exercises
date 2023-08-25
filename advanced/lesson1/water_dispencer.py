from collections import deque

liters = int(input())
name = input()
names = []
names = deque(names)
while name != 'Start':
    names.append(name)
    name = input()
command = input()
while 'End' not in command:
    if 'refill' in command:
        liters += int(command.split()[1])
    else:
        l = int(command)
        if liters >= l:
            liters -= l
            print(f'{names.popleft()} got water')

        else:
            print(f'{names.popleft()} must wait')
    command = input()

print(f'{liters} liters left')

# 10
# Peter
# George
# Amy
# Alice
# Start
# 2
# 3
# 3
# 3
# End
