import turtle

def drawtriangle(t, x):
    for _ in range(3):
        t.forward(x)
        t.right(120)
        
bob = turtle.Turtle()
wn = turtle.Screen()
turtle.Screen().bgcolor('red')

bob.color('white')
bob.penup()
bob.forward(-100)
bob.right(90)
bob.forward(70)
bob.left(90)
bob.left(60)
bob.pendown()

drawtriangle(bob, 100) 

bob.forward(100)

drawtriangle(bob, 100)

bob.right(120)
bob.forward(100)
bob.left(120)

drawtriangle(bob, 100)

wn.exitonclick()
