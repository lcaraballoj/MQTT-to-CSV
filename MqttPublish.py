#importing needed libraries
import paho.mqtt.client as mqtt
import random
import time
import datetime
import json

mqttBroker = "mqtt.eclipseprojects.io"      #Set broker
#mqttBroker = '10.2.0.4'
client = mqtt.Client()                      #Set MQTT client
client.connect(mqttBroker)                  #Connecting broker to client

#Keep runing infinitely
while True:
    currentDateTime = datetime.datetime.now()

    #Lists of values
    sourceList = ["Receiving" for n in range (0, 11)]
    quantityList = ["speed", "torque", "current", "voltage", "VFD WH", "WinTemp1",
                    "BearTemp1", "BearTemp2", "GearTemp", "GearBearTemp", "power mech"]
    timeStampList = [currentDateTime.strftime("%m/%d/%Y, %H:%M:%S") for n in range (0,11)]
    valueList = [random.randint(1,1500) for n in range (0,11)]

    #Dictionary to hold values and headers
    message = {'Source': sourceList,
                'Quantity': quantityList,
                'TimeStamp': timeStampList,
                'value': valueList}

    msg = json.dumps(message)               #Convert dictionary to string

    client.publish (topic = "Owl", payload = msg, qos = 1, retain = False)     #Publish dictionary
    print(msg)      #See what is happening

    time.sleep(1)
    #time.sleep(5)
