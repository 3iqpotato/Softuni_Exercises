month = input()
nights = int(input())

sleeps = nights + 0
studio_price = 0
apartament_price = 0

if month in ['May', 'October']:
    studio_price = 50
    apartament_price = 65
    if 7 < sleeps <= 14:
        studio_price = studio_price * 0.95
    elif sleeps > 14:
        studio_price = studio_price * 0.70
        apartament_price = apartament_price * 0.9
elif month in ['June', 'September']:
    studio_price = 75.2
    apartament_price = 68.7
    if sleeps > 14:
        studio_price = studio_price * 0.8
        apartament_price = apartament_price * 0.9
elif month in ['July', 'August']:
    studio_price = 76
    apartament_price = 77
    if sleeps > 14:
        apartament_price = apartament_price * 0.9

apartament_price = apartament_price * sleeps
studio_price = studio_price * sleeps
print(f'Apartment: {apartament_price:.2f} lv. ')
print(f'Studio: {studio_price:.2f} lv.')

