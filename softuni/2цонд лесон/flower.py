from math import floor, ceil

magnolii = int(input())
zumbuli = int(input())
rozes = int(input())
cactuses = int(input())
prezent_price = float(input())

magnolii_price = magnolii * 3.25
zumbuli_price = zumbuli * 4
rozes_price = rozes * 3.5
cactuses_price = cactuses * 8
full_price = magnolii_price + zumbuli_price + rozes_price + cactuses_price

money_without_tax = full_price - (full_price * 0.05)

if money_without_tax >= prezent_price:
    diff = floor(money_without_tax - prezent_price)
    print(f'She is left with {diff:.0f} leva.')
else:
    diff = ceil(prezent_price - money_without_tax)
    print(f'She will have to borrow {diff} leva.')

