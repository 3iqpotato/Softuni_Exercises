type_fuel = input()
liters_fuel = float(input())
club_card = input()
fuel_price = 0
if type_fuel == 'Gas':
    fuel_price = liters_fuel * 0.93
    if club_card == 'Yes':
        fuel_price = fuel_price - (liters_fuel * 0.08)
        if 20 <= liters_fuel <= 25:
            fuel_price = fuel_price - (fuel_price * 0.08)

        elif liters_fuel > 25:
            fuel_price = fuel_price - (fuel_price * 0.1)
    elif club_card == 'No':
        if 20 <= liters_fuel <= 25:
            fuel_price = fuel_price - (fuel_price * 0.08)
        elif liters_fuel > 25:
            fuel_price = fuel_price - (fuel_price * 0.1)

elif type_fuel == 'Diesel':
    fuel_price = liters_fuel * 2.33
    if club_card == 'Yes':
        fuel_price = fuel_price - (liters_fuel * 0.12)
        if 20 <= liters_fuel <= 25:
            fuel_price = fuel_price - (fuel_price * 0.08)

        elif liters_fuel > 25:
            fuel_price = fuel_price - (fuel_price * 0.1)
    elif club_card == 'No':
        if 20 <= liters_fuel <= 25:
            fuel_price = fuel_price - (fuel_price * 0.08)

        elif liters_fuel > 25:
            fuel_price = fuel_price - (fuel_price * 0.1)
elif type_fuel == 'Gasoline':
    fuel_price = liters_fuel * 2.22
    if club_card == 'Yes':
        fuel_price = fuel_price - (liters_fuel * 0.18)
        if 20 <= liters_fuel <= 25:
            fuel_price = fuel_price - (fuel_price * 0.08)

        elif liters_fuel > 25:
            fuel_price = fuel_price - (fuel_price * 0.1)
    elif club_card == 'No':
        if 20 <= liters_fuel <= 25:
            fuel_price = fuel_price - (fuel_price * 0.08)

        elif liters_fuel > 25:
            fuel_price = fuel_price - (fuel_price * 0.1)

print(f'{fuel_price:.2f} lv.')
