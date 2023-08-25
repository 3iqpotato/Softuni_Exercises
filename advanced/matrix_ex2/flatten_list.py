line = input().split('|')
new_line = []
for el in line:
    new_line.extend([el.split()] if el.split() != [] else el.split())
[print(*el, end=' ') for el in new_line[::-1]]