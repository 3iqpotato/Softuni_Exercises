input_string = input()
dict_nums = {}
while '-' in input_string:
    input_string = input_string.split('-')
    name = input_string[0]
    number = input_string[1]
    dict_nums[name] = number
    input_string = input()

for tries in range(int(input_string)):
    name = input()
    if name in dict_nums:
        print(f"{name} -> {dict_nums[name]}")
    else:
        print(f'Contact {name} does not exist.')

