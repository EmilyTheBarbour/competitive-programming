import cv2
import numpy as np

lowerBound=np.array([33,80,40])
upperBound=np.array([102,255,255])
# lowerBound=np.array([0,     0,    100])
# upperBound=np.array([255,   50,     255])


height = 220
width = 340

cam= cv2.VideoCapture(0)
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

blankImage = np.zeros((height, width, 3), np.uint8)

font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,2,0.5,0,3,1)

while True:
    ret, img=cam.read()
    # img = cv2.imread('opencv\chrome_2018-04-22_15-29-35.png')
    img=cv2.resize(img,(width,height))

    #convert BGR to HSV
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # create the Mask
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal=maskClose
    conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    
    largestVal = 0
    largest = 0
    #cv2.drawContours(img,conts,-1,(255,0,0),3)
    for i in range(len(conts)):
        x,y,w,h=cv2.boundingRect(conts[i])
        if w*h > largestVal:
            largest = i
            largestVal = w*h
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
        #cv2.cv.PutText(cv2.cv.fromarray(img), str(x),(x,y+h),font,(x,y,255))
    blankImage = np.zeros((height, width, 3), np.uint8)

    try:
        
        x,y,w,h=cv2.boundingRect(conts[largest])
        y_offset = max(0, y - 50)
        x_offset = max(0, x - 50)
        w_offset = min(width - x_offset, w + 100)
        h_offset = min(height - y_offset, h + 100)
        region = img[y_offset:y_offset+h_offset, x_offset:x_offset+w_offset]
        pad_x = (width - w_offset) / 2
        pad_y = (height - h_offset) / 2

        for y in range(h_offset):
            for x in range(w_offset):
                blankImage[pad_y + y][pad_x + x] = region[y, x]

        cv2.imshow("region", blankImage)
    except:
        cv2.imshow("region", blankImage)

    cv2.imshow("maskClose",maskClose)
    cv2.imshow("maskOpen",maskOpen)
    cv2.imshow("mask",mask)
    cv2.imshow("cam",img)
    cv2.waitKey(10)