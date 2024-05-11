import os
import paho.mqtt.client as mqtt
import threading
from datetime import datetime
import json
import pika

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
        print('mensagem recebida')

        try:

            payload = json.loads(msg.payload.decode('utf-8'))
            message_content = json.dumps(payload).encode('utf-8')

            #connecting to RabbitMQ Server
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
            channel = connection.channel()

            # creating a queue
            channel.queue_declare(queue='Coordinates')

            routing_key = 'coordinates'

            channel.basic_publish(
                exchange='',
                routing_key= routing_key,
                body=message_content
            )
            print("Foi enviado para a fila corretamente")

            connection.close()
            print(payload)

        except Exception as e:
            print("Falha ao processar a mensagem!")


    def start(self):
        self.thread = threading.Thread(target=self.client.loop_forever)
        self.thread.start()