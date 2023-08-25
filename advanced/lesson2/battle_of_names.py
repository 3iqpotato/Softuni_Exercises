import math

n = int(input())
evens = set()
odds = set()

for row in range(1, n+1):
    name = input()
    sum_asci = 0

    for cr in name:
        sum_asci += ord(cr)

    res = math.floor(sum_asci / row)
    if res % 2 == 0:
        evens.add(res)
    else:
        odds.add(res)

if sum(evens) == sum(odds):
    pr = evens | odds
    print(pr)
    print(*pr, sep=', ')

elif sum(evens) < sum(odds):
    pr = odds.difference(evens)
    print(*pr, sep=', ')
else:
    pr = evens.symmetric_difference(odds)
    print(*pr, sep=', ')
