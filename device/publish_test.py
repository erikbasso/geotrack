import paho.mqtt.publish as publish
import json

message = {"device_id": 'b5b7e6405b904e43b14e29ae6c8d4d98',"latitude": '123.456', "longitude": '987.654'}

payload = json.dumps(message)

publish.single("/Coordinate", payload=payload, hostname="localhost", port=1883)