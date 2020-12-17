import turtle

a =  turtle.Turtle()
#assigh

a.speed(.05)
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


# for i in range(3):
#     print("i=", i)

#     for j in range(3):
#         print("   j=",j)

squares = 16
size = 30
for i in range(squares):
    for j in range(squares):
        if (i + j) % 2 == 0 :
            scolor = 'black'
        else:
            scolor = 'white'
        
        row = (i - squares/2) * size
        col = (j - squares/2) * size
        a.penup()
        a.goto(row , col)
        square(a,scolor,size)
        print(i, j, "row=", row, " col=", col)
    

# print(range(8))

turtle.done()