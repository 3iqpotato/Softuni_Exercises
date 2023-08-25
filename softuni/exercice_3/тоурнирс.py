from math import floor

tournirs = int(input())
starting_pints = int(input())
wins = 0
points = 0
for i in range(tournirs):
    stage = input()
    if stage == 'W':
        points += 2000
        wins += 1
    elif stage == 'F':
        points += 1200
    elif stage == "SF":
        points += 720

total_points = points + starting_pints
average_points = floor(points / tournirs)
percent_wins = (wins / tournirs) * 100
print(f'Final points: {total_points:.0f}\n'
      f'Average points: {average_points:.0f}\n'
      f'{percent_wins:.2f}%')


