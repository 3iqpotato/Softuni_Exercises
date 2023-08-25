while True:
    num = float(input())
    if num < 0:
        print('Negative number!')
        break
    else:
        num = num * 2
        print(f'Result: {num:.2f}')