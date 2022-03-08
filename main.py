"""
Draws a spider using tkinter (via turtle).
"""
__author__ = 'Ethan Kinnear - [superatomic](https://github.com/superatomic)'

import turtle
from math import tau  # 0.5 * tau = pi (https://tauday.com/tau-manifesto)

SCALE = 20


BODY_SIZE = 4 * SCALE
LEG_THICKNESS = SCALE // 2  # 5
LEG_LENGTH = 7 * SCALE


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
        pen.pencolor('black')
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
    screen.setup(width=412, height=412)
    screen.title('Spider')

    # Pen Setup
    pen = turtle.RawPen(screen, visible=False)
    pen.speed('fastest')
    pen.radians()

    # Draw the Spider
    draw_spider(pen)

    # Mainloop until the window is clicked
    screen.exitonclick()


if __name__ == '__main__':
    main()
