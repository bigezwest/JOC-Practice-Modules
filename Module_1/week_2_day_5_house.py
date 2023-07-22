import turtle

num_sides = 4
total_degrees = 360


# Draw a square
def square(length):
    for side in range(num_sides):
        turtle.forward(length)
        turtle.right(total_degrees / num_sides)


# Draw a triangle
def triangle(length):
    t_num_sides = num_sides - 1
    for side in range(t_num_sides):
        turtle.forward(length)
        turtle.left(total_degrees / t_num_sides)


# Create a space, 10 more than size of the length (used in triangle, and square)
def turtle_shift(length):
    turtle.penup()
    turtle.backward(length)
    turtle.pendown()


def house(length):
    triangle(length)
    square(length)


def main():
    size = 100                      # size of one side
    for i in range(5):              # draw 5 times
        house(size)
        turtle_shift(size + 10)     # create a space for the next house
        size *= .75                 # size of next line

    turtle.Screen().exitonclick()


main()

