command = input()
forces_dict = {}
while command != "Lumpawaroo":
    if ' | ' in command:
        command = command.split(" | ")
        user = command[1]
        side = command[0]
        is_in = False
        for sides in forces_dict:
            if user in forces_dict[sides]:
                is_in = True
        if side not in forces_dict and not is_in:
            forces_dict[side] = [user]
        elif not is_in:
            forces_dict[side].append(user)
    else:
        command = command.split(' -> ')
        user = command[0]
        side = command[1]

        for sides in forces_dict:
            if user in forces_dict[sides]:
                forces_dict[sides].remove(user)
                break
        if side not in forces_dict:
            forces_dict[side] = [user]
        else:
            forces_dict[side].append(user)
        # forces_dict[side] = forces_dict.get(side, []) + [user]
        print(f"{user} joins the {side} side!")



    #     else:
    #         if side not in forces_dict:
    #             forces_dict[side] = [user]
    #         else:
    #             forces_dict[side].append(user)
    #
    #   print(f"{user} joins the {side} side!")
    command = input()
for side in forces_dict:
    if len(forces_dict[side]) > 0:
        print(f"Side: {side}, Members: {len(forces_dict[side])}")
        for member in forces_dict[side]:
            print(f"! {member}")
#
# Light | Peter
# Dark | Kim
# Light | Kim
# Lumpawaroo
# Lighter | Royal
# Darker | DCay
# Ivan Ivanov -> Lighter
# DCay -> Lighter
# Lumpawaroo



