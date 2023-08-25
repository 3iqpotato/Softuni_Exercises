first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

functions = {
    'Add': lambda i, x: [first.add(y) if i == 'First' else second.add(y) for y in x],
    'Remove': lambda i, x: [first.discard(y) if i == 'First' else second.discard(y) for y in x],
    'Check': lambda i, x: print(first.issubset(second) or second.issubset(first)),

}

for _ in range(int(input())):
    command, move, *digits = input().split()

    functions[command](move, (int(x) for x in digits))
print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')



# 1 2 3 4 5
# 1 2 3
# 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset