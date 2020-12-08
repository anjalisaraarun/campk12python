import turtle
s = turtle.Turtle()
def snow(color,radius,x,y):
    s.penup()
    s.goto(x,y)
    s.fillcolor(color)
    s.pendown()
    s.begin_fill()
    s.circle(radius)
    s.end_fill()
snow('silver',30,0,0)
snow('silver',50,0,-90)
snow('silver',70,0,-180)

#drawing eyes

snow('black',2,-10,30)
snow('black',2,10,30)
snow('orange',2,0,20)
#button

snow('magenta',3,0,-5)
snow('magenta',3,0,-20)
snow('magenta',3,0,-35)

#hands

s.penup()
s.pensize(4)
s.goto(20,-20)
s.pendown()
s.goto(85,45)

s.penup()
s.pensize(4)
s.goto(-30,-20)
s.pendown()
s.goto(-85,45)

#hat

s.penup()
s.goto(-50,45)
s.pendown()
s.goto(60,45)
s.fillcolor('black')
s.begin_fill()
s.goto(50,45)
s.goto(50,60)
s.goto(-40,60)
s.goto(-40,45)
s.end_fill()











turtle.done()