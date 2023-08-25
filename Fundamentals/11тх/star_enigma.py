import re
attached_planets = []
destroyed_planets = []
star_pattern = r'[s|t|a|r|S|T|A|R]'
info_pattern = r'\@(?P<planet>[A-Za-z]+)[^@\-\!\>\:]*:(?P<population>\d+)[^@\-\!\>\:]*!(?P<type>[A|D])![^@\-\!\>\:]*->(?P<soligers>\d+)'
# info_pattern = r'@(?P<planet>[a-zA-Z]+)[^@\-\!\>\:]*:(?P<population>\d+)[^@\-\!\>\:]*!(?P<type>[A|D])![^@\-\!\>\:]*->(?P<soldiers>\d+)'
times = int(input())
for _ in range(times):
    input_line = input()
    # count_letters = len(re.findall(star_pattern, input_line))

    count_letters = input_line.upper().count("S") + input_line.upper().count("T") + input_line.upper().count("A") + input_line.upper().count("R")

    new_line = ''.join([chr(ord(x) - count_letters) for x in input_line])

    result = re.finditer(info_pattern, new_line)
    for res in result:
        res.groupdict()
        if res['type'] == 'A':
            attached_planets.append(res['planet'])
        elif res['type'] == 'D':
            destroyed_planets.append(res['planet'])
# attached_planets = attached_planets.sort()
# destroyed_planets = destroyed_planets.sort()
print(f'Attacked planets: {len(attached_planets)}')
for planet in sorted(attached_planets):
    print(f'-> {planet}')
print(f'Destroyed planets: {len(destroyed_planets)}')
for planet in sorted(destroyed_planets):
    print(f'-> {planet}')
