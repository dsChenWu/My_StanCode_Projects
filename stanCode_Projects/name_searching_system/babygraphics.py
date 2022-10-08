"""
File: babygraphics.py
Name: Jason Wu
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    return GRAPH_MARGIN_SIZE + (width-2*GRAPH_MARGIN_SIZE) // len(YEARS) * year_index


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width = LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width = LINE_WIDTH)
    for i in range(len(YEARS)):
        x_label = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_label, 0, x_label, CANVAS_HEIGHT, width = LINE_WIDTH)
        canvas.create_text(x_label+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text = YEARS[i], anchor = tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    count = 0  # Check number to control the color of line.
    for ele in lookup_names:
        get_first_year_x = get_x_coordinate(CANVAS_WIDTH, 0)  # Return the x_label

        # To set up the 1900s, first point.
        if str(YEARS[0]) in name_data[ele]:  # Check if the key is in the name of dictionary.
            get_first_rating = name_data[ele][str(YEARS[0])]  # Assign 'get_first_rating'. It is the rating of specific year.
            rating_num = ele + str(' ') + str(get_first_rating)  # Store the Name & rating number and it is string.
            y_0 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT- 2* GRAPH_MARGIN_SIZE) * int(get_first_rating)// MAX_RANK  # To calculate the y_label.
        else:
            rating_num = ele + str('*')  # Store the Name & rating number when there is no date or out of MAX_RANK.
            y_0 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE  # To calculate the y_label.
        canvas.create_text(get_first_year_x + TEXT_DX, y_0, text=rating_num, fill=COLORS[count], anchor=tkinter.SW)

        # Start from 1910s, use for loop to calculate until 2010s.
        for j in range(1, len(YEARS)):
            x_label = get_x_coordinate(CANVAS_WIDTH, j)
            if str(YEARS[j]) in name_data[ele]:  # Check if the key is in the name of dictionary.
                rating = name_data[ele][str(YEARS[j])]  # To get the rating for specific year.
                rating_num = ele + str(' ') + str(rating)  # Store the Name & rating number and it is string.
                y_1 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE) * int(rating) // MAX_RANK
            else:
                rating_num = ele + str('*')
                y_1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            canvas.create_line(get_first_year_x, y_0, x_label, y_1, width=LINE_WIDTH, fill=COLORS[count])
            canvas.create_text(x_label + TEXT_DX, y_1, text=rating_num, fill=COLORS[count], anchor=tkinter.SW)
            get_first_year_x = x_label  # To update the 'get_first_year_x' each time.
            y_0 = y_1 # Update the y_0 each time
        if count == 3:  # Check point for the color of line.
            count = 0
        else:
            count += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
