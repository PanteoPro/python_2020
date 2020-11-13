import turtle

turtle.shape('turtle')

def draw_s():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)


def draw_square():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)


def draw_cirle():
    for step in range(360):
        turtle.forward(1)
        turtle.left(1)


def draw_square_10():
    for i in range(10):
        for j in range(4):
            turtle.forward(i*20+30)
            turtle.left(90)
        turtle.penup()
        turtle.backward(10)
        turtle.left(90)
        turtle.backward(10)
        turtle.right(90)
        turtle.pendown()


def draw_spider():
    length = 200
    for i in range(12):
        turtle.forward(length)
        turtle.stamp()
        turtle.backward(length)
        turtle.right(360/12)


def draw_spiral():
    for i in range(int(360/12*10)):
        turtle.forward(1 + i/20)
        turtle.left(12)


def draw_square_spiral():
    length = 10
    step = 5
    for i in range(12):
        for j in range(4):
            turtle.forward(length)
            length += step
            turtle.left(90)


def draw_true_more_degres():
    sides = 3
    length = 20
    step = 10
    for i in range(12):
        for j in range(sides):
            turtle.left(360/sides)
            turtle.forward(length)
        turtle.penup()
        turtle.forward(step/2)
        turtle.pendown()
        sides += 1
        length += step


def draw_flower():
    num_lepestok = 6
    for i in range(num_lepestok):
        for j in range(int(360/3)):
            turtle.forward(3)
            turtle.left(num_lepestok)
        turtle.left(int(360/3))


def draw_butterfly():
    size = 10
    angle = 12
    num_circles = 10
    turtle.left(90)
    for i in range(num_circles):
        for j in range(int(360/angle)):
            turtle.forward(size)
            turtle.left(angle)
        for j in range(int(360/angle)):
            turtle.forward(size)
            turtle.right(angle)
        size += 1


def draw_spring():
    size = 3
    angle = 6
    count_springs = 5
    turtle.left(90)
    for i in range(count_springs):
        for j in range(int(180/angle)):
            turtle.forward(3)
            turtle.right(angle)
        for j in range(int(180/(angle*5))):
            turtle.forward(3)
            turtle.right(angle*5)


def draw_smile():
    x,y = 0,0
    angle = 3
    turtle.begin_fill()
    for i in range(int(360/angle)):
        turtle.forward(3)
        turtle.right(angle)
    turtle.color("black", "yellow")
    turtle.end_fill()
    turtle.color("black")
    turtle.penup()

    turtle.left(90)
    turtle.goto(-20, -20)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(int(360/(angle*2))):
        turtle.forward(1)
        turtle.right(angle*2)
    turtle.color("black", "blue")
    turtle.end_fill()
    turtle.color("black")
    turtle.penup()

    turtle.goto(20, -20)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(int(360/(angle*2))):
        turtle.forward(1)
        turtle.left(angle*2)
    turtle.color("black", "blue")
    turtle.end_fill()
    turtle.color("black")

    turtle.right(90)


    size_pen = 8
    turtle.width(size_pen)

    turtle.penup()
    turtle.goto(size_pen/2,-50)
    turtle.pendown()
    turtle.goto(size_pen/2,-80)

    turtle.penup()
    turtle.color("red")
    turtle.goto(-20 + size_pen/2, -90)
    turtle.pendown()
    turtle.right(90)
    for i in range(int(180/angle)):
        turtle.forward(1)
        turtle.left(angle)


draw_smile()
# turtle.hideturtle()
input()