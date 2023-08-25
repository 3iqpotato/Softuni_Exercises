from collections import deque

customers_list = deque(int(x) for x in input().split(', '))
taxi_list = deque(int(x) for x in input().split(', '))
time = 0

while taxi_list:
    customer = customers_list.popleft()
    taxi = taxi_list.pop()
    if taxi >= customer:
        time += customer
    else:
        customers_list.appendleft(customer)

if customers_list:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(str(x) for x in customers_list)}')
else:
    print(f'All customers were driven to their destinations')
    print(f'Total time: {time} minutes')