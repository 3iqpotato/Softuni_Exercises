def dragons_filler(current_type, dragon_name, dragons_damage, dragons_health, dragons_armor):
    dragons_damage = int(dragons_damage)
    dragons_health = int(dragons_health)
    dragons_armor = int(dragons_armor)
    dragons_by_names[dragon_name, current_type] = {'damage': dragons_damage, 'health': dragons_health,
                                                   'armor': dragons_armor}


dragons_by_names = {}
num_dragons = int(input())
for dragon in range(num_dragons):
    dragon_stats = input().split()
    type_dragon = dragon_stats[0]
    name = dragon_stats[1]
    damage = dragon_stats[2]
    health = dragon_stats[3]
    armor = dragon_stats[4]
    if damage == 'null':
        damage = 45
    if health == 'null':
        health = 250
    if armor == 'null':
        armor = 10
    dragons_filler(type_dragon, name, damage, health, armor)
# dict(sorted(dragons_by_names.keys()))
# print(dragons_by_names)
dragons_by_type = {}
for name, type_dragon in dragons_by_names:
    if type_dragon not in dragons_by_type:
        dragons_by_type[type_dragon] = {name: dragons_by_names[name, type_dragon]}
    else:
        dragons_by_type[type_dragon].update({name: dragons_by_names[name, type_dragon]})

for type_dragon in dragons_by_type:
    damage_full = 0
    health_full = 0
    armor_full = 0
    dragons = 0

    for dragon in dragons_by_type[type_dragon]:
        dragons += 1
        stats = dragons_by_type[type_dragon][dragon]
        damage, health, armor = stats.values()
        damage_full += damage
        health_full += health
        armor_full += armor
    av_damage = damage_full / dragons
    av_health = health_full / dragons
    av_armor = armor_full / dragons
    print(f'{type_dragon}::({av_damage:.2f}/{av_health:.2f}/{av_armor:.2f})')
    # print(sorted(dragons_by_type[type_dragon]))
    for dragonoid in sorted(dragons_by_type[type_dragon]):
        stats = dragons_by_type[type_dragon][dragonoid]
        damage, health, armor = stats.values()
        print(f'-{dragonoid} -> damage: {damage}, health: {health}, armor: {armor}')





# 5
# Red Bazgargal 100 2500 25
# Black Dargonax 200 3500 18
# Red Obsidion 220 2200 35
# Blue Kerizsa 60 2100 20
# Blue Algordox 65 1800 50
# 4
# Gold Zzazx null 1000 10
# Gold Traxx 500 null 0
# Gold Xaarxx 250 1000 null
# Gold Ardrax 100 1055 50