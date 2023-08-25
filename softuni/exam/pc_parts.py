price_in_dollars_cpu = float(input())
price_in_dollars_gpu = float(input())
price_in_dollars_ram = float(input())
num_rams = int(input())
percent_discount = float(input())

price_cpu = price_in_dollars_cpu * 1.57
price_gpu = price_in_dollars_gpu * 1.57
price_ram = num_rams * (price_in_dollars_ram * 1.57)
discount_cpu = price_cpu - (price_cpu * percent_discount)
discount_gpu = price_gpu - (price_gpu * percent_discount)
full_price = discount_gpu + discount_cpu + price_ram
print(f'Money needed - {full_price:.2f} leva.')
