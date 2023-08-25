team = input()
type_souvenir = input()
num = int(input())
price = 0
flag = True
flag1 = True
if team == 'Argentina':
    if type_souvenir == 'flags':
        price = num * 3.25
    elif type_souvenir == 'caps':
        price = num * 7.2
    elif type_souvenir == 'posters':
        price = num * 5.1
    elif type_souvenir == 'stickers':
        price = num * 1.25
    else:
        flag = False
elif team == 'Brazil':
    if type_souvenir == 'flags':
        price = num * 4.2
    elif type_souvenir == 'caps':
        price = num * 8.5
    elif type_souvenir == 'posters':
        price = num * 5.35
    elif type_souvenir == 'stickers':
        price = num * 1.2
    else:
        flag = False
elif team == 'Croatia':
    if type_souvenir == 'flags':
        price = num * 2.75
    elif type_souvenir == 'caps':
        price = num * 6.9
    elif type_souvenir == 'posters':
        price = num * 4.95
    elif type_souvenir == 'stickers':
        price = num * 1.1
    else:
        flag = False
elif team == 'Denmark':
    if type_souvenir == 'flags':
        price = num * 3.1
    elif type_souvenir == 'caps':
        price = num * 6.5
    elif type_souvenir == 'posters':
        price = num * 4.8
    elif type_souvenir == 'stickers':
        price = num * 0.9
    else:
        flag = False
else:
    flag1 = False

if flag and flag1:
    print(f"Pepi bought {num} {type_souvenir} of {team} for {price:.2f} lv.")
else:
    if flag:
        print("Invalid country!")
    elif flag1:
        print("Invalid stock!")
