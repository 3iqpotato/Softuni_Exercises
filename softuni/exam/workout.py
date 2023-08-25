from math import ceil
days = int(input())
kilometers_fist_day = float(input())
kilometers_run = kilometers_fist_day
all_km = kilometers_run
for _ in range(days):

    percent = int(input())
    kilometers_run += kilometers_run * percent / 100
    all_km += kilometers_run


km_left = abs(1000 - all_km)
km_left = ceil(km_left)
if all_km >= 1000:
    print(f"You've done a great job running {km_left} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {km_left} more kilometers")
