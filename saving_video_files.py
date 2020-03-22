import cv2
#open up the default camera
cap=cv2.VideoCapture(0)
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#25 fps
writer=cv2.VideoWriter('Capture_Me.mp4',cv2.VideoWriter_fourcc(*'XVID'),25,(width,height))
while True:
    ret,frame=cap.read()
    #capturing in grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    writer.write(frame)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
writer.release()
cv2.destroyAllWindows()        
        
