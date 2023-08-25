text = input()
points = 0
for ch in text:
    if ch == 'a':
        points += 1
    elif ch == 'e':
        points += 2
    elif ch == 'i':
        points += 3
    elif ch == 'o':
        points += 4
    elif ch == 'u':
        points += 5
print(points)
