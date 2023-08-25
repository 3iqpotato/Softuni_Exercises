import re
pattern = r'(\=|\/)(?P<location>[A-Z][A-Za-z]{2,})\1'
input_line = input()
result = re.findall(pattern, input_line)
points = 0
destinations = []
for city in result:
    points += len(city[1])
    destinations.append(city[1])

print(f'Destinations: {", ".join(destinations)}')
print(f'Travel Points: {points}')