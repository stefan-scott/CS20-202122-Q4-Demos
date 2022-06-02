# Micro:bit Crash Course
# Mr. Scott
# June 2, 2022
# An initial look at what we do with the micro:bit

import microbit  # don't you dare
                 # save your file as microbit.py
                 
import time, turtle, random

#turtle boilerplate
window = turtle.Screen()
window.setup(600,600)

#Global Variables
t = turtle.Turtle()


# SECTION THREE - ACCELEROMETER

# -1040              0             1040
# LEFT       |      FLAT    |      RIGHT
#           -400           400

turtleSize = 3
colors =  ["CadetBlue", "Coral", "DarkGoldenRod", "DarkOliveGreen",
          "DarkOrange", "FireBrick", "GreenYellow", "RosyBrown"]
t.pensize(turtleSize)

while True:
    
    x = microbit.accelerometer.get_x()
    
    if x < -400:
        direction = "LEFT"
        microbit.display.show(microbit.Image.ARROW_W)
    elif x > 400:
        direction = "RIGHT"
        microbit.display.show(microbit.Image.ARROW_E)
    else:
        direction = "FLAT"
        microbit.display.show("-")
        
    
    #Check for Button Events
    if microbit.button_a.was_pressed():
        #has the button been pressed since you last called this method?
        t.color(random.choice(colors))
    if microbit.button_b.was_pressed():
        #modify the pen size, and reset once it reaches a maximum amount
        turtleSize += 3
        if turtleSize > 20:
            turlteSize = 3
        t.pensize(turtleSize)
    print(turtleSize)
    #Turtle Motion:
    t.forward(10)
    if direction == "LEFT":
        t.left(20)
    elif direction == "RIGHT":
        t.right(20)
    

# SECTION TWO Microbit Button Input
# while True:
#     result = ""
#     if microbit.button_a.is_pressed():
#         result += "BUTTON A"
#     else:
#         result += "--------"
#         
#     if microbit.button_b.is_pressed():
#         result += "\tBUTTON B"
#     else:
#         result += "\t--------"
#         
#     print(result)




# SECTION ONE Microbit Display Functionality
# microbit.display.scroll("Hey there, CS20")

# for letter in ["S", "A", "S", "K"]:  #collections : list, string
#     microbit.display.show(letter)  #displays one char at a time
#     time.sleep(0.5)  #delay measured in seconds
#     
# for letter in "ATCHEWAN":
#     microbit.display.show(letter)  #displays one char at a time
#     time.sleep(0.2)  #delay measured in seconds