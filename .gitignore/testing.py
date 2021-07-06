import json
import random
import datetime

currentDateTime = datetime.datetime.now()

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

print(msg)
