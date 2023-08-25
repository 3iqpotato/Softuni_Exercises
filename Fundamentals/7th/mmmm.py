top_height = 8848
start_height = 5364
days = 1
command = input()
while command != 'END':
    if command == 'Yes':
        days += 1
    if days > 5:
        break
    meters = int(input())
    start_height += meters
    if start_height >= top_height:
        break

    command = input()

if start_height >= top_height and days < 6:
    print(f'Goal reached for {days} days!')
else:
    print('Failed!')
    print(start_height)

