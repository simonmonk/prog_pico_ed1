from machine import Pin
from utime import sleep
from random import randint

led = Pin(25, Pin.OUT)

def throw_dice():
    return randint(1, 6)

def blink(times, delay):
    for x in range(1, times+1):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
        
while True:
    input()
    dice_throw = throw_dice()
    print(dice_throw)
    blink(dice_throw, 0.2)


