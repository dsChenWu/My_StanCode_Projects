"""
File: best_photoshop_award.py
Name: Jason Wu
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.2
BLACK = 100

def main():
    """
    I am a big fan of the comedy series, "FRIENDS" and I found it is fitted since everyone is smiling~
    This figure is when Ross's son born in the world~
    """
    fig = SimpleImage('image_contest/Jason.jpeg')
    bg = SimpleImage('image_contest/test_5.png')
    bg.make_as_big_as(fig)
    combined = combine(fig, bg)
    combined.show()


def combine(fig, bg):
    for x in range(fig.width):
        for y in range(fig.height):
            fig_p = fig.get_pixel(x,y)
            avg = (fig_p.red + fig_p.green + fig_p.blue) // 3
            total = fig_p.red + fig_p.blue + fig_p.green
            if fig_p.green > avg * THRESHOLD and total > BLACK:
                bg_p = bg.get_pixel(x,y)
                fig_p.red = bg_p.red
                fig_p.green = bg_p.green
                fig_p.blue = bg_p.blue
    return fig


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
