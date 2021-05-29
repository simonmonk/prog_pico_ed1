from machine import Pin, PWM
from utime import sleep

red_ch = PWM(Pin(16))
green_ch = PWM(Pin(17))
blue_ch = PWM(Pin(15))

button = Pin(12, Pin.IN, Pin.PULL_UP)
colors = [[255, 0, 0], [127, 127, 0],[0, 255, 0], [0, 127, 127], [0, 0, 255], [127, 0, 127]]

def set_color(rgb):
    red_ch.duty_u16(rgb[0] * 256)
    green_ch.duty_u16(rgb[1] * 256)
    blue_ch.duty_u16(rgb[2] * 256)

index = 0
set_color(colors[index])
while True:
    if button.value() == 0:
        index +=1
        if index >= len(colors):
            index = 0
        sleep(0.2)
    set_color(colors[index])
