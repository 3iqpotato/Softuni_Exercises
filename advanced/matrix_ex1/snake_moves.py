from collections import deque

rows, cols = [int(x) for x in input().split()]
word = input()
copy_word = deque()
for row in range(rows):
    while len(copy_word) < cols:
        copy_word.extend(list(word))

    if row % 2 == 0:
        pr = [copy_word.popleft() for _ in range(cols)]
        print(''.join(pr))
    else:
        print(*[copy_word.popleft() for _ in range(cols)][::-1], sep='')
