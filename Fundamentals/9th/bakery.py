products = input().split()
product_dict = {}
for index in range(0, len(products), 2):
    product_dict[products[index]] = int(products[index+1])
print(product_dict)