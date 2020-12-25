import random

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SERA_NAME = "Sera1"


def get_temperature_from_arduino():
    """
    Get temperature value from arduino, returns integer
    """
    return random.randint(20, 40)


def set_temperature_to_arduino(temperature):
    """
    Set (send) temperature value to arduino
    """
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
    """
    Ana flask app'inden gelen temperature değeri serial ile arduinoya gönderilecek
    Alacak:
    {
      "temperature": 34
    }
    set_temperature_to_arduino(gelen_veri["temperature"])
    """
    pass


if __name__ == '__main__':
    app.run(port=8000, debug=True)  # birden çok cihaz varken port ayarlamaya gerek yok
