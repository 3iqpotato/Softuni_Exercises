command = input()

colection = {}
while command != 'End':
    com, *names = command.split()
    if com == 'Enroll':
        name = names[0]
        if name in colection:
            print(f"{name} is already enrolled.")
        else:
            colection[name] = []

    if com == 'Learn':
        name = names[0]
        spell = names[1]
        if name not in colection:
            print(f"{name} doesn't exist.")

        elif spell in colection[name]:
            print(f"{name} has already learnt {spell}.")

        else:
            colection[name].append(spell)

    if com == 'Unlearn':
        name = names[0]
        spell = names[1]
        if name not in colection:
            print(f"{name} doesn't exist.")

        elif spell not in colection[name]:
            print(f"{name} doesn't know {spell}.")

        else:
            colection[name].remove(spell)
    command = input()

print('Heroes:')
for hero, spells in colection.items():
    print(f'== {hero}: {", ".join(spells)}')

