items_to_buy = input().split('|')
budget = int(input())
old_price_list = []
price_of_things_bought = []
for item_and_price in items_to_buy:
    item = item_and_price.split('->')[0]
    price = float(item_and_price.split('->')[1])

    if item == "Clothes" and price <= 50:
        if budget >= price:
            budget -= price
            old_price_list.append(price)
            price = price * 1.4
            price_of_things_bought.append(price)
        else:
            continue
    if item == "Shoes" and price <= 35:
        if budget >= price:
            budget -= price
            old_price_list.append(price)
            price = price * 1.4
            price_of_things_bought.append(price)
        else:
            continue
    if item == "Accessories" and price <= 20.5:
        if budget >= price:
            budget -= price
            old_price_list.append(price)
            price = price * 1.4
            price_of_things_bought.append(price)
        else:
            continue
profit = sum(price_of_things_bought) - sum(old_price_list)

for i in price_of_things_bought:
    print(f'{i:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')
if sum(price_of_things_bought) + budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
#Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60