material = input()
materials_dict = {}
while material != 'stop':
    quantity = int(input())
    if material in materials_dict:
        materials_dict[material] += quantity
    else:
        materials_dict[material] = quantity
    material = input()

for material in materials_dict:
    print(f"{material} -> {materials_dict[material]}")


