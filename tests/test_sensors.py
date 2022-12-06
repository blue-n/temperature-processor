from src.sensors import firealarm, humidity, laundryroom, temperature, message, smokealarm

def test_firealarm_fire():
    assert firealarm.fireAlarm("fire") == True

def test_firealarm_no_fire():
    assert firealarm.fireAlarm("Not a bbq, promise") == False

# def test_<functionname>():
# assert <functionname>.<functionname>(<parameters>) == <expected result>

#Example
#def test_humidity():
#    assert humidity.humidity("10%") == .1
