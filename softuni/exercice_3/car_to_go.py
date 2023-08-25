budget = float(input())
season = input()
car = ''
class_car = ''
if budget <= 100:
    class_car = 'Economy class'
    if season == 'Summer':
        car = 'Cabrio'
        budget = budget * 0.35
    elif season == 'Winter':
        car = 'Jeep'
        budget = budget * 0.65
elif budget <= 500:
    class_car = 'Compact class'
    if season == 'Summer':
        car = 'Cabrio'
        budget = budget * 0.45
    elif season == 'Winter':
        car = 'Jeep'
        budget = budget * 0.8
elif budget > 500:
    class_car = 'Luxury class'
    car = 'Jeep'
    budget = budget * 0.9

print(class_car)
print(f'{car} - {budget:.2f}')

