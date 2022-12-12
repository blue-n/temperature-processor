from sensors import humidity, firealarm, laundryroom, temperature, smokealarm, message

from flask import Flask

import os
from datetime import datetime
ts = datetime.now()
print("Timestamp is:", ts)

app = Flask(__name__)

host = os.getenv("TEMPERATURE_HOST", "127.0.0.1")
port = os.getenv("TEMPERATURE_PORT", 5001)

print("Hosted on host: ", host)
print("Hosted on port: ", port)

#-----------------------------------------#
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
    app.run(port=port, host=host)
