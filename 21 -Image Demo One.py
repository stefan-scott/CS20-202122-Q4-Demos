# Image Manipulation Demo One
# Mr. Scott
# June 13, 2022
# The very basics - Empty Image and Pixels

import image  #please don't save as image.py

width = 400
height = 300

my_image = image.EmptyImage(width, height) #creates an empty image variable
canvas = image.ImageWin(width, height) #this window is same size as image


# do some work
# creating a pixel:
p = image.Pixel(255,0,0)



# how to fill full image

# for x in range(width):
#     for y in range(height):
#         #print(x, "," , y)
#         my_image.set_pixel(x,y,p)
import random

while True:
    #create a random pixel at a random spot
    new_pixel = image.Pixel(0,0,0)
    
    new_pixel.set_red(random.randint(0,255))
    new_pixel.set_green(random.randint(0,255))
    new_pixel.set_blue(random.randint(0,255))
    
    rand_x = random.randint(0,width-1)
    rand_y = random.randint(0,height-1)
    
    my_image.set_pixel(rand_x, rand_y, new_pixel)

    my_image.draw(canvas)









