import cv2
import datetime
import os

cap = cv2.VideoCapture(0)

## load the opencv haarcascades xml
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascades/haarcascade_frontalface_default.xml")
# smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascades/haarcascade_smile.xml")

face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_smile.xml")

## create the folder to save the images
smile_selfie_folder = 'smile_selfie'
if not os.path.exists(smile_selfie_folder):
    os.mkdir(smile_selfie_folder)

## run the show
while True:
    ret, frame = cap.read()
    
    original_frame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        face_roi = frame[y:y+h, x:x+w] 
        gray_roi = gray[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25) 

        for x1, y1, w1, h1 in smile:
            cv2.rectangle(face_roi, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2) 
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            file_name = f'{smile_selfie_folder}/selfie-{time_stamp}.png' 
            cv2.imwrite(file_name, original_frame)

    cv2.imshow('Smile Cam', frame)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()