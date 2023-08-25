
legendary_materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
junk = {}
ready = False
while not ready:
    input_data = input().lower().split()
    for index in range(0, len(input_data), 2):
        recourse = input_data[index + 1]
        count = int(input_data[index])
        if recourse in legendary_materials:
            legendary_materials[recourse] += count
            if legendary_materials[recourse] >= 250:
                legendary_materials[recourse] -= 250
                print(f'{legendary_items[recourse]} obtained!')
                ready = True
                break
        else:
            if recourse not in junk:
                junk[recourse] = count
            else:
                junk[recourse] += count


for material in legendary_materials:
    print(f'{material}: {legendary_materials[material]}')
for material in junk:
    print(f'{material}: {junk[material]}')



#
# 3 Motes 5 stones 5 Shards
# 6 leathers 255 fragments 7 Shards