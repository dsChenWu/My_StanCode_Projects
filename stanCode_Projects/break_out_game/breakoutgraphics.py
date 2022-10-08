"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10      # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.b_r = ball_radius
        self.p_w = paddle_width
        self.p_h= paddle_height
        self.p_o = paddle_offset
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.b_w = brick_width
        self.b_h = brick_height
        self.b_o = brick_offset
        self.b_s = brick_spacing
        # Default initial velocity for the ball
        self.__b_dx = 0
        self.__b_dy = 0

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(self.p_w, self.p_h)
        self.paddle.filled = True
        self.window.add(self.paddle, x = (self.window.width - self.p_w)/2, y=(self.window.height - self.p_o))

        # Center a filled ball in the graphical window
        self.ball = GOval(self.b_r*2, self.b_r*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width - self.b_r)/2, y=(self.window.height-self.b_r)/2)

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.move_ball)
        self.is_True = True

        # Draw bricks
        self.brick = GRect(self.b_w, self.b_h)
        # The nested for loop should change place, & color of bricks.
        count_vertical = self.b_o  # Assign the 'count_vertical' as brick_offset.
        for i in range(brick_rows):
            count_horizontal = 0  # Assign the 'count_horizontal' as the starter value.
            for j in range(brick_cols):
                self.brick = GRect(self.b_w, self.b_h)
                self.brick.filled = True
                if self.brick.x+self.brick.width+self.b_s <= self.window.width:
                    if 0 <= i <= 1:  # Row 1&2 give the 'red' color
                        self.brick.fill_color='red'
                        self.window.add(self.brick, x=count_horizontal, y= count_vertical)
                        count_horizontal += (self.brick.width+brick_spacing)
                    elif 2 <= i <= 3:  # Row 3&4 give the 'orange' color
                        self.brick.fill_color = 'orange'
                        self.window.add(self.brick, x=count_horizontal, y=count_vertical)
                        count_horizontal += (self.brick.width + brick_spacing)
                    elif 4 <= i <= 5:  # Row 5&6 give the 'yellow' color
                        self.brick.fill_color = 'Yellow'
                        self.window.add(self.brick, x=count_horizontal, y=count_vertical)
                        count_horizontal += (self.brick.width + brick_spacing)
                    elif 6 <= i <= 7:  # Row 7&8 give the 'orange' color
                        self.brick.fill_color = 'green'
                        self.window.add(self.brick, x=count_horizontal, y=count_vertical)
                        count_horizontal += (self.brick.width + brick_spacing)
                    else:  # Row 9&10 give the 'blue' color
                        self.brick.fill_color = 'blue'
                        self.window.add(self.brick, x=count_horizontal, y=count_vertical)
                        count_horizontal += (self.brick.width + brick_spacing)
            count_vertical += (self.brick.height + self.b_s)

    # onmouseclicked(move_ball)
    def move_ball(self, _):
        self.is_True = False
        self.__b_dy = INITIAL_Y_SPEED
        self.__b_dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__b_dx = -self.__b_dx

    # onmousemoved(move_paddle)
    def move_paddle(self, relocate):
        if 0 < relocate.x - self.paddle.width/2 and relocate.x+self.paddle.width/2< self.window.width:
            self.paddle.x = relocate.x - self.paddle.width/2

    # Getter Function:

    def get_x_speed(self):
        return self.__b_dx

    def get_y_speed(self):
        return self.__b_dy



