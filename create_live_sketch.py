import cv2
import numpy as np

def sketch(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

## open your webcam
cap = cv2.VideoCapture(0)

## run the show
while True:
    ret, frame = cap.read()
    cv2.imshow("Your Live Sketcher", sketch(frame))

    ## type q to exit the program
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()