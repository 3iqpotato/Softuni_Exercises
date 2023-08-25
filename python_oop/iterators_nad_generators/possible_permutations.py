from itertools import permutations

def possible_permutations(something):
    for p in permutations(something):
        yield list(p)





[print(n) for n in possible_permutations([1, 2, 3])]