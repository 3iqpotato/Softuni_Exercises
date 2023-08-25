values = tuple(float(x) for x in input().split())
pr = []
for el in values:
    if el in pr:
        continue
    else:
        print(f'{el:.1f} - {values.count(el)} times')
        pr.append(el)