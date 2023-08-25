import re

pattern = r'@#{1,}[A-Z][A-Za-z0-9]{4,}[A-Z]@#{1,}'
nums = r'\d'
lines = int(input())
for _ in range(lines):
    line = input()
    result = re.findall(pattern, line)
    if result:
        numso = re.findall(nums, *result)
        if len(numso) > 0:
            print(f'Product group: {"".join(numso)}')
        else:
            print(f'Product group: 00')
    else:
        print('Invalid barcode')