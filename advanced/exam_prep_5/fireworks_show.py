from collections import deque

fireworks_effects = deque(int(x) for x in input().split(', '))
explosives_power = deque(int(x) for x in input().split(', '))

firework_dict = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}
win = False

while fireworks_effects and explosives_power:

    fire_eff = fireworks_effects.popleft()
    if fire_eff <= 0:
        continue

    explosive_power = explosives_power.pop()
    if explosive_power <= 0:
        fireworks_effects.appendleft(fire_eff)
        continue

    if fire_eff and explosive_power:
        fire_sum = fire_eff + explosive_power

        if fire_sum % 3 == 0 and fire_sum % 5 == 0:
            firework_dict['Crossette Fireworks'] += 1

        elif fire_sum % 5 == 0:
            firework_dict['Willow Fireworks'] += 1

        elif fire_sum % 3 == 0:
            firework_dict['Palm Fireworks'] += 1

        else:
            fire_eff -= 1
            fireworks_effects.append(fire_eff)
            explosives_power.append(explosive_power)

        c = [el for el in firework_dict.values() if el >= 3]
        if len(c) > 2:
            win = True
            break


if win:
    print("Congrats! You made the perfect firework show!")

else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    print(f'Firework Effects left: {", ".join(str(el) for el in fireworks_effects)}')

if explosives_power:
    print(f'Explosive Power left: {", ".join(str(el) for el in explosives_power)}')

for key, values in firework_dict.items():
    print(f'{key}: {values}')
