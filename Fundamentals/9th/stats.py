command = input()
stock_dic = {}
while command != 'statistics':
    food, quantity = command.split(': ')
    if food in stock_dic:
        stock_dic[food] += int(quantity)
    else:
        stock_dic[food] = int(quantity)
    command = input()

print(f'Products in stock:')
for product in stock_dic:
    print(f"- {product}: {stock_dic[product]}")
print(f'Total Products: {len(stock_dic)}')
print(f"Total Quantity: {sum(stock_dic.values())}")

