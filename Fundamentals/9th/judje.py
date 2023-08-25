contest_dict = {}
while True:
    line = input()
    if line == 'no more time':
        break
    user, contest, points = line.split(' -> ')
    points = int(points)
    if contest not in contest_dict:
        contest_dict[contest] = {user: points}
    elif user not in contest_dict[contest]:
        contest_dict[contest].update({user: points})
    elif user in contest_dict[contest]:
        if points > contest_dict[contest][user]:
            contest_dict[contest][user] = points
for contest in contest_dict:
    print(f"{contest}: {len(contest_dict[contest])} participants")
    sorted_by_pts = contest_dict[contest]
    for pos, (key, value) in enumerate(sorted(sorted_by_pts.items(), key=lambda x: (-x[1], x[0])), 1):
        print(f"{pos}. {key} <::> {value}")
    # sorted_by_points = sorted(sorted_by_pts.items(), key=lambda x: (-x[1], x, 1))
    # print(sorted_by_pts)
    # sorted_by_pts.reverse()
    count = 0
    # for user in sorted_by_pts:
    #     count += 1
    #     # print(sorted_by_pts)
    #     print(f'{count}. {user} <::> {contest_dict[contest][user]}')
dict_by_points = {}
for contest in contest_dict:
    for user in contest_dict[contest]:
        if user not in dict_by_points:
            dict_by_points[user] = int(contest_dict[contest][user])
        else:
            dict_by_points[user] += int(contest_dict[contest][user])


# sorted_by_pts = sorted(dict_by_points, key=lambda x: (dict_by_points[x], x))
# sorted_by_pts.reverse()
print('Individual standings:')
count = 0
for position, (key, value) in enumerate(sorted(dict_by_points.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{position}. {key} -> {value}")
# for user in sorted_by_pts:
#     count += 1
#     print(f"{count}. {user} -> {dict_by_points[user]}")

# Peter -> Algo -> 400
# George -> Algo -> 300
# gogo -> Algo -> 300
# Simo -> Algo -> 200
# Peter -> DS -> 150
# Mariya -> DS -> 600
# no more time
