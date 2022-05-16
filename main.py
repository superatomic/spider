"""
Draws a spider using tkinter (via turtle).
"""
__author__ = 'Ethan Kinnear (https://github.com/superatomic)'

import turtle
from math import tau  # 0.5 * tau = pi (https://tauday.com/tau-manifesto)

from generate_images import save

# The main scaling constant. If you want to make the spider bigger or smaller, change this.
SCALE = 20

# Spider properties
BODY_SIZE = 4 * SCALE
LEG_THICKNESS = SCALE // 2  # 5
LEG_LENGTH = 7 * SCALE

# Configuration for the circle that is drawn around the spider
DRAW_BACKGROUND = True  # Set to `False` to not draw a circle in the background
CIRCLE_BORDER_SIZE = SCALE

# WINDOW_SIZE is the actual size of the window, and SCREEN_SIZE is the area that is scrollable.
WINDOW_SIZE = 20 * SCALE
SCREEN_SIZE = 2 * (LEG_LENGTH + CIRCLE_BORDER_SIZE if DRAW_BACKGROUND else 0) + LEG_THICKNESS

assert WINDOW_SIZE > SCREEN_SIZE

# Define the layout of the spider.
# `L` is leg, `E` is eye, and ` ` is nothing.
# noinspection SpellCheckingInspection
TURTLE_BODY_PARTS = 'LLLL LLLL' 'EE'


def draw_spider(pen: turtle.RawPen) -> None:

    # Draw the spider's body
    pen.dot(BODY_SIZE * 2)

    # Draw the spider's legs and eyes
    pen.pensize(LEG_THICKNESS)
    for index, part in enumerate(TURTLE_BODY_PARTS):
        pen.up()
        pen.goto(0, 0)
        pen.setheading(tau * index / len(TURTLE_BODY_PARTS))

        draw_body_part(part, pen)


def draw_body_part(part, pen: turtle.RawPen) -> None:
    """
    Draws a single body part.
    :param part: Either 'L', 'E', or ' '.
    :param pen: The turtle.
    """
    if part == 'L':  # Leg
        pen.down()
        pen.forward(LEG_LENGTH)
    elif part == 'E':  # Eye
        pen.forward(BODY_SIZE * 2 / 3)
        pen.down()
        pen.dot(3 * LEG_THICKNESS - 1, 'white')
        pen.dot(LEG_THICKNESS, 'black')
    elif part != ' ':  # Nothing
        raise ValueError("TURTLE_BODY_PARTS should only contain the characters 'L', 'E', and ' '")


def main():

    # Screen Setup
    screen = turtle.Screen()
    screen.setup(width=WINDOW_SIZE, height=WINDOW_SIZE)
    screen.screensize(SCREEN_SIZE, SCREEN_SIZE)
    screen.title('Spider')

    # Pen Setup
    pen = turtle.RawPen(screen, visible=False)
    pen.pencolor('black')
    pen.speed('fastest')
    pen.radians()

    # Create circle in the background of the turtle.
    if DRAW_BACKGROUND:
        pen.dot(SCREEN_SIZE, 'white')

    # Draw the Spider
    draw_spider(pen)

    # Save the spider as a PostScript file, and as an SVG and PNG file if Inkscape is installed.
    save(screen)

    # Mainloop until the window is clicked
    screen.exitonclick()


if __name__ == '__main__':
    main()
