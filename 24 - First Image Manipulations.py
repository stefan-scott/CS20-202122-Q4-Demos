# Image Manipulation Template
# Jan 18, 2022
# Mr. Scott
# Images Demo 2

import image

img = image.Image("sneakers.jpg")   #load image

width = img.get_width()    #extract the dimensions
height = img.get_height()

window = image.ImageWin(width, height)  #create window



# write some pixel changing functions...
def negative_pixel(p):
    #input:  p → Pixel object
    #output: Pixel object (the negative pixel)
    orig_red = p.get_red()
    orig_green  = p.get_green()
    orig_blue = p.get_blue()
    
    neg_red = 255 - orig_red
    neg_green = 255 - orig_green
    neg_blue = 255 - orig_blue
    
    #generate a new pixel based on new triplet
    new_pixel = image.Pixel(neg_red, neg_green, neg_blue)
    return new_pixel

def average(p):
    #computes the average intensity of a given pixel
    #input: p → Pixel object
    #output: int → average intensity (0-255)
    orig_red = p.get_red()
    orig_green  = p.get_green()
    orig_blue = p.get_blue()
    
    sum_intensity = orig_red + orig_green + orig_blue
    avg = int(sum_intensity / 3) #!!!!!
    return avg

def desaturate(p):
    # make a pixel into a greyscale equivalent
    # input: p → Pixel Object
    # output: Pixel Object (greyscale)
    avg = average(p)
    grey_pixel = image.Pixel(avg, avg, avg)
    return grey_pixel

#loop through all the pixels:
for x in range(width):
    for y in range(height):
        p = img.get_pixel(x,y)
        # make some change based on the pixel value
        updated_pixel = desaturate(p)
        img.set_pixel(x,y,updated_pixel)   
        
    
    img.draw(window)