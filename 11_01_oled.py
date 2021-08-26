from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(0, sda=Pin(4), scl=Pin(5))
oled = SSD1306_I2C(128, 32, i2c)

oled.fill(0)
oled.rect(0, 0, 127, 31, 1)
oled.text("Programming the", 5, 2, 1)
oled.text("Raspberry Pi", 5, 12, 1)
oled.text("Pico", 5, 22, 1)

oled.show()