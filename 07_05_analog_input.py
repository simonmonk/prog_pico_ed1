from machine import ADC, Pin
from utime import sleep

analog = ADC(28)

while True:
    reading = analog.read_u16()
    print(reading)
    sleep(0.5)