import helpers

def fireAlarm(value):
#defined the function firealarm
#processes the information/value from a string to a constant/number that is transfered to the database
    print(value)
    #created an if...else... statement
    if value.lower()=="fire":
        value = True
        print(1)
        print("DANGER: Fire Alert")
        #if fire is equal to "fire", then it will follow through with the command value= True
    else: 
        value = False
        print (0)
        print("No fire")
        #if fire does not equal to "fire" then it will follow through with the else command (value = false)
    p = helpers.Point("fireAlarm").field("fireAlarm", value)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    return value
     #returns (refer to main.py) the value/data that it analyzed to the website