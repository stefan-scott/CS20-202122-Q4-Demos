# L-Systems Demo
# Mr. Scott
# June 10, 2022
# Turtle Graphics Lindenmeyer System

import turtle
t = turtle.Turtle()
win = turtle.Screen()
win.setup(700,700)
t.speed(0)

t.up()
t.goto(-350,0)
t.down()

win.delay(0) 
#win.tracer(False)



def apply_rules(ch):
    #Apply our rules to the current character ch
    if ch == "L":
        return "+RF-LFL-FR+"
    elif ch == "R":
         return "-LF+RFR+FL-"
    else:
        #if the character has no associate rule
        return ch

def process_string(original_str):
    #loop through original_str and apply L-System rules
    next_str = ""
    for c in original_str:
        next_str += apply_rules(c)
    return next_str

def create_l_system(num_iters, axiom):
    #Run the L-System for num_iters generations
    start_string = axiom
    end_string = ""
    for i in range(num_iters):
        end_string = process_string(start_string)
        start_string = end_string
    return end_string

def draw_l_system(instructions, angle, distance):
    # have the turtle interpret out L-system string
    # and visualize it
    for cmd in instructions:
        if cmd == "F":
            t.fd(distance)
        elif cmd == "B":
            t.bk(distance)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)

commands = create_l_system(8, "L")
draw_l_system(commands, 90, 3)


# Accumulator Warm-up
# Task: Multiplication through repeated addition
# 5 x 7   →  7 + 7 + 7 + 7+ 7     

# def my_mult(a, b):  #a*b
#     #calculate the multiplication through
#     #repeated addition
#     result = 0
#     for i in range(b):
#         result += a
#     return result
        
#1:  r: 0+5 = 5
#2:  r: 5+5 = 10
#3:  r: 10+5 = 15

