# Working with Images Day 2
# Mr. Scott
# June 14, 2022
# Recap Empty Images + Loading Images and Manipulation

import image   #cs20-image

## Boilerplate - loading files / creating canvas ###

my_image = image.Image("sneakers.jpg")  #load image

width = my_image.get_width()
height = my_image.get_height()

window = image.ImageWin(width,height) #create window

my_image.draw(window)


## Do some manipulation (inline) ##

# Loop through all pixels
for x in range(width):
    for y in range(height):
        p = my_image.get_pixel(x,y)
        
        # make some change(s) based on the pixel value
        old_red = p.get_red()
        old_green = p.get_green()
        old_blue = p.get_blue()
        
        # FIRST FILTER: Green boost
        new_red = old_red
        new_green = old_green + 100   #0-255
        if new_green > 255:
            new_green = 255
        new_blue = old_blue
        
        new_pixel = image.Pixel(new_red, new_green, new_blue)
        my_image.set_pixel(x,y,new_pixel)
        
    my_image.draw(window)
        









# REVIEW/RECAP

# width = 300
# height = 200
# 
# window = image.ImageWin(width, height) #create a window
# my_image = image.EmptyImage(width, height) #this is our image object
# 
# for x in range(width):
#     for y in range(height):
#         if x % 2 == 0:  #implies an even x position
#             this_pixel = image.Pixel(124, 212, 217)
#             my_image.set_pixel(x,y,this_pixel)
#         else: #odd
#             this_pixel = image.Pixel(0,0,0)
#             my_image.set_pixel(x,y,this_pixel)
#             
# my_image.draw(window)


