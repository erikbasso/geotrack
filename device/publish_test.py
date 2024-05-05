import paho.mqtt.publish as publish
import json

message = {"latitude": '123.456', "longitude": '987.654'}

payload = json.dumps(message)

publish.single("/Coordinate", payload=payload, hostname="localhost", port=1883)