budget = int(input())
season = input()
num_people = int(input())

rent = 0
if season == 'Spring':
    rent = 3000
    if num_people <= 6:
        rent = rent * 0.9
    elif num_people <= 11:
        rent = rent * 0.85
    else:
        rent = rent * 0.75
if season == "Summer" or season == "Autumn":
    rent = 4200
    if num_people <= 6:
        rent = rent * 0.9
    elif num_people <= 11:
        rent = rent * 0.85
    else:
        rent = rent * 0.75
if season == 'Winter':
    rent = 2600
    if num_people <= 6:
        rent = rent * 0.9
    elif num_people <= 11:
        rent = rent * 0.85
    else:
        rent = rent * 0.75

if num_people % 2 == 0 and season != 'Autumn':
    rent = rent * 0.95

diff = abs(budget - rent)

if budget >= rent:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')