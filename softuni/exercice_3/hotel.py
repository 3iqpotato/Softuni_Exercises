days = int(input())
room = input()
rating = input()

nights = days - 1
price_per_sleep = 0
full_price = 0
if room == 'room for one person':
    price_per_sleep = 18
    full_price = price_per_sleep * nights
elif room == 'apartment':
    price_per_sleep = 25
    full_price = price_per_sleep * nights
    if nights < 10:
        full_price = full_price * 0.70
    elif 10 <= nights <= 15:
        full_price = full_price * 0.65
    elif nights > 15:
        full_price = full_price * 0.5
elif room == 'president apartment':
    price_per_sleep = 35
    full_price = price_per_sleep * nights
    if nights < 10:
        full_price = full_price * 0.9
    elif 10 <= nights <= 15:
        full_price = full_price * 0.85
    elif nights > 15:
        full_price = full_price * 0.8

if rating == 'positive':
    full_price = full_price * 1.25
elif rating == 'negative':
    full_price = full_price * 0.9

print(f'{full_price:.2f}')
