year_tax = int(input())

shoes_price = year_tax - (year_tax * 0.4)
basket_ekip = shoes_price - (shoes_price * 0.2)
ball = basket_ekip / 4
acc_price = ball / 5

all_suma = year_tax + shoes_price +basket_ekip + ball + acc_price
print(all_suma)