budget = float(input())
number_of_statists = int(input())
price_of_clotes = float(input())

decor_price = (budget * 0.1)

if number_of_statists > 150:
    price_of_clotes = price_of_clotes - price_of_clotes * 0.1

price_of_all_clotes = price_of_clotes * number_of_statists
diff = abs(budget - (price_of_all_clotes + decor_price))
if price_of_all_clotes + decor_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")

