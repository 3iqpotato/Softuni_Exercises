import re
list_results = []
full_price = 0
input_line = input()
pattern = r'^>>(?P<item>\w*)<<(?P<price>\d*\.?\d*)!(?P<quantity>\d*)\b'
print('Bought furniture:')
while input_line != 'Purchase':
    result = re.finditer(pattern, input_line)
    for res in result:
        res.groupdict()
        print(res['item'])
        full_price += float(res['price']) * float(res['quantity'])

    input_line = input()
print(f'Total money spend: {full_price:.2f}')