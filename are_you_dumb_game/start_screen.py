from tkinter import Tk, Canvas


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
