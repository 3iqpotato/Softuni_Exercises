height = int(input())
lenght = int(input())
winght = int(input())

cum_m_apertament = height * winght * lenght
box = input()
while box != 'Done':
    box = int(box)
    cum_m_apertament -= box
    if cum_m_apertament <= 0:
        break
    box = input()
if cum_m_apertament <= 0:
    print(f'No more free space! You need {abs(cum_m_apertament)} Cubic meters more.')
else:
    print(f'{cum_m_apertament} Cubic meters left.')