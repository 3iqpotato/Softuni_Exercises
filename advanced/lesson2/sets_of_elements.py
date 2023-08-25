m, n = [int(x) for x in input().split()]
set_1 = set(input() for _ in range(m))
set_2 = set(input() for _ in range(n))
print(*(set_1.intersection(set_2)), sep='\n')