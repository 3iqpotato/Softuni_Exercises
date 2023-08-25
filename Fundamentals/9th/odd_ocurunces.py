input_data = input().lower().split()
data_dic = dict.fromkeys(input_data, 0)
for data in input_data:
    data_dic[data] += 1
print(' '.join([item for item, value in data_dic.items() if value % 2 != 0]))
