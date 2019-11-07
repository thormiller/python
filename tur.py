import turtle 

      
spiral = turtle.Turtle()
spiral.pencolor("#32D486")  
spiral.speed(1) 
 
spiral.begin_fill()
if spiral.filling():
   spiral.pensize(5)
else:
    spiral.pensize(3)

for i in range(50):
    spiral.forward(i * 15)
    spiral.right(144)
   
turtle.done()

