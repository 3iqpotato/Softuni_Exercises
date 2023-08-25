from collections import deque

bees = deque(int(x) for x in input().split())
honeys = deque(int(x) for x in input().split())
simbols = deque(input().split())
total_honey = 0

functions = {
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
}

while bees and honeys:
    bee = bees.popleft()
    honey = honeys.pop()

    if honey > bee:
        total_honey += abs(functions[simbols.popleft()](bee, honey))
    elif bee > honey:
        bees.appendleft(bee)

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if honeys:
    print(f"Nectar left: {', '.join(str(x) for x in honeys)}")


