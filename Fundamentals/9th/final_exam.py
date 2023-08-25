import sys


def get_key(val):
    for key, value in users_points[users].items():
        if val == value:
            return key

    return "key doesn't exist"


all_contest_and_pass = {}
while True:
    contest_and_pass = input()
    if contest_and_pass == "end of contests":
        break
    contest_and_pass = contest_and_pass.split(':')
    contest = contest_and_pass[0]
    password = contest_and_pass[1]
    all_contest_and_pass[contest] = password

users_points = {}
while True:
    input_command = input()
    if input_command == 'end of submissions':
        break
    input_command = input_command.split('=>')
    course = input_command[0]
    password = input_command[1]
    user = input_command[2]
    points = int(input_command[3])
    if course in all_contest_and_pass and password == all_contest_and_pass[course]:
        if user not in users_points:
            users_points[user] = {course: points}
            continue
        if course not in users_points[user]:
            users_points[user][course] = points
        else:
            if points > users_points[user][course]:
                users_points[user][course] = points
max_points = -sys.maxsize
best_user = ''
for user in users_points:
    score = 0
    for course in users_points[user]:
        points = users_points[user][course]
        score += points
    if score > max_points:
        max_points = score
        best_user = user
print(f"Best candidate is {best_user} with total {max_points} points.")
users_ordered = sorted(users_points)

print('Ranking:')
for users in users_ordered:
    print(users)
    sorted_points = sorted(users_points[users].values())
    sorted_points.reverse()
    for pts in sorted_points:
        print(f"#  {get_key(pts)} -> {pts}")

        # print(f"#  {pr_course} -> {sorted_points[0]}")

# Part One Interview:success
# JS Fundamentals:fundExam
# C# Fundamentals:fundPass
# Algorithms:fun
# end of contests
# C# Fundamentals=>fundPass=>Tanya=>350
# Algorithms=>fun=>Tanya=>380
# Part One Interview=>success=>Nikola=>120
# Java Basics Exam=>wrong_pass=>Teo=>400
# Part One Interview=>success=>Tanya=>220
# OOP Advanced=>password123=>Kay=>231
# C# Fundamentals=>fundPass=>Tanya=>250
# C# Fundamentals=>fundPass=>Nikola=>200
# JS Fundamentals=>fundExam=>Tanya=>400
# end of submissions