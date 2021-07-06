import paho mqtt.client as mqtt
import time

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
time.sleep(300)

client.loop_end()
