goal = int(input())

money = 0
type_haircut = input()
while type_haircut != 'closed':
    if type_haircut == 'haircut':
        type_hair = input()
        if type_hair == 'mens':
            money += 15
        elif type_hair == 'ladies':
            money += 20
        elif type_hair == 'kids':
            money += 10
    if type_haircut == 'color':
        type_hair = input()
        if type_hair == 'touch up':
            money += 20
        elif type_hair == 'full color':
            money += 30
    if money >= goal:
        break
    type_haircut = input()

if money >= goal:
    print(f'You have reached your target for the day!\nEarned money: {money}lv.')
else:
    diff = goal - money
    print(f'Target not reached! You need {diff}lv. more.\nEarned money: {money}lv.')
