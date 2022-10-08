"""
File: mirror_lake.py
Name: Jason Wu
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filepath):
    """
    In this function, create a new figure which the height is twice than original one.
    To copy each pixel in original to new_image and it is mirror at the adding part.
    """
    img = SimpleImage(filepath)
    b_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x,y)
            b_img_p = b_img.get_pixel(x,y)
            b_img_p.red = img_p.red
            b_img_p.green = img_p.green
            b_img_p.blue = img_p.blue

            b_img_down = b_img.get_pixel(x, b_img.height-1-y) # Follow this rule to get the mirror part of pixel and assign.
            b_img_down.red = img_p.red
            b_img_down.blue = img_p.blue
            b_img_down.green = img_p.green
    return b_img



def main():
    """
    Open original figure.
    Pass by the value to function(reflect) and return target value to main function.
    Show the mirror figure.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()

    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
