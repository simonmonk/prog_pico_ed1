from machine import Pin
from utime import sleep

switch = Pin(10, Pin.IN, Pin.PULL_UP)
led = Pin(25, Pin.OUT)

while True:
    if switch.value() == 0:
        led.on()
        sleep(10)
        led.off()