hours = int(input())
minutes = int(input())

new_minutes = minutes + 15

if new_minutes >= 60:
    new_minutes = new_minutes - 60
    hours = hours + 1

if hours > 23:
    hours = hours - 24
if new_minutes < 10:
    print(f'{hours}:0{new_minutes:.0f}')
else:
    print(f'{hours}:{new_minutes:.0f}')
