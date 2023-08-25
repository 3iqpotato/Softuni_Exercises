trip_price = float(input())
money_saved = float(input())
curent_money = money_saved
days = 0
days_spend = 0
flag = False
while curent_money < trip_price:
    proces = input()
    sum_money = float(input())
    days += 1

    if proces == 'save':
        curent_money += sum_money

        days_spend = 0
    elif proces == 'spend':
        curent_money -= sum_money
        days_spend += 1
        if curent_money < 0:
            curent_money = 0

        if days_spend == 5:
            flag = True
            break
if flag:
    print(f"You can't save the money.\n{days}")
else:
    print(f'You saved the money for {days} days.')
