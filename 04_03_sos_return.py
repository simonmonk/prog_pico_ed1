from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT)

def blink(times, delay):
    for x in range(1, times+1):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
    return times * delay * 2
        
while True:
    print(blink(3, 0.2))
    sleep(0.4)
    print(blink(3, 0.6))
