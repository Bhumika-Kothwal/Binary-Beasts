from flask import Flask, render_template, send_from_directory
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

@app.route("/music/<path:filename>")
def loadfile(filename):
    return send_from_directory('/home/bhumika/app/basic/static/', filename)

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
    try:
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
        print("eye ratio= "+ str(net_eye_ratio) + "    mouth ratio= "+ str(net_mouth_ratio) )

        if net_eye_ratio < 0.25:
            eye_closure_count += 1
        else:
            eye_closure_count = 0
        if net_mouth_ratio > 0.35:
            yawn_duration_count += 1
        else:
            yawn_duration_count = 0
        if (eye_closure_count >= 40) | (yawn_duration_count > 7):
            socketio.emit('my response', True)
        else:
            socketio.emit('my response', False)
    except:
        print("Face not detected")

if __name__ == '__main__':
    socketio.run(app)
