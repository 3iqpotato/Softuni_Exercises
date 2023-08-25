# def evens(numb):
#     even = []
#     for n in numb:
#         if int(n) % 2 == 0:
#             even.append(int(n))
#     return even
#
#
# numbers = [x for x in input().split()]
# print((evens(numbers)))

def is_evens(numb):
    return numb % 2 == 0



numbers = [int(x) for x in input().split()]
print(list(filter(is_evens, numbers)))