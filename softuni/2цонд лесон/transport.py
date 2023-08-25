kilometers = int(input())
day_or_night = input()

if kilometers < 20:
    if day_or_night == 'night':
        price_per_kilometer = kilometers * 0.90
        full_price = price_per_kilometer + 0.70
        print(f'{full_price:.2f}')
    elif day_or_night == 'day':
        price_per_kilometer = kilometers * 0.79
        full_price = price_per_kilometer + 0.70
        print(f'{full_price:.2f}')
elif 20 <= kilometers < 100:
    price_per_kilometer = kilometers * 0.09
    print(f'{price_per_kilometer:.2f}')
elif kilometers >= 100:
    price_per_kilometer = kilometers * 0.06
    print(f'{price_per_kilometer:.2f}')





