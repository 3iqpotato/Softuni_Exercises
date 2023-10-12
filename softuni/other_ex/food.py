chiken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())

chiken_price = chiken_menu * 10.35
fish_price = fish_menu * 12.40
veg_price = veg_menu * 8.15
all_price = chiken_price + fish_price + veg_price
decert = all_price * 0.2
full_price = all_price + decert + 2.50

print(full_price)
