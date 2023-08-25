def valid_ticket(ticketo):
    valid = True

    if len(ticketo) != 20:
        valid = False
        return valid

    return valid
def is_winning(ticketo):
    simbols = ['@', '#', '$', '^']
    valid = False
    simbol = ''
    for simb in simbols:
        if simb in ticketo:
            valid = True
            simbol = simb
    if not valid:
        return valid

    firts_half = ticketo[:10]
    last_half = ticketo[10:]
    count = 0
    end_count = 0
    for idx in range(len(firts_half)):
        if firts_half[idx] == simbol:
            count += 1
            if count >= 6:
                end_count = count
        else:
            count = 0
    count2 = 0
    end_count2 = 0
    for idx in range(len(firts_half)):
        if last_half[idx] == simbol:
            count2 += 1
            if count2 >= 6:
                end_count2 = count2
        else:
            count2 = 0
    if end_count < 6 or end_count2 < 6:
        return False
    return valid

def times(ticketo):
    simbols = ['@', '#', '$', '^']
    simbol = ''
    for simb in simbols:
        if simb in ticketo:
            simbol = simb
    firts_half = ticketo[:10]
    last_half = ticketo[10:]
    count = 0
    end_count = 0
    for idx in range(len(firts_half)):
        if firts_half[idx] == simbol:
            count += 1
            if count >= 6:
                end_count = count
        else:
            count = 0
    count2 = 0
    end_count2 = 0
    for idx in range(len(firts_half)):
        if last_half[idx] == simbol:
            count2 += 1
            if count2 >= 6:
                end_count2 = count2
        else:
            count2 = 0
    return [min(end_count, end_count2), simbol]


tickets = input().replace(" ", '')
tickets = tickets.split(',')
for ticket in tickets:
    if valid_ticket(ticket):
        if is_winning(ticket):
            times_repeated = times(ticket)
            if times_repeated[0] == 10:
                print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
            else:
                print(f'ticket "{ticket}" - {times_repeated[0]}{times_repeated[1]}')
        else:
            print(f'ticket "{ticket}" - no match')

    else:
        print("invalid ticket")