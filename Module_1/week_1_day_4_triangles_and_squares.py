import turtle
turtle.color("red")
# ------------------------------------------------------------------------------------------
# This function accepts 2 parameters.  Distance, and angle.  Both given  as int values.
# Triangle() will open turtle and draw 3 sides of a triangle with given arguments.
# ------------------------------------------------------------------------------------------


def triangle(distance, angle):
    for i in range(1, 4):
        turtle.forward(distance)
        turtle.left(angle)


# ------------------------------------------------------------------------------------------
# This function accepts 2 parameters.  Disantance and angle.  Both given as int values.
# Square() will open turtle and draw 3 sides of a square with given length and angles.
# ------------------------------------------------------------------------------------------


def square(distance, angle, color):
    for i in range(1, 5):
        turtle.color(color)
        turtle.forward(distance)
        turtle.right(angle)


# ------------------------------------------------------------------------------------------
# This function accepts 1 parameter.  The length.
# back() will shift the position of the turtle to a new point (length) on the screen before
# drawing.
# ------------------------------------------------------------------------------------------

def back(length):
    for i in range(4):
        turtle.penup()
        turtle.backward(length)
        turtle.pendown()

'''
# test  Triangle
triangle(100, 120, "red")
back(50)
triangle(50, 120, "orange")
back(35)
triangle(25, 120, "green")
turtle.done()
'''

# test Square
square(90, 90, "green")
back(35)
square(90, 90, 'purple')
back(35)
square(90, 90, "red")

turtle.done()
