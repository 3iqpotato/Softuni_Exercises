# def formating(type, data):
#     if type == 'int':
#       data = int(data) * 2
#     if type == "real":
#        data = int(data) * 1.5
#        data = f'{data:.2f}'
#     if type == "string":
#        data = f'${data}$'
#     return data
#
#
# tipe = input()
# data = input()
# print(formating(tipe, data))
#
# tipe = input()
# data = input()
# if tipe == 'int':
#     data = int(data) * 2
# if tipe == "real":
#     data = int(data) * 1.5
#     data = f'{data:.2f}'
# if tipe == "string":
#     data = f'${data}$'
#
# print(data)
type = input()
if type == 'int':
    data = int(input())
    print(data * 2)
elif type == 'real':
    data = float(input())
    print(f'{data * 1.5:.2f}')
elif type == 'string':
    data = input()
    print(f'${data}$')
# def calculate():
#   while True:
#     try:
#       expression = input("Enter your calculation: ")
#       result = eval(expression)
#       print("Result: ", result)
#       break
#     except:
#       print("Invalid expression. Try again.")
#
# calculate()