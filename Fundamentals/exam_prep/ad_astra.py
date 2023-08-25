from math import floor
import re
pattern = r'([\||#])(?P<item>[A-Za-z\ ]+)\1(?P<data>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d+)\1'
calories = 0
input_line = input()
result = re.finditer(pattern, input_line)
for res in result:
    res.groupdict()
    calories += int(res['calories'])

days = calories/2000

print(f'You have food to last you for: {floor(days):.0f} days!')
result = re.finditer(pattern, input_line)
for resa in result:
    resa.groupdict()
    print(f"Item: {resa['item']}, Best before: {resa['data']}, Nutrition: {resa['calories']}")