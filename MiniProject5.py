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
    peri = cv.arcLength(cnt, True)
    approx=cv.approxPolyDP(cnt,0.04*peri,True)
    if len(approx)==3:
        shape='Triangle'
    elif len(approx)==4:
        shape='Sqaure'
    else:
        shape='Circle'
    face=cv.CascadeClassifier(cv.data.haarcascades+"haarcascade_frontalface_default.xml")
    faces=face.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv.imshow("Faces ",frame)
    if cv.waitKey(1) & 0xFF==27:
        break
img.release()
cv.destroyAllWindows()