# More Turtle Methods PART TWO
# Mr. Scott
# June6, 2022
# A few more turtle methods:  Colors, Shapes, Stamps
# Fills, RGB, Tracer

# Basic Turtle Setup Code:
import turtle, random

t = turtle.Turtle()

window = turtle.Screen()
window.setup(600,600)
window.colormode(255)  #numbered colors 0-255
window.bgcolor(random.randint(0,255), 212, 171)  #use R,G,B rather than colorstring
window.tracer(False) #don't do any animation updates


# PART THREE - Gradients, Fills, Superfast Tracer

def zigzags(r,g,b):
    #create some filled-in mountains, using the RGB color
    t.fillcolor(r,g,b)
    t.color(r,g,b)
    t.left(45)
    t.begin_fill()  #this is where the shape starts
    t.down()
    
    for i in range(5):  #5 peaks
        t.fd(40)
        t.right(90)
        t.fd(40)
        t.left(90)
    t.right(45)
    t.backward(200 * 2**0.5)
    t.end_fill()
 
#main drawing code
t.speed(0)

blue_value = 0
green_value = 180
red_value = 0

for angle in range(0,360, 2):  #iterating 180
    window.delay(0)
    t.setheading(angle)
    zigzags(int(red_value),green_value,blue_value)
    blue_value += 1
    green_value -= 1
    red_value = red_value + 1.41
    
    
    




# PART TWO - stamp and shape
# shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
# t.up()
# t.goto(-300,0) #leftmost edge
# t.shape("turtle")
# 
# for i in range(0, 80, 5):  #0, 5, 10, 15, 20, 25..
#     t.fd(i)  #move amount will be increasing each time through the loop
#     t.shape(random.choice(shapes))
#     t.stamp()  #pastes an impression of the current turtle in-place

# PART ONE try out a few new things (circle, dot)
# t.circle(5)
# t.circle(30)
# t.circle(50)
# t.fd(60)
# for i in range(10): # 10 times
#     t.dot(15)
#     t.forward(20)