# Processing Python Demo
# First look at using Processing 4 
# in Python Mode
# Mr. Scott, June 17, 2022

bg_color = color(200,170,100)
y = 300

def mousePressed():
    global bg_color
    #this is triggered once per click. DON"T EXPLICITLY CALL THIS METHOD
    bg_color = color(50, 100, 150)
    
def keyPressed():
    global bg_color
    if key == 'g':
        bg_color = color(10, 200, 70)
    if keyCode == UP:
        bg_color = color(255)

def circle_and_square():  
    global y
    if keyPressed and keyCode == UP:
        y -= 5
    elif keyPressed and keyCode == DOWN:
        y += 5
        
            
    fill(0,255,255)
    stroke(255,200,50)
    strokeWeight(5)
    square(300,y,50)
    
    # this repeats over and over. Target is 60 fps
    fill(255,0,0)
    circle(mouseX,mouseY, 40)

def bar_graph():
    #using loops and mouse, draw a bar graph
    #try out mouse interactions
    if mousePressed:  #style   //mouse_pressed - snake case   mousePressed - camel case
        fill(0,0,255)
    else:  #not pressed
        fill(255,0,255) 
    
    for x in range(0, mouseX, 20):
        rect(x, 350, 18,30)
        

def setup():
    # this happens once, at the start
    size(400,400)


def draw():
    #optional: clear the screen with background
    background(bg_color)
    circle_and_square()
    bar_graph()
    
    #update the screen at the end of draw


    
   
    
    print(mouseX, mouseY)
