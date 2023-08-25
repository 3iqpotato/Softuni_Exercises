from tkinter import Tk, PhotoImage, Canvas


def start_window():
    window = Tk()
    window.title("Loli Shop")
    window.geometry(f'900x700')
    window.resizable(False, False)

    path = r'C:\Users\KIKO-ASUS\PycharmProjects\Softuni/advanced/my_shop/files_and_pictures/08ab433a664b1a747e411ecdf2581f1e.png'
    photo = PhotoImage(file=path)
    window.wm_iconphoto(False, photo)

    return window


window = start_window()


def create_frame():
    frame = Canvas(window, width=800, height=800)
    frame.grid(row=0, column=0)

    return frame

frame = create_frame()