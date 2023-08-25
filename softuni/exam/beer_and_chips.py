import math
name = input()
budget = float(input())
num_beer_cans = int(input())
num_chips = int(input())

all_beers_price = num_beer_cans * 1.2
chips_price = (all_beers_price * 0.45)
all_chips_price = math.ceil(chips_price * num_chips)
all_price = all_chips_price + all_beers_price

diff = abs(all_price - budget)
if budget >= all_price:
    print(f"{name} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name} needs {diff:.2f} more leva!")