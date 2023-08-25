list_rooms = input().split("|")
health = 100
money = 0
days = 0
for room in list_rooms:
    days += 1
    room = room.split()
    command = room[0]
    number = int(room[1])
    if command == "potion":
        healed = 0
        for hp in range(number):
            if health == 100:
                break
            else:
                healed += 1
                health += 1
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")
    elif command == 'chest':
        money += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")

        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {days}")
            exit()

print("You've made it!")
print(f'Bitcoins: {money}')
print(f'Health: {health}')