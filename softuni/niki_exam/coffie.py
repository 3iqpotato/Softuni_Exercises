coffie_list = input().split()

for _ in range(int(input())):
    command, *other = input().split()

    if command == 'Include':
        coffie_list.append(other[0])

    elif command == 'Remove':
        n = int(other[1])
        if len(coffie_list) >= n:
            if other[0] == 'last':
                for _ in range(n):
                    coffie_list.pop(-1)
            if other[0] == 'first':
                for _ in range(n):
                    coffie_list.pop(0)

    elif command == 'Prefer':
        c1 = int(other[0])
        c2 = int(other[1])
        if len(coffie_list) >= c1 and len(coffie_list) >= c2:
            coffie_list[c1], coffie_list[c2] = coffie_list[c2], coffie_list[c1]

    elif command == 'Reverse':
        coffie_list.reverse()

print('Coffees:')
print(" ".join(coffie_list))

# Arabica Liberica Charrieriana Magnistipula Robusta BulkCoffee StrongCoffee
# 5
# Include TurkishCoffee
# Remove first 2
# Remove last 1
# Prefer 3 1
# Reverse