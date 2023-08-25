import math
num_ppaint_box = int(input())
rolls_tapets = int(input())
gloes_pair_price = float(input())
brush_price_per_one = float(input())

paint_price = num_ppaint_box * 21.5
rolls_price = rolls_tapets * 5.2
gloves_num = math.ceil(rolls_tapets * 0.35)
brush_num = math.floor(num_ppaint_box * 0.48)
gloves_price = gloves_num * gloes_pair_price
brush_price = brush_num * brush_price_per_one
full_price = brush_price + gloves_price + rolls_price + paint_price
deliver_price = full_price / 15
print(f'This delivery will cost {deliver_price:.2f} lv.')