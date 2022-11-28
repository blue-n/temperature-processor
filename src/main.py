import json

import helpers
from sensors import humidity, firealarm

from flask import Flask

from datetime import datetime
ts = datetime.now()
print("Timestamp is:", ts)

app = Flask(__name__)

#-----------------------------------------#

def temperature(input):
    #for i in range(1,3600): do curl "http://localhost:5000/metric/temperature/$((50 + $RANDOM % 20 ))c"; sleep 1; done
    temp = float(input.strip('c'))
    p = helpers.Point("temperature").field("temperature", temp)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    print("Temperature:{0}c".format(temp))
    return temp

    #temp = float("25c".strip('c'))
    #temp = float("25")
    #temp = 25
    # print("Temperature:{0}c".format(25))
    # print("Temperature:25c")

def laundryRoom(value):
    print(value)
    p = helpers.Point("laundryRoom").field("laundryRoom", value)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    return value

def smokeAlarm(input):
    print(input)
    if input.lower() == "smoke":
        metric = True
        print(1)
        print("DANGER: Smoke Alert")
    else: 
        metric = False
        print(0)
        print("No smoke")
    p = helpers.Point("smokeAlarm").field("smokeAlarm", metric)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    return metric
#change a false = 0 and true = 1
#if smoke is equal to "smoke", then follow through with the command metric= True
#if smoke does not equal to smoke then it will follow through with the else command (metric = false)

def message(value):
    print(value)
    p = helpers.Point("message").field("message", value)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    return value

""" def main():
    with open('sensor.json', 'r') as f:
        data = json.load(f)

    for item in data:
        for key, value in item.items():
            # print(item)
            # print(item["laundryRoom"])

            if key == "laundryRoom":
                print("Laundry Room: ", value)
            elif key == "temperature":
                temperature(value)
                #print("Temperature: ", value)
            elif key == "humidity":
                # What it might look like to factor in other logic than just the read  & print
                humidity(value)
            elif key == "smokeAlarm":
                print("Smoke Alarm: ", value)
            elif key == "fireAlarm":
                print("Fire Alarm: ", value)
            elif key == "message":
                message(value)
            else:
                print(key) """

@app.route("/metric/<key>/<enter>")
def processor(key, enter):
    if key == "laundryRoom":
        return str("Laundry Room: "+ enter)
    elif key == "temperature":
        return str(temperature(enter))
        #print("Temperature: ", value)
    elif key == "humidity":
        # What it might look like to factor in other logic than just the read  & print
        return str(humidity.humidity(enter))
    elif key == "smokeAlarm":
        return str(smokeAlarm(enter))
    elif key == "fireAlarm":
        return str(firealarm.fireAlarm(enter))
    elif key == "message":
        return str(message(enter))
    else:
        return str(key)

if __name__ == "__main__":
    #main()
    app.run(port=5001)
