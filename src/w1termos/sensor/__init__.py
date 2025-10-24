from w1thermsensor import W1ThermSensor

def get_sensors():
    for sensor in W1ThermSensor.get_available_sensors():
       yield sensor