game_times = int(input())

points = 0
points_9 = 0
points_19 = 0
points_29 = 0
points_39 = 0
points_50 = 0
invalid = 0

for i in range(game_times):
    nums = int(input())

    if 0 <= nums <= 9:
        points_9 += 1
        points += nums * 0.2
    elif 10 <= nums <= 19:
        points_19 += 1
        points += nums * 0.3
    elif 20 <= nums <= 29:
        points_29 += 1
        points += nums * 0.4
    elif 30 <= nums <= 39:
        points_39 += 1
        points += 50
    elif 40 <= nums <= 50:
        points_50 += 1
        points += 100
    else:
        invalid += 1
        points /= 2
percent_9 = (points_9 / game_times) * 100
percent_19 = points_19 / game_times * 100
percent_29 = points_29 / game_times * 100
percent_39 = points_39 / game_times * 100
percent_49 = points_50 / game_times * 100
percent_invalid = invalid / game_times * 100

print(f'{points:.2f}')
print(f'From 0 to 9: {percent_9:.2f}%')
print(f'From 10 to 19: {percent_19:.2f}%')
print(f'From 20 to 29: {percent_29:.2f}%')
print(f'From 30 to 39: {percent_39:.2f}%')
print(f'From 40 to 50: {percent_49:.2f}%')
print(f'Invalid numbers: {percent_invalid:.2f}%')