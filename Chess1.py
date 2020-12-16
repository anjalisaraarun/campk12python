import turtle

a =  turtle.Turtle()
#assigh

a.speed(0.5)
a.pensize(1)   
turtle.bgcolor('green')

#square

def square(pen,color,size):
    pen.penup()
    pen.goto(-250,-250)
    pen.pendown()
    pen.fillcolor(color)
    pen.pencolor(color)
    pen.begin_fill()
    pen.setheading(0)
    for i in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()


for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 :
            scolor = 'black'
        else:
            scolor = 'white'
        a.penup()
        a.goto((i - 8) * 80 , (j - 8) * 80)
        square(a,scolor,80)



turtle.done()