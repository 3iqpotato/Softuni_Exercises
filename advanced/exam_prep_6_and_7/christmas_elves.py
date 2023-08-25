from collections import deque

elves_energy = deque(int(x) for x in input().split())
materials = deque(int(x) for x in input().split())
count = 0
toys = 0
energy = 0

while elves_energy and materials:
    elf = elves_energy.popleft()

    if elf < 5:
        continue

    count += 1
    material = materials[-1]
    current_toys = 0

    if count % 3 == 0:
        material *= 2
        current_toys += 1

    if elf >= material:
        elf -= material
        current_toys += 1

        if count % 5 == 0:
            current_toys = 0

        else:
            elf += 1

        materials.pop()
        energy += material

    else:
        elf *= 2
        current_toys = 0

    toys += current_toys
    elves_energy.append(elf)


print(f'Toys: {toys}')
print(f'Energy: {energy}')
if elves_energy:
    print(f'Elves left: {", ".join(str(x) for x in elves_energy)}')
if materials:
    print(f'Boxes left: {", ".join(str(x) for x in materials)}')


