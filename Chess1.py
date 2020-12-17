import turtle


a =  turtle.Turtle()

#assigh

a.speed(.001)
a.pensize(1)   
turtle.bgcolor('cyan')

#square

def square(pen,color,size, row, col):
    pen.penup()
    pen.goto(row,col)
    pen.pendown()
    pen.fillcolor(color)
    pen.pencolor(color)
    pen.begin_fill()
    pen.setheading(0)
    for i in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()

cell = 8                                                                                                                  
row = -350
jump = 75
for i in range(cell):
    
    col = -360
    for j in range(cell):
        if (i + j) % 2 == 0 :
            scolor = 'black'
        else:
            scolor = 'white'
        a.penup()
        
        col = col + jump

        print(row, col)
        a.goto(row, col)
        square(a,scolor,jump, row, col)

    row = row + jump



turtle.done()