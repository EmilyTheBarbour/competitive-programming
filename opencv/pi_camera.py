# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

resolution = (160, 120)

lowerBound=np.array([33,80,40])
upperBound=np.array([102,255,255])

kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

blankImage = np.zeros((resolution[1], resolution[0], 3), np.uint8)

camera = PiCamera()
camera.resolution = resolution
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=resolution)

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    img = frame.array

    #convert BGR to HSV
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # create the Mask
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    #morphology
    maskOpen = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose = cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal = maskClose
    image, conts, h = cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    largestVal = 0
    largest = 0
    for i in range(len(conts)):
        x,y,w,h=cv2.boundingRect(conts[i])
        if w*h > largestVal:
            largest = i
            largestVal = w*h
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
    blankImage = np.zeros((resolution[1], resolution[0], 3), np.uint8)

    try:
        x,y,w,h=cv2.boundingRect(conts[largest])
        y_offset = max(0, y - 50)
        x_offset = max(0, x - 50)
        w_offset = min(resolution[0] - x_offset, w + 100)
        h_offset = min(resolution[1] - y_offset, h + 100)
        region = img[y_offset:y_offset+h_offset, x_offset:x_offset+w_offset]
        pad_x = (resolution[0] - w_offset) / 2
        pad_y = (resolution[1] - h_offset) / 2
        for y in range(h_offset):
            for x in range(w_offset):
                blankImage[pad_y + y][pad_x + x] = region[y, x]

        cv2.imshow("region", blankImage)
    except:
        cv2.imshow("region", blankImage)
    
    cv2.imshow("frame", img)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        break
