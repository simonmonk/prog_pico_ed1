from machine import Pin, I2C, Timer
from ssd1306 import SSD1306_I2C

i2c = I2C(0, sda=Pin(4), scl=Pin(5))
oled = SSD1306_I2C(128, 32, i2c)

h, m, s = (12, 0, 0)

def show_time():
    oled.fill(0)
    time_str = "{:02d}:{:02d}:{:02d}".format(h, m, s)
    print(time_str)
    oled.text(time_str, 0, 0, 1)
    oled.show()

def tick(timer):
    global h, m, s
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
    show_time()

Timer().init(freq=1, mode=Timer.PERIODIC, callback=tick)