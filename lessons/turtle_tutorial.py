from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

"""turtle_object_variable.method_name() --> Makes the turtle do anything"""
"""to repeat something a certain number of times: while(<counter_variable> <number_of_times>)"""

""""i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1"""    

"""to change the color with a string value: <turtlevariable>.color("color")"""
colormode(255)
leo.color(165, 230, 251)

"""to prevent the turtle from drawing: <turtlevariable>.penup() or <turtlevariable>.up()"""
"""to allow the turtle to draw: <turtlevariable.pendown() or <turtlevariable>.down()"""
"""to move the turtle to a new x, y position: <turtlevariable>.goto(<x_coordinate>, <y_coordinate>)"""

leo.penup()
leo.goto(-140, -75)
leo.pendown()

leo.fillcolor(165, 230, 251)
leo.begin_fill()
leo.speed(50)

side_length: int = 300

i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1

leo.end_fill()
leo.hideturtle()

bob: Turtle = Turtle()
bob.color(0, 0, 0)
bob.penup()
bob.goto(-140, -75)
bob.pendown()

i: int = 0
while (i < 50):
    bob.forward(side_length)
    side_length = side_length * 0.97
    bob.left(123)
    i = i + 1

done()

"""def main() -> None:"""
   
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