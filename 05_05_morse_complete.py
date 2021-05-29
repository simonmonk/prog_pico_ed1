from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT)

dot_duration = 0.2
dash_duration = dot_duration * 3
word_gap = dot_duration * 7

durations = {"." : dot_duration, "-" : dash_duration}

codes = {
    "a" : ".-",   "b" : "-...",  "c" : "-.-.",
    "d" : "-..",  "e" : ".",     "f" : "..-.",
    "g" : "--.",  "h" : "....",  "i" : "..",
    "j" : ".---", "k" : "-.-",   "l" : ".-..",
    "m" : "--",   "n" : "-.",    "o" : "---",
    "p" : ".--.", "q" : "--.-",  "r" : ".-.",
    "s" : "...",  "t" : "-",     "u" : "..-",
    "v" : "...-", "w" : ".--",   "x" : "-..-",
    "y" : "-.--", "z" : "--.."
}

def send_pulse(dot_or_dash):
    if dot_or_dash == '.':
        delay = dot_duration
    else:
        delay = dash_duration
    led.on()
    sleep(delay)
    led.off()
    sleep(delay)

def send_morse_for(character):
    if character == ' ':
        sleep(word_gap)
    else:
        dots_n_dashes = codes.get(character.lower())
        if dots_n_dashes:
            print(character + " " + dots_n_dashes)
            for pulse in dots_n_dashes:
                send_pulse(pulse)
            sleep(dash_duration)
        else:
            print("unknown character: " + character)
            

while True:
    text = input("Message: ")
    for character in text:
        send_morse_for(character)