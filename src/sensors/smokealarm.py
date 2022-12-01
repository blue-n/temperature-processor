import helpers

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
