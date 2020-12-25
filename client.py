# import socket
# import serial
import random
import requests
import time

# ser = serial.Serial('COM1', baudrate = 9600, timeout=1)              # COM1 portundan 9600 bandında seri haberleşme başlat
# s = socket.socket()                                                  # socket haberleşme kütüphanesini import et
# host = "25.62.0.242"                                                # Sunucunun ip adresi
# port = 80                                                            # Sunucunun port numarası


while True:
    arduinoData = f"Sera{random.randint(1,4)}: {random.randint(20,40)}" # Sera4: 35
    sera_number = arduinoData.split(":")[0] # Sera4
    temperature = int(arduinoData.split(":")[1].strip()) # 35
    data = {
        "sera_number": sera_number,
        "temperature": temperature
    }
    requests.post("http://127.0.0.1:5000/read-temperature/", json=data)
    time.sleep(0.5)
