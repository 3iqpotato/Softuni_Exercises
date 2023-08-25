from tkinter import Tk, Canvas
from tkinter import Button
import random


def clean():
    frame.delete('all')


def create_entry(x = 300, y = 200):
    coord_x = x
    coord_y = y
    register_button = Button(
        window,
        text='No',
        bg='red',
        fg='black',
        borderwidth=0,
        font=('Arial', 18),
        activebackground='#345',
        width=13,
        height=2,
        command=lambda x=coord_x, y=coord_y: click(x, y)
    )

    loggin_button = Button(
        window,
        text='Yes',
        bg='green',
        fg='black',
        borderwidth=0,
        font=('Arial', 18),
        activebackground='#345',
        width=13,
        height=2,
        command=lambda: click_yes()

    )
    frame.create_text(400, 120, text=f"Are you DumP ???", fill='red', font=("Arial", 40))
    frame.create_window(x, y, window=register_button)
    frame.create_window(480, 200, window=loggin_button)

    if len(clicks) >= 100:
        exit_page()

def click(x, y):
    clicks.append('1')
    clean()
    x = random.randrange(60, 740)
    y = random.randrange(30, 370)
    if 460 < x < 510 or 175 < y < 225:
        return click(x, y)

    create_entry(x, y)

clicks = []

def exit_page():
    clean()
    frame.create_text(400, 140, text=f"You are the dumbest!!!", fill='red', font=("Arial", 40))
    exit_button = Button(
        window,
        text='Exit',
        bg='green',
        fg='black',
        borderwidth=0,
        font=('Arial', 18),
        activebackground='#345',
        width=13,
        height=2,
        command=lambda: exit_command()

    )
    frame.create_window(400, 200, window=exit_button)


def exit_command():
    exit(0)


def click_yes():
    clean()
    frame.create_text(400, 140, text=f"Know it Hahaha!", fill='red', font=("Arial", 40))


def start_window():
    window = Tk()
    window.title("Are_You_DumP")
    window.geometry(f'800x400')
    window.resizable(False, False)

    return window


window = start_window()


def create_frame():
    frame = Canvas(window, width=800, height=800)
    frame.grid(row=0, column=0)

    return frame


frame = create_frame()



if __name__ == '__main__':
    create_entry()
    window.mainloop()