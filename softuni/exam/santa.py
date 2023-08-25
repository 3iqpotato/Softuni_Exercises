days = int(input())
type_room = input()
grade = input()
nights = days - 1
price = 0
if type_room == 'room for one person':
    price = nights * 18

elif type_room == 'apartment':
    price = nights * 25
    if days < 10:
        price *= 0.7
    elif 10 < days < 15:
        price *= 0.65
    elif days > 15:
        price *= 0.5

elif type_room == 'president apartment':
    price = nights * 35
    if days < 10:
        price *= 0.9
    elif 10 < days < 15:
        price *= 0.85
    elif days > 15:
        price *= 0.8

if grade == 'positive':
    price += price * 0.25
elif grade == 'negative':
    price -= price * 0.1

print(f'{price:.2f}')

