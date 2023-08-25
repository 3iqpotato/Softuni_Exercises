seconds1 = int(input())
seconds2 = int(input())
seconds3 = int(input())

full_time = seconds1 + seconds3 + seconds2
minutes = full_time // 60
seconds = full_time % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')