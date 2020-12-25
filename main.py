from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

temperatures = {
    "Sera1": 0,
    "Sera2": 0,
    "Sera3": 5,
    "Sera4": 0,
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/current-temperatures/")
def current_temperature():
    return temperatures


@app.route("/read-temperature/", methods=["POST"])
def read_temperature():
    temperatures[request.json["sera_number"]] = request.json["temperature"]
    return temperatures


@app.route("/set-temperature/", methods=["POST"])
def set_temperature():
    # temperatures[request.json["sera_number"]] = request.json["temperature"]
    # arduinoya da göndermek gerekiyor
    return temperatures


if __name__ == "__main__":
    app.run(debug=True)
