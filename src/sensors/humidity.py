import helpers

def humidity(value):
#defined the function humidity
#processes the given value/input and returns it back as an integer that is then transferred/returned to the database
    pct = float(value.strip('%'))/100
    #it was divided by a 100 because it is a percentage
    p = helpers.Point("humidity").field("humidity", pct)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    print("Humidity: {0:.2%}".format(pct))
    return pct
     #returns (refer to main.py) the value/data that it analyzed to the website