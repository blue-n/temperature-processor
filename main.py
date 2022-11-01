import json

from datetime import datetime
ts = datetime.now()
print("Timestamp is:", ts)

def temperature(value):
  temp = float(value.strip('c'))
  print("Temperature:{0}c".format(temp))

  #temp = float("25c".strip('c'))
  #temp = float("25")
  #temp = 25
  #print("Temperature:{0}c".format(25))
  #print("Temperature:25c")

#smoke_alarm = ['red']
  #Having a bit of trouble with the if statements/ the true or false statements I was thinking if somehow I can colour code it so the computer knows like ok the smoke alarm is the colour red if it's red then nothing wrong, if it isn't then something is wrong

#if smoke_alarm == red:
  #print("There is nothing wrong")

  #elif:
    #print("Alarm is turned on")


def humidity(value):
    pct = float(value.strip('%'))/100
    print("Humidity: {0:.2%}".format(pct))

def humidity2(value):
    humid = float(value.strip('%'))/100
    print("Humidity:{0}".format(humid))

def main():
    with open('sensor.json', 'r') as f:
        data = json.load(f)

    for item in data:
      for key, value in item.items():
      #print(item)
      #print(item["laundryRoom"])
     

        if key == "laundryRoom":
            print("Laundry Room: ", value)
        elif key == "temperature":
            temperature(value)
              #print("Temperature: ", value)
        elif key == "humidity":
              #What it might look like to factor in other logic than just the read  & print
            humidity(value)
        elif key == "smokeAlarm"
          print("Smoke Alarm: ", value)
        elif key == "fireAlarm":
          print("Fire Alarm: ", value)
        elif key == "humidity2":
          print("Humidity: ", value)
        else:
            print(key)

if __name__ == "__main__":
    main()
