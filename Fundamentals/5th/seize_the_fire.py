list_tipe_value = input().split('#')
water = int(input())
total_fire = 0
ceils_out_of_fire = []
for cicle in range(len(list_tipe_value)):
    ceil_and_fire = list_tipe_value[cicle]
    fire_level = ceil_and_fire.split(' = ')[0]
    ceil_num = ceil_and_fire.split(' = ')[1]
    ceil_num = int(ceil_num)
    if water < ceil_num:
        continue
    if fire_level == 'High' and 81 <= ceil_num <= 125:
        water -= ceil_num
        total_fire += ceil_num
        ceils_out_of_fire.append(ceil_num)
    elif fire_level == 'Medium' and 51 <= ceil_num <= 80:
        water -= ceil_num
        total_fire += ceil_num
        ceils_out_of_fire.append(ceil_num)
    elif fire_level == 'Low' and 1 <= ceil_num <= 50:
        water -= ceil_num
        total_fire += ceil_num
        ceils_out_of_fire.append(ceil_num)


effor = total_fire * 0.25
print('Cells:')
for ceil in range(len(ceils_out_of_fire)):
    print(f' - {ceils_out_of_fire[ceil]}')
print(f'Effort: {effor:.2f}')
print(f'Total Fire: {total_fire}')