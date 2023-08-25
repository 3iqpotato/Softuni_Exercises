import re
pattern_for_letters = r'[A-Za-z]'
pattern_for_digits = r'\d'
people_dict = {}
participants = input().split(', ')
for nam in participants:
    people_dict[nam] = 0
while True:
    line = input()
    if line == 'end of race':
        break

    result_name = re.findall(pattern_for_letters, line)
    name = ''.join(result_name)
    result_score = re.findall(pattern_for_digits, line)
    score = sum(int(x) for x in result_score)
    if name in people_dict:
        people_dict[name] += score
count = 0
for position, (key, value) in enumerate(sorted(people_dict.items(), key=lambda x: (-x[1]))):
    if count == 3:
        break
    elif count == 0:
        if key:
            print(f'1st place: {key}')
    elif count == 1:
        if key:
            print(f'2nd place: {key}')
    else:
        if key:
            print(f'3rd place: {key}')
    count += 1
# positions = {1: '1st', 2: '2nd', 3: '3rd'}
# sorted_dict = sorted(people_dict.items(), key=lambda x: -x[1])
#
# for num, (person_name, km) in enumerate(sorted_dict[:3], 1):
#     print(f"{positions[num]} place: {person_name}")