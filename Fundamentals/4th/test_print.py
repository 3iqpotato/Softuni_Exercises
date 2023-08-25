times = int(input())
calculated_min = 0
calco_sec = 0
for song in range(times):
    min = int(input())
    sec = float(input())

    calculated_min += min
    calco_sec += sec
    if calco_sec >= 60:
        calculated_min += 1
        calco_sec -= 60

print(f'{calculated_min}\n'
      f'{calco_sec}')