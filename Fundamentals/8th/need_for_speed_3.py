num = int(input())
car_dict = {}
for _ in range(num):
    car_input = input().split('|')
    car = car_input[0]
    mileage = int(car_input[1])
    fuel = int(car_input[2])
    car_dict[car] = {'mileage': mileage, 'fuel': fuel}

while True:
    input_line = input().split(' : ')
    command = input_line[0]
    if command == 'Stop':
        break
    elif command == 'Drive':
        car = input_line[1]
        distance = int(input_line[2])
        fuel = int(input_line[3])
        if car_dict[car]['fuel'] < fuel:
            print("Not enough fuel to make that ride")
        else:
            car_dict[car]['fuel'] -= fuel
            car_dict[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if car_dict[car]['mileage'] >= 100000:
                print(f'Time to sell the {car}!')
                car_dict.pop(car)
    elif command == 'Refuel':
        car = input_line[1]
        fuel = int(input_line[2])
        before_fueling = car_dict[car]['fuel']
        car_dict[car]['fuel'] = min(car_dict[car]['fuel'] + fuel, 75)
        print(f'{car} refueled with {car_dict[car]["fuel"] - before_fueling} liters')
    elif command == 'Revert':
        car = input_line[1]
        kilometers = int(input_line[2])
        before_km = car_dict[car]['mileage']
        car_dict[car]['mileage'] -= kilometers
        if car_dict[car]['mileage'] < 10000:
            car_dict[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {before_km - car_dict[car]['mileage']} kilometers")

for car in car_dict:
    print(f"{car} -> Mileage: {car_dict[car]['mileage']} kms, Fuel in the tank: {car_dict[car]['fuel']} lt.")
# 3
# Audi A6|38000|62
# Mercedes CLS|11000|35
# Volkswagen Passat CC|45678|5
# Drive : Audi A6 : 543 : 47
# Drive : Mercedes CLS : 94 : 11
# Drive : Volkswagen Passat CC : 69 : 8
# Refuel : Audi A6 : 50
# Revert : Mercedes CLS : 500
# Revert : Audi A6 : 30000

# 4
# Lamborghini Veneno|11111|74
# Bugatti Veyron|12345|67
# Koenigsegg CCXR|67890|12
# Aston Martin Valkryie|99900|50
# Drive : Koenigsegg CCXR : 382 : 82
# Drive : Aston Martin Valkryie : 99 : 23
# Drive : Aston Martin Valkryie : 2 : 1
# Refuel : Lamborghini Veneno : 40
# Revert : Bugatti Veyron : 2000
# Stop