from collections import deque


def check_between(mix):
    for key, value in dict_items.items():
        if value[0] <= mix <= value[1]:
            return key


materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())


dict_items = {
    'Diamond Jewellery': [400, 499, 0],
    'Gemstone': [100,  199, 0],
    'Gold': [300, 399, 0],
    'Porcelain Sculpture': [200, 299, 0],


}

while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()

    mix_magic_and_material = magic + material

    if mix_magic_and_material < 100 and mix_magic_and_material % 2 == 0:
        mix_magic_and_material = material * 2 + magic * 3

    elif mix_magic_and_material < 100 and mix_magic_and_material % 2 == 1:
        mix_magic_and_material = material * 2 + magic * 2

    elif mix_magic_and_material > 499:
        mix_magic_and_material = material / 2 + magic / 2

    craft = check_between(mix_magic_and_material)

    if craft:
        dict_items[craft][2] += 1


if dict_items['Gemstone'][2] > 0 and dict_items['Porcelain Sculpture'][2] > 0:
    print('The wedding presents are made!')

elif dict_items['Gold'][2] > 0 and dict_items['Diamond Jewellery'][2] > 0:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')
if materials:
    print(f'Materials left: {", ".join(str(x) for x in materials)}')
if magic_levels:
    print(f'Magic left: {", ".join(str(x) for x in magic_levels)}')
for key, value in dict_items.items():
    if value[2] > 0:
        print(f'{key}: {value[2]}')