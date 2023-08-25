cities_dict = {}
while True:
    input_line = input().split('||')
    if 'Sail' in input_line:
        break
    citi = input_line[0]
    population = int(input_line[1])
    gold = int(input_line[2])
    if citi not in cities_dict:
        cities_dict[citi] = [population, gold]
    else:
        cities_dict[citi][0] += population
        cities_dict[citi][1] += gold
while True:
    input_line = input().split('=>')
    if 'End' in input_line:
        break
    command = input_line[0]
    if command == 'Prosper':
        town = input_line[1]
        gold = int(input_line[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_dict[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities_dict[town][1]} gold.")

    if command == 'Plunder':
        town = input_line[1]
        people = int(input_line[2])
        gold = int(input_line[3])
        cities_dict[town][0] -= people
        cities_dict[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities_dict[town][0] <= 0 or cities_dict[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del cities_dict[town]
if cities_dict:
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
    for town in cities_dict:
        print(f"{town} -> Population: {cities_dict[town][0]} citizens, Gold: {cities_dict[town][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

# Nassau||95000||1000
# San Juan||930000||1250
# Campeche||270000||690
# Port Royal||320000||1000
# Port Royal||100000||2000
# Sail
# Prosper=>Port Royal=>-200
# Plunder=>Nassau=>94000=>750
# Plunder=>Nassau=>1000=>150
# Plunder=>Campeche=>150000=>690
# End
# def rec(a, b):
#     if a == 0:
#         return b
#     else:
#         return rec(a -1, a + b)
# print(rec(8, 12))