from math import floor
free_days = int(input())

work_days = 365 - free_days

play_time = (work_days * 63) + free_days * 127
difference = abs(30000 - play_time)
difference_in_hours = floor(difference / 60)
diff_in_min = floor(difference - difference_in_hours * 60)
if play_time >= 30000:
    print("Tom will run away")
    print(f'{difference_in_hours:.0f} hours and {diff_in_min:.0f} minutes more for play')

else:
    print("Tom sleeps well")
    print(f'{difference_in_hours} hours and {diff_in_min} minutes less for play')