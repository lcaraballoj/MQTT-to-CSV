#Importing Libraries
import paho.mqtt.client as mqtt
import time
import csv
import datetime
import pandas as pd
import ftplib

#from pathlib import Path

#Function to receive message, convert to string, convert to dictionary, and then write to csv file
def on_message (client, userdata, message):
    msg = message.payload.decode('utf-8')               #Decode MQTT Message
    print ("Received message: ", msg)                   #Message receipt
    #print ("Type: ", type(msg), "\n")                   #Debug to see original message type
            
    msgDict = eval(msg)                                 #Convert MQTT Message to dictionary                               
    #print ("Type: ", type(msgDict), "\n")               #Debug to see new message type

    currentDateTime = datetime.datetime.now()                           #Get current date and time
    dateTime = str(currentDateTime.strftime("%Y%m%dT%H%M%S"))+'.csv'    #Create filename for csv
    #p = Path("./MQTT-to-CSV")
    
    #Try to write the dictonary to a csv file
    try:
        df = pd.DataFrame.from_dict(msgDict)                            #Define the dataframes
        #df.to_csv (Path(p, dateTime, index = False, header = True)
        df.to_csv(dateTime, index = False, header =  True)              #Write dataframes to csv

        send = send_to_ftp(dateTime)                                    #Send the csv file to a FTPS

        print ("Recorded in CSV file: ", dateTime)                      #Confirming message is sent

        #return dateTime

    #Excepting to handle the wrong data type
    except ValueError as ve:
        print("Wrong type")

#Function to send files to a FTP Server
def send_to_ftp (csv):
    host = '127.0.0.1'          #Define host
    username = 'ftpuser'        #Username for server
    passwd = 'owl'              #Password for server

    ftp_server = ftplib.FTP(host, username, passwd)     #Define FTP Server
    ftp_server.encoding = "utf-8"                       #Define type of data encoding of network

    testFile = open(csv, 'rb')                          #Open file

    ftp_server.storbinary("STOR %s" %csv, testFile)     #Store file data in FTP Server

    testFile.close()            #Close file
    ftp_server.quit()           #End user session


def main():
    while True: 
        mqttBroker = "mqtt.eclipseprojects.io"                  #Server to recieve messages
        client = mqtt.Client("Device")                          #Connect to MQTT Client
        client.connect(mqttBroker)                              #Connect client to broker

        client.loop_start()                                     #Start MQTT loop

        client.subscribe(topic = "Owl", qos = 1)               #Subscribe
        client.on_message = on_message                          #Run function to take in message and perform required actions

        print ("Type: ", type(on_message))                      #Debug to print the received message

        #send = send_to_ftp(client.on_message)

        time.sleep(1)                                         #Time to wait for a message

        client.disconnect()

        client.loop_forever()                                   #Keep looping


main()

