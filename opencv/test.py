import cv2
import numpy as np

print(cv2.__version__)

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ans = False
    while ans == False:
        ret, frame = cap.read()
        ans = ret

    # Our operations on the frame come here
    frame = cv2.flip(frame, flipCode=1) 
    # ^ that command flips the image about y axis, making the camera act like a mirror

    # Display the resulting frame
    cv2.imshow('frame', frame)

    #pause, allowing the image to be displayed
    if cv2.waitKey(1)== ord('q'):
        break #quit if you press q during the pause

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()