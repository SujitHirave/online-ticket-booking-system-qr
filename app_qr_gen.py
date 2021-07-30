import qrcode
from PIL import Image
import cv2
import imutils
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from time import strftime
import os
def function2():
    qr = qrcode.QRCode(version=12,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=2,border=8)
    df = pd.read_csv("Data.csv")

    for ind in df.index :


        Name = df['Name'][ind]

        Email= df['Email'][ind]
        Contact= df['Contact'][ind]
        Location= df['Location'][ind]

        # for index in range(len(df)):
        # data=[]
        data = f'''
        Name: {Name} \n

        Email: {Email} \n
        Contact:{Contact} \n
        Location:{Location}
        '''

        qr.add_data(data)
    qr.make()
    img = qr.make_image()
    img.save('qrcode_test_csv_5.png')




    img = 255*np.ones((512,512,3), np.uint8)
    cv2.rectangle(img, (10, 50), (500, 100), (0, 255, 255), -1)
    cv2.putText(img,'Date-',(10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,0),2,cv2.LINE_8)
    cv2.putText(img, strftime("%d:%m:%Y"), (55,90), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2,cv2.LINE_8)
    cv2.putText(img,'Time-',(10,70), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,0),2,cv2.LINE_4)
    cv2.putText(img, strftime("%H:%M:%S"), (56,70), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2,cv2.LINE_8)

    cv2.putText(img,'TMPL',(200,150), cv2.FONT_ITALIC, 1.5,(0,0,128),2,cv2.LINE_4)

    cv2.line(img, (10,155), (500,155), (0,0,0), 2)

    cv2.putText(img,'Name:',(10,190), cv2.FONT_ITALIC, 0.6,(0,0,0),2,cv2.LINE_4)
    cv2.putText(img,'Location:',(10,220), cv2.FONT_ITALIC, 0.6,(0,0,0),2,cv2.LINE_4)
    df = pd.read_csv("Data.csv")
    for ind in df.index :


        Name = df['Name'][ind]
        cv2.putText(img,f'{Name}',(70,190), cv2.FONT_ITALIC, 0.6,(255,0,128),2,cv2.LINE_4)
        cv2.putText(img,f'{Location}',(95,220), cv2.FONT_ITALIC, 0.6,(255,0,128),2,cv2.LINE_4)

    # cv2.imshow("img",img)
    # cv2.waitKey(0)
    cv2.imwrite('image.jpg', img)
    img_bg =  Image.open('image.jpg')

    img_qr = Image.open('qrcode_test_csv_5.png')

    pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])

    img_bg.paste(img_qr, pos)
    img_bg.save('qrcode_Final_4.png')

    os.remove('image.jpg')
    os.remove('qrcode_test_csv_5.png')
    os.remove('Data.csv')


def function3():
    from pyzbar.pyzbar import decode
    from PIL import Image

    # d=decode(Image.open('qrcode_test_1.png'))
    # d=decode(Image.open('qrcode_test_2.png'))
    d=decode(Image.open('qrcode_Final_4.png'))
    # d=decode(Image.open('qrcode_greet_4.png'))
    print(d[0].data.decode())

# function3()
