import turtle
n = int(input("enter a number of sides for a shape: "))

bob = turtle.Turtle()
wn = turtle.Screen()
turtle.Screen().bgcolor('lightblue')

bob.color('white')

bob.penup()
bob.forward(-45)
bob.left(90)
bob.forward(90)
bob.right(90)
bob.pendown()

for x in range(n):
    bob.forward(500/n)
    bob.right(360/n)
    
wn.exitonclick()
