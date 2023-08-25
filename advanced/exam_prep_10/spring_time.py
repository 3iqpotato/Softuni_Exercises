def start_spring(**kwargs):
    dict_flowers = {}
    for key, value in kwargs.items():
        if value in dict_flowers:
            dict_flowers[value].append(key)
        else:
            dict_flowers[value] = [key]
    res = ''
    dict_flowers = dict(sorted(dict_flowers.items(), key=lambda x: (-len(x[1]), x[0])))
    print(dict_flowers)
    for key, value in dict_flowers.items():
        res += f'{key}:\n'
        for x in sorted(value):
            res += '-' + x + '\n'

    return res




example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
