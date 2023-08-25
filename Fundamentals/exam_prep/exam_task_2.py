import re
pattern = r'\|(?P<name>[A-Z]{4,})\|:#(?P<pass>[A-Za-z]+\ [A-Za-z]+)#'
num = int(input())
for _ in range(num):
    input_line = input()
    result = re.findall(pattern, input_line)
    if result:
        res = ' '.join(result[0]).split()
        name = res.pop(0)
        password = ' '.join(res)
        print(f"{name}, The {password}")
        print(f'>> Strength: {len(name)}')
        print(f'>> Armor: {len(password)}')

    else:
        print("Access denied!")
