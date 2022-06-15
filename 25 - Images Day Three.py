# Working with Images pt3
# Mr. Scott
# June 15, 2022
# Conditional Filters, Output Images

import image

source_image = image.Image("moon.jpg")

width = source_image.width
height = source_image.height

window = image.ImageWin(width, height)

source_image.draw(window)


def average(p):
    #return average intensity
    return int((p.get_red() + p.get_green() + p.get_blue())/3)

def change_sky(p):
    #This function will modify the color of pixels that are "sky"
    #input p → Pixel object to potentially modify
    #output → Pixel (either modified or unchanged)
    if average(p) > 15: #MOON
        return p  #return an unchanged pixel
    else: #sky
        new_pixel = image.Pixel(50, 50, 230)
        return new_pixel


# Another main loop, for some pixel-copy operations
source_image = image.Image("sneakers.jpg")

width = source_image.width
height = source_image.height

result_image = image.EmptyImage(width,height)

for x in range(width):
    for y in range(height):
        #get current pixel
        p = source_image.get_pixel(x,y)
        
        #copy it somewhere
        if y < height/3:  #top third- straight copy
            result_image.set_pixel(x,y,p)
        elif y > height/3*2: #bottom third - same
            result_image.set_pixel(x,y,p)
        else: #middle third - mirror horizontally
            new_x = (width-1) - x
            result_image.set_pixel(new_x, y, p)
    #draw image
    result_image.draw(window)



#Loop for each pixel in the upper-left quadrant:

# for y in range(int(height/2)):
#     for x in range(int(width/2)):
#         #getting the current pixel(x,y)
#         p = source_image.get_pixel(x,y)
#         
#         #run our function to modify the pixel
#         new_pixel = change_sky(p)
#         
#         #update the pixel
#         source_image.set_pixel(x,y, new_pixel)
#         
#     source_image.draw(window)