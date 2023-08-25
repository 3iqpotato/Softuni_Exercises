from collections import deque

materials = deque(int(x) for x in input().split())
magics = deque(int(x) for x in input().split())
crafted = []

toys_dict = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

while materials and magics:
    material = materials.pop() if magics[0] or materials[-1] == 0 else 0
    magic = magics.popleft() if material or magics[0] == 0 else 0

    if magic and material:
        product = magic * material
        if product < 0:
            materials.append(material + magic)
        elif product in toys_dict.keys():
            crafted.append(toys_dict[product])
        else:
            materials.append(material + 15)

if {'Doll', 'Wooden train'}.issubset(set(crafted)) or {'Teddy bear', 'Bicycle'}.issubset(set(crafted)):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
if magics:
    print(f"Magic left: {', '.join(str(x) for x in magics)}")

for doll in sorted(set(crafted)):
    print(f"{doll}: {crafted.count(doll)}")
