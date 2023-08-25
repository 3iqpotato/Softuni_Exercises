data = input()
items_price = {}
items_quantity = {}
while data != 'buy':
    data = data.split()
    item = data[0]
    price = float(data[1])
    quantity = int(data[2])
    items_price[item] = price
    if item in items_quantity:
        items_quantity[item] += quantity
    else:
        items_quantity[item] = quantity
    data = input()

for item in items_price:
    print(f"{item} -> {items_price[item] * items_quantity[item]:.2f}")