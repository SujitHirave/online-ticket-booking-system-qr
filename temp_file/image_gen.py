# from PIL import Image, ImageFont, ImageDraw, ImageEnhance



import cv2
from PIL import Image
import numpy as np
import pandas as pd
from time import strftime
import os
# # black blank image
# blank_image = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
# # print(blank_image.shape)
# # cv2.imshow("Black Blank", blank_image)
# # white blank image
# blank_image2 = 255 * np.ones(shape=[512, 512, 3], dtype=np.uint8)
# cv2.imshow("White Blank", blank_image2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Create a black image
img = 255*np.ones((512,512,3), np.uint8)

# font = cv2.FONT_HERSHEY_SIMPLEX



# cv2.putText(img,'Hack Projects',(10,500), font=font, (0,0,255),2)
cv2.rectangle(img, (10, 50), (500, 100), (0, 255, 255), -1)
cv2.putText(img,'Date-',(10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,0),2,cv2.LINE_8)
cv2.putText(img, strftime("%d:%m:%Y"), (55,90), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2,cv2.LINE_8)
cv2.putText(img,'Time-',(10,70), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,0),2,cv2.LINE_4)
cv2.putText(img, strftime("%H:%M:%S"), (56,70), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2,cv2.LINE_8)

cv2.putText(img,'TMPL',(200,150), cv2.FONT_ITALIC, 1.5,(0,0,128),2,cv2.LINE_4)

# line_thickness = 2
# cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), thickness=line_thickness)
cv2.line(img, (10,155), (500,155), (0,0,0), 2)

cv2.putText(img,'Name:',(10,190), cv2.FONT_ITALIC, 0.6,(0,0,0),2,cv2.LINE_4)
# Name=input()
df = pd.read_csv("Data.csv")
for ind in df.index :


    Name = df['Name'][ind]
    cv2.putText(img,f'{Name}',(70,190), cv2.FONT_ITALIC, 0.6,(255,0,128),2,cv2.LINE_4)

cv2.putText(img,'Location:',(10,220), cv2.FONT_ITALIC, 0.6,(0,0,0),2,cv2.LINE_4)
text=input()
cv2.putText(img,text,(95,220), cv2.FONT_ITALIC, 0.6,(255,0,128),2,cv2.LINE_4)

# cv2.imwrite('image.jpg', img)
# img_bg =  Image.open('image.jpg')
#
# img_qr = Image.open('qrcode_test_csv_5.png')
#
# pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])
#
# img_bg.paste(img_qr, pos)
# img_bg.save('qrcode_Final_4.png')
#
# os.remove('image.jpg')

# Display the image
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
