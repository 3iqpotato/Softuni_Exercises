import random
from pyfiglet import Figlet


def enter_symbol():

    figlet = Figlet(font="big")
    print(figlet.renderText("Tic-Tac-Toe"))

    player_1 = input('Player 1 enter your name: ')
    player_2 = input('Player 2 enter your name: ')

    players = [player_1, player_2]
    symbols = ['X', 'O']

    chosen_player = random.choice((player_1, player_2))
    print(f"First is {chosen_player}!")

    while True:
        chosen_player_symbol = input(f"{chosen_player} enter your symbol X or O: ").upper()
        if chosen_player_symbol in symbols:

            symbols.remove(chosen_player_symbol)
            players.remove(chosen_player)

            return [[chosen_player, chosen_player_symbol], [players[0], symbols[0]]]

        print('Enter valid symbol!')


def printing(start=False):
    if start:
        print(f'This is your board.')
        [print(f"| {' | '.join(str(x) for x in w)} |") for w in matrix]

    else:
        [print(f"| {' | '.join(str(x) for x in w)} |") for w in board]


def place_symbol(player, s):
    while True:
        try:
            position = int(input(f'{player} enter a number between 1-9: '))

        except ValueError:
            print('Enter valid number!')
            continue

        if 0 < position <= SIZE*SIZE:
            r, c = (position - 1) // SIZE, (position - 1) % SIZE

            if board[r][c] == ' ':
                board[r][c] = s
                break

        print('Enter valid number!')


def check_for_win(symbol):
    row_win = any(True for r in board if r.count(symbol) == 3)
    col_win = any([all(board[r][c] == symbol for r in range(SIZE)) for c in range(SIZE)])

    first_diagonal = all([board[i][i] == symbol for i in range(SIZE)])
    second_diagonal = all([board[i][SIZE - i - 1] == symbol for i in range(SIZE)])

    if any([row_win, col_win, first_diagonal, second_diagonal]):
        return True


def playing():
    count = 0
    players_data = enter_symbol()
    printing(start=True)

    while True:
        if count == SIZE * SIZE:
            figlet = Figlet(font="big")
            print(figlet.renderText("Draw!"))
            break

        player, symbol = players_data[0]
        place_symbol(player, symbol)

        printing()
        players_data.reverse()

        count += 1

        if count > 4:
            if check_for_win(symbol):
                figlet = Figlet(font="big")
                print(figlet.renderText(f'{player} wins!'))
                print('Congratulations!!!')
                break


SIZE = 3

matrix = [[i, (i + 1), (i + 2)] for i in range(1, SIZE * SIZE, 3)]
board = [[' ', ' ', ' '] for i in range(1, SIZE * SIZE, 3)]


playing()
