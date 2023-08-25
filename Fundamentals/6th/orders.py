def calculation(drink, quantoty):
    resut = 0
    if drink == "water":
        resut = quantoty
    elif drink == "coffee":
        resut = quantoty * 1.5
    elif drink == "coke":
        resut = quantoty * 1.4
    elif drink == "snacks":
        resut = quantoty * 2
    return resut


item = input()
quantity = int(input())
result = calculation(item, quantity)
print(f'{result:.2f}')

