budget = float(input())
season = input()

country = ""
place = ''

if budget <= 100:
    country = "Bulgaria"
    if season == 'summer':
        place = 'Camp'
        budget = budget * 0.3
    elif season == "winter":
        place = "Hotel"
        budget = budget * 0.7
elif budget <= 1000:
    country = "Balkans"
    if season == 'summer':
        place = 'Camp'
        budget = budget * 0.4
    elif season == "winter":
        budget = budget * 0.8
        place = "Hotel"
elif budget > 1000:
    budget = budget * 0.9
    place = "Hotel"
    country = "Europe"

print(f'Somewhere in {country}')
print(f'{place} - {budget:.2f}')
