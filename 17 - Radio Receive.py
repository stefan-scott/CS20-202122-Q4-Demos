# Radio Receive Demo:
# Mr. Scott
# June 9, 2022
# A look at basics of radio module usage (micro:bit)

import microbit, time

microbit.radio.on()  #enables radio module, power 6/7
microbit.radio.config(queue=30)
print("beginning to listen")

while True:
    # mailbox with 3 spaces
    incoming = microbit.radio.receive()
    if incoming != "None": 
        print(incoming)
    if microbit.button_a.was_pressed():
        microbit.radio.send("Mr. Scott")
        
        