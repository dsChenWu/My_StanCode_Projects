"""
File: blur.py
Name: Jason Wu
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    The function can help us to recalculate each pixel and give the new_RBG.
    At the end, return the new_RBG to main function.
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            # Todo: get pixel of new_img at x,y
            new_img_p = new_img.get_pixel(x,y)

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            if x == 0 and y ==0:
                # Get pixel at the top-left corner of the image.
                new_r = (img.get_pixel(x,y).red + img.get_pixel(x,y+1).red +img.get_pixel(x+1,y).red+ img.get_pixel(x+1,y+1).red) // 4
                new_g = (img.get_pixel(x,y).green + img.get_pixel(x,y+1).green +img.get_pixel(x+1,y).green + img.get_pixel(x+1,y+1).green) // 4
                new_b = (img.get_pixel(x,y).blue + img.get_pixel(x,y+1).blue +img.get_pixel(x+1,y).blue + img.get_pixel(x+1,y+1).blue) // 4
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b


            elif x == img.width -1 and y==0 :
                # Get pixel at the top-right corner of the image.
                new_r = (img.get_pixel(x,y).red + img.get_pixel(x - 1 , y).red + img.get_pixel(x-1 , y+1).red + img.get_pixel(x , y+1).red) // 4
                new_g = (img.get_pixel(x,y).green + img.get_pixel(x - 1 , y).green + img.get_pixel(x-1 , y+1).green + img.get_pixel(x, y+1).green) // 4
                new_b = (img.get_pixel(x,y).blue + img.get_pixel(x - 1 , y).blue + img.get_pixel(x-1 , y+1).blue + img.get_pixel(x, y+1).blue) // 4
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b

            elif x == 0 and y == new_img.height-1:
                # Get pixel at the bottom-left corner of the image
                new_r = (img.get_pixel(x,y).red +img.get_pixel(0, y-1).red + img.get_pixel(x+1, y-1).red + img.get_pixel(x+1, y).red) // 4
                new_g = (img.get_pixel(x,y).green +img.get_pixel(0, y-1).green + img.get_pixel(1, y-1).green + img.get_pixel(x+1, y).green) // 4
                new_b = (img.get_pixel(x,y).blue +img.get_pixel(0, y-1).blue + img.get_pixel(1, y-1).blue + img.get_pixel(x+1, y).blue) // 4
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b

            elif x == new_img.width-1 and y == new_img.height-1:
                # Get pixel at the bottom-right corner of the image
                new_r = (img.get_pixel(x, y).red + img.get_pixel(x-1, y).red + img.get_pixel(x-1 , y-1).red + img.get_pixel(x,y-1).red) // 4
                new_g = (img.get_pixel(x, y).green + img.get_pixel(x-1,y).green + img.get_pixel(x-1 , y-1).green + img.get_pixel(x , y-1).green) // 4
                new_b = (img.get_pixel(x, y).blue + img.get_pixel(x-1,y).blue + img.get_pixel(x-1 , y-1).blue + img.get_pixel(x, y-1).blue) // 4
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b

            elif 0 < x < new_img.width-1 and y== 0:
                # Get top edge's pixels (without two corners)
                new_r = (img.get_pixel(x,y).red+ img.get_pixel(x - 1, 0).red + img.get_pixel(x - 1, y + 1).red + img.get_pixel(x ,y+ 1).red + img.get_pixel(x+1, y+1).red + img.get_pixel(x+1,y).red) // 6
                new_g = (img.get_pixel(x,y).green+ img.get_pixel(x - 1, 0).green + img.get_pixel(x - 1, y + 1).green + img.get_pixel(x ,y+ 1).green + img.get_pixel(x+1, y+1).green + img.get_pixel(x+1,0).green) // 6
                new_b = (img.get_pixel(x,y).blue +img.get_pixel(x - 1, 0).blue + img.get_pixel(x - 1, y + 1).blue + img.get_pixel(x ,y+ 1).blue + img.get_pixel(x+1, y+1).blue + img.get_pixel(x+1,0).blue) // 6
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b

            elif 0 < x < new_img.width-1 and y== new_img.height-1 :
                # Get bottom edge's pixels (without two corners)
                new_r = (img.get_pixel(x,y).red +img.get_pixel(x - 1, y).red + img.get_pixel(x - 1, y - 1).red + img.get_pixel(x,y - 1).red + img.get_pixel(x + 1, y - 1).red + img.get_pixel(x + 1, y).red) // 6
                new_g = (img.get_pixel(x,y).green +img.get_pixel(x - 1, y).green + img.get_pixel(x - 1, y - 1).green + img.get_pixel(x,y - 1).green + img.get_pixel(x + 1, y - 1).green + img.get_pixel(x + 1, y).green) // 6
                new_b = (img.get_pixel(x,y).blue +img.get_pixel(x - 1, y).blue + img.get_pixel(x - 1, y - 1).blue + img.get_pixel(x,y - 1).blue + img.get_pixel(x + 1, y - 1).blue + img.get_pixel(x + 1, y).blue) // 6
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b

            elif x == 0 and 0 < y < new_img.height:
                # Get left edge's pixels (without two corners)
                new_r = (img.get_pixel(x,y).red +img.get_pixel(x, y-1).red + img.get_pixel(x, y - 1).red + img.get_pixel(x+1 ,y).red + img.get_pixel(x + 1, y +1).red + img.get_pixel(x , y+1).red) // 6
                new_g = (img.get_pixel(x,y).green +img.get_pixel(x, y-1).green + img.get_pixel(x, y - 1).green + img.get_pixel(x+1 ,y).green + img.get_pixel(x + 1, y +1).green + img.get_pixel(x , y+1).green) // 6
                new_b = (img.get_pixel(x,y).blue +img.get_pixel(x, y-1).blue + img.get_pixel(x, y - 1).blue + img.get_pixel(x+1 ,y).blue + img.get_pixel(x + 1, y +1).blue + img.get_pixel(x , y+1).blue) // 6
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b

            elif x == new_img.width-1 and 0 < y < new_img.height :
                # Get right edge's pixels (without two corners)
                new_r = (img.get_pixel(x,y).red +img.get_pixel(x, y - 1).red + img.get_pixel(x-1, y - 1).red + img.get_pixel(x-1 ,y).red + img.get_pixel(x -1, y + 1).red + img.get_pixel(x, y + 1).red) // 6
                new_g = (img.get_pixel(x,y).green +img.get_pixel(x, y - 1).green + img.get_pixel(x-1, y - 1).green + img.get_pixel(x-1 ,y).green + img.get_pixel(x -1, y + 1).green + img.get_pixel(x, y + 1).green) // 6
                new_b = (img.get_pixel(x,y).blue +img.get_pixel(x, y - 1).blue + img.get_pixel(x-1, y - 1).blue + img.get_pixel(x-1 ,y).blue + img.get_pixel(x -1, y + 1).blue + img.get_pixel(x, y + 1).blue) // 6
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b
                

            else:
                # Inner pixels.
                new_r = (img.get_pixel(x-1, y - 1).red + img.get_pixel(x, y - 1).red + img.get_pixel(x+1,y-1).red + img.get_pixel(x+1, y).red + img.get_pixel(x+1 , y + 1).red + img.get_pixel(x, y+1).red + img.get_pixel(x-1, y+1).red + img.get_pixel(x-1, y).red +img.get_pixel(x,y).red ) // 9
                new_g = (img.get_pixel(x - 1, y - 1).green + img.get_pixel(x, y - 1).green + img.get_pixel(x + 1,y - 1).green + img.get_pixel(x + 1, y).green + img.get_pixel(x + 1, y + 1).green + img.get_pixel(x, y + 1).green + img.get_pixel(x - 1,y + 1).green + img.get_pixel(x - 1, y).green + img.get_pixel(x, y).green) // 9
                new_b = (img.get_pixel(x - 1, y - 1).blue + img.get_pixel(x, y - 1).blue + img.get_pixel(x + 1,y - 1).blue + img.get_pixel(x + 1, y).blue + img.get_pixel(x + 1, y + 1).blue + img.get_pixel(x, y + 1).blue + img.get_pixel(x - 1,y + 1).blue + img.get_pixel(x - 1, y).blue + img.get_pixel(x, y).blue) // 9
                new_img_p.red = new_r
                new_img_p.green = new_g
                new_img_p.blue = new_b
    return new_img


def main():
    """
    In main function, open original figure and pass by the value to function(blur).
    At the end, it will show the blurred figure.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
