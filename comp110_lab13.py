"""
Module: comp110_lab13

Starter code for Lab 13 (Image convolution)
"""

import comp110_image


def apply_kernel(img, img_copy, x, y, kernel):
    """
    Applies the given kernel to the pixel in img at (x,y).

    Params:
    img (type: Picture) - The picture to modify
    img_copy (type: Picture) - An unmodified version of img (used for reading
        values)
    x (type: int) - The x value of the pixel to modify
    y (type: int) - The y value of the pixel to modify
    kernel (type: 2D list of int) - The kernel to apply.
    """

    red_sum = 0
    green_sum = 0
    blue_sum = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            
            pix = img_copy.getPixel( x + i, y + j)
            multiplier = kernel[j + 1][i + 1]


            red = pix.getRed() * multiplier
            green = pix.getGreen() * multiplier
            blue = pix.getBlue() * multiplier

            red_sum += red
            green_sum += green
            blue_sum += blue

            # To do: Get the correct neighborhood pixel

            # To do: add to red_sum, green_sum, and blue_sum based on
            # multiplication the pixel's color with the kernel.
            # Note that you will use getPixel to get the pixel from img_copy
            # and kernel[???][???] to get the value in the kernel.
            pass
    if red_sum > 255:
        red_sum = 255
    elif red_sum < 0:
        red_sum = 0
    
    if green_sum > 255:
        green_sum = 255
    elif green_sum < 0:
        green_sum = 0
    
    if blue_sum > 255:
        blue_sum = 255
    elif blue_sum < 0:
        blue_sum = 0
    rgb_tuple = (red_sum, green_sum, blue_sum)
  
    img.setPixel(x,y, rgb_tuple)




    # To do: set the red, green, and blue components of the pixel at (x,y) to
    # the sums we calculated.
    # IMPORTANT: Before setting the color, use if statements to see if the
    # red, green, or blue sum are out of range and update the value of each
    # accordingly (e.g. set to 0 if the sum is less than 0.)


def convolution(img, kernel):
    """
    Performs convolution on all non-border pixels in the img, using the given
    convolution kernel.

    Params:
    img (type: Picture) - The picture to modify.
    kernel (type: 2D list of int) - The kernel to apply.
    """
    img_copy = img.copy()

    # To Do: modify range to avoid border pixels
    for x in range(1, img.getWidth() - 1 ):
        for y in range(1, img.getHeight() - 1 ):
            apply_kernel (img, img_copy, x, y, kernel)
            pass

def main():
    # Do not modify this function

    cat_img = comp110_image.Picture(filename="cute-cat.jpg")
    cat_img.setTitle("Before convolution (edge detect)")
    cat_img.show()
    convolution(cat_img, [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    cat_img.setTitle("After convolution (edge detect)")
    cat_img.show()


""" DO NOT MODIFY ANYTHING BELOW THIS LINE! """
if __name__ == "__main__":
    main()
