# Turtle Demo One
# Mr. Scott
# May 30th, 2022
# A first foray into using the turtle library

import turtle       # looks for a file called turtle.py
                    # it will look for it in the lib folder
                    # but it will look in the same folder
                    # as this program first.
                    #
                    # so don't name your file turtle.py !!!!
                    
# create and setup a window object
window = turtle.Screen()
window.bgcolor("LavenderBlush")  #RGB -> 16 million  Gamut,   CMYK, HSB/HSV,  LAB


# create at least one turtle object
my_turtle = turtle.Turtle()
my_turtle.color("MidnightBlue")
my_turtle.pensize(3)
my_turtle.speed(0)  #hyperspeed   like the think() in reeborg



#Part Three - Regular Polygons

def draw_triangle():
    #draw a regular polygon with 3 sides
    for i in range(3):
        my_turtle.forward(100)
        my_turtle.left(120)

def draw_pentagon():
    #draw a regular polygon with 5 sides
    for i in range(5):
        my_turtle.fd(100)
        my_turtle.left(72)

def r_poly(n, side_length):
    #draw n-sided regular polygon
    for i in range(n):
        my_turtle.fd(side_length)
        my_turtle.left(360/n)

#r_poly(5, 100)
r_poly(9, 60)
#r_poly(16, 30)






# Part Two -> use some control structures to make something cool

def draw_square(side_length, line_color, pen_thickness):
    # A function to have the turtle draw a square:
    # side_length    -> (INT) length of a side
    # line_color     -> (colorstring) outline color to use
    # pen_thickness  -> (INT) outline thickness to use
    
    my_turtle.color(line_color)
    my_turtle.pensize(pen_thickness)
    
    for i in range(4):  #repeat 4
        my_turtle.forward(side_length)
        my_turtle.right(90)

# import random
# my_colors = ["Crimson", "CornflowerBlue", "Aquamarine", "DarkSlateBlue", "Grey"]
#     
# for length in range(100, 300, 2):
#     draw_square(length, random.choice(my_colors), 2)
#     my_turtle.right(3)









# Part One - basic movement

# my_turtle.forward(100)   #go forward 100 pixels
# my_turtle.left(90)
# my_turtle.forward(50)
# .right()   .backward()

# my_turtle.up()  #lift the pen up
# my_turtle.goto(200,200)
# my_turtle.down()  #puts the pen down
# my_turtle.fd(100)  #.forward()