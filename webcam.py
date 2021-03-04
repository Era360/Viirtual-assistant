import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

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


    for (x, y, w, h) in faces:
        current = [(x, y), (x+w , y+h)]
        left_bound = [(left_coordinates, 0), (left_coordinates, b)]
        right_bound = [(right_coordinates, 0), (right_coordinates, b)]

        if current > left_bound:
            print('fine')
        elif current < right_bound:
            print('correct')
        else:
            print('your out')

        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w , x:x+w]

        print(x, y, w, h)
    
    
    cv2.imshow('track', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
