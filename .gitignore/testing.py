import json
import random
import datetime
import csv
import pandas as pd

test_csv = 'test.csv'

currentDateTime = datetime.datetime.now()

sourceList = ["Receiving" for n in range (0, 11)]
quantityList = ["speed", "torque", "current", "voltage", "VFD WH", "WinTemp1",
                "BearTemp1", "BearTemp2", "GearTemp", "GearBearTemp", "power mech"]
timeStampList = [currentDateTime.strftime("%Y/%m/%d, %H:%M:%S") for n in range (0,11)]
valueList = [random.randint(1,1500) for n in range (0,11)]

#Dictionary to hold values and headers
message = {'Source': sourceList,
            'Quantity': quantityList,
            'TimeStamp': timeStampList,
            'value': valueList}

msg = json.dumps(message)               #Convert dictionary to string

print("Type: ", type(msg), '\n')

print(msg, '\n')

newmsg = eval(msg)

print("Type: ", type(newmsg), '\n')

print(newmsg, '\n')


dateTime = str(currentDateTime.strftime("%Y%m%dT%H%M%S"))+'.csv'

# columnNames = ["Source", "Quantity", "TimeStamp", "value"]

# with open("test.csv", 'a') as csvFile:
#         wr = csv.DictWriter(csvFile, fieldnames=columnNames)
#         wr.writeheader()
#         for ele in newmsg:
#             wr.writerow(ele)

df = pd.DataFrame.from_dict(newmsg)

df.to_csv(dateTime, index = False, header=True)

print ("Recorded in CSV file")
