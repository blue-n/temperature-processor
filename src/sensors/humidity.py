import helpers

def humidity(value):
#defined the function humidity
    pct = float(value.strip('%'))/100
    #it was divided by a 100 because it is a percentage
    p = helpers.Point("humidity").field("humidity", pct)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    print("Humidity: {0:.2%}".format(pct))
    return pct
     #returns (refer to main.py) the value/data that it analyzed to the website