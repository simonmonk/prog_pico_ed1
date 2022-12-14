from machine import Pin
led = Pin(25, Pin.OUT) # For Pico W change 25 to LED see https://forums.raspberrypi.com/viewtopic.php?t=336836
led.on()
