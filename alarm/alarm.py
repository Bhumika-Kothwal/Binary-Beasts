from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    print("HTML page rendered")
    return render_template("alarmpage.html")


if __name__ == '__main__':
    app.run()
