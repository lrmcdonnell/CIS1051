import turtle
bob = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('pink')

bob.color('white')
bob.pensize(5)

bob.speed(10)
bob.shape('turtle')

bob.penup()

for x in range(12):
    bob.forward(90)
    bob.pendown()
    bob.forward(10)
    bob.penup()
    bob.forward(20)
    bob.stamp()
    bob.backward(120)
    bob.right(30)
    
bob.penup()
wn.exitonclick()
