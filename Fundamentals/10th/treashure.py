def get_material(string):
    material = ''
    for idx in range(len(string)):
        if string[idx] == '&':
            idx+=1
            while string[idx] != '&':
                material += string[idx]
                idx += 1
            return material

def get_coords(string):
    coords = ''
    for idx in range(len(string)):
        if string[idx] == '<':
            idx+=1
            while string[idx] != '>':
                coords += string[idx]
                idx += 1
            return coords

keys = [int(x) for x in input().split()]
all_string_lines = []
while True:
    string_lines = input()
    if string_lines == 'find':
        break
    all_string_lines.append(string_lines)
new_string = ''
list_new_strs = []
for string in all_string_lines:
    count = 0
    for idx in range(len(string)):
        if count >= len(keys):
            count = 0
        new_string += chr(ord(string[idx]) - keys[count])
        count += 1
    list_new_strs.append(new_string)
    new_string = ''
for idx in range(len(list_new_strs)):
    print(f'Found {get_material(list_new_strs[idx])} at {get_coords(list_new_strs[idx])}')

# 1 2 1 3
# ikegfp'jpne)bv=41P83X@
# ujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA
# find