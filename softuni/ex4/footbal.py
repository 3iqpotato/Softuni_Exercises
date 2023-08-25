capacity = int(input())
fans = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
for _ in range(fans):
    sector = input()
    if sector == 'A':
        sector_a += 1
    elif sector == 'B':
        sector_b += 1
    elif sector == 'V':
        sector_v += 1
    elif sector == 'G':
        sector_g += 1


a_per = sector_a / fans * 100
b_per = sector_b / fans * 100
v_per = sector_v / fans * 100
g_per = sector_g / fans * 100
per = fans / capacity * 100
print(f'{a_per:.2f}%')
print(f'{b_per:.2f}%')
print(f'{v_per:.2f}%')
print(f'{g_per:.2f}%')
print(f'{per:.2f}%')

