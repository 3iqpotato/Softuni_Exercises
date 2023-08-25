lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
broken_helmets = 0
lost_game_count = 0
broken_swords = 0
broken_shields = 0
broken_armor = 0
for loss in range(1, lost_fights + 1):
    if loss % 2 == 0:
        broken_helmets += 1
    if loss % 3 == 0:
        broken_swords += 1
    if loss % 6 == 0:
        broken_shields += 1
    if loss % 12 == 0:
        broken_armor += 1

money_spend = broken_shields * shield_price + broken_swords * sword_price + broken_armor * armor_price + \
    broken_helmets * helmet_price

print(f'Gladiator expenses: {money_spend:.2f} aureus')