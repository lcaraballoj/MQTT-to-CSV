import paho.mqtt.client as mqtt
import time
import json

def on_message (client, userdata, message):
        print ("Received message: ", json.loads(message.payload.decode('utf-8')))
        if message.retain == 1:
            print("This is a retained message")

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Device")
client.connect(mqttBroker)

client.loop_start()

client.subscribe(topic = "Test", qos = 1)
client.on_message = on_message

print ("Type: ", type(on_message))

time.sleep(300)

client.loop_end()

import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    topic = message.topic
    msg_decode = str(message.payload.decode('utf-8', 'ignore'))
    message_handler(client, msg_decode, topic)
    print ("Message Received")

def message_handler(client, message, topic):
    data = dict()
    data = eval(message)
