full_penciq = 0
flag = True
penciq = ''
destination = ''
while flag:
    destination = input()
    if destination == "End":
        flag = False
        break
    trip_price = float(input())
    penciq = input()
    if penciq == 'End':
        flag = False
        break


    while flag:
        if penciq == 'End':
            flag = False
            break
        if destination == "End":
            flag = False
            break
        else:
            penciq = float(penciq)
            full_penciq += penciq

        if full_penciq >= trip_price:
            print(f'Going to {destination}!')
            full_penciq = 0
            break
        penciq = input()
