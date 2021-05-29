from machine import ADC, Pin
from utime import sleep
from math import sqrt

light_sensor = ADC(28)
dark_reading = 200
scale_factor = 2.5

def read_light():
    reading = light_sensor.read_u16()
    # print(reading)
    percent = int(sqrt(reading - dark_reading) / scale_factor)
    if percent < 0:
        percent = 0
    elif percent > 100:
        percent = 100
    return (percent)

while True:
    light_level = read_light()
    print(light_level)
    sleep(0.2)