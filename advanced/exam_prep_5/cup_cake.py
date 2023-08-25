def stock_availability(list_products, *args):
    if args[0] == 'delivery':
        for box in args[1:]:
            list_products.append(box)

    elif args[0] == 'sell':
        if len(args) > 1:
            if str(args[1]).isdigit():
                for _ in range(args[1]):
                    list_products.pop(0)

            else:
                for box in args[1:]:
                    if box in list_products:
                        c = list_products.count(box)
                        for _ in range(c):
                            list_products.remove(box)
        else:
            list_products.pop(0)

    return list_products







print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
