import cv2

xml_haar_cascade = 'haarcascade_frontalface.xml'


#Carrega classificado
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)


#Inicia camera
capture = cv2.VideoCapture(0)
#capture = cv2.VideoCapture('http://192.168.0.200:8080/video')

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while not cv2.waitKey(20) & 0xFF == ord("q"):
    ret, frame_color = capture.read()

    gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)

    
    faces = faceClassifier.detectMultiScale(gray)

    print(faces)

    for x, y, w, h in faces:
        cv2.rectangle(frame_color, (x, y), (x + y, y + h), (0, 0, 255), 2 )

    cv2.imshow('color', frame_color)
    #cv2.imshow('gray', gray)


