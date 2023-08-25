def is_perfect(num):
    sums = 0
    for delitel in range(1, num):
        if num % delitel == 0:
            sums += delitel
    return sums == num


number = int(input())
if is_perfect(number):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")
