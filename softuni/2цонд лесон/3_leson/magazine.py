fruit = input()
day = input()
number = float(input())

flag = True
price = 0
if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    if fruit == 'banana':
        price = number * 2.5
    elif fruit == 'apple':
        price = number * 1.2
    elif fruit == 'orange':
        price = number * 0.85
    elif fruit == 'grapefruit':
        price = number * 1.45
    elif fruit == 'kiwi':
        price = number * 2.7
    elif fruit == 'pineapple':
        price = number * 5.5
    elif fruit == 'grapes':
        price = number * 3.85
    else:
        flag = False
elif day in ['Saturday', 'Sunday']:
    if fruit == 'banana':
        price = number * 2.7
    elif fruit == 'apple':
        price = number * 1.25
    elif fruit == 'orange':
        price = number * 0.9
    elif fruit == 'grapefruit':
        price = number * 1.6
    elif fruit == 'kiwi':
        price = number * 3
    elif fruit == 'pineapple':
        price = number * 5.6
    elif fruit == 'grapes':
        price = number * 4.2
    else:
        flag = False
else:
    flag = False
if flag:
    print(f'{price:.2f}')
else:
    print('error')
