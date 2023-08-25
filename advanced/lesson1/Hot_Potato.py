from collections import deque

names = input().split()
times = int(input())
names = deque(names)
while len(names) > 1:
    names.rotate(-times+1)
    print(f'Removed {names.popleft()}')

print(f'Last is {names[0]}')

# Tracy Emily Daniel
# 2