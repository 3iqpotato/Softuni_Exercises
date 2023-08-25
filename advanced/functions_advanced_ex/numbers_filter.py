def even_odd_filter(**kwargs):

    for com, nums in kwargs.items():

        if com == 'even':
            kwargs[com] = [x for x in nums if x % 2 == 0]
        else:
            kwargs[com] = [x for x in nums if x % 2 != 0]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))

print(even_odd_filter(
 odd=[1, 2, 3, 4, 10, 5],
 even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
