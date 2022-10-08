"""
File: fire.py
Name: Jason Wu
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(highlight):
    """
    In this function, it can help us to find out the area which is on fire based on the RGB value.
    """
    img = SimpleImage(highlight)
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        elif pixel.red < avg * HURDLE_FACTOR:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return img


def main():
    """
    To open the image and show the figure for original image and highlighted image.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
