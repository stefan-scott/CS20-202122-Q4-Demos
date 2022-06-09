# Individual Pixel Control - Micro:bit
# Mr. Scott
# June 8, 2022
# Set Pixel, get Pixel, grid, etc...

import microbit, random, time

# list (of lists) to represent the 5x5 grid on the micro:bit
grid = [[5, 0, 0, 0, 0],
        [0, 5, 0, 0, 0],
        [0, 0, 5, 0, 0],
        [0, 0, 0, 5, 0],
        [0, 0, 0, 0, 5]]

#functions for our GRID
def print_grid():
    # print out the grid in an easy-to-read format
    for row in grid:
        print(row)

def show_grid():
    # convert our 2D list into a propertly formatted string
    # and then display on the micro:bit
    result = ""
    for row in grid:
        for pixel in row:
            result += str(pixel)
        result += ":"
    result = result[0:-1] #slice off the trailing ":"
    print(result)
    microbit.display.show(microbit.Image(result))

def set_pixel(x,y,intensity):
    #set a pixel at (x,y) to brightess: intensity 0-9
    grid[y][x] = intensity
    show_grid()
    
def queue_pixel(x,y,intensity):
    #queue a change for a (x,y) pixel
    grid[y][x] = intensity
    
def plot(x,y):
    #turn on pixel at x,y FULL
    set_pixel(x,y,9)

def unplot(x,y):
    #turn off pixel at x,y
    set_pixel(x,y,0)
    

def random_sparkle():
    #set random pixel to random intensity
    x = random.randint(0,4)
    y = random.randint(0,4)
    intensity = random.randint(0,9)
    set_pixel(x,y,intensity)
    
def set_all(intensity):
    #fills all pixels to level "intensity"
    for x in range(5):  #x: 0 1 2 3 4
        for y in range(5):  #y: 0 1 2 3 4
            queue_pixel(x,y,intensity)
    show_grid()

def fade_effect():
    # an animation fading full screen fills
    for cycle in range(5):
        
        for brightness in range(10):  #0-9
            set_all(brightness)
            time.sleep(0.02)
            
        for brightness in range(8, 0, -1):
            set_all(brightness)
            time.sleep(0.02)

def get_pixel(x,y):
    #return the intensity at position x,y
    return grid[y][x]
  
# while True:
#     random_sparkle()

# Game Mechanics - Driving a player around:
set_all(0) #clear the screen

player_x = 2
player_y = 4  #bottom row

plot(player_x, player_y)

while True:
    #left and right movement (A/B Buttons)
    if microbit.button_a.was_pressed():
        #was_pressed() → once per button press
        if player_x > 0:
            unplot(player_x, player_y)
            player_x = player_x - 1
            plot(player_x, player_y)
    
    if microbit.button_b.was_pressed():
        if player_x < 4:
            unplot(player_x, player_y)
            player_x += 1
            plot(player_x, player_y)
    
    
    
    
    
    
    
    
    