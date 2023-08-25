dict_plants = {}
num = int(input())
for _ in range(num):
    plants = input().split('<->')
    plant_name = plants[0]
    plant_rarity = plants[1]
    dict_plants[plant_name] = {'rarity': plant_rarity, 'rating': []}

while True:
    input_line = input().split()
    if 'Exhibition' in input_line:
        break
    command = input_line[0]
    plant = input_line[1]
    if plant not in dict_plants:
        print('error')
    elif command == 'Rate:':
        rating = int(input_line[3])
        dict_plants[plant]['rating'].append(rating)

    elif command == 'Update:':
        new_rarity = (input_line[3])
        dict_plants[plant]['rarity'] = new_rarity
    elif command == 'Reset:':
        dict_plants[plant]['rating'] = []

print('Plants for the exhibition:')
for plant in dict_plants:
    if len(dict_plants[plant]['rating']) > 0:
        print(f"- {plant}; Rarity: {dict_plants[plant]['rarity']}; Rating: {sum(dict_plants[plant]['rating'])/ len(dict_plants[plant]['rating']):.2f}")
    else:
        print(f"- {plant}; Rarity: {dict_plants[plant]['rarity']}; Rating: 0.00")