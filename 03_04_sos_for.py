from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT)

while True:
    for x in range(1, 4):
        led.on()
        sleep(0.2)
        led.off()
        sleep(0.2)
    sleep(0.4)
    for x in range(1, 4):
        led.on()
        sleep(0.6)
        led.off()
        sleep(0.6)
