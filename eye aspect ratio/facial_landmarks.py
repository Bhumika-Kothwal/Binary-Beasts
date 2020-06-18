from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True, help='path to facial landmark predictor')
ap.add_argument('-i', '--image', required=True, help='path to input image')
args = vars(ap.parse_args())

# initializing dlib's face detector and creating facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# loading the input image, resize it, and convert it to grayscale
image = cv2.imread(args['image'])
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detecting face in grayscale image
rects = detector(gray, 1)

# looping over face detections
for (i, rect) in enumerate(rects):
    # determining the facial landmarks for face region
    # converting facial landmark (x,y)-coordinates to a NumPy
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)

    # converting dlib_s rectangle to a OpenCV-style bounding box
    (x, y, w, h) = face_utils.rect_to_bb(rect)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # showing face number
    cv2.putText(image, "Face #{}".format(i+1), (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    # looping over (x, y)-coordinates for facial landmarks and draw them on image
    for (a, b) in shape:
        cv2.circle(image, (a,b), 1, (0, 0, 255), -1)

cv2.imshow("Output", image)
cv2.waitKey(0)
