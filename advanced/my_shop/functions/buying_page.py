from json import load, dump
from tkinter import Button

from ..functions.helping import clean
from PIL import Image, ImageTk
from ..functions.my_canvas import frame, window


def display_products():
    clean()
    display_images()


def display_images():
    path = r'C:\Users\KIKO-ASUS\PycharmProjects\Softuni\advanced\my_shop\files_and_pictures\preducts_storage.json'
    with open(path, 'r') as products:
        info = load(products)

    x, y = 150, 50

    for item_name, item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info['picture']))

        frame.create_text(x, y, text=item_name)
        frame.create_image(x, y + 130, image=item_img)

        if item_info['quantity'] > 0:
            item_button = Button(
                window,
                text="Buy",
                bg='green',
                fg='white',
                width=5,
                command=lambda x=item_name, y=info: buy_product(x, y)
            )

            frame.create_window(x, y + 270, window=item_button)
            frame.create_text(x, y + 250, text=f"Left: {item_info['quantity']}")
        else:
            frame.create_text(x, y + 250, text=f"Out of stock!", fill='red')
        img.append(item_img)

        x += 230

        if x > 700:
            x = 150
            y += 300


img = []

def buy_product(product, info):
    info[product]['quantity'] -= 1
    path = r'C:\Users\KIKO-ASUS\PycharmProjects\Softuni\advanced\my_shop\files_and_pictures\preducts_storage.json'
    with open(path, 'w') as products:
        dump(info, products)

    display_products()


