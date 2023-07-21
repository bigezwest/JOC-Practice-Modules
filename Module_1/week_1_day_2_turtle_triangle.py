import turtle

# Variables for turtle
distance = 250   # length of line
angle = 120     # angle degrees

# turtle.forward(size)
turtle.color("green")
turtle.right(angle)
turtle.forward(distance)
turtle.color("red")
turtle.right(angle)
turtle.forward(distance)
turtle.color("blue")
turtle.right(angle)
turtle.forward(distance)

turtle.done()
