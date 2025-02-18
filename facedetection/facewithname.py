import cv2
import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np 
import pickle
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   
GPIO.setup(7, GPIO.OUT, initial=GPIO.HIGH) 

#relay_pin = [26]

with open('labels', 'rb') as f:
    #dict = pickle.load(f)
    dict = pickle.load(f)
    f.close()

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

font = cv2.FONT_HERSHEY_SIMPLEX

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame = frame.array
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for (x, y, w, h) in faces:
        roiGray = gray[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roiGray)

        for name, value in dict.items():
            if value == id_:
                print(name)

        if conf >= 70:
            GPIO.output(7, GPIO.LOW) 
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, name + str(conf), (x, y), font, 2, (0, 0 ,255), 2,cv2.LINE_AA)

        else:
            GPIO.output(7, GPIO.HIGH) 

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    rawCapture.truncate(0)

    if key == 27:
        break

cv2.destroyAllWindows()
