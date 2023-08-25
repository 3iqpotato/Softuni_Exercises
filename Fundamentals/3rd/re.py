lines = int(input())
is_open = False
has_open_brackets = False
balanced = True
last = ''
for _ in range(lines):
    line = input()
    if line not in ["(", ")"]:
        continue
    if line == '(':
        is_open = True
    if line == ')':
        is_open = False
    if has_open_brackets == is_open:
        balanced = False
    has_open_brackets = is_open


if balanced:
    print('BALANCED')
else:
    print("UNBALANCED")