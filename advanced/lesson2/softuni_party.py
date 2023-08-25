n = int(input())
ticket = set()


for _ in range(n):
    id = input()
    ticket.add(id)

id = input()
while id != 'END':
    if id in ticket:
        ticket.remove(id)
    id = input()

print(len(ticket))
print('\n'.join(sorted(ticket)))
