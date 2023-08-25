from collections import deque
import operator
from colorama import Fore
# import openai
#
#
# openai.api_key='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'
#

class NotValidIdx(Exception):
    pass
#
# def responding():
#     response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "player", "content": "you are playing game enter a number between 1 and 7."},
#     ]
# )
#     print(response)


def is_valid_idx(r, c):
    return 0 <= r < ROWS and 0 <= c < COlS


def printing():
    [print(*w) for w in matrix]


def place_symbol(col):
    for r in range(ROWS-1, -1, -1):
        if matrix[r][col] == zero:
            return [r, col]


def get_count(row, col, x, y, operator_func):
    s = 0
    for i in range(1, 4):
        r = operator_func(row, x * i)
        c = operator_func(col, y * i)
        if not is_valid_idx(r, c):
            break
        if matrix[r][c] == zero:
            break
        if matrix[r][c] != symbol:
            break
        s += 1
    return s


def is_player_winning(curr_row, curr_col):
    for row, col in moves:
        count = get_count(curr_row, curr_col, row, col, operator.add) + \
                get_count(curr_row, curr_col, row, col, operator.sub) + 1

        if count >= 4:
            return True

    else:
        return False


zero = Fore.BLACK + "0" + Fore.RESET
ROWS, COlS = 6, 7
matrix = [[zero]*COlS for _ in range(ROWS)]

players_and_marks = deque([["Player 1", Fore.BLUE + 'X' + Fore.RESET],
                           ['Player 2', Fore.LIGHTMAGENTA_EX + 'Y' + Fore.RESET]])
win = False
count_moves = 0
all_moves = COlS * ROWS
moves = [[1, 0], [0, 1], [1, 1], [-1, 1]]

while not win:
    player, symbol = players_and_marks[0]
    printing()
    # if player == 'Player 2':
    #     responding()
    try:
        column = int(input(Fore.GREEN + f'{player}, please choose a column: ' + Fore.RESET)) - 1
        if not is_valid_idx(0, column):
            raise NotValidIdx

    except ValueError:
        print(Fore.RED + f'Please enter a number!' + Fore.RESET)
        continue

    except NotValidIdx:
        print(Fore.RED + f'Please enter a number between 1 - {COlS}' + Fore.RESET)
        continue

    placed = place_symbol(column)

    if placed:
        matrix[placed[0]][placed[1]] = symbol
        count_moves += 1

        is_he_winning = is_player_winning(placed[0], placed[1])
        if is_he_winning:
            printing()
            print(Fore.LIGHTBLUE_EX + f'{player} wins!' + Fore.RESET)
            break
    else:
        print(Fore.RED + f'This column is full try again!' + Fore.RESET)
        continue

    if count_moves == all_moves:
        print('Draw!')
        break

    players_and_marks.rotate()



# s = 0
# for i in range(1, 4):
#     r = curr_row + row * i
#     c = curr_col + col * i
#     if not is_valid_idx(r, c):
#         break
#     if matrix[r][c] == '0':
#         break
#     if matrix[r][c] != mark:
#         break
#     s += 1
#
# for i in range(1, 4):
#     r = curr_row - row * i
#     c = curr_col - col * i
#     if not is_valid_idx(r, c):
#         break
#     if matrix[r][c] == '0':
#         break
#     if matrix[r][c] != mark:
#         break
#     s += 1
#
# if s >= 3:
#     return True

