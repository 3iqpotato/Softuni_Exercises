def even_odd(*args):
    com = args[-1]
    if com == 'even':
        res = [el for el in args[:-1] if el % 2 == 0]

    else:
        res = [el for el in args[:-1] if el % 2 != 0]

    return res
print(even_odd(1, 2, 3, 4, 5, 6, "even"))