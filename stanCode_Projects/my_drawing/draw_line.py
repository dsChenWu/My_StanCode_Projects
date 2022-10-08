"""
File: draw_line
Name: Jason Wu
-------------------------
TODO: Have infinite time to follow the rule to draw a line.
"""



from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked



# Constants control the size of circle
SIZE =20

# Global variables
window = GWindow()
count = 1
hole = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click)


def click(event):
    global count
    if count %2 != 0:
        hole.filled = False
        window.add(hole, x = event.x- SIZE/2, y= event.y- SIZE/2)
        count +=1
    else:
        count+= 1
        line = GLine(hole.x+SIZE/2, hole.y+SIZE/2, event.x, event.y)    # To make sure the length of line meets the requirement.
        window.add(line)
        window.remove(hole)


if __name__ == "__main__":
    main()
