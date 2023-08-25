lili_age = int(input())
washing_machine_price = float(input())
toys_price = int(input())

money_per_year = 0
money = 0
toys = 0
brother_steal = 0

for year in range(1, lili_age + 1):
    if year % 2 == 0:
        money_per_year += 10
        money += money_per_year
        brother_steal += 1
    else:
        toys += 1
toys_money = toys * toys_price
total_money = (toys_money + money) - brother_steal
diff = abs(total_money - washing_machine_price)
if washing_machine_price <= total_money:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
