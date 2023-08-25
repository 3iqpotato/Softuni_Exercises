from tkinter import Tk, Canvas, PhotoImage


def create_root():
    root = Tk()
    root.title("GUI Shop")
    root.geometry(f"700x600")
    root.resizable(False, False)

    path = 'C:/Users/KIKO-ASUS/PycharmProjects/Softuni/advanced\my_shop/files_and_pictures/08ab433a664b1a747e411ecdf2581f1e.png'
    photo = PhotoImage(file=path)
    root.wm_iconphoto(False, photo)

    return root

root = create_root()


def create_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)

    return frame

frame = create_frame()
# from tkinter import Tk, PhotoImage, Canvas
#
#
# def start_window():
#     root = Tk()
#     root.title('Loli Shop')
#     root.geometry('900x700')
#     root.resizable(False, False)
#
#     path = 'C:/Users/KIKO-ASUS/PycharmProjects/Softuni/advanced\my_shop/files_and_pictures/08ab433a664b1a747e411ecdf2581f1e.png'
#     photo = PhotoImage(file=path)
#     root.wm_iconphoto(False, photo)
#
#     return root
#
#
# root = start_window()
#
#
# def create_frame():
#     frame = Canvas(root, width=900, height=800)
#     frame.grid(row=0, column=0)
#
#
# frame = create_frame()