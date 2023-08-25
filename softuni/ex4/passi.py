control_num = int(input())
count = 0
password = ''
maybe_pass = ''
for a in range(1, 10):
    for b in range(1, 10):
        if a >= b:
            continue
        for c in range(1, 10):
            for d in range(1, 10):
                if c <= d:
                    continue
                else:
                    test = a * b + c * d
                    if test == control_num:
                        maybe_pass = f'{a}{b}{c}{d}'
                        print(maybe_pass, end=' ')
                        count += 1
                        if count == 4:
                            password = f'{a}{b}{c}{d}'


if count < 4:
    print()
    print('No!')
else:
    print()
    print(f'Password: {password}')
