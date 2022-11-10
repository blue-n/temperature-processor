import json

from flask import Flask

app = Flask(__name__)

@app.route("/test_metric/temperature/<value>")
def test_metric(value):
    return str(temperature(value))

from datetime import datetime
ts = datetime.now()
print("Timestamp is:", ts)

def temperature(value):
    temp = float(value.strip('c'))
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

def smokeAlarm(value):
    print(value)
    return value

def fireAlarm(value):
    print(value)
    return value

def humidity(value):
    pct = float(value.strip('%'))/100
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

@app.route("/metric/<key>/<value>")
def processor(key, value):
    if key == "laundryRoom":
        return str("Laundry Room: "+ value)
    elif key == "temperature":
        return str(temperature(value))
        #print("Temperature: ", value)
    elif key == "humidity":
        # What it might look like to factor in other logic than just the read  & print
        return str(humidity(value))
    elif key == "smokeAlarm":
        return str("Smoke Alarm: "+ value)
    elif key == "fireAlarm":
        return str("Fire Alarm: "+ value)
    elif key == "message":
        return str(message(value))
    else:
        return str(key)

if __name__ == "__main__":
    main()
