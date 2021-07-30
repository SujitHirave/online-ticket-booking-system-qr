
from pyzbar.pyzbar import decode
from PIL import Image

d=decode(Image.open('qrcode_Final_4.png'))
# d=decode(Image.open('qrcode_test_2.png'))
# d=decode(Image.open('qrcode_face_3.png'))
# d=decode(Image.open('qrcode_greet_4.png'))
print(d[0].data.decode())
