budget = float(input())
season = input()
hotel = ''
destination = ''
if budget <= 1000:
    hotel = 'Camp'
    if season == 'Winter':
        destination = 'Morocco'
        budget = budget * 0.45
    elif season == "Summer":
        destination = 'Alaska'
        budget = budget * 0.65
elif 1000 < budget <= 3000:
    hotel = "Hut"
    if season == 'Winter':
        destination = 'Morocco'
        budget = budget * 0.6
    elif season == "Summer":
        destination = 'Alaska'
        budget = budget * 0.8
elif budget > 3000:
    hotel = "Hotel"
    if season == 'Winter':
        destination = 'Morocco'
        budget = budget * 0.9
    elif season == "Summer":
        destination = 'Alaska'
        budget = budget * 0.9

print(f'{destination} - {hotel} - {budget:.2f}')
