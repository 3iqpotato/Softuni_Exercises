def naughty_or_nice_list(santa_list, *args, **kwargs):
    naughty_list = []
    nice_list = []
    result = []
#
    def place_kid():
        if len(kids) == 1:
            if type_of_kid == 'Nice':
                nice_list.append(kids[0][1])
            else:
                naughty_list.append(kids[0][1])
            santa_list.remove(*kids)

    for kid_data in args:
        num, type_of_kid = kid_data.split('-')
        kids = [info for info in santa_list if info[0] == int(num)]
        place_kid()

    for name, type_of_kid in kwargs.items():
        kids = [info for info in santa_list if info[1] == name]
        place_kid()


    if nice_list:
        result.append(f'Nice: {", ".join(nice_list)}')
    if naughty_list:
        result.append(f'Naughty: {", ".join(naughty_list)}')
    if santa_list:
        result.append(f'Not found: {", ".join(k[1] for k in santa_list)}')

    return '\n'.join(result)






print(naughty_or_nice_list(
 [
 (3, "Amy"),
 (1, "Tom"),
 (7, "George"),
 (3, "Katy"),
 ],
 "3-Nice",
 "1-Naughty",
 Amy="Nice",
 Katy="Naughty",
))
print(naughty_or_nice_list(
 [
 (6, "John"),
 (4, "Karen"),
 (2, "Tim"),
 (1, "Merry"),
 (6, "Frank"),
 ],
 "6-Nice",
 "5-Naughty",
 "4-Nice",
 "3-Naughty",
 "2-Nice",
 "1-Naughty",
 Frank="Nice",
 Merry="Nice",
 John="Naughty",
))

