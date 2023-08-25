meters_area = float(input())
price1 = meters_area * 7.61
discount = price1 * 0.18
price2 = price1 - discount
print("The final price is " + str(price2) + " lv.")
print(f'The discount is {discount} lv.')

