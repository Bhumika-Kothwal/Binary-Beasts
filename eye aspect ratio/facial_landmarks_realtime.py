from imutils import face_utils
from imutils.video import VideoStream
import numpy as np
import imutils
import dlib
import cv2 as cv
from scipy.spatial import distance as d


def calculate_ratio(eye):
    A = d.euclidean(eye[1], eye[5])
    B = d.euclidean(eye[2], eye[4])
    C = d.euclidean(eye[0], eye[3])
    ratio = (A+B)/(2.0*C)
    return ratio


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
# cap = cv.VideoCapture(0)
vs = VideoStream().start()
# while cap.isOpened():
count = 0
while True:
    # _, image = cap.read()
    image = vs.read()
    image = imutils.resize(image, width=500)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    left_eye = []
    right_eye = []
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv.putText(image, "Face No. {}".format(i+1), (x-10, y-10), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)
        left_eye_ratio = calculate_ratio(shape[36:42])
        right_eye_ratio = calculate_ratio(shape[42:48])
        net_ratio = (left_eye_ratio + right_eye_ratio) / 2
        net_ratio = round(net_ratio, 3)
        if net_ratio < 0.21:
            count += 1
        else:
            count = 0
        if count >= 40:
            cv.putText(image, "Are you drowsy??", (x-40, y-40), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
        print('face no.= {}  ratio= {}'.format(i+1, net_ratio))
    cv.imshow('face shape detection using live video', image)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# cap.release()
cv.destroyAllWindows()
vs.stop()
