from collections import deque


def flights(*args):
    args = deque(args)
    dict_flights = {}
    while args:
        destination = args.popleft()
        if destination == 'Finish':
            break
        else:
            passagers = int(args.popleft())
            if destination in dict_flights:
                dict_flights[destination] += passagers
            else:
                dict_flights[destination] = passagers

    return dict_flights





print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))