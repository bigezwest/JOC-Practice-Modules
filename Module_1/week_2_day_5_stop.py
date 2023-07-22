import turtle

colors = ("red", "blue", "orange")

# Draw a rectangle
def rectangle(length, width):
    total_degrees = 360
    num_sides = 4

    for i in range(2):
        turtle.forward(width)
        turtle.right(total_degrees / num_sides)
        turtle.forward(length)
        turtle.right(total_degrees / num_sides)


# Draw an octagon
def octagon(o_len):
    total_degrees = 360
    num_sides = 8

    for i in range(8):
        turtle.forward(o_len)
        turtle.left(total_degrees / num_sides)

# Shift to the next space
def t_shift(o_len):
    turtle.penup()
    turtle.forward(o_len)
    turtle.pendown()


def stop(o_len):
    for i in range(3):
        turtle.color(colors[i])
        octagon(o_len)
        turtle.forward(o_len * 3 / 8)
        rectangle(o_len * 2, o_len / 5)
        t_shift(o_len * 2)
        o_len *= .75


def main():
    t_shift(-250)
    stop(100)
    turtle.Screen().exitonclick()

main()
