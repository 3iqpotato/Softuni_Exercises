text = input()
digits = ''
letters = ''
others = ''
for idx in text:
    if idx.isdigit():
        digits += idx
    elif idx.isalpha():
        letters += idx
    else:
        others += idx

print(digits)
print(letters)
print(others)