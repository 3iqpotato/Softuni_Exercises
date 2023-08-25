num = int(input())
piece_dict = {}
for _ in range(num):
    input_line = input().split('|')
    piece = input_line[0]
    composter = input_line[1]
    key = input_line[2]
    piece_dict[piece] = {composter: key}

while True:
    command = input().split('|')
    if 'Stop' in command:
        break
    move = command[0]
    if move == 'Add':
        piece = command[1]
        composter = command[2]
        key = command[3]
        if piece in piece_dict:
            print(f"{piece} is already in the collection!")
        else:
            piece_dict[piece] = {composter: key}
            print(f"{piece} by {composter} in {key} added to the collection!")
    elif move == "Remove":
        piece = command[1]
        if piece not in piece_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            piece_dict.pop(piece)
            print(f'Successfully removed {piece}!')
    elif move == 'ChangeKey':
        piece = command[1]
        new_key = command[2]
        if piece not in piece_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            com = piece_dict[piece].keys()
            composter = ''.join(com)
            piece_dict[piece][composter] = new_key

            print(f"Changed the key of {piece} to {new_key}!")

for key, values in piece_dict.items():
    for key1, values1 in piece_dict[key].items():
        print(f"{key} -> Composer: {key1}, Key: {piece_dict[key][key1]}")