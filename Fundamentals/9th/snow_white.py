drafts_dict = {}
while True:
    command = input()
    if command == 'Once upon a time':
        break
    name, hat_color, physics = command.split(' <:> ')
    physics = int(physics)
    if (name, hat_color) not in drafts_dict:
        drafts_dict[name, hat_color] = physics
    else:
        if physics > drafts_dict[name, hat_color]:
            drafts_dict[name, hat_color] = physics
# print(drafts_dict)
sorting_drafts = {}
for (name, hat) in drafts_dict:
    if hat not in sorting_drafts:
        sorting_drafts[hat] = {name: drafts_dict[name, hat]}
    else:
        sorting_drafts[hat].update({name: drafts_dict[name, hat]})
# print(sorting_drafts)
# for key, value in sorted(sorting_drafts.items(), key=lambda x: (-x[1], x[0])):
#     print(f'{key} {value}')
dwarfs_list = []
for hat in sorting_drafts.keys():
    for name_dwarf, physics_dwarf in sorting_drafts[hat].items():
        dwarfs_list.append({"length": len(sorting_drafts[hat]), "hat_colour": hat, "dwarf name": name_dwarf, "dwarf physics": physics_dwarf})

for final in sorted(dwarfs_list, key=lambda x: (-x["dwarf physics"], -x["length"])):
    print(f"({final['hat_colour']}) {final['dwarf name']} <-> {final['dwarf physics']}")
# print(sorting_drafts)

# sort_by_pts = []
# for pts in drafts_dict.values():
#     sort_by_pts.append(pts)
# sort_by_pts = sorted(sort_by_pts)
# sort_by_pts.reverse()
# print(sort_by_pts)
# Peter <:> Red <:> 2000
# Teodor <:> Blue <:> 1000
# George <:> Green <:> 1000
# Simon <:> Yellow <:> 4500
# Dopey <:> Simon <:> 1000
# Once upon a time