def numsmsms():

    if positiv_nums > abs(negativ_nums):
        return f'The positives are stronger than the negatives'
    else:
        return f'The negatives are stronger than the positives'


nums = [int(el) for el in input().split()]
positiv_nums = sum([el for el in nums if el > 0])
negativ_nums = sum([el for el in nums if el < 0])


print(negativ_nums)
print(positiv_nums)
print(numsmsms())