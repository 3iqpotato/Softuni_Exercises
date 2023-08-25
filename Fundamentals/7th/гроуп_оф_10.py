from math import ceil
numbers = [int(x) for x in input().split(", ")]

groups = ceil(max(numbers) / 10)
for x in range(1, groups + 1):
    group = []
    for year in numbers:
        if x*10 - 10 < year <= x*10:
            group.append(year)
    print(f"Group of {x*10}'s: {group}")