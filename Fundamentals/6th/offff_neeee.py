times = int(input())
seconds = 0
mins = 0
hours = 0
for i in range(times):

    min = int(input())
    sec = int(input())
    seconds += sec
    mins += min
    if seconds >= 60:
        mins += 1
        seconds -= 60
    if mins >= 60:
        hours += 1
        mins -= 60
print(f'{hours}:{mins}:{seconds}')



