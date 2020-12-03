import turtle
import math

fj = turtle.Turtle()
fj.color('red','yellow')

fj.begin_fill()
fj.speed(100)
for i in range(100):
    fj.forward(math.sqrt(i)*10)
    fj.left(168.5)
    
fj.end_fill()
