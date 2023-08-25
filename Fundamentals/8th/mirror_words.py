import re
input_line = input()
pattern = r'(#|@)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
result = re.findall(pattern, input_line)

list = []
for res in result:
    if res[1] == res[2][::-1]:
        list.append(f'{res[1]} <=> {res[2]}')
        # print(f'{res[1]} <=> {res[2]}', sep=', ')

if len(result) == 0:
    print(f'No word pairs found!')
else:
    print(f'{len(result)} word pairs found!')
if len(list) == 0:
    print("No mirror words!")
else:
    print('The mirror words are:')
    print(', '.join(list))