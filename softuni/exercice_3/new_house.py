type_flower = input()
num_flowers = int(input())
budget = int(input())

price = 0
if type_flower == 'Roses':
    price = num_flowers * 5
    if num_flowers > 80:
        price = price * 0.9
elif type_flower == 'Dahlias':
    price = num_flowers * 3.8
    if num_flowers > 90:
        price = price * 0.85
elif type_flower == 'Tulips':
    price = num_flowers * 2.8
    if num_flowers > 80:
        price = price * 0.85
elif type_flower == 'Narcissus':
    price = num_flowers * 3
    if num_flowers < 120:
        price = price * 1.15
elif type_flower == 'Gladiolus':
    price = num_flowers * 2.5
    if num_flowers < 80:
        price = price * 1.20

diff = abs(budget - price)

if budget >= price:
    print(f'Hey, you have a great garden with {num_flowers} {type_flower} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')
