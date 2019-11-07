import turtle
t = turtle.Turtle()

  
  
def start(t,length):
	for side in range (0,5):
		t.forward(length)
		t.right(144)

def octagon(t,length):
	for side in range (0,8):
		t.forward(length)
		t.right(45)
		


def callMike():
    w = turtle.Screen()
    w.setup(1000,1000)
    w.clear()
    w.bgcolor("white")
    t = turtle.Turtle()
    t.penup()
    x = 50
    y = 90
    count = 0             
    t.color("blue")
    while (count < 10):
        t.goto(x,y)
        t.pendown()
        t.circle(100)
        start(t,100)
        octagon(t,100)
        count = count + 1
        x = x - 10 
        y = y + 10
        if (count > 1):
            t.color("red",)
     		 
        print(x,y,count)
    w.exitonclick()
		



def main():
    callMike()
    
if __name__ == '__main__':
	main()
