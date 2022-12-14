from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT) # For Pico W change 25 to LED see https://forums.raspberrypi.com/viewtopic.php?t=336836

delays = [0.2, 0.2, 0.2, 0.6, 0.6, 0.6]

while True:
    for delay in delays:
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
        