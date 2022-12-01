import helpers

def laundryRoom(value):
    print(value)
    p = helpers.Point("laundryRoom").field("laundryRoom", value)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    return value