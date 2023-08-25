import tkinter as tk
from tkinter import *
import time
#
#
def get_num():
    age = input_field.get()
    name = input_field2.get()
    return age, name


def display_text():
    age, name = get_num()
    text = f'Your name is {age} and you are {name} years old.'
    canvas.create_text(250, 100, text=f"{text}", fill="black", font=('Helvetica 15 bold'))




window = tk.Tk()
window.title("Mind reader")
window.geometry("500x350")  # width x height
canvas= Canvas(window, width= 1000, height= 750, bg="SpringGreen2")
canvas.create_text(100, 30, text="Enter your age: ", fill="black", font=('Helvetica 10 bold'))
canvas.create_text(94, 60, text="Enter your name: ", fill="black", font=('Helvetica 10 bold'))
canvas.pack()


input_field = tk.Entry(window)
input_field.place(x=165, y=20)
input_field2 = tk.Entry(window)
input_field2.place(x=165, y=50)

generate_button = tk.Button(window, text="Calculate", height=1, command=display_text)
generate_button.place(x=300, y=30)




window.mainloop()
# from colorama import Fore
# player_symbol = input(Fore.RED + 'What symbol would you like to play with' + Fore.RESET)
#
# print(player_symbol)
