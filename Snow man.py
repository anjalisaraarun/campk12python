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
snow('white',2,0,0)