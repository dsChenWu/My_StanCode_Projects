"""
File: bouncing_ball
Name: Jason Wu
-------------------------
TODO: In this program, user can click the mouse to start the animation. The will not be impact by the mouse once started.
      The animation can repeat three times and then it will stop no matter how many time clicking the mouse.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


# Constant control the diameter of the window
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


# Global variables
window = GWindow(800, 500, title='bouncing_ball.py')
black_ball = GOval(SIZE, SIZE)
count = 0   # it is a key to control the mouse
numeric = 0 # To calculate how many time the animation has been done.
is_open = True  # it is a key to control the mouse

def main():
    global count
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    black_ball.filled = True
    window.add(black_ball,x=START_X, y=START_Y)
    onmouseclicked(click)


def click(event):
    """
    In this function, it will base on the criteria to start the animation or stop it.
    """
    global count
    global numeric
    vy = 0
    if count ==0:
        if numeric < 3:
            count +=1
            numeric+=1
            while True:
                black_ball.move(VX, vy)
                vy += GRAVITY
                if black_ball.y + black_ball.height >= window.height or black_ball.y <= 0:
                    vy = vy * REDUCE
                    vy = -vy
                if black_ball.x > window.width:
                    break
                pause(DELAY)
            window.add(black_ball, x=START_X, y=START_Y)
            count += -1


if __name__ == "__main__":
    main()
