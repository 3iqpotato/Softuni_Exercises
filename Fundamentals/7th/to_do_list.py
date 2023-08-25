# command = input()
# # Create the output list to put the data in
# to_do = []
#
# # Fill in the list with all commands
# while command != "End":
#     to_do.append(command)
#     command = input()
#
# # Now that we have the to-do list, we just have to sort it, so we turn the first part into a digit and then we sort it
# for i in range(len(to_do)):
#     to_do[i] = to_do[i].split("-")
#     to_do[i][0] = int(to_do[i][0])
# to_do = sorted(to_do)
#
# # Now we have a sorted list, so we just remove the int in from of every action, using pop()
# for i in range(len(to_do)):
#     to_do[i].pop(0)
#     # Because we have lists inside the list and we need strings inside the list, we have to use join() for each of the lists
#     to_do[i] = "".join(to_do[i])
#
# print(to_do)
comand = input().split('-')
# potato = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# potato.sort()
# print(potato)
to_do_list = []
while 'End' not in comand:
    # comand[0] = int(comand[0])
    to_do_list.append(comand)
    comand = input().split('-')


to_do_list.sort()
for idx in range(len(to_do_list)):
    to_do_list[idx].pop(0)
    to_do_list[idx] = "".join(to_do_list[idx])

print(to_do_list)
