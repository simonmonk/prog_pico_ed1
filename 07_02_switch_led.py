from machine import Pin
from utime import sleep

switch = Pin(10, Pin.IN, Pin.PULL_UP)
led = Pin(25, Pin.OUT) # For Pico W change 25 to LED see https://forums.raspberrypi.com/viewtopic.php?t=336836

while True:
    if switch.value() == 0:
        led.on()
        sleep(10)
        led.off()