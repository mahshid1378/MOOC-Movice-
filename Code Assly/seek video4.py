import cv2
from circular_buffer import CircularBuffer
from pynput.mouse import Button, Controller

face_cascade = cv2.CascadeClassifier('C:/Users/hp 850/Desktop/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/hp 850/Desktop/haarcascade_eye_tree_eyeglasses.xml')
vid = cv2.VideoCapture(0)
roi_gray = None
roi_color = None
eyes_on_screen = True
circular_buffer = CircularBuffer(26)
mouse = Controller()

while vid.isOpened():
    _, frame = vid.read()

    #rescaling frame
    width = int(frame.shape[1] * 25/ 100)
    height = int(frame.shape[0] * 25/ 100)
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y , w ,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0 , 0), 1)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey ,ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 1)

    # Display the output
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    circular_buffer.record(len(eyes))
    previous_iteration = eyes_on_screen
    eyes_on_screen = sum([num > 0 for num in circular_buffer.log]) > circular_buffer.max_size / 2

    if previous_iteration != eyes_on_screen:
        mouse.position = (500, 500)
        mouse.press(Button.left)
        mouse.release(Button.left)

vid.release()