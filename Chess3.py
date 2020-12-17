import turtle

a =  turtle.Turtle()
#assigh

a.speed(0.5)
a.pensize(1)   
turtle.bgcolor('green')

#square

def square(pen,color,size):
    pen.penup()
    # pen.goto(-250,-250)
    pen.pendown()
    pen.fillcolor(color)
    pen.pencolor(color)
    pen.begin_fill()
    pen.setheading(0)
    for i in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()

size = 80
ranges = 8

for i in range(ranges):
    for j in range(ranges):
        if (i + j) % 2 == 0 :
            scolor = 'black'
        else:
            scolor = 'white'
        a.penup()
        a.goto((i - 4) * size , (j - 4) * size)
        square(a,scolor,size)



turtle.done()