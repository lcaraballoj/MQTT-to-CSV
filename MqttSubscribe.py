import paho.mqtt.client as mqtt
import time
import csv
import datetime
import pandas as pd
import ftplib

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
        
        send = send_to_ftp(dateTime)

        print ("Recorded in CSV file: ", dateTime)

        #return dateTime

    except ValueError as ve:
        print("Wrong type")

def send_to_ftp (csv):
    host = '127.0.0.1'
    username = 'ftpuser'
    passwd = 'owl'

    ftp_server = ftplib.FTP(host, username, passwd)
    ftp_server.encoding = "utf-8"

    testFile = open(csv, 'rb')

    ftp_server.storbinary("STOR %s" %csv, testFile)

    testFile.close()
    ftp_server.quit()

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Device")
client.connect(mqttBroker)

client.loop_start()

client.subscribe(topic = "Test", qos = 1)
client.on_message = on_message

print ("Type: ", type(on_message))

#send = send_to_ftp(client.on_message)

time.sleep(300)

client.loop_stop()

