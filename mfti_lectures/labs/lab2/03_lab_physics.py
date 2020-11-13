import turtle

start_x = -300
start_y = -100

x = start_x
y = start_y

def go_to_start():
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()

def jump(x, y):
    vx = 4
    dt = 1
    ay = 0.5
    vy = 6
    k = 0.04
    for step in range(1000):
        x += vx * dt
        vy -= ay * dt
        vx -= k * dt
        y += vy*dt + ay * dt ** 2/2
        dt += 0.001
        if y <= start_y:
            y = start_y
            vy = -vy/1.5
        if vx <= 0:
            break
        turtle.goto(x,y)
    
    return x,y

go_to_start()
turtle.speed(1)
turtle.shape("circle")
turtle.width(4)

turtle.forward(600)
go_to_start()
x,y = jump(x,y)
x,y = jump(x,y)


input()