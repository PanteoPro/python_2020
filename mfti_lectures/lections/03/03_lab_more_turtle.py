from random import randint
import turtle


number_of_turtles = 20
steps_of_time_number = 100

pool = [turtle.Turtle(shape="circle") for i in range(number_of_turtles)]

for unit in pool:
    unit.penup()
    unit.speed(100)
    unit.right(randint(0,360))
    unit.goto(randint(0,200), randint(0,200))




for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(20)
        
        x,y = unit.pos()

        if x <= 0 or x >= 200 or y <= 0 or y >= 200:
            unit.right(10)

