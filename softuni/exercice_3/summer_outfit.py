degree = int(input())
part_of_day = input()

outfit = ''
shoes = ''
if part_of_day == 'Morning':
    if 10 <= degree <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif degree <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degree > 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'

elif part_of_day == 'Afternoon':
    if 10 <= degree <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degree <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif degree > 24:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

elif part_of_day == "Evening":
    if 10 <= degree <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degree <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degree > 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degree} degrees, get your {outfit} and {shoes}.")