hrizantema_num = int(input())
rose_num = int(input())
lale_num = int(input())
season = input()
work_or_rest_day = input()

price_hrizantema = 0
price_rose = 0
price_lale = 0

lale_promotion = False
rose_promotion = False
num_flowers = rose_num + lale_num + hrizantema_num
if season in ['Spring', 'Summer']:
    price_lale = 2.5
    price_hrizantema = 2
    price_rose = 4.10
    if season == "Spring" and lale_num > 5:
        lale_promotion = True

elif season in ['Autumn', 'Winter']:
    price_lale = 4.15
    price_rose = 4.5
    price_hrizantema = 3.75
    if season == "Winter" and rose_num >= 10:
        rose_promotion = True


hrizantema_cost = price_hrizantema * hrizantema_num
rose_cost = price_rose * rose_num
lale_cost = lale_num * price_lale

if work_or_rest_day == 'Y':
    hrizantema_cost = hrizantema_cost * 1.15
    rose_cost = rose_cost * 1.15
    lale_cost = lale_cost * 1.15
full_cost = hrizantema_cost + rose_cost + lale_cost
if lale_promotion:
    full_cost = full_cost * 0.95
if rose_promotion:
    full_cost = full_cost * 0.9
if num_flowers > 20:
    full_cost = full_cost * 0.8
#avanzirane
full_cost = full_cost + 2

print(f'{full_cost:.2f}')
