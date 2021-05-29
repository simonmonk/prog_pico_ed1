from machine import Pin, Timer
from utime import sleep

led = Pin(25, Pin.OUT)

def tick(timer):
    global led
    led.toggle()

Timer().init(freq=2, mode=Timer.PERIODIC, callback=tick)

x = 0
while True:
    print(x)
    x += 1
    sleep(1.2)  