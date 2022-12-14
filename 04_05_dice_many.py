from machine import Pin
from utime import sleep
from random import randint

led = Pin(25, Pin.OUT) # For Pico W change 25 to LED see https://forums.raspberrypi.com/viewtopic.php?t=336836

def throw_dice(num_dice=1):
    total = 0
    for x in range(1, num_dice+1):
        total += randint(1, 6)
    return total

def blink(times, delay):
    for x in range(1, times+1):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
        
while True:
    input()
    dice_throw = throw_dice(num_dice=2)
    print(dice_throw)
    blink(dice_throw, 0.2)
    