from collections import deque


cups = deque(int(el) for el in input().split())
bottles = [int(el) for el in input().split()]
wasted_water = 0

while cups and bottles:
    cup = cups.popleft()
    while cup > 0:
        cup -= bottles.pop()
    wasted_water += abs(cup)

if cups:
    print(f'Cups: {" ".join(str(el) for el in cups)}')
    print(f'Wasted litters of water: {wasted_water}')
else:
    bottles.reverse()
    print(f'Bottles: {" ".join(str(el) for el in bottles)}')
    print(f'Wasted litters of water: {wasted_water}')


