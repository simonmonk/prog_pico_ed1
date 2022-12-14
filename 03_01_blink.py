from machine import Pin
from utime import sleep

led = Pin(16, Pin.OUT)

while True:
    led.on()
    sleep(0.5) # pause
    led.off()
    sleep(0.5)
    