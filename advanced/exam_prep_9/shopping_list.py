def shopping_list(budget, **kwargs):
    if budget < 100:
        return f'You do not have enough budget.'

    basket = []

    for key, values in kwargs.items():
        price = values[0] * values[1]
        if price > budget:
            continue
        else:
            budget -= price
            basket.append(f'You bought {key} for {price:.2f} leva.')
            if len(basket) == 5:
                break
    return '\n'.join(basket)







print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
