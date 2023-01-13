import helpers

def message(value):
    #defined the function message
    print(value)
    p = helpers.Point("message").field("message", value)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    return value
    #returns (refer to main.py) the value/data that it analyzed to the website