pack_weight = float(input())
type_service = input()
distance = int(input())
price = 0
price_per_km = 0

if pack_weight < 1:
    price_per_km = 0.03
elif pack_weight < 10:
    price_per_km = 0.05
elif pack_weight < 40:
    price_per_km = 0.1
elif pack_weight < 90:
    price_per_km = 0.15
elif pack_weight < 150:
    price_per_km = 0.2
if type_service == "standard":
    price = distance * price_per_km
if type_service == 'express':
    price = distance * price_per_km
    if pack_weight < 1:
        price_per_km *= 0.8
    elif pack_weight < 10:
        price_per_km *= 0.4
    elif pack_weight < 40:
        price_per_km *= 0.05
    elif pack_weight < 90:
        price_per_km *= 0.02
    elif pack_weight < 150:
        price_per_km *= 0.01
    over_price_per_km = pack_weight * price_per_km
    full_overprice = distance * over_price_per_km
    price += full_overprice

print(f'The delivery of your shipment with weight of {pack_weight:.3f} kg. would cost {price:.2f} lv.')