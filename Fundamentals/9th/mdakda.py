forces_dict = {'dark': ['gogo']}
side = "dark"
user = "gogo"

forces_dict[side] = forces_dict.get(side, []) + [user]
print(forces_dict)