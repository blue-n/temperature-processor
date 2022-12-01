import json

import helpers
from sensors import humidity, firealarm, laundryroom, temperature, smokealarm, message

from flask import Flask

from datetime import datetime
ts = datetime.now()
print("Timestamp is:", ts)

app = Flask(__name__)

#-----------------------------------------#

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
        return str(laundryroom.laundryRoom(enter))
    elif key == "temperature":
        return str(temperature.temperature(enter))
        #print("Temperature: ", value)
    elif key == "humidity":
        # What it might look like to factor in other logic than just the read  & print
        return str(humidity.humidity(enter))
    elif key == "smokeAlarm":
        return str(smokealarm.smokeAlarm(enter))
    elif key == "fireAlarm":
        return str(firealarm.fireAlarm(enter))
    elif key == "message":
        return str(message.message(enter))
    else:
        return str(key)

if __name__ == "__main__":
    #main()
    app.run(port=5001)
