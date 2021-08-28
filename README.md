# MQTT to CSV
A project to create MQTT messages, send them, read them, and then convert those MQTT messages into individual CSV files that will then be uploaded to a FTP server.
# Index
1. [The Why](#the-why)
2. [Process](#process)
3. [Understanding the Code](#understanding-the-code)
    1. [MqttPublish](#mqttpublish)
    2. [MqttSubscribe](#mqttsubscribe)
5. [Resources](#resources)

# The Why
MQTT messages are very common in IoT and converting them to CSV makes them easier to read and sort the data into a database.

MQTT is a lightweight publish/subscribe messaging protocol which is used for machine-to-machine communication. It accommodates bandwith and CPU limitations and was designed to be used with machines to provide a reliable and effective path for communication on devices. 

MQTT is bi-directiona and can be scaled to work with millions of devices in a reliable way and with many IoT devices, even those connecting over unreliable networks. Messages can also be easily encrypcted increasing the security making MQTT a powerful IoT messaging protocol.

# Process
1. Clone the GitHub repository
2. In the terminal run `pip install -r requirements.txt` to download the needed libraries
3. Create a MQTT broker or use an online one. (In this example an [online Mosquitto Eclipse broker](https://mqtt.eclipseprojects.io/) is used which limits the amount of messages that can be sent so creating a local one for use is ideal.)
4. In `MqttPublish.py` at the top of code edit: `mqttBroker = [MQTT Broker]` and in `MqttSubscribe.py` at the top of the function `def main()` edit: `mqttBroker = [MQTT Broker]` 
5. In `MqttPublish.py` users can change the data that is being outputted and even import/add functions to read sensor data
6. In `MqttSubscribe.py` users can choose to output the .csv file to a specific location or to a FTP server
7. To change the ftp server in `MqttSubscribe` edit this part of the code:
    ```
    def send_to_ftp(csv):
      host = [Host Name]
      username = [Username]
      passwd = [Password]
    ```
6. If users want to see their data being sent and received in real time they can download tmux and split the screen and then run both `MqttPublish.py` and `MqttSubscribe.py` and see the data flowing

# Understanding the Code
## MqttPublish
This Python script creates the MQTT message and sends it. 

In order for the code to run you need an *MQTT broker* and to understand what the end message is going to look like. This will help when formatting the MQTT message as it will later be converted to a CSV and understanding the desire format is important. 

The first part of the code is there to start the MQTT client by connecting to the broker: 
```
mqttBroker = "mqtt.eclipseprojects.io"      #Set broker
client = mqtt.Client()                      #Set MQTT client
client.connect(mqttBroker)                  #Connecting broker to client
```
The second part of the code is where the message is generated.
```
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
```
  
To understand this part of the code better it is helpful to understand what the desire outcome in the csv form will look like:

![image](https://user-images.githubusercontent.com/71469786/131067376-8555a127-7363-4ee4-a8bc-8898074daa98.png)

This shows that we need four columns, a header, and then 11 rows (not including the header). 

To start generating the message lets analyze the first part of the while loop, generating the lists of values:
```
    sourceList = ["Receiving" for n in range (0, 11)]
    quantityList = ["speed", "torque", "current", "voltage", "VFD WH", "WinTemp1",
                    "BearTemp1", "BearTemp2", "GearTemp", "GearBearTemp", "power mech"]
    timeStampList = [currentDateTime.strftime("%m/%d/%Y, %H:%M:%S") for n in range (0,11)]
    valueList = [random.randint(1,1500) for n in range (0,11)]
```

This part of the Python script generates a list of the rows in column form, so `sourceList = ["Receiving" for n in range (0,11)]` will be this part of the Excel sheet: 

![image](https://user-images.githubusercontent.com/71469786/131067395-3b70635e-6af1-4c0d-bcba-8050b00e4226.png)

The list will print out 11 strings of `"Recieving"`. 

All the other lists `quantityList`, `timeStampList`, and `valueList` provide similar results, but with different values based on the Excel sheet. For `timeStampList` it takes the `currentDateTime`, which is simply a time stamp, from the `datetime` library and `valueList` generates 11 random numbers for its values. 

Now lets take a look at the next section of code, the generation of the dictionary:
```
    #Dictionary to hold values and headers
    message = {'Source': sourceList,
                'Quantity': quantityList,
                'TimeStamp': timeStampList,
                'value': valueList}
```

This part of the code takes the lists we created above and uses them to create a key, value pair which is necessary for a dictionary.

The number of keys matches the number of desire columns, so the Excel file we are trying to replicate has 4 columns, thus we have 4 keys, each matching the value of the columns in the Excel. Each key is attached to one of the lists that we generated above and this is an example of what the dictionary will look like, keep in mind that the datetime and values will be different each time.

```
{'Source': ['Receiving', 'Receiving', 'Receiving', 'Receiving', 'Receiving', 'Receiving', 'Receiving', 'Receiving', 'Receiving', 'Receiving', 'Receiving'], 'Quantity':
['speed', 'torque', 'current', 'voltage', 'VFD WH', 'WinTemp1', 'BearTemp1', 'BearTemp2', 'GearTemp', 'GearBearTemp', 'power mech'], 'TimeStamp': ['08/27/2021, 
03:40:49', '08/27/2021, 03:40:49', '08/27/2021, 03:40:49', '08/27/2021, 03:40:49', '08/27/2021, 03:40:49', '08/27/2021, 03:40:49', '08/27/2021, 03:40:49', '08/27/2021, 
03:40:49', '08/27/2021, 03:40:49', '08/27/2021, 03:40:49', '08/27/2021, 03:40:49'], 'value': [1103, 160, 1046, 1215, 19, 652, 275, 74, 425, 647, 1394]}
```

We can see that it simply attaches all 11 values from the lists we generated above to the key we associated the lists with. So, `'Source': sourceList` generated `'Source': ['Receiving', 'Receiving', 'Receiving', 'Receiving', 'Receiving', 'Receiving', 'Receiving', 'Receiving', 'Receiving', 'Receiving', 'Receiving']`. 

Now looking at the last part of the code, this is what formats the MQTT message and sends it.
```
    msg = json.dumps(message)               #Convert dictionary to string

    client.publish (topic = "Owl", payload = msg, qos = 1, retain = False)     #Publish dictionary
    print(msg)      #See what is happening

    time.sleep(1)
```

We convert the dictionary type into a string type in order to send it as an MQTT message. This is because MQTT messages do not accept dictionary types, but do accept string types, so we simply have to make the dictionary a string, which will not affect the overall structure of the dictionary we already generated.

After doing this we must publish the message to the client using the broker. The topic can be changed, but make sure that it is the **same** in both `MqttSubscribe.py` and `MqttPublish.py`. We also print the message, so we see the dictionary, just to as a confirmation that everything went through, and then `time.sleep(1)` pauses the script for one second and then it continues until the program is canceled. 

## MqttSubscribe
This Python script subscribes, or receives, the messages that are being published, sent, from the `MqttPublish.py` script.

Just like with `MqttPublish.py` a *MQTT broker* is needed as well as a `FTP server` to save the csv files to. 

This script is made up of three functions, so let's look at the first function **`send_to_ftp(csv)`**: 
```
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
```

This function will send the received message to the FTP server. We are looking at this one first because this function is called within the function that reads the received MQTT message. 

The information for the ftp server, `host`, `username`, `passwd` may be different for each user, so be sure to coordinate logins. 
The next two lines of code are there to take actually connect to the FTP server using the `host`, `username`, and `passwd` infromation provided and then defines the type of data encoding. 

The next line of code `testFile = open(csv, 'rb)` takes a csv file and opens it and read it in binary mode, saving it under the temporary variable name `testFile`. 
`ftp_server.storbinary("STOR %s" %csv, testFile)` then stores that information in the FTP server.

The next two lines of code simply close the file that is being read and then ends the FTP server session.

The second function **`msg(client, userdata, message)`**:
```
def on_message (client, userdata, message):
    msg = message.payload.decode('utf-8')               #Decode MQTT Message
    print ("Received message: ", msg)                   #Message receipt
    print ("Type: ", type(msg), "\n")                   #Debug to see original message type
            
    msgDict = eval(msg)                                 #Convert MQTT Message to dictionary                               
    print ("Type: ", type(msgDict), "\n")               #Debug to see new message type

    currentDateTime = datetime.datetime.now()                           #Get current date and time
    dateTime = str(currentDateTime.strftime("%Y%m%dT%H%M%S"))+'.csv'    #Create filename for csv
    
    #Try to write the dictonary to a csv file
    try:
        df = pd.DataFrame.from_dict(msgDict)                            #Define the dataframes
        df.to_csv(dateTime, index = False, header =  True)              #Write dataframes to csv

        send = send_to_ftp(dateTime)                                    #Send the csv file to a FTPS

        print ("Recorded in CSV file: ", dateTime)                      #Confirming message is sent

    #Excepting to handle the wrong data type
    except ValueError as ve:
        print("Wrong type")
```
Is there to receive the message, covert it to a dictionary to be written as a csv, creates the csv file name, and then calls `send_to_ftp` to send it to the FTP server.

Let's breakdown this part of the code as it is what actually creates the csv file, though unlike `sent_to_ftp` much of this code should not need to be adjusted too much. 


The first couple of lines:
```
    msg = message.payload.decode('utf-8')               #Decode MQTT Message
    print ("Received message: ", msg)                   #Message receipt
```
receives the MQTT message and confirms receipt of the message by printing the message in the terminal.

Then in order for us to write the MQTT message to a csv file we must convert the message into a dictionary, `msgDict = eval(msg)` so that we can utilize the [Pandas](https://pypi.org/project/pandas/) functions. 

We then need to assign a filename to the csv file we will generate. 
```
   currentDateTime = datetime.datetime.now()                           #Get current date and time
   dateTime = str(currentDateTime.strftime("%Y%m%dT%H%M%S"))+'.csv'    #Create filename for csv
```
In this case we are just using a time stamp as a filename for the csv file. We do this by utilizing the datetime library and then formating it so that it will display the year, month, day, and then time, hours, minutes, and then seconds. 

The next part of the code uses a try and except block in order to prevent the program from crashing if a wrong type is detected. 
In the try block we have: 
```
        df = pd.DataFrame.from_dict(msgDict)                            #Define the dataframes
        df.to_csv(dateTime, index = False, header =  True)              #Write dataframes to csv

        send = send_to_ftp(dateTime)                                    #Send the csv file to a FTPS

        print ("Recorded in CSV file: ", dateTime)                      #Confirming message is sent

```

Which takes the dictionary and writes it to dataframes, a funtion of the [Pandas](https://pypi.org/project/pandas/) library, and then takes those dataframes and writes it to a csv file using the filename we generated `dateTime`. We then send it to the FTP server and send a confirmation that the message has been recored. 

The except block: 
```
    except ValueError as ve:
        print("Wrong type")
```
The Python ValueError exception is raised when the function receivest the wrong data type. It allows the code to keep running even if the wrong type is accepted whihc prevents crashes.

The third funtion is the **`main()`** function: 
```
def main():
    while True: 
        mqttBroker = "mqtt.eclipseprojects.io"                  #Server to recieve messages
        #mqttBroker = '10.2.0.4'
        client = mqtt.Client("Device")                          #Connect to MQTT Client
        client.connect(mqttBroker)                              #Connect client to broker

        client.loop_start()                                     #Start MQTT loop
        
        #client.connect(mqttBroker)

        client.subscribe(topic = "Owl", qos = 1)               #Subscribe
        client.on_message = on_message                          #Run function to take in message and perform required actions

        print ("Type: ", type(on_message))                      #Debug to print the received message

        #send = send_to_ftp(client.on_message)

        time.sleep(1)                                         #Time to wait for a message

        client.disconnect()

        client.loop_forever()                                   #Keep looping
```

The first several lines are the same as the first part of **`MqttPublish.py`**.

The next part creates a loop to continue to run the code to receive the messages, but we first need to subscribe to the client using the topic that we defined in **`MqttPublish.py`**. We then use the message received and use that as the parameter to run the `on_message` function. From here the rest of the code runs, and then the script is paused for a second before running again and will only stop when canceled.


# Resources
[Converting to CSV File](https://www.datasciencelearner.com/convert-python-dict-to-csv-implementation/)

[Converting to CSV File Using Pandas](https://www.datasciencelearner.com/convert-python-dict-to-csv-implementation/)

[Converting Dictionary to String](https://www.geeksforgeeks.org/python-convert-dictionary-object-into-string/)

[Python MQTT Messages](http://www.steves-internet-guide.com/mqtt-python-beginners-course/)

[How to setup and use FTP Server in Ubuntu Linux](https://linuxconfig.org/how-to-setup-and-use-ftp-server-in-ubuntu-linux)
