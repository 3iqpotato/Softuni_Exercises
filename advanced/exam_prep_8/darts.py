from math import ceil


def is_valid_coords(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE


def hits_d(r, c):
    moves = [
        (r, 0),
        (r, SIZE - 1),
        (0, c),
        (SIZE - 1, c)
    ]
    points = 0
    for move in moves:
        points += int(board[move[0]][move[1]])
    return points


player1, player2 = input().split(', ')
dict_score = {player1: 501, player2: 501}
players_list = [player1, player2]
SIZE = 7
board = [[x for x in input().split()] for _ in range(SIZE)]
winner = ''
throws = 0

while not winner:
    coords = [int(x) for x in input()[1:-1].split(', ')]
    row, col = coords
    player = players_list[0]
    throws += 1
    if is_valid_coords(row, col):
        position = board[row][col]
        if not position.isalpha():
            dict_score[player] -= int(position)
        else:
            if position == 'D':
                dict_score[player] -= hits_d(row, col) * 2
            elif position == 'T':
                dict_score[player] -= hits_d(row, col) * 3
            elif position == "B":
                dict_score[player] -= 501

    if dict_score[player] <= 0:
        winner = player

    players_list.reverse()


print(f'{winner} won the game with {ceil(throws / 2)} throws!')