import requests

from flask import Flask, render_template
from flask_apscheduler import APScheduler
from flask_cors import CORS

app = Flask(__name__)
scheduler = APScheduler()
CORS(app)

ip_addresses = {
    "Sera1": "127.0.0.1:8000",
    "Sera2": "",
    "Sera3": "",
    "Sera4": "",
}

temperatures = {
    "Sera1": 0,
    "Sera2": 0,
    "Sera3": 5,
    "Sera4": 0,
}


def collect_temperatures():
    for name, address in ip_addresses.items():
        if address:
            response = requests.get(f"http://{address}/get-temperature/")
            temperatures[response.json()["sera_name"]] = response.json()["temperature"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/current-temperatures/")
def current_temperature():
    return temperatures


@app.route("/set-temperature/", methods=["POST"])
def set_temperature():
    """
    JS'den post atılıp sera numarası ve değer verilecek, bu değerler ile o sera'nın
    ip'si ile endpointine istek atılacak.
    Alacak:
    {
      "sera_name": "Sera1",
      "temperature": 34
    }
    Gönderecek:
    {
      "temperature": 34
    }
    """
    pass


if __name__ == "__main__":
    scheduler.add_job(
        id="collect_temperatures",
        func=collect_temperatures,
        trigger="interval",
        seconds=1
    )
    scheduler.start()
    app.run(debug=True)
