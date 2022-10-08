"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""


from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
import random

# Constant variable:
FRAME_RATE = 15         # 100 frames per second
NUM_LIVES = 3			# Number of attempts

# Global variable:
numeric = 0



def main():
    """
    In main function, when user click the mouse, it will start the game and ball will start to move as long as ball.y
    is less than window.height. When ball touch the brick, it will destroy the brick or it will move mirror side after
    touch the paddle. The game will be closed when trying three times or destroy all bricks.
    """
    global numeric
    count = 0
    graphics = BreakoutGraphics()
    while True:
        if not graphics.is_True:
            vx = graphics.get_x_speed()
            vy = graphics.get_y_speed()
            if numeric < 3:
                numeric += 1
                while True:
                    # Update
                    graphics.ball.move(vx,vy)
                    # check
                    if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                        vx = -vx
                    if graphics.ball.y <= 0:
                        vy = -vy
                    if graphics.ball.y > graphics.window.height:
                        break
                    if count == graphics.brick_cols*graphics.brick_rows:
                        break
                    # Pause
                    pause(FRAME_RATE)
                    # Get x_label & y_label
                    left_u_corner = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                    right_u_corner = graphics.window.get_object_at(graphics.ball.x+2*graphics.b_r, graphics.ball.y)
                    left_d_corner = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2*graphics.b_r)
                    right_d_corner = graphics.window.get_object_at(graphics.ball.x+2*graphics.b_r, graphics.ball.y+ 2*graphics.b_r)
                    # Start to check each corner when animation action
                    if left_d_corner is not None:  # Check left-downside corner. The other 'elif' following the same logic.
                        if left_d_corner is not graphics.paddle:  # Check if the object is brick.
                            graphics.window.remove(left_d_corner)
                            vy = -vy
                            count += 1
                        elif left_d_corner is graphics.paddle and vy > 0:  # Check if the object is paddle.
                            vy = -vy
                    elif right_d_corner is not None:
                        if right_d_corner is not graphics.paddle:
                            graphics.window.remove(right_d_corner)
                            vy = -vy
                            count += 1
                        elif right_d_corner is graphics.paddle and vy > 0:
                            vy = -vy
                    elif left_u_corner is not None:
                        if left_u_corner is not graphics.paddle:
                            graphics.window.remove(left_u_corner)
                            vy = -vy
                            count += 1
                        elif left_u_corner is graphics.paddle and vy > 0:
                            vy = -vy
                    elif right_u_corner is not None:
                        if right_u_corner is not graphics.paddle:
                            graphics.window.remove(right_u_corner)
                            vy = -vy
                            count += 1
                        elif right_u_corner is graphics.paddle and vy > 0:
                            vy = -vy
                # When ball is drop below the window, ball will show in same place and move after click the mouse.
                graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.b_r)/2, y=(graphics.window.height - graphics.b_r)/2)
            graphics.is_True = True
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
