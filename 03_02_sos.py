from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT) # For Pico W change 25 to LED see https://forums.raspberrypi.com/viewtopic.php?t=336836

while True:
    # S
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.6)
    # O
    led.on()
    sleep(0.6)
    led.off()
    sleep(0.6)
    led.on()
    sleep(0.6)
    led.off()
    sleep(0.6)
    led.on()
    sleep(0.6)
    led.off()
    sleep(0.6)