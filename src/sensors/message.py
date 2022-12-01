import helpers

def message(value):
    print(value)
    p = helpers.Point("message").field("message", value)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    return value