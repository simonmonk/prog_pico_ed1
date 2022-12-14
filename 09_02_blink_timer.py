from machine import Pin, Timer
from utime import sleep

led = Pin(25, Pin.OUT) # For Pico W change 25 to LED see https://forums.raspberrypi.com/viewtopic.php?t=336836

def tick(timer):
    global led
    led.toggle()

Timer().init(freq=2, mode=Timer.PERIODIC, callback=tick)

x = 0
while True:
    print(x)
    x += 1
    sleep(1.2)  