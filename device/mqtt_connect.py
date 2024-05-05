import os
import paho.mqtt.client as mqtt
import threading
from datetime import datetime
import json

class MqttConnect:

    def __init__(self):
        try:
            self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
            self.client.on_message = self.on_message
            self.client.connect("localhost", 1883, 3)
            self.client.subscribe("/Coordinate", qos=0)
            print('Conectado ao broker MQTT')
        except Exception as e:
            print("Não foi possível conectar com o broker MQTT:", str(e))

    def on_message(self, client, userdata, msg):
        print('Recebeu mensagem')
        payload = json.loads(msg.payload.decode('utf-8'))
        print(payload)


    def start(self):
        self.thread = threading.Thread(target=self.client.loop_forever)
        self.thread.start()