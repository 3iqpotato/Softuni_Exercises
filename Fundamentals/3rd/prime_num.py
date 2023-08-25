num = int(input())
count = 0
for dells in range(1, num + 1):
    if num % dells == 0:
        count += 1
if count > 2:
    print('False')
else:
    print('True')