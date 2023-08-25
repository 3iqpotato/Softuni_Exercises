numbers_dictionary = {}

line = input()

while line != "Search":
    try:
        number = int(input())
        numbers_dictionary[line] = number
    except ValueError:
        print('The variable number must be an integer')

    line = input()

searching_line = input()
while line != "Remove":
    try:
        print(numbers_dictionary[searching_line])
    except KeyError:
        print('Number does not exist in dictionary')

    searching_line = input()

removing_line = input()
while line != "End":
    try:
        del numbers_dictionary[removing_line]
    except KeyError:
        print('Number does not exist in dictionary')
    removing_line = input()

print(numbers_dictionary)
