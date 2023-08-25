monts = int(input())

water = 0
wifi = 0
elec = 0
other = 0
full_tax = 0
for i in range(monts):
    electricity = float(input())
    water += 20
    wifi += 15
    elec += electricity
    other += (35 + electricity) * 1.2
    full_tax = wifi + water + elec + other

average = full_tax / monts
print(f'Electricity: {elec:.2f} lv\n'
      f'Water: {water:.2f} lv\n'
      f'Internet: {wifi:.2f} lv\n'
      f'Other: {other:.2f} lv\n'
      f'Average: {average:.2f} lv')
