money_saved = float(input())
year_of_death = int(input())

age = 18
money_spend = 0

for year in range(1800, year_of_death + 1):
    if year % 2 == 0:
        money_spend += 12000
    else:
        money_spend += 12000 + 50 * age
    age += 1

diff = abs(money_spend - money_saved)

if money_saved >= money_spend:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')
else:
    print(f'He will need {diff:.2f} dollars to survive.')