import turtle
import math

fj = turtle.Turtle()
fj.color('red','yellow')

fj.begin_fill()
fj.speed(400)
for i in range(2000):
    fj.forward(10)
    fj.left(math.sin(i/10*25))
    fj.left(20)
    
    
fj.end_fill()