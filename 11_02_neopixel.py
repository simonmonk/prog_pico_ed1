import array, time
from machine import Pin
import rp2
from random import randint

NUM_LEDS = 24

# Start of Magic programmable IO code
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(22))
sm.active(1) # Start the StateMachine
pixels = array.array("I", [0 for _ in range(NUM_LEDS)])
# End of Magic programmable IO code

def set_led(led, red, green, blue):
    pixels[led] = (red << 16) + (green << 8) + blue

def show():
    sm.put(pixels, 8)

def clear():
    for i in range(NUM_LEDS):
        set_led(i, 0, 0, 0)
    show()
    
def randomize():
    clear()
    for i in range(NUM_LEDS):
        set_led(i, randint(0, 50), randint(0, 50), randint(0, 50))
        show()
        time.sleep(0.1)
    
clear()

print("Enter the LED's number to turn it on")
print("or c-clear r-randomize")
while True:
    led_str = input("command: ")
    if (led_str == 'c'):
        clear()
    elif (led_str == 'r'):
        randomize()
    else:
        led = int(led_str)
        set_led(led, 50, 50, 50) # white
        show()
