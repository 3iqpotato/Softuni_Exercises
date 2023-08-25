from collections import deque
from math import floor

input_str = deque(input().split())
idx = 0

functions = {
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: floor(x / y),
}


while idx <= len(input_str):
    ch = input_str[idx]
    if not ch.isdigit():
        if ch in '-+*/':
            input_str.remove(ch)
            for _ in range(idx - 1):
                input_str.appendleft(functions[ch](int(input_str.popleft()), int(input_str.popleft())))
            idx = 1

    idx += 1

print(*input_str)



