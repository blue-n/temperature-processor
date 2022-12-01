import helpers

def humidity(value):
    pct = float(value.strip('%'))/100
    #for i in range(1,3600): do curl "http://localhost:5000/metric/humidity/$((50 + $RANDOM % 20 ))"; sleep 1; done
    p = helpers.Point("humidity").field("humidity", pct)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    print("Humidity: {0:.2%}".format(pct))
    return pct