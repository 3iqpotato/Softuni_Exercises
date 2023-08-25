lenght_meters = float(input())
width_meters = float(input())

width_without_corridor = width_meters - 1
width_sm = width_without_corridor * 100
desks_in_width = width_sm // 70
lenght_sm = lenght_meters * 100
desks_in_lenght = lenght_sm // 120
number_desks = desks_in_lenght * desks_in_width - 3
print(number_desks)
