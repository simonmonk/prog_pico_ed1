from machine import Pin, PWM

out_pin = PWM(Pin(16))
out_pin.freq(10000000)

out_pin.duty_u16(32768) # 50%
