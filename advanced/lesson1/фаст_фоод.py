from collections import deque

food = int(input())
clients_order = deque([int(x) for x in input().split()])
print(max(clients_order))

for order in clients_order.copy():
    if food >= order:
        food -= order
        clients_order.popleft()
    else:
        print(f'Orders left: {" ".join(str(x) for x in clients_order)}')
        break
else:
    print('Orders complete')