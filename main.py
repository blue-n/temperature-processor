import json

from flask import Flask

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

app = Flask(__name__)

myBucket = "sensor"
influxClient = InfluxDBClient(url="http://localhost:8086", token="initadmintoken", org="admin")
influxWrite = influxClient.write_api(write_options=SYNCHRONOUS)
influxRead = influxClient.query_api()

@app.route("/test_metric/temperature/<value>")
def test_metric(value):
    return str(temperature(value))

from datetime import datetime
ts = datetime.now()
print("Timestamp is:", ts)

def temperature(input):
    temp = float(input.strip('c'))
    p = Point("temperature").field("temperature", temp)
    influxWrite.write(bucket=myBucket, record=p)
    print("Temperature:{0}c".format(temp))
    return temp

    #temp = float("25c".strip('c'))
    #temp = float("25")
    #temp = 25
    # print("Temperature:{0}c".format(25))
    # print("Temperature:25c")

def laundryRoom(value):
    print(value)
    return value

def smokeAlarm(input):
    #print(value)
    if input.lower() == "false":
        metric = False
        print(0)
    else: 
        metric = True
        print(1)
    p = Point("smokeAlarm").field("smokeAlarm", metric)
    influxWrite.write(bucket=myBucket, record=p)
    return metric
#change a false = 0 and true = 1

def fireAlarm(value):
    print(value)
    if fireAlarm(value):
        value = False
        print(0)
        value = True
        print (1)
    p = Point("fireAlarm").field("fireAlarm", value)
    influxWrite.write(bucket=myBucket, record=p)
    return value

def humidity(value):
    pct = float(value.strip('%'))/100
    p = Point("humidity").field("humidity", pct)
    influxWrite.write(bucket=myBucket, record=p)
    print("Humidity: {0:.2%}".format(pct))
    return pct

def message(value):
    print(value)
    return value

def main():
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
                print(key)

@app.route("/metric/<key>/<enter>")
def processor(key, enter):
    if key == "laundryRoom":
        return str("Laundry Room: "+ enter)
    elif key == "temperature":
        return str(temperature(enter))
        #print("Temperature: ", value)
    elif key == "humidity":
        # What it might look like to factor in other logic than just the read  & print
        return str(humidity(enter))
    elif key == "smokeAlarm":
        return str(smokeAlarm(enter))
    elif key == "fireAlarm":
        return str("Fire Alarm: "+ enter)
    elif key == "message":
        return str(message(enter))
    else:
        return str(key)

if __name__ == "__main__":
    main()
