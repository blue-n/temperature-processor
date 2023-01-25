import helpers

def temperature(input):
#the function temperature is defined
#Processes the temperature value that was received from the url/website and returns the value back as a string
    temp = float(input.strip('c'))
    p = helpers.Point("temperature").field("temperature", temp)
    helpers.influxWrite.write(bucket=helpers.myBucket, record=p)
    print("Temperature:{0}c".format(temp))
    return temp
     #returns (refer to main.py) the value/data that it analyzed to the website

    #temp = float("25c".strip('c'))
    #temp = float("25")
    #temp = 25
    # print("Temperature:{0}c".format(25))
    # print("Temperature:25c")