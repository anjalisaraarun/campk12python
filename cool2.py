import turtle
import math

fj = turtle.Turtle()
fj.color('red','yellow')

fj.begin_fill()
fj.speed(400)
for i in range(2000):
    fj.forward(math.sqrt(i))
    fj.left(i%180)
    
    
fj.end_fill()