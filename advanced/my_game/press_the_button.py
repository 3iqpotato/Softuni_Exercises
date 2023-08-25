from tkinter import Tk, Button, PhotoImage, Canvas
from PIL import ImageTk, Image
from tkinter.ttk import *

def start_window():
    window = Tk()
    window.title("press_the_button")
    window.geometry(f'700x600')
    window.resizable(False, False)

    return window


window = start_window()


def create_frame():
    frame = Canvas(window, width=900, height=800)
    frame.grid(row=0, column=0)

    return frame


frame = create_frame()



path = r'C:\Users\KIKO-ASUS\PycharmProjects\Softuni\advanced\my_game\img.png'

photo = PhotoImage(file=path)
img = Image.open(path)
resized_img = img.resize((300, 300), Image.ANTIALIAS)
img_obj = ImageTk.PhotoImage(resized_img)
my_button = Button(window, image=img_obj,)
frame.create_window(350, 300, window=my_button)





window.mainloop()
