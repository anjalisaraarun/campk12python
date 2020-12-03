import turtle

fj = turtle.Turtle()
fj.speed(20)

fwd = 200
angle = 135

startAngle = 10
for shape in range(180):
    for i in range (30):
        fj.forward(10)
        fj.left(startAngle)
    
    # fj.down(50)
    startAngle = startAngle + 1

    fj.clear()

    print(shape, startAngle)




















turtle.done()