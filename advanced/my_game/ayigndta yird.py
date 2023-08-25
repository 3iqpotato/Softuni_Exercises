import tkinter as tk
from tkinter import PhotoImage

def print_hello():
    print('hello')

root = tk.Tk()
root.geometry("900x600")

imagetest = PhotoImage(file="img.png")

button_qwer = tk.Button(root, text="asdfasdf", image=imagetest, command=print_hello)
button_qwer.pack()   # <-- don't forget to place the button in the window

root.mainloop()