def checkio(number: int) -> int:
    num = 1
    for idx in str(number):
        if int(idx) > 0:
            num *= int(idx)

    return num

# #
# def checkio(number: int) -> int:
#     res = 1
#     for char in str(number):
#         if num := int(char):
#             res *= num
#
#     return res

print("Example:")
print(checkio(123405))

# These "asserts" are used for self-checking
assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")