num_of_packs = int(input())

full_price = 0
full_tons = 0
car_tons = 0
truck_tons = 0
train_tons = 0

for i in range(1, num_of_packs + 1):
    pack_kg = int(input())

    if pack_kg <= 3:
        full_price += 200 * pack_kg
        full_tons += pack_kg
        car_tons += pack_kg
    elif 4 <= pack_kg <= 11:
        full_price += 175 * pack_kg
        full_tons += pack_kg
        truck_tons += pack_kg
    elif pack_kg >= 12:
        full_price += 120 * pack_kg
        full_tons += pack_kg
        train_tons += pack_kg
diff = full_price / full_tons
percent_car = car_tons / full_tons * 100
percent_truck = truck_tons / full_tons * 100
percent_train = train_tons / full_tons * 100


print(f'{diff:.2f}')
print(f'{percent_car:.2f}%')
print(f'{percent_truck:.2f}%')
print(f'{percent_train:.2f}%')