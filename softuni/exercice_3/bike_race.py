young_bikers = int(input())
seniors_bikers = int(input())
trail = input()

num_bikers = young_bikers + seniors_bikers
young_ticket = 0
old_ticket = 0
flag = True
if trail == 'trail':
    young_ticket = 5.5
    old_ticket = 7
elif trail == 'cross-country':
    young_ticket = 8
    old_ticket = 9.5
    if num_bikers >= 50:
        flag = False

elif trail == 'downhill':
    young_ticket = 12.25
    old_ticket = 13.75
elif trail == 'road':
    young_ticket = 20
    old_ticket = 21.5

young_tickets = young_bikers * young_ticket
old_tickets = old_ticket * seniors_bikers
full_price = old_tickets + young_tickets
if flag:
    full_price = full_price * 0.95
    print(f'{full_price:.2f}')
else:
    full_price = full_price * 0.75
    full_price = full_price * 0.95
    print(f'{full_price:.2f}')
