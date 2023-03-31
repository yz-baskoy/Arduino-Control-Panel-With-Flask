import random
import serial
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SERA_NAME = "Sera2"


def get_temperature_from_arduino():
    arduinoData = ser.readline().decode('utf-8')
    if arduinoData != "":
        return float(arduinoData)
    else:
        return 0


def set_temperature_to_arduino(temperature):
    getData = str(temperature)
    if getData != "":                                    
        ser.write(getData.encode())  
    pass


@app.route("/get-temperature/")
def get_temperature():
    temperature = get_temperature_from_arduino()
    data = {
        "sera_name": SERA_NAME,
        "temperature": temperature
    }
    return data


@app.route("/set-temperature/", methods=["POST"])
def set_temperature():
    set_temperature_to_arduino(request.json["temperature"])


if __name__ == '__main__':
    ser = serial.Serial('COM1', baudrate = 9600, timeout=1)
    app.run(port=8000, debug=True)
