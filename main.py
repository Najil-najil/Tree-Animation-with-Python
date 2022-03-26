from ast import Return
import turtle as tu

roo = tu.Turtle()
wn = tu.Screen()
wn.bgcolor("black")
wn.title("Fractal Tree Pattern")
roo.left(98)
roo.speed(1000)


def draw(l):
    if (l < 10):
        return
    else:

        roo.pensize(2)
        roo.pencolor("yellow")
        roo.forward(l)
        roo.left(38)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(20)

roo.right(90)
roo.speed(200000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("green")
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(20)

roo.left(270)
roo.speed(200000)

# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("red")
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(20)

roo.right(90)
roo.speed(200000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor('#FFF8DC')
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(20)

def draw(l):
    if (l < 10):
        return
    else:

        roo.pensize(3)
        roo.pencolor('#FFF8DC')
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)

roo.right(90)
roo.speed(200000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("yellow")
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)

roo.left(270)
roo.speed(200000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("green")
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)

roo.right(90)
roo.speed(200000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("red")
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)
wn.exitonclick()
