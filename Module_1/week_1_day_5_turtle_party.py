import turtle
turtle.color("red")


def back(length):
    turtle.penup()
    turtle.backward(length)
    turtle.pendown()


def move(length):
    back(-1 * length)


def polygon(num, size):
    if num < 3:
        print('There are not enough sides for this shape. ')
        print('Continuing to the next shape. ')
    else:
        for i in range(num):
            turtle.forward(size)
            turtle.left(360 / num)


def spiral(length, angle):
    for i in range(length, 5, -5):
        turtle.forward(i)
        turtle.right(angle)

'''
for n in range(3, 10):
    move(50)
    polygon(n, 100 / n)
    back(50)
    turtle.right(360 / 7)
'''
spiral(75, 45)
move(150)
turtle.color("blue")
spiral(100, 90)
turtle.done()



