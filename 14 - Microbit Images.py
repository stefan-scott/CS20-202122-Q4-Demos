# Micro:bit Images Demo
# Mr. Scott
# June 7, 2022
# Predefined and Custom Image usage

import microbit, time

# display a single image
# microbit.display.show(microbit.Image.ROLLERSKATE)

clock_images = [microbit.Image.CLOCK1,
                microbit.Image.CLOCK2,
                microbit.Image.CLOCK3,
                microbit.Image.CLOCK4,
                microbit.Image.CLOCK5,
                microbit.Image.CLOCK6,
                microbit.Image.CLOCK7,
                microbit.Image.CLOCK8,
                microbit.Image.CLOCK9,
                microbit.Image.CLOCK10,
                microbit.Image.CLOCK11,
                microbit.Image.CLOCK12 ]

#create an animation to cycle through these images. 0-11
current_index = 0
delay_amount = 0.1

while True:
    microbit.display.show(clock_images[current_index])
    current_index += 1
    #check if it's time to wrap around current_index
    if current_index > 11:
        current_index = 0
    
    time.sleep(delay_amount)




