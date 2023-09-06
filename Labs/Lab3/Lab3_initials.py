import turtle
l = turtle.Turtle()
m = turtle.Turtle()

wn = turtle.Screen()
turtle.Screen().bgcolor('pink')

l.color('white')
m.color('white')

l.penup()
l.left(90)
l.forward(50)
l.right(90)
l.forward(-50)
l.right(90)
l.pendown()

m.penup()
m.left(90)
m.forward(50)
m.right(90)
m.right(90)
m.pendown()

l.forward(100)
l.left(90)
l.forward(30)

m.forward(100)
m.forward(-100)
m.left(45)
m.forward(30)
m.left(90)
m.forward(30)
m.right(135)
m.forward(100)

wn.exitonclick()
