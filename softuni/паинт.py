nylon_m2 = float(input())
paint_pre_liter = float(input())
tinner = float(input())
hours_of_work = int(input())

all_paint = paint_pre_liter + paint_pre_liter * 0.10
nylon_sum = (nylon_m2 + 2) * 1.50
paint_sum = all_paint * 14.50
tinner_sum = tinner * 5
money_for_material = nylon_sum + paint_sum + tinner_sum + 0.40
money_for_workers = (money_for_material * 0.3) * hours_of_work
all_sume = money_for_workers + money_for_material

print(all_sume)

