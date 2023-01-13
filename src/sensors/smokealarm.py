import helpers

def smokeAlarm(input):
#smokealarm
    print(input)
    #Created an if statement
    if input.lower() == "smoke":
        metric = True
        print(1)
        print("DANGER: Smoke Alert")
        #if smoke is equal to "smoke", then follow through with the command metric= True
    else: 
        metric = False
        print(0)
        print("No smoke")
        #if smoke does not equal to smoke then it will follow through with the else command (metric = false)
    p = helpers.Point("smokeAlarm").field("smokeAlarm", metric)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    return metric
     #returns (refer to main.py) the value/data that it analyzed to the website
#false = 0 and true = 1

