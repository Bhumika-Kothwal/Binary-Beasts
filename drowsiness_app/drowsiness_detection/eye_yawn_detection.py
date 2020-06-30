from imutils import face_utils
from scipy.spatial import distance as d
import sounddevice as sd
import soundfile as sf
import cv2 as cv

def calculate_ratio(eye):
    A = d.euclidean(eye[1], eye[5])
    B = d.euclidean(eye[2], eye[4])
    C = d.euclidean(eye[0], eye[3])
    ratio = (A + B) / (2.0 * C)
    return ratio


class DrowsinessEyeYawn:
    def __init__(self):
        image = None

    def detect_shape(self, gray, rect, predictor):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        return shape

    def calculate_net_eye_ratio(self, lefteye, righteye):
        left_eye_ratio = calculate_ratio(lefteye)
        right_eye_ratio = calculate_ratio(righteye)
        net_ratio = (left_eye_ratio + right_eye_ratio) / 2
        net_ratio = round(net_ratio, 3)
        return net_ratio

    def calculate_net_mouth_ratio(self, mouth):
        P = d.euclidean(mouth[1], mouth[7])
        Q = d.euclidean(mouth[2], mouth[6])
        R = d.euclidean(mouth[3], mouth[5])
        S = d.euclidean(mouth[0], mouth[4])
        mouth_ratio = (P + Q + R) / (3.0 * S)
        return mouth_ratio

    def playalarm(self, image):
        cv.putText(image, "Are you drowsy??", (10, image.shape[0] - 40), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
        filename = 'alarm.wav'
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs)
        status = sd.wait()

