from math import floor
from math import ceil
area_loze = int(input())
grape_pre_m = float(input())
liters_vine = int(input())
workers = int(input())
all_grape = area_loze * grape_pre_m
grape_for_vine = (all_grape * 0.40) / 2.5

vine_left = floor(abs(grape_for_vine - liters_vine))
vine_for_worker = ceil(vine_left / workers)
if grape_for_vine >= liters_vine:
    grape_for_vine = ceil(all_grape * 0.40) / 2.5
    print(f'Good harvest this year! Total wine: {grape_for_vine:.0f} liters.')
    print(f'{vine_left} liters left -> {vine_for_worker} liters per person.')
else:
    print(f'It will be a tough winter! More {vine_left:.0f} liters wine needed.')

