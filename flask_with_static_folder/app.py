from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from drowsiness_detection import DrowsinessEyeYawn

app = Flask(__name__)
socketio = SocketIO(app)

eye_closure_count = 0
yawn_duration_count = 0

@app.route('/')
def home():
    print("SERVER STARTED")
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print("SOCKET CONNECTED")


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    global eye_closure_count ,yawn_duration_count
    obj = DrowsinessEyeYawn()
    left_eye = []
    right_eye = []
    mouth_coordinate = []
    lefteye = json['data'][0]['landmarks']['_positions'][36:42]
    righteye = json['data'][0]['landmarks']['_positions'][42:48]    # net_mouth_ratio = obj.calculate_net_mouth_ratio(shape[60:68])
    mouth = json['data'][0]['landmarks']['_positions'][60:68]
    for eye in lefteye:
        left_eye.append([eye['_y'], eye['_x'] ])
    for eye in righteye:
        right_eye.append([eye['_y'], eye['_x'] ])
    for m in mouth:
        mouth_coordinate.append([m['_y'], m['_x'] ])

    net_eye_ratio = obj.calculate_net_eye_ratio(left_eye, right_eye)
    net_mouth_ratio = obj.calculate_net_mouth_ratio(mouth_coordinate)

    if net_eye_ratio < 0.302:
        eye_closure_count += 1
    else:
        eye_closure_count = 0
    if net_mouth_ratio > 0.4:
        yawn_duration_count += 1
    else:
        yawn_duration_count = 0
    # print("eye ratio= "+ str(net_eye_ratio) + "    mouth ratio= "+ str(net_mouth_ratio) + "  eye closure count=" + str(eye_closure_count) + "  yawn count=" + str(yawn_duration_count) )
    if (eye_closure_count >= 40) | (yawn_duration_count > 10):
        return "PLAY"
    else:
        return None



if __name__ == '__main__':
    socketio.run(app)
