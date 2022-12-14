from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT) # For Pico W change 25 to LED see https://forums.raspberrypi.com/viewtopic.php?t=336836

while True:
    # This loop does 3 dots (S)
    for x in range(1, 4):
        led.on()
        sleep(0.2)
        led.off()
        sleep(0.2)
    sleep(0.4) # Gap between S and O
    # This loop does 3 dashes (O)
    for x in range(1, 4):
        led.on()
        sleep(0.6)
        led.off()
        sleep(0.6)
