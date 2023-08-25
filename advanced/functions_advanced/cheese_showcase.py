def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    res = ''
    for chees_name, quantity in sorted_cheeses:
        quantity = sorted(quantity, reverse=True)
        res += chees_name + '\n'
        for q in quantity:
         res += str(q) + '\n'

    return res


print(
 sorting_cheeses(
 Parmesan=[102, 120, 135],
 Camembert=[100, 100, 105, 500, 430],
 Mozzarella=[50, 125],
 )
)
