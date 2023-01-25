import json

import helpers
#importing the file helpers.py that is under the folder src
from sensors import humidity, firealarm, laundryroom, temperature, smokealarm, message
#from the file sensors under the folder src, import all the files related to the sensors

from flask import Flask
#flask helps to create a web application which is where you would be testing the code making sure it works

from datetime import datetime
#shows the time and date that each information/data is received and sent
ts = datetime.now()
print("Timestamp is:", ts)

app = Flask(__name__)

#-----------------------------------------#
@app.route("/metric/<key>/<enter>")
#(/metric/key/enter)connects the code to the website (like a url)
# the app.route is what helped create the website
def processor(key, enter):
#Defined the function processor
#takes the string/value from the url (website) and inputs it into one of the functions
    #Created an if..elif..else statement
    if key == "laundryRoom":
        return str(laundryroom.laundryRoom(enter))
        #return means that if key is equal to laundryroom (in this case) it will return the data as a string and it will go to where laundryroom is defined
        #returns the data back to the website that was made
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
