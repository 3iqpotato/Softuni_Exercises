full_sum = int(input())
product_price = input()
times = 0
current_sum = 0
current_sum1 = 0
times_cesh = 0
times_card = 0

while product_price != "End":
    product_price = int(product_price)

    times += 1
    if times % 2 != 0:
        if product_price > 100:
            print('Error in transaction!')
        else:
            print('Product sold!')
            current_sum += product_price
            times_cesh += 1
    else:
        if product_price < 10:
            print('Error in transaction!')
        else:
            print('Product sold!')
            current_sum1 += product_price
            times_card += 1
    if current_sum + current_sum1 >= full_sum:
        break
    product_price = input()

if current_sum + current_sum1 >= full_sum:
    average_card = current_sum1 / times_card
    average_cesh = current_sum / times_cesh
    print(f'Average CS: {average_cesh:.2f}\nAverage CC: {average_card:.2f}')
else:
    print('Failed to collect required money for charity.')