#import

import turtle
import math
import random

#varible

screen = turtle.Screen()
screen.bgcolor('black')
pen = turtle.Turtle()
pen.speed(0.5)
pen.color('white')

#circle

def circle(position,size):
    for i in range(10):
        position.circle(size)
        size = size - 4

def cirli(position,size,repeat):
    for i in range(repeat):
        circle(position,size)
        pen.right(360/repeat)

cirli(pen,100,10)

ypen = turtle.Turtle()
ypen.speed(0.5)
ypen.color('cyan')


def circle(position,size):
    for i in range(10):
        position.circle(size)
        size = size - 10

def cirli(position,size,repeat):
    for i in range(repeat):
        circle(position,size)
        ypen.right(360/repeat)

cirli(ypen,100,10)


yypen = turtle.Turtle()
yypen.speed(0.5)
yypen.color('yellow')


def circle(position,size):
    for i in range(10):
        position.circle(size)
        size = size - 20

def cirli(position,size,repeat):
    for i in range(repeat):
        circle(position,size)
        yypen.right(360/repeat)

cirli(yypen,100,10)

yyypen = turtle.Turtle()
yyypen.speed(0.5)
yyypen.color('orange')


def circle(position,size):
    for i in range(10):
        position.circle(size)
        size = size - 30

def cirli(position,size,repeat):
    for i in range(repeat):
        circle(position,size)
        yyypen.right(360/repeat)

cirli(yyypen,100,10)

    
turtle.done()
