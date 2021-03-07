import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# assigning the trained data sets
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
fullbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# initializing iteration of the full process
while True:
    ret, frame = cap.read()
    b, a, c = frame.shape

    # allocating line coordinates
    left_coordinates = int( (a / 2) / 2)

    right_coordinates = int( (a / 2) + left_coordinates)


    #drawing vertical lines
    cv2.line(frame, (left_coordinates, 0), (left_coordinates, b), (0, 255, 0), 5)
    cv2.line(frame, (right_coordinates, 0), (right_coordinates, b), (0, 255, 0), 5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    
    # rectangle for the frontal face
    for (x, y, w, h) in faces:
        current_x = x
        current_y = x + w
        current = [(x, y), (x+w , y+h)]
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w , x:x+w]
        if current_x > left_coordinates:
            print('fine')
        elif current_y > right_coordinates:
            print('none')
        else:
            print('your out')
        print(x, y, x+w, y+h)
    
    cv2.imshow('track', frame)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
