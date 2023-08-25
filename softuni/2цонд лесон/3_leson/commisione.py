town = input()
sales = float(input())

money = 0
flag = True
if town == "Sofia":
    if 0 <= sales <= 500:
        money = sales * 0.05
    elif 500 < sales <= 1000:
        money = sales * 0.07
    elif 1000 < sales <= 10000:
        money = sales * 0.08
    elif sales > 10000:
        money = sales * 0.12
    else:
        flag = False

elif town == "Plovdiv":
    if 0 <= sales <= 500:
        money = sales * 0.055
    elif 500 < sales <= 1000:
        money = sales * 0.08
    elif 1000 < sales <= 10000:
        money = sales * 0.12
    elif sales > 10000:
        money = sales * 0.145
    else:
        flag = False


elif town == "Varna":
    if 0 <= sales <= 500:
        money = sales * 0.045
    elif 500 < sales <= 1000:
        money = sales * 0.075
    elif 1000 < sales <= 10000:
        money = sales * 0.1
    elif sales > 10000:
        money = sales * 0.13
    else:
        flag = False
else:
    flag = False

if flag:
    print(f'{money:.2f}')
else:
    print('error')