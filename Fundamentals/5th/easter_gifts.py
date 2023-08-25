gifts = input().split()

while True:
    command_gifts = input()
    if command_gifts == 'No Money':
        break
    command = command_gifts.split()[0]

    if command == "OutOfStock":
        gift = command_gifts.split()[1]
        for idx in range(len(gifts)):
            if gifts[idx] == gift:
                gifts[idx] = 'None'

    if command == 'Required':
        gift = command_gifts.split()[1]
        idx = command_gifts.split()[2]
        idx = int(idx)
        if idx in range(len(gifts)):
            gifts[int(idx)] = gift
    if command == 'JustInCase':
        gift = command_gifts.split()[1]
        gifts[-1] = gift

for idx in gifts:
    if idx == "None":
        continue
    else:
        print(idx, end=' ')
