import helpers

def laundryRoom(value):
#defined the function laundryroom
#processes the value that was received for laundry room and returns the value to the url
    print(value)
    p = helpers.Point("laundryRoom").field("laundryRoom", value)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    return value
     #returns (refer to main.py) the value/data that it analyzed to the website