import helpers

def temperature(input):
    #for i in range(1,3600): do curl "http://localhost:5000/metric/temperature/$((50 + $RANDOM % 20 ))c"; sleep 1; done
    temp = float(input.strip('c'))
    p = helpers.Point("temperature").field("temperature", temp)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    print("Temperature:{0}c".format(temp))
    return temp

    #temp = float("25c".strip('c'))
    #temp = float("25")
    #temp = 25
    # print("Temperature:{0}c".format(25))
    # print("Temperature:25c")