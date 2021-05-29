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

def send_morse_for(character):
    if character == ' ':
        print("space")
    else:
        dots_n_dashes = codes.get(character.lower())
        if dots_n_dashes:
            print(character + " " + dots_n_dashes)
        else:
            print("unknown character: " + character)
            
while True:
    text = input("Message: ")
    for character in text:
        send_morse_for(character)