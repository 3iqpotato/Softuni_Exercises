sum = input().split(', ')
beggars = int(input())
beggars_print = [0] * beggars
for idx in range(len(sum)):
    num = int(sum[idx])
    beggars_print[idx % beggars] += (num)
print(beggars_print)