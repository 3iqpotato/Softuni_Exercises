heroes_dict = {}
while True:
    input_line = input().split()
    if 'End' in input_line:
        break
    command = input_line[0]
    name = input_line[1]
    if command == 'Enroll':
        if name in heroes_dict:
            print(f"{name} is already enrolled.")
        else:
            heroes_dict[name] = []
    elif command == 'Learn':
        spell = input_line[2]
        if name not in heroes_dict:
            print(f"{name} doesn't exist.")
        elif spell in heroes_dict[name]:
            print(f"{name} has already learnt {spell}.")
        else:
            heroes_dict[name].append(spell)
    elif command == 'Unlearn':
        spell = input_line[2]
        if name not in heroes_dict:
            print(f"{name} doesn't exist.")
        elif spell not in heroes_dict[name]:
            print(f"{name} doesn't know {spell}.")
        else:
            heroes_dict[name].remove(spell)

print('Heroes:')
for hero in heroes_dict:
    print(f'== {hero}: {", ".join(heroes_dict[hero])}')