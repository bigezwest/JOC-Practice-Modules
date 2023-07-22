"""
Week 2, Day 5, Project Turtle
Thomas D'Angelo

Step 1: Draw a line
    1. create a new file for your turtle program.
Step 2: Draw a square
    1. Draw a square on the screen.
    2. Change its color.
    3. Make the line thicker by changing the pensize or width.
    4. Change the speed the turtle draws
"""
import turtle
# Var for number of sides
num_sides = 4
total_degrees = 360
# distance = 90
t_colors = ("red", "blue", "yellow", "green")

# Step 1
# turtle.forward(distance)

# Step 2
'''
for side in range(num_sides):
    turtle.speed(10)                    # increase speed
    turtle.pensize(5)                   # change pensize
    turtle.color(t_colors[side])        # rotate colors for each side
    turtle.forward(distance)            
    turtle.left(total_degrees / num_sides)

# Step 3
for i in range(2):
    turtle.color(t_colors[i])  # rotate colors for each side
    for side in range(num_sides):
        turtle.speed()                    # increase speed
        turtle.pensize(5)                   # change pensize

        turtle.forward(distance)
        turtle.left(total_degrees / num_sides)
    turtle.penup()
    turtle.forward(distance * 2)
    turtle.pendown()
'''


# Step 4 - Create a square function
def square(distance):
    for side in range(num_sides):
        # turtle.speed()  # increase speed
        # turtle.pensize(5)  # change pensize
        turtle.forward(distance)
        turtle.left(total_degrees / num_sides)
    # turtle.penup()
    # turtle.forward(distance * 2)
   #  turtle.pendown()


# Step 5 - Create a rectangle function
def rectangle(length, width):
    turtle.forward(length)
    turtle.left(total_degrees / num_sides)
    turtle.forward(width)
    turtle.left(total_degrees / num_sides)
    turtle.forward(length)
    turtle.left(total_degrees / num_sides)
    turtle.forward(width)
    turtle.left(total_degrees / num_sides)

# Step 6 - Create a house


def main():
    distance = 90

    # for i in range(2):
    #     square_t(distance)

    length = 300
    width = 200

    for i in range(10):
        turtle.color(t_colors[i % 4])
        rectangle(length, width)
        square(distance)
        length -= 10
        width -= 10
        distance -= 10


    turtle.Screen().exitonclick()


main()

# turtle.done()
