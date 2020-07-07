from drowsiness_detection import DrowsinessEyeYawn
from imutils.video import VideoStream
from flask import Response
from flask import Flask, redirect, url_for
from flask import render_template
import threading
import argparse
import datetime
import imutils
from imutils import face_utils
import time
import cv2 as cv
import dlib

outputFrame = None
lock = threading.Lock()
detection = False
vs = VideoStream(src=0).start()

# getting the classifiers
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# initialize a flask object
app = Flask(__name__)


@app.route("/")
def index():
    # return the rendered template
    return render_template("index.html")


@app.route("/start", methods=['GET', 'POST', 'DELETE'])
def start():
    global detection
    detection = True
    return render_template("start.html")


def detect():
    global vs, outputFrame, lock, detection
    obj = DrowsinessEyeYawn()
    eye_closure_count = 0
    yawn_duration_count = 0
    while True:
        if detection is True:
            image = vs.read()
            image = imutils.resize(image, width=500)

            # grab the current timestamp and draw it on the frame
            timestamp = datetime.datetime.now()
            cv.putText(image, timestamp.strftime("%A %d %B %Y %I:%M:%S%p"), (10, image.shape[0] - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            rects = detector(gray, 1)
            for (i, rect) in enumerate(rects):
                shape = obj.detect_shape(gray, rect, predictor)
                (x, y, w, h) = face_utils.rect_to_bb(rect)
                cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv.putText(image, "Face No. {}".format(i + 1), (x - 10, y - 10), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0),
                           2)
                net_eye_ratio = obj.calculate_net_eye_ratio(shape[36:42], shape[42:48])
                net_mouth_ratio = obj.calculate_net_mouth_ratio(shape[60:68])
                if net_eye_ratio < 0.25:
                    eye_closure_count += 1
                else:
                    eye_closure_count = 0
                if net_mouth_ratio > 0.35:
                    yawn_duration_count += 1
                else:
                    yawn_duration_count = 0
                if (eye_closure_count >= 40) | (yawn_duration_count > 7):
                    obj.playalarm(image)

            with lock:
                outputFrame = image.copy()


def generate():
    # grab global references to the output frame and lock variables
    global outputFrame, lock

    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if outputFrame is None:
                continue

            # encode the frame in JPEG format
            (flag, encodedImage) = cv.imencode(".jpg", outputFrame)

            # ensure the frame was successfully encoded
            if not flag:
                continue

        # yield the output frame in the byte format
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')


@app.route("/video_feed")
def video_feed():
    # return the response generated along with the specific media
    # type (mime type)
    return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/start/stop")
def stop():
    global detection
    detection = False
    return redirect(url_for('index'))


if __name__ == '__main__':
    # start a thread that will perform drowsiness detection
    t = threading.Thread(target=detect)
    t.daemon = True
    t.start()
    # start the flask app
    app.run(debug=True, threaded=True, use_reloader=False)

vs.stop()