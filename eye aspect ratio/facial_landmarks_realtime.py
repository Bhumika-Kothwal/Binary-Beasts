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
    print(A, B, C)
    ratio = (A+B)/(2.0*C)
    print(ratio)
    return ratio


# cap = cv.VideoCapture(0)
vs = VideoStream().start()
# while cap.isOpened():
while True:
    # _, image = cap.read()
    image = vs.read()
    image = imutils.resize(image, width=500)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    rects = detector(gray, 1)
    left_eye = []
    right_eye = []
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv.putText(image, "Face No. {}".format(i+1), (x-10, y-10), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)
        rng = range(37, 49)
        '''for (j, (a, b)) in zip(rng, shape[37:49]):
            cv.circle(image, (a, b), 1, (255, 0, 0), -1)
            if j < 43:
                left_eye.append((a, b))
            else:
                right_eye.append((a, b))
        left_eye_ratio = calculate_ratio(left_eye)
        #right_eye_ratio = calculate_ratio(right_eye)
        #net_ratio = (left_eye_ratio + right_eye_ratio) / 2.0
        #qnet_ratio = round(net_ratio, 3)
    # print(left_eye_ratio)
    # print(right_eye_ratio)'''
        left_eye_ratio = calculate_ratio(shape[37:43])
        right_eye_ratio = calculate_ratio(shape[43:49])
        net_ratio = (left_eye_ratio + right_eye_ratio) / 2
        net_ratio = round(net_ratio, 3)
        print('face no.= {}  ratio= {}'.format(i+1, net_ratio))
    cv.imshow('face shape detection using live video', image)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# cap.release()
cv.destroyAllWindows()
vs.stop()
