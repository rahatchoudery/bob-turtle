import turtle
bob = turtle.Turtle()

#draw the big square
for i in range(4):
    bob.forward(320)
    bob.left(90)

#draw horizontal lines
for i in range(8):
    bob.forward(320)
    bob.left(90)
    bob.forward(20)
    bob.left(90)
    bob.forward(320)
    bob.right(90)
    bob.forward(20)
    bob.right(90)

#draw vertical lines
for i in range(8):

    bob.forward(20)
    bob.right(90)
    bob.forward(320)
    bob.left(90)
    bob.forward(20)
    bob.left(90)
    bob.forward(320)
    bob.right(90)
  
#return to original position
bob.left(180)
bob.forward(320)
bob.left(90)
bob.forward(320)
bob.left(90)

turtle.exitonclick()
turtle.done()
