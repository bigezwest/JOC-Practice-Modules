import turtle


def back(length):
    turtle.penup()
    turtle.backward(length)
    turtle.pendown()


def move(length):
    back(-1 * length)


def polygon(num, side):
    colors = ["red", "orange", "yellow", "green",
              'blue', "purple", "pink", "black"]
    angle = 360 / num

    if num < 3:
        print('There are not enough sides for this shape. ')
        print('Continuing to the next shape. ')
    else:
        for i in range(num):
            turtle.color(colors[i % len(colors)])
            turtle.forward(side)
            turtle.left(angle)


def main():
    polygon(12, 25)
    turtle.done()


main()
