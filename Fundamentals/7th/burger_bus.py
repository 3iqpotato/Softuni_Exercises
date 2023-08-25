number_cities = int(input())
total_profit = 0
for city in range(1, number_cities + 1):
    name = input()
    money_made = float(input())
    expences = float(input())
    if city % 5 == 0:
        money_made *= 0.9
    elif city % 3 == 0:
        expences += expences * 0.5
    money_made -= expences
    total_profit += money_made

    print(f'In {name} Burger Bus earned {money_made:.2f} leva.')
print(f"Burger Bus total profit: {total_profit:.2f} leva.")