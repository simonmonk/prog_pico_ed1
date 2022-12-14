from machine import Pin, PWM
from utime import sleep

led = PWM(Pin(25)) # For Pico W change 25 to LED see https://forums.raspberrypi.com/viewtopic.php?t=336836

while True:
    brightness_str = input("brightness (0-100):")
    brightness = int(int(brightness_str) * 65534 / 100)
    led.duty_u16(brightness)