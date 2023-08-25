num_lines = int(input())
hero_dict = {}
max_hp = 100
max_mp = 200
for hero in range(num_lines):
    input_line = input().split()
    name = input_line[0]
    hp = int(input_line[1])
    mp = int(input_line[2])
    hero_dict[name] = {'hp': hp, 'mp': mp}


while True:
    input_line = input().split(' - ')
    if "End" in input_line:
        break
    command = input_line[0]
    name = input_line[1]
    if command == 'CastSpell':
        mp_needed = int(input_line[2])
        spell_name = input_line[3]
        if hero_dict[name]['mp'] >= mp_needed:
            hero_dict[name]['mp'] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {hero_dict[name]['mp']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif command == 'TakeDamage':
        damage = int(input_line[2])
        attacker = input_line[3]
        hero_dict[name]['hp'] -= damage
        if hero_dict[name]['hp'] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {hero_dict[name]['hp']} HP left!")
        else:
            print(f"{name} has been killed by {attacker}!")
            hero_dict.pop(name)
    elif command == 'Recharge':
        amount = int(input_line[2])
        before_mp = hero_dict[name]['mp']
        hero_dict[name]['mp'] = min(hero_dict[name]['mp'] + amount, max_mp)
        print(f"{name} recharged for {hero_dict[name]['mp'] - before_mp} MP!")
    elif command == 'Heal':
        amount = int(input_line[2])
        before_hp = hero_dict[name]['hp']
        hero_dict[name]['hp'] = min(hero_dict[name]['hp'] + amount, max_hp)
        print(f"{name} healed for {hero_dict[name]['hp'] - before_hp} HP!")

for hero in hero_dict:
    print(hero)
    print(f"  HP: {hero_dict[hero]['hp']}")
    print(f"  MP: {hero_dict[hero]['mp']}")