import turtle
r = turtle.Turtle()
y = turtle.Turtle()
g = turtle.Turtle()
blu = turtle.Turtle()
blk = turtle.Turtle()

wn = turtle.Screen()
wn.bgcolor('white')

r.color('red')
r.pensize(5)
r.speed(10)

y.color('yellow')
y.pensize(5)
y.speed(10)

g.color('green')
g.pensize(5)
g.speed(10)

blu.color('blue')
blu.pensize(5)
blu.speed(10)

blk.pensize(5)
blk.speed(10) 

blk.penup()
blk.left(90)
blk.forward(50)
blk.right(90)
blk.pendown()

blu.penup()
blu.forward(-90)
blu.left(90)
blu.forward(50)
blu.right(90)
blu.pendown()

r.penup()
r.forward(90)
r.left(90)
r.forward(50)
r.right(90)
r.pendown()

y.penup()
y.forward(-45)
y.pendown()

g.penup()
g.forward(45)
g.pendown()

for x in range(36):
    blk.forward(7)
    blu.forward(7)
    r.forward(7)
    y.forward(7)
    g.forward(7)
    blk.right(360/36)
    blu.right(360/36)
    r.right(360/36)
    y.right(360/36)
    g.right(360/36)

wn.exitonclick()
