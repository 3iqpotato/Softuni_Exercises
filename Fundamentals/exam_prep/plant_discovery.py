class plant:
    def __init__(self, plant, rarity, rate=0):
        self.name = plant
        self.rarity = rarity
        self.rate = [rate]



list_plants = []
num = int(input())
for _ in range(num):
    plants = input().split('<->')
    plant_name = plants[0]
    plant_rarity = plants[1]
    list_plants.append(plant(plant_name, plant_rarity))

while True:
    input_line = input().split()
    if 'Exhibition' in input_line:
        break
    command = input_line[0]
    planto = input_line[1]
    if planto not in [list_plants[idx].__dict__['name'] for idx in range(len(list_plants))]:
        print('error')
    if command == 'Rate:':
        ratingo = input_line[3]
        p_name = [idx for idx in range(len(list_plants)) if list_plants[idx].__dict__['name'] == planto]
        idx = int(*p_name)
        list_plants[idx] = plant(list_plants[idx].__dict__['name'], list_plants[idx].__dict__['rarity'], int(ratingo))
        # print(list_plants[idx].__dict__)
    elif command == 'Update:':
        new_rarity = int(input_line[3])
        p_name = [idx for idx in range(len(list_plants)) if list_plants[idx].__dict__['name'] == planto]
        idx = int(*p_name)
        list_plants[idx] = plant(list_plants[idx].__dict__['name'], new_rarity, list_plants[idx].__dict__['rate'])
    elif command == 'Reset:':
        p_name = [idx for idx in range(len(list_plants)) if list_plants[idx].__dict__['name'] == planto]
        idx = int(*p_name)
        list_plants[idx] = plant(list_plants[idx].__dict__['name'], list_plants[idx].__dict__['rarity'])

print('Plants for the exhibition:')
for idx in range(len(list_plants)):
    print(f'- {list_plants[idx].__dict__["name"]}; Rarity: {list_plants[idx].__dict__["rarity"]}; Rating: {list_plants[idx].__dict__["rate"]:.2f}')