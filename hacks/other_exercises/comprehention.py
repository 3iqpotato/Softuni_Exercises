x = int(input())
y = int(input())
z = int(input())
n = int(input())
# my_list = []
# for idx1 in range(x + 1):
#     for idx2 in range(y + 1):
#         for idx3 in range(z + 1):
#             if idx3 + idx2 + idx1 != n:
#                 my_list.append([idx1, idx2, idx3])

my_list = [[idx1, idx2, idx3] for idx1 in range(x + 1) for idx2 in range(y + 1) for idx3 in range(z + 1) if idx3 + idx2 + idx1 != n]
print(my_list)
