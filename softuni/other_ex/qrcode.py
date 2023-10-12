import pyqrcode
import png
from pyqrcode import QRCode

adress = 'https://memegenerator.net/instance/65295885/funny-cat-ahhhhhhhhh-now-i-see-youre-gay-p'
url = pyqrcode.create(adress)
url.png('example_qr.png', scale=8)