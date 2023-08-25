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
        if last == line:
            balanced = False
    if line == ')':
        is_open = False
        if line == last:
            balanced = False

    last = line
if is_open:
    balanced = False
if balanced:
    print('BALANCED')
else:
    print("UNBALANCED")