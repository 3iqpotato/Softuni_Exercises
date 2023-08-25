num = int(input())

tree = (num // 100)
two = (num // 10) % 10
one = (num // 1) % 10
for first in range(1, one + 1):
    for second in range(1, two + 1):
        for third in range(1, tree + 1):
            answer = third * second * first
            print(f'{first} * {second} * {third} = {answer};')

