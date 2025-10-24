from w1thermsensor import W1ThermSensor

def get_sensors():
    for sensor in W1ThermSensor.get_available_sensors():
       yield sensor
       
def get_celcius(sensor: W1ThermSensor):
    return sensor.get_temperature()

def get_sensor(id: str):
    return W1ThermSensor(sensor_id=id)