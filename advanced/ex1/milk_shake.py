from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
cups_of_milk = deque(int(x) for x in input().split(', '))
milk_shakes = 0


while milk_shakes < 5 and chocolates and cups_of_milk:
    choko = chocolates.pop() if cups_of_milk[0] > 0 or chocolates[-1] <= 0 else 0
    cup = cups_of_milk.popleft() if cups_of_milk[0] <= 0 or choko > 0 else 0

    if not cup or not choko:
        continue

    if choko == cup:
        milk_shakes += 1
    else:
        cups_of_milk.append(cup)
        chocolates.append(choko - 5)

if milk_shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f'Chocolate: {", ".join(str(x) for x in chocolates) if chocolates else "empty"}')
print(f'Milk: {", ".join(str(x) for x in cups_of_milk) if cups_of_milk else "empty"}')


