import cv2
webcam = cv2.VideoCapture(0)
FaceDetector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
count = 0
while count < 30:
    ret, img = webcam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = FaceDetector.detectMultiScale(gray, 2, 3)
    print(face)
    for (x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w,y+h), (240, 65, 3), 5)
        face_resize = gray[y:y+h, x:x+w]
        picture = cv2.resize(face_resize, (130,100))
        cv2.imwrite(f"{count}.png", picture)
    count += 1
    cv2.imshow("webcam.mp4", img)
    k = cv2.waitKey(10)
    if k == 27:
        break