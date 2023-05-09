import turtle

turtle.hideturtle()
turtle.speed(0)
turtle.width(3)
turtle.color('red')
turtle.begin_fill()

turtle.Screen()
turtle.left(140)
turtle.forward(50)
for i in range(200):
    turtle.right(1)
    turtle.forward(0.5)

turtle.left(120)
for i in range(200):
    turtle.right(1)
    turtle.forward(0.5)

turtle.speed(0)
turtle.forward(58)
turtle.end_fill()
turtle.done()