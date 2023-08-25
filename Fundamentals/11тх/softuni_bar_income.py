import re
total_income = 0
while True:
    line = input()
    if line == 'end of shift':
        break
    pattern = r'^\%(?P<name>[A-Z][a-z]+)%.*?<(?P<product>\w+)>.*?\|(?P<count>\d+)\|.*?(?P<price>\d+\.?\d*)\$'
    result = re.finditer(pattern, line)
    for res in result:
        res.groupdict()
        money = float(res['price']) * int(res['count'])
        total_income += money
        print(f"{res['name']}: {res['product']} - {money:.2f}")

print(f'Total income: {total_income:.2f}')