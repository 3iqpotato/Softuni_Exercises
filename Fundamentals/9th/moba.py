players_dict = {}
while True:
    command = input()
    if command == 'Season end':
        break
    if 'vs' in command:
        player1, player2 = command.split(' vs ')
        if player1 in players_dict and player2 in players_dict:
            if any(x in players_dict[player1].keys() for x in players_dict[player2].keys()):
                player1_stats = sum(players_dict[player1].values())
                player2_stats = sum(players_dict[player2].values())
                if player1_stats == player2_stats:
                    continue
                elif player1_stats > player2_stats:
                    del players_dict[player2]
                else:
                    del players_dict[player1]
            continue
        else:
            continue

    name, position, skill = command.split(' -> ')
    skill = int(skill)
    if name not in players_dict:
        players_dict[name] = {position: skill}
    else:
        if position not in players_dict[name]:
            players_dict[name].update({position: skill})
        elif skill > players_dict[name][position]:
            players_dict[name][position] = skill
# print(players_dict)
players_points = {}
for player in players_dict:
    player_pts = sum(players_dict[player].values())
    players_points[player] = player_pts

for key, value in sorted(players_points.items(), key=lambda x: (-x[1], x[0])):
    print(f"{key}: {value} skill")
    positions_points = {}
    for position in players_dict[key]:
        positions_points[position] = players_dict[key][position]

    for key, value in sorted(positions_points.items(), key=lambda x: (-x[1], x[0])):
        print(f'- {key} <::> {value}')
# Peter -> Adc -> 400
# George -> Jungle -> 300
# Simon -> Mid -> 200
# Simon -> Support -> 250
# Season end
# Peter -> Adc -> 400
# Bush -> Tank -> 150
# Frank -> Mid -> 200
# Frank -> Support -> 250
# Frank -> Tank -> 250
# Peter vs Frank
# Frank vs Bush
# Frank vs Hide
# Season end