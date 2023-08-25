events = input().split('|')
my_energy = 100
my_money = 100
ended = False
for event in events:
    event_type = event.split('-')[0]
    if event_type == 'rest':
        energy = event.split('-')[1]
        gained_energy = 0
        for energy_gained in range(int(energy)):
            if my_energy == 100:
                break
            else:
                my_energy += 1
            gained_energy += 1
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {my_energy}.')

    elif event_type == 'order':
        earned_coins = event.split('-')[1]

        if my_energy >= 30:
            my_energy -= 30
            print(f'You earned {earned_coins} coins.')
            my_money += int(earned_coins)
        else:
            my_energy += 50
            print("You had to rest!")
    else:
        coins_cost = event.split('-')[1]
        item = event.split('-')[0]
        if my_money >= int(coins_cost):
            print(f"You bought {item}.")
            my_money -= int(coins_cost)
        else:
            print(f"Closed! Cannot afford {item}.")
            ended = True
            exit()




if not ended:
    print('Day completed!')
    print(f'Coins: {my_money}')
    print(f'Energy: {my_energy}')


