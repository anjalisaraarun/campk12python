import turtle
def circle():
    print('Hello')
circle()
def draw_circle(turtle,color,size,x,y):
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
turtuga.speed(10)



draw_circle(turtuga,'green',50,0,0)
draw_circle(turtuga,'blue',50,-50,0)
draw_circle(turtuga,'yellow',50,-100,0)
turtle.penup()
turtle.goto(-70,-50)
turtle.color('green')
turtle.write("Let's learn Python!")




turtle.done()



