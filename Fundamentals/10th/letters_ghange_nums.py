import string
lol_leters = string.ascii_lowercase
up_str = string.ascii_uppercase
full_num = 0
input_line = input().split()
for chars in input_line:
    first_letter = chars[0]
    last_letter = chars[-1]
    num = int(chars[1:-1])
    if first_letter.isupper():
        num /= up_str.index(first_letter) + 1
    else:
        num *= lol_leters.index(first_letter) + 1
    if last_letter.isupper():
        num -= up_str.index(last_letter) + 1
    else:
        num += lol_leters.index(last_letter) + 1
    full_num += num
print(f'{full_num:.2f}')