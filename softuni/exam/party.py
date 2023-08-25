party_cost = float(input())
love_letter = int(input())
rose = int(input())
key = int(input())
caricature = int(input())
lucks = int(input())

count = love_letter + rose + key + caricature + lucks

price = love_letter * 0.6 + rose * 7.2 + key * 3.60 + caricature * 18.2 + lucks * 22
if count >= 25:
    price *= 0.65

price *= 0.9
diff = abs(party_cost - price)
if price >= party_cost:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
