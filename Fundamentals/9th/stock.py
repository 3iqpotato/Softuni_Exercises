products = input().split()
product_dict = {}
for index in range(0, len(products), 2):
    product_dict[products[index]] = int(products[index+1])

scan_products = input().split()
for product in scan_products:
    if product in product_dict:
        print(f"We have {product_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

