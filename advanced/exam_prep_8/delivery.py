from collections import deque

pizza_orders = deque(int(x) for x in input().split(', '))
employees_capacity = deque(int(x) for x in input().split(', '))

pizzas_made = 0

while pizza_orders and employees_capacity:
    pizza = pizza_orders.popleft()

    if 0 >= pizza or pizza > 10:
        continue

    worker = employees_capacity.pop()

    if pizza > worker:
        pizza -= worker
        pizzas_made += worker
        pizza_orders.appendleft(pizza)
    else:
        pizzas_made += pizza


if employees_capacity:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas_made}')
    print(f'Employees: {", ".join(str(x) for x in employees_capacity)}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(str(x) for x in pizza_orders)}')