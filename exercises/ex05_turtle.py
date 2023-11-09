"""Turtle  Scene."""
__author__ = "730578454"

from turtle import Turtle, colormode, done

yertle: Turtle = Turtle()
squirtle: Turtle = Turtle()

def main() -> None:
    """The entrypoint of my scene."""
    yertle.speed(50)
    squirtle.speed(50)
    colormode(255)
    yertle.color(94, 155, 70)
    squirtle.color(95, 74, 74)


    squirtle.penup()
    squirtle.goto(250, -175)
    squirtle.pendown()

    width: int = 2
    height: int = 30

    def tree_trunk():
        """Creates the first tree trunk: brown."""
        squirtle.begin_fill()
        squirtle.fillcolor(95, 74, 74)
        i: int = 0
        while (i < 4):
            squirtle.forward(width)
            squirtle.left(90)
            squirtle.forward(height)
            i = i + 1
        squirtle.end_fill()
    tree_trunk()

    def move_squirtle():
        """Moves squirtle to a specific point."""
        squirtle.penup()
        squirtle.goto(-250, -175)
        squirtle.pendown()
    move_squirtle()

    tree_trunk()

    squirtle.penup()
    squirtle.goto(-150, -25)
    squirtle.pendown()
    tree_trunk()

    squirtle.penup()
    squirtle.goto(150, -45)
    squirtle.pendown()
    tree_trunk()

    def move_yertle():
        """Moves yertle to a specific point."""
        yertle.penup()
        yertle.goto(200, -145)
        yertle.pendown()
    move_yertle()

    def tree_leaves():
        """Creates triangular tree leaves."""
        yertle.begin_fill()
        yertle.fillcolor("green")
        i: int = 0
        while (i < 3):
            yertle.forward(70)
            yertle.left(120)
            i = i + 1
        yertle.end_fill()
    tree_leaves()

    yertle.penup()
    yertle.goto(100,-20)
    yertle.pendown()
    tree_leaves()

    yertle.penup()
    yertle.goto(-200,0)
    yertle.pendown()
    tree_leaves()

    yertle.penup()
    yertle.goto(-300, -145)
    yertle.pendown()
    tree_leaves()

    squirtle.penup()
    squirtle.goto(0,100)
    squirtle.pendown()

    def mountain():
        """Creates a Mountain in the background."""
        squirtle.begin_fill()
        squirtle.fillcolor(134, 147, 163)
        i: int = 0
        while (i < 3):
            squirtle.forward(100)
            squirtle.left(120)
            i = i + 1
        squirtle.end_fill()
    mountain()

    squirtle.penup()
    squirtle.goto(100,100)
    squirtle.pendown()
    mountain()

    squirtle.penup()
    squirtle.goto(200,100)
    squirtle.pendown()
    mountain()

    squirtle.penup()
    squirtle.goto(10, -100)
    squirtle.pendown()

    def draw_lake():
        squirtle.fillcolor("blue")
        squirtle.shape("circle")
        squirtle.shapesize(5, 11, 2)
    draw_lake()


    yertle.hideturtle()

if __name__ == "__main__":
    main()
done()