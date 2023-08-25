cars = int(input())
parking = set()

for _ in range(cars):
    command, number = input().split(', ')
    if command == 'IN':
        parking.add(number)
    elif command == "OUT":
        if number in parking:
            parking.remove(number)

if parking:
    print('\n'.join(parking))
else:
    print('Parking Lot is Empty')
#
# 10
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# IN, CA9999TT
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU

# 4
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# OUT, CA1234TA
