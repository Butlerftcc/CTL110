"""
CTI 110
Turtle graphics
9/26/23
"""
import turtle

Turtle = turtle.Turtle()

Turtle.home()
Turtle.pensize(7)
Turtle.pencolor("magenta")

#Makes an "A"
Turtle.setheading(65)
Turtle.forward(200)
Turtle.setheading(295)
Turtle.forward(200)
Turtle.backward(100)
Turtle.setheading(180)
Turtle.forward(85)
Turtle.up()

#makes a "B", but it's a little sharp
Turtle.goto(200, 0)
Turtle.pencolor("blue")
Turtle.down()
Turtle.setheading(90)
Turtle.forward(165)
Turtle.setheading(330)
Turtle.forward(75)
Turtle.setheading(215)
Turtle.forward(75)
Turtle.setheading(330)
Turtle.forward(75)
Turtle.setheading(215)
Turtle.forward(80)
Turtle.up()

#square
Turtle.goto(-350, 200)
Turtle.pencolor("orange")
Turtle.fillcolor("red")
Turtle.pensize(30)
Turtle.begin_fill()
Turtle.down()
Turtle.setheading(180)
sides = 4
while sides > 0:
    Turtle.left(90)
    Turtle.forward(200)
    sides -= 1

Turtle.end_fill()

#triangle
Turtle.fillcolor("yellow")
Turtle.begin_fill()
sides = 3
while sides > 0:
    Turtle.right(120)
    Turtle.forward(200)
    sides -= 1

Turtle.end_fill()
Turtle.up()

