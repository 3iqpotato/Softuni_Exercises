cards = input().split()

team_a_removed = []
team_b_removed = []
removed_a = 0
removed_b = 0

for card in cards:
    team = card[0]
    number = int(card[2:])



    if team == 'A':
        if number not in team_a_removed:
            team_a_removed.append(number)
            removed_a +=1
        else:
            continue
    else:
        if number not in team_b_removed:
            team_b_removed.append(number)
            removed_b += 1
        else:
            continue
    if removed_a > 4 or removed_b > 4:
        break


print(f'Team A - {11 - removed_a}; Team B - {11 - removed_b}')
if removed_a > 4 or removed_b > 4:
    print('Game was terminated')
