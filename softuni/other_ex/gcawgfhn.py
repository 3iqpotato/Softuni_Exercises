num1, delitel = [int(x) for x in input('Enter number and delitel separated by space:').split()]
intervals = [int(x) for x in input('Enter the four intervals separated by spaces:').split()]
if num1 % delitel == 0:
    print(f'Chisloto {num1} se deli na {delitel}')
    if intervals[0] < num1*num1 < intervals[1]:
        print(f'Kvadrata mu e vintervala ot {intervals[0]}-{intervals[1]}')
    else:
        print(f'Kvadrata mu ne e vintervala ot {intervals[0]}-{intervals[1]}')
else:
    print(f'Chisloto {num1} ne se deli na {delitel}')
    if intervals[2] < num1*2 < intervals[3]:
        print(f'udvoenata mu stoinost e v  intervala ot {intervals[2]}-{intervals[3]}')
    else:
        print(f'udvoenata mu stoinost ne e v intervala ot {intervals[2]}-{intervals[3]}')


name = input()
if name == 'Johnny':
    print(f'Hello, my love!')
else:
    print(f"Hello, {name}!")