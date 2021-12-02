from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import time

i2c = I2C(0, sda=Pin(4), scl=Pin(5))
oled = SSD1306_I2C(128, 32, i2c)

pushButton = Pin(17, Pin.IN, Pin.PULL_UP)
analog = ADC(28)

oled.fill(0)
oled.rect(0, 0, 127, 31, 1)

oled.text("Pico", 5, 22, 1)

oled.show()

while True:
    if pushButton.value() == 0:
        oled.fill(1)
        oled.show()
        time.sleep(1)
    reading = analog.read_u16() # 0 to 65535
    w = int(reading / 512)
    n = int(reading / 6553.5) 
    oled.fill(0)
    oled.fill_rect(0, 0, w, 31, 1)
    oled.text(str(n), 0, 10, 0)
    oled.show()
    