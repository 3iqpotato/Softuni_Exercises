money = float(input())
coin = 0

money_st = money * 100
while money_st > 0:

    if money_st >= 200:
        money_st -= 200

    elif money_st >= 100:
        money_st -= 100

    elif money_st >= 50:
        money_st -= 50

    elif money_st >= 20:
        money_st -= 20

    elif money_st >= 10:
        money_st -= 10

    elif money_st >= 5:
        money_st -= 5

    elif money_st >= 2:
        money_st -= 2
    elif money_st >= 1:
        money_st -= 1
    else:
        break
    coin += 1

print(coin)


