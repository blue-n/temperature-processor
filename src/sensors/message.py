import helpers

def message(value):
    #defined the function message
    #processes the values that is connected to the defined function message and sends an alert/a string
    print(value)
    p = helpers.Point("message").field("message", value)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    return value
    #returns (refer to main.py) the value/data that it analyzed to the website