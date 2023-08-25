season = input()
km_per_month = float(input())

lv_per_km = 0
if km_per_month <= 5000:
    if season in ["Spring", "Autumn"]:
        lv_per_km = 0.75
    elif season == 'Summer':
        lv_per_km = 0.9
    elif season == "Winter":
        lv_per_km = 1.05
elif km_per_month <= 10000:
    if season in ["Spring", "Autumn"]:
        lv_per_km = 0.95
    elif season == 'Summer':
        lv_per_km = 1.1
    elif season == "Winter":
        lv_per_km = 1.25
else:
    lv_per_km = 1.45

money_earned = (lv_per_km * km_per_month) * 4
money_earned = money_earned * 0.9

print(f'{money_earned:.2f}')

