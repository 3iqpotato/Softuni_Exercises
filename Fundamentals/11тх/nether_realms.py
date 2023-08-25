import re

nums_pattern = r'(?:\+|-)?[0-9]+(?:\.[0-9]+)?'
letters_pattern = r'[^\d\+\-\*\/\.]'
simbols_patter = r'[*\/]'

demons_list = input().split(',')
demons_dict = {}
for demon in demons_list:
    demon = demon.strip()
    letters = re.findall(letters_pattern, demon)
    health = sum(ord(x) for x in letters)
    nums_in_name = re.findall(nums_pattern, demon)
    base_damage = 0
    for num in nums_in_name:
        base_damage += float(num)
    simbols = re.findall(simbols_patter, demon)
    for simbol in simbols:
        if simbol == '*':
            base_damage *= 2
        elif simbol == '/':
            base_damage /= 2
    demons_dict[demon] = [health, base_damage]
for demon in sorted(demons_dict):
    print(f'{demon} - {demons_dict[demon][0]} health, {demons_dict[demon][1]:.2f} damage')