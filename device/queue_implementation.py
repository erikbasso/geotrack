import threading

from django.conf import settings

from datetime import datetime

import uuid

import json, pika

import models

DeviceManager = models.Device.objects

class queue:
    def __init__(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()
    
    def run_queue(self):
        try:
            print("Tentativa de conexão com a fila (RabbitMQ)")

            connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
            channel = connection.channel()
            print("Conexão funcionou!")

            channel.queue_declare(queue = 'coordinates')

            def callback(ch, method, properties, body):
                try:
                    payload = body.decode('utf-8')
                    payload = json.loads(payload)
                    device_id = payload.get('device_id')
                    latitude = payload.get('latitude')
                    longitude = payload.get('longitude')
                    if DeviceManager.filter(id=device_id).exists():
                        coordinates = models.Coordinate(
                            latitude = latitude,
                            longitude = longitude,
                            datetime = datetime.now()
                        )
                        coordinates.save()
                except Exception as e:
                    print("Problema ao salvar mensagem no banco de dados!")


            channel.basic_consume(queue='coordinates', on_message_callback=callback, auto_ack = True)
            print("Esperando por mensagens")
            channel.start_consuming()

        except Exception as e:
            print("Falha na conexão com o broker!")
