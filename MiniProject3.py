import cv2 as cv
img=cv.VideoCapture(0)
while True:
    ret,frame=img.read()
    if not ret:
        break
    cv.imshow("Camera ",frame)
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    rett,thresh=cv.threshold(gray,127,255,cv.THRESH_BINARY)
    contours,hire=cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x,y,w,h=cv.boundingRect(cnt)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    if cv.waitKey(1) & 0xFF==27:
        break
img.release()
cv.destroyAllWindows()