command = input().split('-')
exam_dict = {}
languages = {}
while "exam finished" not in command:
    username = command[0]
    if 'banned' in command:
        if username in exam_dict:
            exam_dict.pop(username)
            break
    language = command[1]
    points = int(command[2])
    if username not in exam_dict:
        exam_dict[username] = points
    else:
        if exam_dict[username] < points:
            exam_dict[username] = points
    if language not in languages:
        languages[language] = 1
    else:
        languages[language] += 1

    command = input().split('-')
print("Results:")
for student in exam_dict:
    print(f"{student} | {exam_dict[student]}")
print("Submissions:")
for l in languages:
    print(f"{l} - {languages[l]}")


# Peter-Java-84
# George-C#-84
# George-C#-70
# Katy-C#-94
# exam finished
# Peter-Java-91
# George-C#-84
# Katy-Java-90
# Katy-C#-50
# Katy-banned
# exam finished