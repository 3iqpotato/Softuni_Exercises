budget = float(input())
category = input()
people = int(input())

price = 0
if category == 'VIP':
    price = 499.99
elif category == 'Normal':
    price = 249.99

if people <= 4:
    budget = budget * 0.25
elif people <= 9:
    budget = budget * 0.4
elif people <= 24:
    budget = budget * 0.5
elif people <= 49:
    budget = budget * 0.6
elif people >= 50:
    budget = budget * 0.75

oll_price = people * price
diff = abs(oll_price - budget)
if budget >= oll_price:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')