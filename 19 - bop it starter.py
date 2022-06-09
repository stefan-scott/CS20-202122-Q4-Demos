# Micro:bit Bop IT starter
# Mr. Scott
# June 9, 2022
# Beginning our bop-it game

import microbit, time, random

action_choices = ["A", "B", "L", "R"]
target_action = random.choice(action_choices)


while True:
    #main loop
    microbit.display.show(target_action) #display target action
    #update time variables
    
    
    #wait/check for user action
    if microbit.button_a.was_pressed():
        # check if it was correct
        if target_action == "A":
            #user was correct
            #display an image/animation showing it was correct
            #increase score
            #reset timer
            target_action = random.choice(action_choices)
    
    
    #check if time is elapsed??
