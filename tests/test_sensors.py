from src.sensors import firealarm, humidity, laundryroom, temperature, message, smokealarm

def test_firealarm_fire():
    assert firealarm.fireAlarm("fire") == True

def test_firealarm_no_fire():
    assert firealarm.fireAlarm("Not a bbq, promise") == False

# def test_<functionname>():
# assert <functionname>.<functionname>(<parameters>) == <expected result>

#Example
def test_humidity_positive():
    assert humidity.humidity("10%") == .1

def test_humidity_negative():
    assert humidity.humidity("-5%") == -0.05

def test_laundryroom_positive():
    assert laundryroom.laundryRoom("100") == "100"

def test_laundryroom_words():
    assert laundryroom.laundryRoom("berry") == "berry"

def test_smokealarm_True():
    assert smokealarm.smokeAlarm("smoke") == True

def test_smokealarm_False():
    assert smokealarm.smokeAlarm("No smoke") == False

def test_temperature_positive():
    assert temperature.temperature("25") == 25

def test_temperature_negative():
    assert temperature.temperature("-535") == -535

def test_message_words():
    assert message.message("everything is working") == "everything is working"