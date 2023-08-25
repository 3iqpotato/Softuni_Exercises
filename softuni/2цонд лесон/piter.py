budget = float(input())
gpu_num = int(input())
cpu_num = int(input())
ram_num = int(input())

gpu_price = gpu_num * 250
cpu_price = gpu_price * 0.35
ram_price = gpu_price * 0.1
full_price = gpu_price + cpu_price * cpu_num + ram_price * ram_num
if gpu_num > cpu_num:
    full_price = full_price - (full_price * 0.15)

diff = abs(budget - full_price)
if budget >= full_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
