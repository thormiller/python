import turtle
t = turtle.Turtle()
t.speed(1)
  
  
def start(t,length):
	for side in range (0,5):
		t.forward(length)
		t.right(144)

def octagon(t,length):
	for side in range (0,8):
		t.forward(length)
		t.right(45)
		
if t.begin_fill():
   t.fillcolor("red")
 
else:
	t.color("green") 
 
 
for i in range(75):
    t.speed(0)	  
    t.goto(0,-150)
    t.circle(50)
    t.right(5)    

 
def callMike():
    w = turtle.Screen()
    w.setup(1000,1000)
    w.clear()
    w.bgcolor("white")
    t.pendown()
    x = 50
    y = 90
    t.goto(x,y)
    t.pendown()
    count = 0             
    t.color("blue")

    while (count < 10):
        t.goto(x,y)
        t.pendown()
        t.fillcolor("green")
        t.circle(100)              
        start(t,100)
        octagon(t,100)
        count = count + 1
        x = x - 10 
        y = y + 10
        if (count > 5):
            t.color("red",)                    	                            	 
        print(x,y,count)
        
        if (count < 5):
            t.color("green")
        print(x,y,count)
    w.exitonclick()
		
t.end_fill()


def main():
    callMike()
    
if __name__ == '__main__':
	main()

