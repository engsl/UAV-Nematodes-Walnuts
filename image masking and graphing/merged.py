import cv2
import numpy as np
from PIL import Image

#masks the normal image to remove all non green in color range
def normalimgcrop(img1):
    hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    hsv_blur = cv2.GaussianBlur(hsv, (75,75), 0)

    lower_blue=np.array([25,19, 0])
    upper_blue = np.array([80 ,255,255])

    mask=cv2.inRange(hsv_blur, lower_blue,upper_blue)
    res=cv2.bitwise_and(img1,img1, mask=mask)

    cv2.imwrite('pics/normalimgcrop.jpg', res)

#masks IR image to remove all non blue in color range
def irimgcrop(img2):
    img2 = cv2.resize(img2, (640, 480))

    hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
    lower_blue=np.array([90,0,0])
    upper_blue = np.array([140 ,255,255])
    
    mask=cv2.inRange(hsv, lower_blue,upper_blue)
    res=cv2.bitwise_and(img2,img2, mask=mask)

    
    cv2.imwrite('pics/irimgcrop.jpg', res)

#overlays green image on top of blue to remove all non needed blue
def overlay(img1):
    img2 = cv2.imread('pics/irimgcrop.JPG')
    img1 = cv2.resize(img1, (640, 480))

    hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    hsv_blur = cv2.GaussianBlur(hsv, (75,75), 0)

    lower_blue=np.array([15,19, 0])
    upper_blue = np.array([80 ,255,255])

    mask=cv2.inRange(hsv_blur, lower_blue,upper_blue)
    res=cv2.bitwise_and(img2,img2, mask=mask)

    cv2.imwrite('pics/overlayedtree.jpg', res)

img1 = cv2.imread('pics/djitestnorm.JPG')
img2 = cv2.imread('pics/djitestir.JPG')

normalimgcrop(img1)
irimgcrop(img2)
overlay(img1)