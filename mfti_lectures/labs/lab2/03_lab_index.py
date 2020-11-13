import turtle
from random import *
import math

LINE = 50
LINE2 = 100
DIAG = math.sqrt(LINE**2+LINE**2)
SPACE = 15
END = (90, 0, 1)
TIRES = 6
SPACE_BETWEEN_TIRES = 3


numbers = []

def load_data():
    with open("lectures/movements_turtle.txt", "r") as f:
        for line in f:
            number = []
            movements = line.rstrip().replace("(", "")[:-1].split("),")
            for step in movements:
                move = step.replace(" ", "").split(",")
                number.append(tuple(map(float, move)))
            numbers.append(number)
    
load_data()

# 1 - right() 2 - length 3 - penup?
# number_zero = [(0, LINE, 0), (90, LINE2, 0), (90, LINE, 0), (90, LINE2, 0), END]
# number_one = [(90, LINE, 1), (180+45, DIAG, 0), (45+90, LINE2, 0), (90, LINE, 1), (90, LINE2, 1), END]
# number_two = [(0, LINE, 0), (90, LINE, 0), (45, DIAG, 0), (45+180, LINE, 0), (180, LINE, 1), (90, LINE2, 1), END]
# number_three = [(0, LINE, 0), (90+45, DIAG, 0), (45+180, LINE, 0), (90+45, DIAG, 0), (45+90, LINE2, 1), END]
# number_four = [(90, LINE, 0), (270, LINE, 0), (270, LINE, 1), (180, LINE2, 0), (90, LINE, 1), (90, LINE2, 1), END]
# number_five = [(0,LINE, 1), (180, LINE, 0), (270, LINE, 0), (270, LINE, 0), (90, LINE, 0), (90, LINE, 0), (90, LINE2, 1), END]
# number_six = [(0, LINE, 1), (90+45, DIAG, 0), (45+180, LINE, 0), (90, LINE, 0), (90, LINE, 0), (90, LINE, 0), (0, LINE, 1), END]
# number_seven = [(0, LINE, 0), (90+45, DIAG, 0), (45+270, LINE, 0), (180, LINE2, 1), END]
# number_eight = [(0, LINE, 0), (90, LINE2, 0), (90, LINE, 0), (90, LINE, 0), (90, LINE, 0), (180, LINE, 1), (90, LINE, 0), END]
# number_nine = [(0, LINE, 0), (90, LINE, 0), (45, DIAG, 0), (45+90, LINE, 1), (90, LINE, 0), (180, LINE, 1), (90, LINE, 0), END]
# tires = [(0,LINE, 0), (90, LINE, 0), (0, LINE, 0), (90, LINE, 0), (90, LINE, 0), (0, LINE, 0), (90, LINE, 1), (90+45, DIAG, 0), (45+180, LINE, 0), (90+45, DIAG, 0), (45+90, LINE2, 1), END]

turtle.shape("turtle")
turtle.penup()
turtle.backward(400)
turtle.pendown()

def next_number(count=1, side=1):
    turtle.penup()
    turtle.forward((LINE+SPACE)*count*side)
    turtle.pendown()


def draw_number(tuple_number, flag=True):
    print(tuple_number)
    for angle, length, draw in tuple_number:
        if(draw):
            turtle.penup()
        turtle.right(angle)
        turtle.forward(length)
        if(draw):
            turtle.pendown()
    
    if flag:
        next_number()


def draw_index(index):
    list_numbers = list(map(int, str(index)))
    turtle.color("grey")
    turtle.width(2)
    for number in range(len(list_numbers)):
        draw_number(numbers[-1])
    next_number(len(list_numbers), -1)
    turtle.color("blue")
    turtle.width(4)
    for number in list_numbers:
        draw_number(numbers[number])


draw_index(141700228332)
turtle.color("black")
turtle.width(1)
input()