"""This turtle will draw a condo with sunlight."""

__author__ = "730312196"

from turtle import Turtle, colormode, done

colormode(255)


def main() -> None:
    """The entrypoint of my condo."""
    ertle: Turtle = Turtle()
    drtle: Turtle = Turtle()
    frtle: Turtle = Turtle()
    hrtle: Turtle = Turtle()
    # condo outline
    draw_squares(ertle, -200.0, -250.0, 200, 10)
    draw_squares(ertle, 0.0, -250.0, 200, 10)
    draw_squares(ertle, -200, -50.0, 200, 10)
    draw_squares(ertle, 0.0, -50.0, 200, 10)
    # window outline
    draw_squares(ertle, -130.0, -165.0, 50, 2)

    draw_squares(ertle, 80.0, -165.0, 50, 2)

    draw_squares(ertle, -130.0, 25.0, 50, 2)

    draw_squares(ertle, 80.0, 25.0, 50, 2)
    # window lines
    draw_lines(drtle, -105.0, -165.0, 90.0, 50, 2)
    draw_lines(drtle, -130.0, -140.0, 0.0, 50, 2)

    draw_lines(drtle, 105.0, -165.0, 90.0, 50, 2)
    draw_lines(drtle, 80, -140.0, 0.0, 50, 2)

    draw_lines(drtle, -105.0, 25.0, 90.0, 50, 2)
    draw_lines(drtle, -130.0, 50.0, 0.0, 50, 2)

    draw_lines(drtle, 105.0, 25.0, 90.0, 50, 2)
    draw_lines(drtle, 80.0, 50.0, 0.0, 50, 2)

    # draw triangles
    draw_tri(frtle, -200.0, 150.0, 200.0, 10)
    draw_tri(frtle, 0.0, 150.0, 200.0, 10)
    
    # draw sun
    draw_sun(hrtle, 250, 250, 30)
    done()


def draw_squares(a_turtle: Turtle, x: float, y: float, width: float, size: int) -> None:
    """Draw the outline of the square with x,y being bottom left corner."""
    a_turtle.hideturtle()
    a_turtle.speed(200)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.setheading(0.0)
    i: int = 0
    while i < 4:  
        a_turtle.pensize(size)
        a_turtle.forward(width)
        a_turtle.left(90)
        i = i + 1


def draw_lines(b_turtle: Turtle, x: float, y: float, direction: float, length: float, size: int) -> None:
    """Draws the lines that make the window panes."""
    b_turtle.pencolor(0, 128, 0)
    b_turtle.pensize(2)
    b_turtle.hideturtle()
    b_turtle.speed(200)
    b_turtle.penup()
    b_turtle.goto(x, y)
    b_turtle.pendown()
    b_turtle.setheading(0.0)
    b_turtle.left(direction)
    b_turtle.forward(length)


def draw_tri(c_turtle: Turtle, x: float, y: float, length: float, size: int) -> None:
    """This draws the triangles."""
    c_turtle.hideturtle()
    c_turtle.speed(200)
    c_turtle.penup()
    c_turtle.goto(x, y)
    c_turtle.pendown()
    c_turtle.setheading(0.0)
    c_turtle.pensize(size)
    i: int = 0
    while i < 3:
        c_turtle.forward(length)
        c_turtle.left(120)
        i = i + 1


def draw_sun(d_turtle: Turtle, x: float, y: float, length: float) -> None:
    """This will draw the sun."""
    d_turtle.hideturtle()
    d_turtle.speed(200)
    d_turtle.penup()
    d_turtle.goto(x, y)
    d_turtle.pendown()
    d_turtle.setheading(0.0)
    d_turtle.color(255, 255, 0)
    d_turtle.begin_fill()
    i: int = 0
    while i < 8:
        d_turtle.forward(length)
        d_turtle.left(45)
        i = i + 1
    d_turtle.end_fill()


if __name__ == "__main__":
    main()