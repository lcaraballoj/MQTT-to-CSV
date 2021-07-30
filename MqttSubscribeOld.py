import paho.mqtt.client as mqtt
import time
import csv
import datetime
import pandas as pd

def on_message (client, userdata, message):
    msg = message.payload.decode('utf-8')
    print ("Received message: ", msg)
    # if message.retain == 1:
    #     print("This is a retained message")
    print ("Type: ", type(msg), "\n")

    msgDict = eval(msg)

    print ("Type: ", type(msgDict), "\n")

    currentDateTime = datetime.datetime.now()
    dateTime = str(currentDateTime.strftime("%Y%m%dT%H%M%S"))+'.csv'

    try:
        df = pd.DataFrame.from_dict(msgDict)
        df.to_csv (dateTime, index = False, header = True)

        print ("Recorded in CSV file: ", dateTime)

    except ValueError as ve:
        print("Wrong type")

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Device")
client.connect(mqttBroker)

client.loop_start()

client.subscribe(topic = "Owl", qos = 1)
client.on_message = on_message

print ("Type: ", type(on_message))

time.sleep(1)

client.loop_stop()
