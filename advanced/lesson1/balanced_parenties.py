input_line = input()
copy_line = input_line

opened = []

for chr in copy_line:
    if chr in '({[':
        opened.append(chr)
    else:
        if not opened:
            print('NO')
            break

        if f'{opened.pop()}{chr}' not in '(){}[]':
            print('NO')
            break

else:
    print('YES')