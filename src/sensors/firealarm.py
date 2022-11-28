import helpers

def fireAlarm(value):
    print(value)
    if value.lower()=="fire":
        value = True
        print(1)
        print("DANGER: Fire Alert")
    else: 
        value = False
        print (0)
        print("No fire")
    p = helpers.Point("fireAlarm").field("fireAlarm", value)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    return value