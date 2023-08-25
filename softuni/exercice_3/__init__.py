type_cinema = input()
rows = int(input())
colons = int(input())

price = 0
seats = rows * colons
if type_cinema == 'Premiere':
    price = 12
elif type_cinema == 'Normal':
    price = 7.5
elif type_cinema == 'Discount':
    price = 5

money = price * seats
print(f'{money:.2f} leva')