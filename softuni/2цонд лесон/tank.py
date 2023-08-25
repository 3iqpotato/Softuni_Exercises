fuel_tipe = input()
liters_fuel = float(input())

if fuel_tipe == 'Gas':
    if liters_fuel >= 25:
        print('You have enough gas.')
    else:
        print('Fill your tank with gas!')
elif fuel_tipe == "Diesel":
    if liters_fuel >= 25:
        print('You have enough diesel.')
    else:
        print('Fill your tank with diesel!')
elif fuel_tipe == 'Gasoline':
    if liters_fuel >= 25:
        print('You have enough gasoline.')
    else:
        print('Fill your tank with gasoline!')
else:
    print('Invalid fuel!')
