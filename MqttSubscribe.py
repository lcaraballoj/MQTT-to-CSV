import paho mqtt.client as mqtt
import time
import json
import random
import datetime
import csv
import pandas as pd

def on_message (client, userdata, message):
        print ("Received message: ", str(message.payload.decode('utf-8')))
        if message.retain == 1:
            print("This is a retained message")

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Device")
client.connect(mqttBroker)

client.loop_start()

client.subscribe(topic = "Test", qos = 1)
client.on_message = on_message

msg = eval(client.on_message)

fileName = str(currentDateTime.strftime("%Y%m%dT%H%M%S"))+'.csv'

df = pd.DataFrame.from_dict(msg)

df.to_csv(dateTime, index = False, header=True)

print ("Recorded in CSV file")

time.sleep(300)

client.loop_end()
