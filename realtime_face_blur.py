import cv2

## load the haarcascades xml
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascades/haarcascade_frontalface_default.xml') ## if file is in the same folder
face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

if face_cascade == None:
    print("face_cascade file not found")


## open your webcam
cap = cv2.VideoCapture(0)

## run the show
while True:
    success, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w] 
        blur = cv2.GaussianBlur(face_roi, (91, 91), 0)
        frame[y:y+h, x:x+w] = blur
    
    if faces == ():
        cv2.putText(frame, "No Face Found!", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))

    cv2.imshow("Face Blur", frame)

    ## type q to exit the program
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()