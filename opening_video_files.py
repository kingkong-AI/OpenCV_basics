import cv2
import time
cap=cv2.VideoCapture('first_example.mp4')
fps=25
if cap.isOpened()==False:
    print('possible error in file path')
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        #show at the desired fps
        time.sleep(1/fps)
        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
# Closes all the frames
cv2.destroyAllWindows()        
    
