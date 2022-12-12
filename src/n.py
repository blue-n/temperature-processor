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