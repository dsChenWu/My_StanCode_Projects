"""
File: sierpinski.py
Name: Jason Wu
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6            # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

DELAY = 400

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Input: Call a function.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""

	"""
	if order == 1:
		pass
	else:
		# Recursion:
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)  # Upper left section
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)  # Upper right section
		sierpinski_triangle(order - 1, length / 2, upper_left_x + (length / 2)*0.5, upper_left_y + length*0.5 * 0.866)  # Middle one section
		# Upper Left section:
		line_l_1 = GLine(upper_left_x, upper_left_y, upper_left_x + length*0.5, upper_left_y)
		line_l_2 = GLine(upper_left_x, upper_left_y, upper_left_x + length*0.5*0.5, upper_left_y+length*0.5*0.866)
		line_l_3 = GLine(upper_left_x + length*0.5, upper_left_y, upper_left_x + length*0.5 - 0.5 * length*0.5, upper_left_y + length*0.5 * 0.866)
		window.add(line_l_1)
		window.add(line_l_2)
		window.add(line_l_3)
		# #Upper right section:

		line_r_1 = GLine(upper_left_x+length*0.5, upper_left_y, upper_left_x + length*0.5+length*0.5, upper_left_y)
		line_r_2 = GLine(upper_left_x+length*0.5, upper_left_y, (upper_left_x + length*0.5)+ length*0.5 * 0.5, upper_left_y + length*0.5 * 0.866)
		line_r_3 = GLine(upper_left_x + length*0.5 + length*0.5, upper_left_y, (upper_left_x+length*0.5+length*0.5)-length*0.5*0.5, upper_left_y+length*0.5*0.866)
		window.add(line_r_1)
		window.add(line_r_2)
		window.add(line_r_3)
		# Middle one section:
		line_m_1 = GLine(upper_left_x+length*0.5*0.5, upper_left_y+length*0.5 * 0.866, upper_left_x+length*0.5*0.5+length*0.5, upper_left_y+length*0.5*0.866)
		line_m_2 = GLine(upper_left_x+length*0.5*0.5, upper_left_y+length*0.5 * 0.866, upper_left_x+length*0.5*0.5+length*0.5*0.5, upper_left_y+length*0.5*0.866+length*0.5*0.866)
		line_m_3 = GLine(upper_left_x+length*0.5*0.5+length*0.5, upper_left_y+length*0.5*0.866, upper_left_x+length*0.5*0.5+ length*0.5 - length*0.5*0.5, upper_left_y+length*0.5*0.866+length*0.5*0.866 )
		window.add(line_m_1)
		window.add(line_m_2)
		window.add(line_m_3)

		pause(DELAY)


if __name__ == '__main__':
	main()