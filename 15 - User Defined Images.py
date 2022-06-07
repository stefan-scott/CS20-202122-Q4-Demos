# Microbit User-Defined Images
# Mr. Scott
# June 7, 2022
# How to create our own images for Micro:bit

# NEXT TIME - use a for loop to animate the rolling sequence...

import microbit, time, random

dice_one = "44444:" \
           "40004:" \
           "40904:" \
           "40004:" \
           "44444"

# temp_image = microbit.Image(dice_one)
# microbit.display.show(temp_image)

dice_two = "44444:" \
           "40004:" \
           "49094:" \
           "40004:" \
           "44444"

dice_three = "44444:"\
             "40094:"\
             "40904:"\
             "49004:"\
             "44444"

dice_four = "44444:" \
            "49094:" \
            "40004:" \
            "49094:" \
            "44444"

dice_images = [dice_one, dice_two, dice_three, dice_four]
microbit.display.show(microbit.Image(random.choice(dice_images)))

# allow the user to actually "roll"
SHAKE_THRESHOLD = 200
while True:
    motion = microbit.accelerometer.get_z()
    print(motion)
#     time.sleep(0.4)
    if motion > SHAKE_THRESHOLD: #consider this a "shake"
        microbit.display.show(microbit.Image(random.choice(dice_images)))
        time.sleep(0.4) # "no shake detect" buffer time
    
    



