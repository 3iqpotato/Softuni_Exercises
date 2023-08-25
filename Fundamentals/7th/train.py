def add(people):
    wagons[-1] += people



wagons_num = int(input())
wagons = [0] * wagons_num
command = input().split()
while 'End' not in command:
    if 'add' in command:
        add(int(command[1]))
    if 'insert' in command:
        people = int(command[2])
        index = int(command[1])
        wagons[index] += people
    if 'leave' in command:
        people = int(command[2])
        index = int(command[1])
        wagons[index] -= people
    command = input().split()

print(wagons)