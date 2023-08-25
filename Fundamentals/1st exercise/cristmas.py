quantity = int(input())
days_till_cristmas = int(input())

money_spend = 0
points = 0
for days in range(1, days_till_cristmas + 1):
    if days % 11 == 0:
        quantity += 2
    if days % 2 == 0:
        money_spend += quantity * 2
        points += 5
    if days % 3 == 0:
        money_spend += quantity * 5 + quantity * 3
        points += 13
    if days % 5 == 0:
        money_spend += quantity * 15
        points += 17
    if days % 10 == 0:
        points -= 20
        money_spend += 23
    if days % 15 == 0:
        points += 30
if days_till_cristmas % 10 == 0:
    points -= 30

print(f'Total cost: {money_spend}')
print(f'Total spirit: {points}')