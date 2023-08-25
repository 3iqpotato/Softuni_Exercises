import os
import time

aba = os.path.abspath
absolute_path = os.path.dirname(os.path.abspath(__file__)) # namira kyde se namira sega[niq fail
file_path = os.path.join(absolute_path, 'text.txt') # добавя към пътя името на фаила които искаме да отвори

file = open(file_path, 'r')


with open(file_path, 'a') as file:
    print(file.write('mq'))


print('ready')

# from PIL import Image
# im = Image.open('C:\\Users\\KIKO-ASUS\\Desktop\\Potato_save\\wallpepers\\kurumi\\674712.png')
#
# with im.show('image') as img:
#     im.show('image')
#     im.close()
#     time.sleep(1)
# print('ready')