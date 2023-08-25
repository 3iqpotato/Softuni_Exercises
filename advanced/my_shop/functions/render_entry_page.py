from tkinter import Button, Entry
from ..functions.my_canvas import window, frame
from advanced.my_shop.functions.helping import clean
from json import loads, dump
from ..functions.buying_page import display_products


def create_entry():
    register_button = Button(
        window,
        text='Register',
        bg='green',
        fg='black',
        borderwidth=0,
        font=('Arial', 18),
        activebackground='#345',
        width=17,
        height=2,
        command=register
    )

    loggin_button = Button(
        window,
        text='Login',
        bg='pink',
        fg='black',
        borderwidth=0,
        font=('Arial', 18),
        activebackground='#345',
        width=17,
        height=2,
        command=logging
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 330, window=loggin_button)


def register():
    clean()

    frame.create_text(100, 50, text='First name:')
    frame.create_text(94, 100, text='Second name:')
    frame.create_text(100, 150, text='Username:')
    frame.create_text(100, 200, text='Password:')

    frame.create_window(250, 50, window=first_name_box)
    frame.create_window(250, 100, window=second_name_box)
    frame.create_window(250, 150, window=username_box)
    frame.create_window(250, 200, window=password_box)

    register_button = Button(
        window,
        text='Register',
        bg='green',
        fg='black',
        borderwidth=0,
        font=('Arial', 13),
        activebackground='#345',
        width=13,
        height=2,
        command=registration
    )

    frame.create_window(250, 250, window=register_button)


def registration():
    info_dict = {
        'First name': first_name_box.get(),
        'Second name': second_name_box.get(),
        'Username': username_box.get(),
        'Password': password_box.get()
    }

    if check_registration(info_dict):
        path = r'C:\Users\KIKO-ASUS\PycharmProjects\Softuni\advanced\my_shop\files_and_pictures\registered_acc'
        with open(path, 'a') as file:
            dump(info_dict, file)
            file.write('\n')
            display_products()


def check_registration(info):
    frame.delete('error')
    for key, value in info.items():
        if not value.strip():
            frame.create_text(
                300,
                300,
                text=f'{key} cannot be empty!',
                fill='red',
                tags='error'
            )
            return False

    info_data = get_users_data()

    for record in info_data:
        if record['Username'] == info['Username']:
            frame.create_text(
                300,
                300,
                text=f'Username is already taken!',
                fill='red',
                tags='error'
            )
            return False
    return True


def get_users_data():
    info_data = []

    path = r'C:\Users\KIKO-ASUS\PycharmProjects\Softuni\advanced\my_shop\files_and_pictures\registered_acc'
    with open(path, 'r') as users_data:
        for line in users_data:
            info_data.append(loads(line))
    return info_data


first_name_box = Entry(window, bd=4, bg='pink')
second_name_box = Entry(window, bd=4, bg='pink')
username_box = Entry(window, bd=4,  bg='pink')
password_box = Entry(window, bd=4,  bg='pink', show='X')


def logging():
    clean()

    frame.create_text(100, 150, text='Username:')
    frame.create_text(100, 200, text='Password:')

    frame.create_window(250, 150, window=username_box)
    frame.create_window(250, 200, window=password_box)

    login_button = Button(
        window,
        text='Login',
        bg='pink',
        fg='black',
        borderwidth=0,
        font=('Arial', 13),
        activebackground='#345',
        width=13,
        height=2,
        command=log_in
    )

    frame.create_window(250, 250, window=login_button)


def log_in():
    info_dict = {
        'Username': username_box.get(),
        'Password': password_box.get()
    }

    if check_log(info_dict):
        display_products()


def check_log(info):
    frame.delete('error')
    for key, value in info.items():
        if not value.strip():
            frame.create_text(
                300,
                300,
                text=f'{key} cannot be empty!',
                fill='red',
                tags='error'
            )
            return False

    info_data = get_users_data()
    for record in info_data:
        if record['Username'] == info['Username'] and record['Password'] == info['Password']:

            return True
        else:
            frame.create_text(
                300,
                300,
                text=f'Invalid Username or password!',
                fill='red',
                tags='error'
            )
            return False
