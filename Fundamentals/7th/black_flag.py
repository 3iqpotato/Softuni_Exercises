days = int(input())
daily_plunger = int(input())
expected_plunger = float(input())
plungers = 0
for day in range(1, days+1):
    plungers += daily_plunger
    if day % 3 == 0:
        plungers += daily_plunger * 0.5
    if day % 5 == 0:
        plungers *= 0.7
if plungers >= expected_plunger:
    print(f"Ahoy! {plungers:.2f} plunder gained.")
else:
    percent = plungers / expected_plunger * 100
    print\
        (f'Collected only {percent:.2f}% of the plunder.')