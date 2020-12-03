import turtle
def circle():
    print('Hello')
circle()
def draw_circle(color,size,x,y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

turtuga = turtle.Turtle()
turtuga.shape('turtle')
turtuga.speed(500)



draw_circle('green',50,0,0)
draw_circle('blue',50,-50,0)
draw_circle('yellow',50,-100,0)






turtle.done()