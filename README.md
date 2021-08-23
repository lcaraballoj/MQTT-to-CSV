# MQTT to CSV
A project to create MQTT messages, send them, read them, and then convert those MQTT messages into individual CSV files that will then be uploaded to the AWS cloud.
# Index
1. [The Why](#the-why)
2. [Process](#process)
3. [Resources](#resources)

# The Why
MQTT messages are very common in IoT and converting them to CSV makes them easier to read and sort the data into a database.

MQTT is a lightweight publish/subscribe messaging protocol which is used for machine-to-machine communication. It accommodates bandwith and CPU limitations and was designed to be used with machines to provide a reliable and effective path for communication on devices. 

MQTT is bi-directiona and can be scaled to work with millions of devices in a reliable way and with many IoT devices, even those connecting over unreliable networks. Messages can also be easily encrypcted increasing the security making MQTT a powerful IoT messaging protocol.

# Process
1. Create a MQTT broker or use an online one
2. In `MqttPublish.py` at the top of code edit: `mqttBroker = [MQTT Broker]` and in `MqttSubscribe.py` at the top of the function `def main()` edit: `mqttBroker = [MQTT Broker]` 
3. In `MqttPublish.py` users can change the data that is being outputted and even import/add functions to read sensor data
4. In `MqttSubscribe.py` users can choose to output the .csv file to a specific location or to a ftp server
5. To change the ftp server in `MqttSubscribe` edit this part of the code:
    ```
    def send_to_ftp(csv):
      host = [Host Name]
      username = [Username]
      passwd = [Password]
    ```
6. If users want to see their data being sent and received in real time they can download tmux and split the screen and then run both `MqttPublish.py` and `MqttSubscribe.py` and see the data flowing

# Resources
[Converting to CSV File](https://www.datasciencelearner.com/convert-python-dict-to-csv-implementation/)

[Converting to CSV File Using Pandas](https://www.datasciencelearner.com/convert-python-dict-to-csv-implementation/)

[Converting Dictionary to String](https://www.geeksforgeeks.org/python-convert-dictionary-object-into-string/)

[Python MQTT Messages](http://www.steves-internet-guide.com/mqtt-python-beginners-course/)

[How to setup and use FTP Server in Ubuntu Linux](https://linuxconfig.org/how-to-setup-and-use-ftp-server-in-ubuntu-linux)
