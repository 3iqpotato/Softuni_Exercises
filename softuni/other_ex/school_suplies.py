pencils = int(input())
markers = int(input())
liters_preparat = int(input())
percent_discount = int(input())

price_for_pen = pencils * 5.80
price_for_markers = markers * 7.20
price_of_preparat = liters_preparat * 1.20
discount = percent_discount / 100

price_without_discount = price_of_preparat + price_for_pen + price_for_markers
price_with_discount = price_without_discount - price_without_discount * discount
print(price_with_discount)